# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epochDialog.ui'
#
# Created: Sat Jun  1 17:25:39 2013
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(412, 451)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelTmin = QtGui.QLabel(Dialog)
        self.labelTmin.setObjectName(_fromUtf8("labelTmin"))
        self.horizontalLayout_2.addWidget(self.labelTmin)
        self.doubleSpinBoxTmin = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxTmin.setMinimum(-10.0)
        self.doubleSpinBoxTmin.setSingleStep(0.1)
        self.doubleSpinBoxTmin.setProperty("value", -0.2)
        self.doubleSpinBoxTmin.setObjectName(_fromUtf8("doubleSpinBoxTmin"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxTmin)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelTmax = QtGui.QLabel(Dialog)
        self.labelTmax.setObjectName(_fromUtf8("labelTmax"))
        self.horizontalLayout.addWidget(self.labelTmax)
        self.doubleSpinBoxTmax = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxTmax.setMaximum(9.9)
        self.doubleSpinBoxTmax.setSingleStep(0.1)
        self.doubleSpinBoxTmax.setProperty("value", 0.5)
        self.doubleSpinBoxTmax.setObjectName(_fromUtf8("doubleSpinBoxTmax"))
        self.horizontalLayout.addWidget(self.doubleSpinBoxTmax)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelInclude = QtGui.QLabel(Dialog)
        self.labelInclude.setObjectName(_fromUtf8("labelInclude"))
        self.verticalLayout.addWidget(self.labelInclude)
        self.textEditInclude = QtGui.QTextEdit(Dialog)
        self.textEditInclude.setObjectName(_fromUtf8("textEditInclude"))
        self.verticalLayout.addWidget(self.textEditInclude)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.checkBoxMag = QtGui.QCheckBox(Dialog)
        self.checkBoxMag.setChecked(True)
        self.checkBoxMag.setObjectName(_fromUtf8("checkBoxMag"))
        self.horizontalLayout_6.addWidget(self.checkBoxMag)
        self.checkBoxGrad = QtGui.QCheckBox(Dialog)
        self.checkBoxGrad.setChecked(True)
        self.checkBoxGrad.setObjectName(_fromUtf8("checkBoxGrad"))
        self.horizontalLayout_6.addWidget(self.checkBoxGrad)
        self.checkBoxEeg = QtGui.QCheckBox(Dialog)
        self.checkBoxEeg.setChecked(True)
        self.checkBoxEeg.setObjectName(_fromUtf8("checkBoxEeg"))
        self.horizontalLayout_6.addWidget(self.checkBoxEeg)
        self.checkBoxStim = QtGui.QCheckBox(Dialog)
        self.checkBoxStim.setChecked(True)
        self.checkBoxStim.setObjectName(_fromUtf8("checkBoxStim"))
        self.horizontalLayout_6.addWidget(self.checkBoxStim)
        self.checkBoxEog = QtGui.QCheckBox(Dialog)
        self.checkBoxEog.setChecked(True)
        self.checkBoxEog.setObjectName(_fromUtf8("checkBoxEog"))
        self.horizontalLayout_6.addWidget(self.checkBoxEog)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelExclude = QtGui.QLabel(Dialog)
        self.labelExclude.setObjectName(_fromUtf8("labelExclude"))
        self.verticalLayout_2.addWidget(self.labelExclude)
        self.textEditExclude = QtGui.QTextEdit(Dialog)
        self.textEditExclude.setObjectName(_fromUtf8("textEditExclude"))
        self.verticalLayout_2.addWidget(self.textEditExclude)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelRejections = QtGui.QLabel(Dialog)
        self.labelRejections.setObjectName(_fromUtf8("labelRejections"))
        self.verticalLayout_3.addWidget(self.labelRejections)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.labelGradReject_3 = QtGui.QLabel(Dialog)
        self.labelGradReject_3.setObjectName(_fromUtf8("labelGradReject_3"))
        self.horizontalLayout_31.addWidget(self.labelGradReject_3)
        self.doubleSpinBoxGradReject_3 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxGradReject_3.setPrefix(_fromUtf8(""))
        self.doubleSpinBoxGradReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxGradReject_3.setProperty("value", 4000.0)
        self.doubleSpinBoxGradReject_3.setObjectName(_fromUtf8("doubleSpinBoxGradReject_3"))
        self.horizontalLayout_31.addWidget(self.doubleSpinBoxGradReject_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.labelEegReject_3 = QtGui.QLabel(Dialog)
        self.labelEegReject_3.setObjectName(_fromUtf8("labelEegReject_3"))
        self.horizontalLayout_32.addWidget(self.labelEegReject_3)
        self.doubleSpinBoxEEGReject_3 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxEEGReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxEEGReject_3.setProperty("value", 40.0)
        self.doubleSpinBoxEEGReject_3.setObjectName(_fromUtf8("doubleSpinBoxEEGReject_3"))
        self.horizontalLayout_32.addWidget(self.doubleSpinBoxEEGReject_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_30.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.labelMagReject_3 = QtGui.QLabel(Dialog)
        self.labelMagReject_3.setObjectName(_fromUtf8("labelMagReject_3"))
        self.horizontalLayout_33.addWidget(self.labelMagReject_3)
        self.doubleSpinBoxMagReject_3 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxMagReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxMagReject_3.setProperty("value", 4000.0)
        self.doubleSpinBoxMagReject_3.setObjectName(_fromUtf8("doubleSpinBoxMagReject_3"))
        self.horizontalLayout_33.addWidget(self.doubleSpinBoxMagReject_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.labelEogReject_3 = QtGui.QLabel(Dialog)
        self.labelEogReject_3.setObjectName(_fromUtf8("labelEogReject_3"))
        self.horizontalLayout_34.addWidget(self.labelEogReject_3)
        self.doubleSpinBoxEOGReject_3 = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxEOGReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxEOGReject_3.setProperty("value", 250.0)
        self.doubleSpinBoxEOGReject_3.setObjectName(_fromUtf8("doubleSpinBoxEOGReject_3"))
        self.horizontalLayout_34.addWidget(self.doubleSpinBoxEOGReject_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_30.addLayout(self.verticalLayout_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_30)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QObject.connect(self.checkBoxMag, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.doubleSpinBoxMagReject_3.setEnabled)
        QtCore.QObject.connect(self.checkBoxGrad, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.doubleSpinBoxGradReject_3.setEnabled)
        QtCore.QObject.connect(self.checkBoxEeg, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.doubleSpinBoxEEGReject_3.setEnabled)
        QtCore.QObject.connect(self.checkBoxEog, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.doubleSpinBoxEOGReject_3.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Meggie - Epoch creation", None))
        self.labelTmin.setText(_translate("Dialog", "Start time:", None))
        self.labelTmax.setText(_translate("Dialog", "End time:", None))
        self.labelInclude.setText(_translate("Dialog", "Include:", None))
        self.checkBoxMag.setText(_translate("Dialog", "mag", None))
        self.checkBoxGrad.setText(_translate("Dialog", "grad", None))
        self.checkBoxEeg.setText(_translate("Dialog", "eeg", None))
        self.checkBoxStim.setText(_translate("Dialog", "stim", None))
        self.checkBoxEog.setText(_translate("Dialog", "eog", None))
        self.labelExclude.setText(_translate("Dialog", "Exclude:", None))
        self.labelRejections.setText(_translate("Dialog", "Rejection parameters", None))
        self.labelGradReject_3.setText(_translate("Dialog", "Grad:", None))
        self.doubleSpinBoxGradReject_3.setSuffix(_translate("Dialog", " fT/cm", None))
        self.labelEegReject_3.setText(_translate("Dialog", "EEG:", None))
        self.doubleSpinBoxEEGReject_3.setSuffix(_translate("Dialog", " uV", None))
        self.labelMagReject_3.setText(_translate("Dialog", "Mag:", None))
        self.doubleSpinBoxMagReject_3.setSuffix(_translate("Dialog", " fT", None))
        self.labelEogReject_3.setText(_translate("Dialog", "EOG:", None))
        self.doubleSpinBoxEOGReject_3.setSuffix(_translate("Dialog", " uV", None))
