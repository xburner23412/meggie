""" Contains controlling logic for the spectrum implementation.
"""

import os
import logging

from copy import deepcopy
from collections import OrderedDict

import mne

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

import meggie.utilities.filemanager as filemanager

from meggie.datatypes.spectrum.spectrum import Spectrum

from meggie.utilities.validators import assert_arrays_same
from meggie.utilities.formats import format_floats
from meggie.utilities.plotting import color_cycle
from meggie.utilities.plotting import create_channel_average_plot
from meggie.utilities.channels import average_to_channel_groups
from meggie.utilities.channels import iterate_topography
from meggie.utilities.channels import clean_names
from meggie.utilities.channels import get_channels_by_type
from meggie.utilities.units import get_power_unit
from meggie.utilities.decorators import threaded
from meggie.utilities.stats import prepare_data_for_permutation
from meggie.utilities.stats import permutation_analysis
from meggie.utilities.stats import report_permutation_results
from meggie.utilities.stats import plot_permutation_results

from meggie.utilities.events import get_raw_blocks_from_intervals


@threaded
def create_power_spectrum(subject, spectrum_name, params, intervals):
    """ Creates a power spectrum item.
    """
    # get raw objects organized with average groups as keys
    ival_times, raw_block_groups = get_raw_blocks_from_intervals(subject,
                                                                 intervals)

    raw = subject.get_raw()
    picks = mne.pick_types(raw.info, meg=True, eeg=True,
                           exclude='bads')

    # remove zero channels from picks
    zero_idxs = []
    for idx, row in enumerate(raw._data):
        if np.all(row == 0):
            zero_idxs.append(idx)
    picks = [pick for pick in picks if pick not in zero_idxs]


    fmin = params['fmin']
    fmax = params['fmax']
    nfft = params['nfft']
    overlap = params['overlap']

    # compute psd's
    psd_groups = OrderedDict()
    for key, raw_blocks in raw_block_groups.items():
        for raw_block in raw_blocks:
            length = len(raw_block.times)
            psds, freqs = mne.time_frequency.psd_welch(
                raw_block, fmin=fmin, fmax=fmax,
                n_fft=nfft, n_overlap=overlap, picks=picks,
                proj=True)

            if key not in psd_groups:
                psd_groups[key] = []

            psd_groups[key].append((psds, freqs, length))

    for psd_list in psd_groups.values():
        freqs = psd_list[0][1]
        break

    psds = []
    for psd_list in psd_groups.values():
        # do a weighted (raw block lengths as weights) average of psds inside a
        # group
        weights = np.array([length for psds_, freqs, length in psd_list])
        weights = weights.astype(float) / np.sum(weights)
        psd = np.average([psds_ for psds_, freqs, length in psd_list],
                         weights=weights, axis=0)
        psds.append(psd)

    info = mne.pick_info(raw.info, sel=picks)
    psd_data = dict(zip(psd_groups.keys(), psds))

    params = deepcopy(params)
    params['conditions'] = [elem for elem in psd_groups.keys()]
    params['intervals'] = ival_times

    spectrum = Spectrum(spectrum_name, subject.spectrum_directory,
                        params, psd_data, freqs, info)

    spectrum.save_content()
    subject.add(spectrum, 'spectrum')


def plot_spectrum_averages(experiment, name, log_transformed=True):
    """ Plots spectrum averages.
    """

    subject = experiment.active_subject
    subject_name = subject.name

    spectrum = subject.spectrum.get(name)

    data = spectrum.content
    freqs = spectrum.freqs
    ch_names = spectrum.ch_names 
    channel_groups = experiment.channel_groups
    info = spectrum.info

    colors = color_cycle(len(data))
    conditions = spectrum.content.keys()

    averages = {}
    for key, psd in sorted(data.items()):

        data_labels, averaged_data = average_to_channel_groups(
            psd, info, ch_names, channel_groups)

        for label_idx, label in enumerate(data_labels):
            if not label in averages:
                averages[label] = []
            averages[label].append((key, averaged_data[label_idx]))

    ch_types = sorted(set([label[0] for label in averages.keys()]))
    for ch_type in ch_types:

        ch_groups = sorted([label[1] for label in averages.keys()
                            if label[0] == ch_type])

        def plot_fun(ax_idx, ax):
            ch_group = ch_groups[ax_idx]
            ax.set_title(ch_group)
            ax.set_xlabel('Frequency (Hz)')
            ax.set_ylabel('Power ({})'.format(
                get_power_unit(ch_type, log_transformed)))

            for color_idx, (key, curve) in enumerate(averages[(ch_type, ch_group)]):
                if log_transformed:
                    curve = 10 * np.log10(curve)
                ax.plot(freqs, curve, color=colors[color_idx])

        title = ' '.join([name, ch_type])
        legend = list(zip(conditions, colors))
        create_channel_average_plot(len(ch_groups), plot_fun, title, legend)

    plt.show()


