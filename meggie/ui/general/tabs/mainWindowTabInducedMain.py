import os
import logging
import shutil

from PyQt4 import QtGui

from meggie.ui.general.tabs.mainWindowTabInducedUi import Ui_mainWindowTabInduced  # noqa

from meggie.ui.analysis.TFRDialogMain import TFRDialog
from meggie.ui.analysis.TFRPlotTopologyDialogMain import TFRPlotTopologyDialog

from meggie.ui.utils.messaging import messagebox
from meggie.ui.utils.messaging import exc_messagebox
from meggie.ui.utils.decorators import threaded

from meggie.ui.widgets.epochWidgetMain import EpochWidget

from meggie.code_meggie.analysis.spectral import group_average_tfr

import meggie.code_meggie.general.fileManager as fileManager
import meggie.code_meggie.general.mne_wrapper as mne


class MainWindowTabInduced(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self)
        self.parent = parent
        self.ui = Ui_mainWindowTabInduced()
        self.ui.setupUi(self)

        self.epochList = EpochWidget(self, 
            epoch_getter=self.parent.get_epochs)
        self.epochList.setParent(self.ui.groupBoxEpochs)
        self.epochList.setSelectionMode(
            QtGui.QAbstractItemView.MultiSelection)

        self.initialize_ui()


    def initialize_ui(self):

        if not self.parent.experiment:
            return

        active_subject = self.parent.experiment.active_subject

        if active_subject is None:
            return

        # populate epoch widget
        self.epochList.clearItems()
        for epoch_name in active_subject.epochs:
            item = QtGui.QListWidgetItem(epoch_name)
            self.epochList.add_item(item)

        self.ui.listWidgetTFR.clear()
        for name in active_subject.tfrs:
            item = QtGui.QListWidgetItem(name)
            self.ui.listWidgetTFR.addItem(item)

    def on_listWidgetTFR_currentItemChanged(self, item):
        if not item:
            self.ui.textBrowserTFRInfo.clear()
            return

        experiment = self.parent.experiment

        tfr_name = str(item.text())
        tfr = experiment.active_subject.tfrs.get(tfr_name)
        info = 'Name: ' + str(tfr_name) + '\n'

        freqs = tfr.tfr.freqs
        fmin, fmax = "%.1f" % freqs[0], "%.1f" % freqs[-1]
        info += 'Freqs: ' + fmin + ' - ' + fmax + ' hz\n'

        decim = tfr.decim
        info += 'Decim: ' + str(decim) + '\n'

        evoked_subtracted = tfr.evoked_subtracted
        info += 'Evoked subtracted: ' + str(evoked_subtracted) + '\n'

        n_cycles = tfr.n_cycles
        if type(n_cycles) is list:
            cmin, cmax = "%.1f" % n_cycles[0], "%.1f" % n_cycles[-1]
            info += 'Cycles: ' + cmin + ' - ' + cmax + '\n'
        else:
	    info += 'Cycles: ' + str(n_cycles) + '\n'

        self.ui.textBrowserTFRInfo.setText(info)

    @property
    def preferencesHandler(self):
        return self.parent.preferencesHandler

    @property
    def update_ui(self):
        return self.parent.update_ui


    def on_pushButtonPlotTFRTopology_clicked(self, checked=None):
        """
        """
        if checked is None:
            return

        experiment = self.parent.experiment
        if not experiment:
            return

        active_subject = experiment.active_subject
        if not active_subject:
            return

        tfr_item = self.ui.listWidgetTFR.currentItem()
        if not tfr_item:
            return

        self.tfr_plot_dialog = TFRPlotTopologyDialog(
            self, experiment, tfr_item.text())
        self.tfr_plot_dialog.show()

    def on_pushButtonGroupAverage_clicked(self, checked=None):
        if checked is None:
            return

        experiment = self.parent.experiment
        if not experiment:
            return

        if experiment.active_subject is None:
            return

        tfr_item = self.ui.listWidgetTFR.currentItem()
        if not tfr_item:
            return

        tfr_name = tfr_item.text()

        @threaded
        def group_average(*args, **kwargs):
            group_average_tfr(experiment, tfr_name)

        group_average(do_meanwhile=self.update_ui)

        experiment.save_experiment_settings()
        self.initialize_ui()


    def on_pushButtonDeleteTFR_clicked(self, checked=None):
        if checked is None:
            return

        experiment = self.parent.experiment
        if not experiment:
            return

        active_subject = experiment.active_subject
        if not active_subject:
            return

        tfr_item = self.ui.listWidgetTFR.currentItem()
        if not tfr_item:
            return

        message = 'Permanently remove a TFR?'
        reply = QtGui.QMessageBox.question(self, 'Delete TFR',
                                           message, QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            try:
                self.parent.experiment.active_subject.remove_tfr(
                    tfr_item.text()
                )
            except Exception as e:
                exc_messagebox(self, e)

            self.parent.experiment.save_experiment_settings()
            self.initialize_ui()


    def on_pushButtonGroupDeleteTFR_clicked(self, checked=None):
        if checked is None:
            return

        experiment = self.parent.experiment
        if not experiment:
            return

        active_subject = experiment.active_subject
        if not active_subject:
            return

        tfr_item = self.ui.listWidgetTFR.currentItem()
        if not tfr_item:
            return

        tfr_name = tfr_item.text()

        message = 'Permanently remove TFR from all subjects?'
        reply = QtGui.QMessageBox.question(self, "Delete TFR's",
                                           message, QtGui.QMessageBox.Yes |
                                           QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            for subject in experiment.subjects.values():
                if tfr_name in subject.tfrs:
                    subject.remove_tfr(
                        tfr_name,
                    )

        logging.getLogger('ui_logger').info("Removed TFR's.")
        experiment.save_experiment_settings()
        self.initialize_ui()


    def on_pushButtonComputeTFR_clicked(self, checked=None):
        """Open the dialog for plotting TFR from a single channel."""
        if checked is None:
            return

        experiment = self.parent.experiment
        if not experiment:
            return

        active_subject = experiment.active_subject
        if not experiment.active_subject:
            return
        
        if self.epochList.currentItem() is None:
            message = 'You must select epochs before TFR.'
            messagebox(self, message)
            return
        
        selected_items = self.epochList.ui.listWidgetEpochs.selectedItems()
        
        if len(selected_items) == 1:
            collection_name = selected_items[0].text()
        else:
            message = 'Select exactly one epoch collection.'
            messagebox(self, message)
            return
        
        self.tfr_dialog = TFRDialog(self, experiment, collection_name)
        self.tfr_dialog.show()
        
