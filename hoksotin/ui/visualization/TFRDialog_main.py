#Copyright (c) <2013>, <Kari Aliranta, Jaakko Leppäkangas, Janne Pesonen and Atte Rautio>
#All rights reserved.
#
#Redistribution and use in source and binary forms, with or without
#modification, are permitted provided that the following conditions are met: 
#
#1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer. 
#2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution. 
#
#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
#ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
#(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
#ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The views and conclusions contained in the software and documentation are those
#of the authors and should not be interpreted as representing official policies, 
#either expressed or implied, of the FreeBSD Project.

# coding: latin1
"""
Created on Apr 26, 2013

@author: Jaakko Leppakangas
Contains the TFRDialog-class used for creating TFRs.
"""
import messageBox

import mne

from PyQt4 import QtCore,QtGui
from TFRDialog_Ui import Ui_DialogEpochsTFR

class TFRDialog(QtGui.QDialog):
    """
    Class containing the logic for TFRDialog. Collects the necessary parameter
    values and passes them to the Caller-class.
    """
    
    def __init__(self, parent, raw, epoch):
        """
        Constructor. Sets up the dialog
        
        Keyword arguments:
        
        parent    --    Parent of the dialog
        raw       --    raw data file
        epoch     --    a collection of epochs
        """
        QtGui.QDialog.__init__(self)
        self.parent = parent
        self.raw = raw
        self.epoch = epoch
        ch_names = self.epoch.epochs.ch_names
        self.ui = Ui_DialogEpochsTFR()
        self.ui.setupUi(self)
        self.ui.comboBoxChannels.addItems(ch_names)
    
    def accept(self):
        """
        Collects parameters and calls the caller class to create a TFR.
        """
        minfreq = self.ui.doubleSpinBoxMinFreq.value()
        maxfreq = self.ui.doubleSpinBoxMaxFreq.value()
        ch_index = self.ui.comboBoxChannels.currentIndex()
        interval = self.ui.doubleSpinBoxFreqInterval.value()
        ncycles =  self.ui.spinBoxNcycles.value()
        decim = self.ui.spinBoxDecim.value()
        try:
            self.parent.caller.TFR(self.raw, self.epoch.epochs, ch_index,
                                   minfreq, maxfreq, interval, ncycles, decim)
        except Exception, err:
            self.messageBox = messageBox.AppForm()
            self.messageBox.labelException.setText(str(err))
            self.messageBox.show()
            return
        self.close()