# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TFRfromEpochs.ui'
#
# Created: Tue Apr 30 13:36:42 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogEpochsTFR(object):
    def setupUi(self, DialogEpochsTFR):
        DialogEpochsTFR.setObjectName(_fromUtf8("DialogEpochsTFR"))
        DialogEpochsTFR.resize(293, 314)
        self.verticalLayout_2 = QtGui.QVBoxLayout(DialogEpochsTFR)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(DialogEpochsTFR)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 275, 257))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(197, 134))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.groupBoxFrequencies = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxFrequencies.setGeometry(QtCore.QRect(0, 0, 241, 231))
        self.groupBoxFrequencies.setObjectName(_fromUtf8("groupBoxFrequencies"))
        self.layoutWidget = QtGui.QWidget(self.groupBoxFrequencies)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 221, 189))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.comboBoxChannels = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxChannels.setObjectName(_fromUtf8("comboBoxChannels"))
        self.verticalLayout_6.addWidget(self.comboBoxChannels)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.labelMinFreq = QtGui.QLabel(self.layoutWidget)
        self.labelMinFreq.setObjectName(_fromUtf8("labelMinFreq"))
        self.horizontalLayout_13.addWidget(self.labelMinFreq)
        self.doubleSpinBoxMinFreq = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMinFreq.setMinimum(7.0)
        self.doubleSpinBoxMinFreq.setMaximum(30.0)
        self.doubleSpinBoxMinFreq.setObjectName(_fromUtf8("doubleSpinBoxMinFreq"))
        self.horizontalLayout_13.addWidget(self.doubleSpinBoxMinFreq)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.labelMaxFreq = QtGui.QLabel(self.layoutWidget)
        self.labelMaxFreq.setObjectName(_fromUtf8("labelMaxFreq"))
        self.horizontalLayout_12.addWidget(self.labelMaxFreq)
        self.doubleSpinBoxMaxFreq = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMaxFreq.setMinimum(7.0)
        self.doubleSpinBoxMaxFreq.setMaximum(30.0)
        self.doubleSpinBoxMaxFreq.setProperty("value", 30.0)
        self.doubleSpinBoxMaxFreq.setObjectName(_fromUtf8("doubleSpinBoxMaxFreq"))
        self.horizontalLayout_12.addWidget(self.doubleSpinBoxMaxFreq)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelFrequencyInterval = QtGui.QLabel(self.layoutWidget)
        self.labelFrequencyInterval.setObjectName(_fromUtf8("labelFrequencyInterval"))
        self.horizontalLayout.addWidget(self.labelFrequencyInterval)
        self.doubleSpinBoxFreqInterval = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxFreqInterval.setMinimum(0.0)
        self.doubleSpinBoxFreqInterval.setMaximum(99.99)
        self.doubleSpinBoxFreqInterval.setProperty("value", 3.0)
        self.doubleSpinBoxFreqInterval.setObjectName(_fromUtf8("doubleSpinBoxFreqInterval"))
        self.horizontalLayout.addWidget(self.doubleSpinBoxFreqInterval)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelNcycles = QtGui.QLabel(self.layoutWidget)
        self.labelNcycles.setObjectName(_fromUtf8("labelNcycles"))
        self.horizontalLayout_2.addWidget(self.labelNcycles)
        self.doubleSpinBoxNcycles = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxNcycles.setProperty("value", 7.0)
        self.doubleSpinBoxNcycles.setObjectName(_fromUtf8("doubleSpinBoxNcycles"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxNcycles)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(DialogEpochsTFR)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogEpochsTFR)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogEpochsTFR.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogEpochsTFR.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogEpochsTFR)
        DialogEpochsTFR.setTabOrder(self.scrollArea, self.comboBoxChannels)
        DialogEpochsTFR.setTabOrder(self.comboBoxChannels, self.doubleSpinBoxMinFreq)
        DialogEpochsTFR.setTabOrder(self.doubleSpinBoxMinFreq, self.doubleSpinBoxMaxFreq)
        DialogEpochsTFR.setTabOrder(self.doubleSpinBoxMaxFreq, self.doubleSpinBoxFreqInterval)
        DialogEpochsTFR.setTabOrder(self.doubleSpinBoxFreqInterval, self.doubleSpinBoxNcycles)
        DialogEpochsTFR.setTabOrder(self.doubleSpinBoxNcycles, self.buttonBox)

    def retranslateUi(self, DialogEpochsTFR):
        DialogEpochsTFR.setWindowTitle(_translate("DialogEpochsTFR", "TFR from epochs", None))
        self.groupBoxFrequencies.setTitle(_translate("DialogEpochsTFR", "Frequency window", None))
        self.labelMinFreq.setText(_translate("DialogEpochsTFR", "Minimum frequency:", None))
        self.labelMaxFreq.setText(_translate("DialogEpochsTFR", "Maximum frequency:", None))
        self.labelFrequencyInterval.setText(_translate("DialogEpochsTFR", "Frequency interval:", None))
        self.labelNcycles.setText(_translate("DialogEpochsTFR", "Number of cycles:", None))