def run_permutation_test(experiment, window, selected_name, groups, time_limits,
                         frequency_limits, location_limits, threshold,
                         significance, n_permutations, design):
    """ Runs permutation test computation and reports the results.
    """
    if location_limits[0] == "ch_name" and frequency_limits is not None:
        raise Exception('Cannot run permutation tests with both location and frequency limits')

    spectrum_item = experiment.active_subject.spectrum[selected_name]
    conditions = list(spectrum_item.content.keys())
    groups = OrderedDict(sorted(groups.items()))
    freqs = spectrum_item.freqs

    chs_by_type = get_channels_by_type(spectrum_item.info)
    if location_limits[0] == 'ch_type':
        ch_type = location_limits[1]
    else:
        ch_type = [key for key, vals in chs_by_type.items() if location_limits[1] in vals][0]

    log_transformed = False

    info, data, adjacency = prepare_data_for_permutation(
        experiment, design, groups, 'spectrum', selected_name,
        location_limits, time_limits, frequency_limits,
        data_format=('locations', 'freqs'),
        do_meanwhile=window.update_ui)

    results = permutation_analysis(data, design, conditions, groups, threshold, adjacency, n_permutations,
                                   do_meanwhile=window.update_ui)

    report_permutation_results(results, design, selected_name, significance,
                               location_limits=location_limits, 
                               frequency_limits=frequency_limits)

    if design == 'within-subjects':
        title_template = 'Cluster {0} for group {1} (p {2})'
    else:
        title_template = 'Cluster {0} for condition {1} (p {2})'

    def frequency_fun(cluster_idx, cluster, pvalue, res_key):
        fig, ax = plt.subplots()
        if design == 'within-subjects':
            colors = color_cycle(len(conditions))
            for cond_idx, condition in enumerate(conditions):
                spectrum = np.mean(data[res_key][cond_idx][:, :, np.unique(cluster[-1])],
                                   axis=(0, -1))
                ax.plot(freqs, spectrum, label=condition, color=colors[cond_idx])

        else:
            colors = color_cycle(len(groups))
            for group_idx, (group_key, group) in enumerate(groups.items()):
                spectrum = np.mean(data[res_key][group_idx][:, :, np.unique(cluster[-1])],
                                   axis=(0, -1))
                ax.plot(freqs, spectrum, label=group_key, color=colors[group_idx])

        fig.suptitle(title_template.format(cluster_idx+1, res_key, pvalue))
        fig.canvas.set_window_title('Cluster spectrum')

        ax.legend()
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Power ({})'.format(
            get_power_unit(ch_type, log_transformed)))
        fmin = np.min(freqs[cluster[0]])
        fmax = np.max(freqs[cluster[0]])
        ax.axvspan(fmin, fmax, alpha=0.5, color='blue')

    def location_fun(cluster_idx, cluster, pvalue, res_key):
        map_ = [1 if idx in cluster[-1] else 0 for idx in 
                range(len(info['ch_names']))]

        fig, ax = plt.subplots()
        mne.viz.plot_topomap(np.array(map_), info, vmin=0, vmax=1,
                             cmap='Reds', axes=ax, ch_type=ch_type,
                             contours=0)

        fig.suptitle(title_template.format(cluster_idx+1, res_key, pvalue))
        fig.canvas.set_window_title('Cluster topomap')

    plot_permutation_results(results, significance, window,
                             location_limits=location_limits, 
                             frequency_limits=frequency_limits, 
                             location_fun=location_fun,
                             frequency_fun=frequency_fun)


