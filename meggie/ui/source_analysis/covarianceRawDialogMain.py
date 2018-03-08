'''
Created on 7.1.2015

@author: Kari Aliranta, Erkka Heinila
'''

import logging
import os

from PyQt4 import QtGui

import meggie.code_meggie.general.mne_wrapper as mne
import meggie.code_meggie.general.fileManager as fileManager

from meggie.ui.source_analysis.covarianceRawDialogUi import Ui_covarianceRawDialog


from meggie.ui.utils.messaging import exc_messagebox
from meggie.ui.utils.messaging import messagebox


class CovarianceRawDialog(QtGui.QDialog):
    """
    The class containing the logic for the dialog for collecting the
    parameters computing the noise covariance for a raw file.
    """

    def __init__(self, experiment, on_close=None):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_covarianceRawDialog()
        self.ui.setupUi(self)

        self.experiment = experiment
        self.on_close = on_close
           
           
    def accept(self):
        """
        """

        tmin = self.ui.doubleSpinBoxStartTime.value()
        tmax = self.ui.doubleSpinBoxEndTime.value()

        name = str(self.ui.lineEditName.text()) + '-cov.fif'
        if name in self.experiment.active_subject.get_covfiles():
            messagebox(self, "Covariance matrix of this name already exists",
                       exec_=True)
            return

        if self.ui.radioButtonElsewhere.isChecked():
            try:
                path = self.ui.lineEditRawFile.text()
                subject_raw = self.experiment.active_subject.get_working_file()
                raw = fileManager.open_raw(path)

                # apply ssp and bads to this new data
                raw.info['bads'] = subject_raw.info['bads']
                raw.add_proj([pp.copy() for pp in subject_raw.info['projs']])
                raw.apply_proj()

            except Exception as exc:
                exc_messagebox(self, exc, exec_=True)
                return
        else:
            raw = self.experiment.active_subject.get_working_file().copy()
            raw.apply_proj()

        try:
            cov = mne.compute_raw_covariance(raw, tmin=tmin, tmax=tmax)
            path = os.path.join(self.experiment.active_subject.cov_directory, 
                                name)
            mne.write_cov(path, cov)
        except Exception as exc:
            exc_messagebox(self, exc, exec_=True)
            return

        if self.on_close:
            self.on_close()

        self.close()
        
        
    def on_pushButtonBrowse_clicked(self, checked=None):
        """
        Open file browser for raw data file.
        """
        if checked is None: 
            return

        fname = QtGui.QFileDialog.getOpenFileName(self, 
            'Select raw ' + 'to use')
        self.ui.lineEditRawFile.setText(fname)

        