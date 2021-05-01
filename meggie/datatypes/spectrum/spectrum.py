# coding: utf-8

"""
"""

import os
import re
import logging

import numpy as np
import mne

import meggie.utilities.filemanager as filemanager

from meggie.utilities.datatype import Datatype


class Spectrum(Datatype):
    """
    """
    def __init__(self, name, spectrum_directory, params,
                 content=None, freqs=None, info=None):
        """
        """
        # name has no group number and no '.fif'
        self._name = name
        self._spectrum_directory = spectrum_directory
        self._params = params

        self._content = {}
        if content is not None:
            self._content = content

        self._params['info_set'] = True

        self._freqs = freqs
        self._info = info

    def _load_content(self):
        info, data_dict, freqs, ch_names = self._get_content()
        self._info = info
        self._freqs = freqs
        self._content = data_dict

    def _get_content(self):

        # load info
        info_path = os.path.join(self._spectrum_directory,
                                 self._name + '-info.fif')
        info = mne.io.meas_info.read_info(info_path)

        # load data
        data_dict = {}
        template = self.name + '_' + r'([a-zA-Z1-9_]+)\.csv'
        for fname in os.listdir(self._spectrum_directory):
            match = re.match(template, fname)
            if match:
                try:
                    key = str(match.group(1))
                except Exception as exc:
                    raise Exception("Unknown file name format.")

                # if proper condition parameters set,
                # check if the key is in there.
                if 'conditions' in self._params:
                    if key not in [str(elem) for elem in
                                   self._params['conditions']]:
                        continue

                logging.getLogger('ui_logger').debug(
                    'Reading spectrum file: ' + str(fname))

                freqs, row_descs, psd = filemanager.load_csv(
                    os.path.join(self._spectrum_directory, fname))

                ch_names = [desc[0] for desc in row_descs]

                # for backwards compatibility
                # (used to have possibility to have spectrum data
                # saved as log transformed)
                if 'log_transformed' in self._params:
                    if self._params['log_transformed'] is True:
                        if np.mean(psd) < 0:
                            psd = 10 ** (psd / 10.0)

                freqs = np.array(freqs).astype(np.float)
                data_dict[key] = np.array(psd)

        return info, data_dict, freqs, ch_names

    def save_content(self):
        # save info
        info_path = os.path.join(self._spectrum_directory,
                                 self._name + '-info.fif')
        mne.io.meas_info.write_info(info_path, self._info)
        self._params['info_set'] = True
        try:
            # save data
            for key, psd in self._content.items():

                row_descs = [(ch_name,) for ch_name in self.ch_names]
                column_names = self._freqs.tolist()
                data = psd.tolist()

                path = os.path.join(self._spectrum_directory,
                                    self._name + '_' + str(key) + '.csv')

                filemanager.save_csv(path, data, column_names, row_descs)
        except Exception as exc:
            logging.getLogger('ui_logger').exception('')
            raise IOError('Writing spectrums failed')

    def delete_content(self):

        # delete info
        info_path = os.path.join(self._spectrum_directory,
                                 self._name + '-info.fif')
        if os.path.exists(info_path):
            os.remove(info_path)

        # delete data
        template = self.name + '_' + r'([a-zA-Z1-9_]+)\.csv'
        for fname in os.listdir(self._spectrum_directory):
            match = re.match(template, fname)
            if match:
                try:
                    key = str(match.group(1))
                except Exception as exc:
                    continue

                # if proper condition parameters set,
                # check if the key is in there.
                if 'conditions' in self._params:
                    if key not in [str(elem) for elem in
                                   self._params['conditions']]:
                        continue

                logging.getLogger('ui_logger').debug(
                    'Removing existing spectrum file: ' + str(fname))
                os.remove(os.path.join(self._spectrum_directory, fname))

    def set_info(self, subject):
        """
        """
        info = subject.get_raw(preload=False, verbose='warning').info

        # filter to correct set of channels
        _, _, _, ch_names = self._get_content()
        picks = [ch_idx for ch_idx, ch_name in enumerate(info['ch_names'])
                 if ch_name in ch_names]
        info = mne.pick_info(info, sel=picks)

        self._info = info
        self.save_content()

    @property
    def data(self):
        """ Convenient wrapper for getting data
        """
        return self.content

    @property
    def content(self):
        if not self._content:
            self._load_content()
        return self._content

    @property
    def freqs(self):
        if not self._content:
            self._load_content()
        return self._freqs

    @property
    def ch_names(self):
        return self.info['ch_names']

    @property
    def info(self):
        if not self._content:
            self._load_content()
        return self._info

    @property
    def name(self):
        return self._name

    @property
    def params(self):
        return self._params