def plot_spectrum_topo(experiment, name, log_transformed=True, ch_type='meg'):
    """ Plots spectrum topography.
    """

    subject = experiment.active_subject
    subject_name = subject.name
    spectrum = subject.spectrum.get(name)
    data = spectrum.content
    freqs = spectrum.freqs
    ch_names = spectrum.ch_names
    info = spectrum.info
    if ch_type == 'meg':
        picked_channels = [ch_name for ch_idx, ch_name in enumerate(info['ch_names'])
                           if ch_idx in mne.pick_types(info, meg=True, eeg=False)]
    else:
        picked_channels = [ch_name for ch_idx, ch_name in enumerate(info['ch_names'])
                           if ch_idx in mne.pick_types(info, eeg=True, meg=False)]
    info = info.copy().pick_channels(picked_channels)

    colors = color_cycle(len(data))

    def individual_plot(ax, info_idx, names_idx):
        """
        """
        ch_name = ch_names[names_idx]
        for color_idx, (key, psd) in enumerate(sorted(data.items())):

            if log_transformed:
                curve = 10 * np.log10(psd[names_idx])
            else:
                curve = psd[names_idx]

            ax.plot(freqs, curve, color=colors[color_idx],
                    label=key)

        title = ' '.join([name, ch_name])
        ax.figure.canvas.set_window_title(title.replace(' ', '_'))
        ax.figure.suptitle(title)
        ax.set_title('')

        ax.legend()
        ax.set_xlabel('Frequency (Hz)')
        ax.set_ylabel('Power ({})'.format(get_power_unit(
            mne.io.pick.channel_type(info, info_idx),
            log_transformed
        )))

        plt.show()

    fig = plt.figure()

    for ax, info_idx, names_idx in iterate_topography(
            fig, info, ch_names, individual_plot):

        handles = []
        for color_idx, (key, psd) in enumerate(sorted(data.items())):

            if log_transformed:
                curve = 10 * np.log10(psd[names_idx])
            else:
                curve = psd[names_idx]

            handles.append(ax.plot(curve, color=colors[color_idx],
                                   linewidth=0.5, label=key)[0])

    if not handles:
        return

    fig.legend(handles=handles)
    title = '{0}_{1}'.format(name, ch_type)
    fig.canvas.set_window_title(title)
    plt.show()

@threaded
def group_average_spectrum(experiment, spectrum_name, groups, new_name):
    """ Computes a group average spectrum item.
    """
    # check data cohesion
    keys = []
    freq_arrays = []
    for group_key, group_subjects in groups.items():
        for subject_name in group_subjects:
            try:
                subject = experiment.subjects.get(subject_name)
                spectrum = subject.spectrum.get(spectrum_name)
                keys.append(tuple(sorted(spectrum.content.keys())))
                freq_arrays.append(tuple(spectrum.freqs))
            except Exception as exc:
                continue

    assert_arrays_same(keys, 'Conditions do not match')
    assert_arrays_same(freq_arrays, 'Freqs do not match')

    # handle channel differences
    ch_names = []
    for group_key, group_subjects in groups.items():
        for subject_name in group_subjects:
            try:
                subject = experiment.subjects.get(subject_name)
                spectrum = subject.spectrum.get(spectrum_name)
                ch_names.append(tuple(clean_names(spectrum.ch_names)))
            except Exception as exc:
                continue

    if len(set(ch_names)) != 1:
        logging.getLogger('ui_logger').info(
            "PSD's contain different sets of channels. Identifying common ones..")

        common_ch_names = list(set.intersection(*map(set, ch_names)))

        logging.getLogger('ui_logger').info(
            str(len(common_ch_names)) + ' common channels found.')
        logging.getLogger('ui_logger').debug(
            'Common channels are ' + str(common_ch_names))
    else:
        common_ch_names = ch_names[0]

    grand_psds = {}
    for group_key, group_subjects in groups.items():
        for subject in experiment.subjects.values():
            if subject.name not in group_subjects:
                continue

            spectrum = subject.spectrum.get(spectrum_name)
            if not spectrum:
                continue

            subject_ch_names = clean_names(spectrum.ch_names) 

            for spectrum_item_key, spectrum_item in spectrum.content.items():
                grand_key = (group_key, spectrum_item_key)

                # get common channels in "subject specific space"
                idxs = [subject_ch_names.index(ch_name) for ch_name 
                        in common_ch_names]

                spectrum_item = spectrum_item[idxs]

                if grand_key not in grand_psds:
                    grand_psds[grand_key] = []
                grand_psds[grand_key].append(spectrum_item)

    grand_averages = {}
    for key, grand_psd in grand_psds.items():
        new_key = str(key[1]) + '_group_' + str(key[0])
        if len(grand_psd) == 1:
            grand_averages[new_key] = grand_psd[0].copy()
        else:
            grand_averages[new_key] = np.mean(grand_psd, axis=0)

    subject = experiment.active_subject

    try:
        spectrum = subject.spectrum.get(spectrum_name)
    except Exception as exc:
        raise Exception('Active subject should be included in the groups')

    spectrum_directory = subject.spectrum_directory

    info = spectrum.info
    common_idxs = [ch_idx for ch_idx, ch_name in enumerate(clean_names(info['ch_names']))
                   if ch_name in common_ch_names]
    info = mne.pick_info(info, sel=common_idxs)

    freqs = spectrum.freqs
    data = grand_averages

    params = deepcopy(spectrum.params)

    # individual intervals not relevant in the group item
    params.pop('intervals', None)

    params['groups'] = groups
    params['conditions'] = [elem for elem in grand_averages.keys()]

    spectrum = Spectrum(new_name, subject.spectrum_directory,
                        params, data, freqs, info)

    spectrum.save_content()
    subject.add(spectrum, 'spectrum')

@threaded
def save_all_channels(experiment, selected_name):
    """ Saves all channesl of a spectrum item to a csv file. """
    column_names = []
    row_descs = []
    csv_data = []

    for subject in experiment.subjects.values():
        spectrum = subject.spectrum.get(selected_name)
        if not spectrum:
            continue
        for key, psd in spectrum.content.items():
            csv_data.extend(psd.tolist())
            column_names = format_floats(spectrum.freqs)

            for ch_name in spectrum.ch_names:
                row_desc = (subject.name, key, ch_name)
                row_descs.append(row_desc)

    folder = filemanager.create_timestamped_folder(experiment)
    fname = selected_name + '_all_subjects_all_channels_spectrum.csv'
    path = os.path.join(folder, fname)

    filemanager.save_csv(path, csv_data, column_names, row_descs)
    logging.getLogger('ui_logger').info('Saved the csv file to ' + path)

@threaded
def save_channel_averages(experiment, selected_name, log_transformed=False):
    """ Saves channel averages of a spectrum item to a csv file. """
    column_names = []
    row_descs = []
    csv_data = []

    channel_groups = experiment.channel_groups

    # accumulate csv contents
    for subject in experiment.subjects.values():
        spectrum = subject.spectrum.get(selected_name)
        if not spectrum:
            continue

        ch_names = spectrum.ch_names
        freqs = spectrum.freqs
        info = spectrum.info

        for key, psd in spectrum.content.items():

            data_labels, averaged_data = average_to_channel_groups(
                psd, info, ch_names, channel_groups)

            if log_transformed:
                csv_data.extend(10 * np.log10(averaged_data.tolist()))
            else:
                csv_data.extend(averaged_data.tolist())

            column_names = format_floats(freqs)

            for ch_type, area in data_labels:
                row_desc = (subject.name, key, ch_type, area)
                row_descs.append(row_desc)

    folder = filemanager.create_timestamped_folder(experiment)
    fname = selected_name + '_all_subjects_channel_averages_spectrum.csv'
    path = os.path.join(folder, fname)

    filemanager.save_csv(path, csv_data, column_names, row_descs)
    logging.getLogger('ui_logger').info('Saved the csv file to ' + path)
