# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventSelectionDialog.ui'
#
# Created: Wed Sep 18 12:46:11 2013
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

class Ui_EventSelectionDialog(object):
    def setupUi(self, EventSelectionDialog):
        EventSelectionDialog.setObjectName(_fromUtf8("EventSelectionDialog"))
        EventSelectionDialog.setWindowModality(QtCore.Qt.WindowModal)
        EventSelectionDialog.resize(828, 508)
        self.gridLayout = QtGui.QGridLayout(EventSelectionDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(600, 0, -1, -1)
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.pushButtonCancel = QtGui.QPushButton(EventSelectionDialog)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_10.addWidget(self.pushButtonCancel)
        self.pushButtonCreateEpochs = QtGui.QPushButton(EventSelectionDialog)
        self.pushButtonCreateEpochs.setObjectName(_fromUtf8("pushButtonCreateEpochs"))
        self.horizontalLayout_10.addWidget(self.pushButtonCreateEpochs)
        self.gridLayout.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(EventSelectionDialog)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 810, 451))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(741, 400))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.layoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 0, 766, 444))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.labelName = QtGui.QLabel(self.layoutWidget)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.horizontalLayout_5.addWidget(self.labelName)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lineEditName = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.horizontalLayout_5.addWidget(self.lineEditName)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 2, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.labelEventID = QtGui.QLabel(self.layoutWidget)
        self.labelEventID.setObjectName(_fromUtf8("labelEventID"))
        self.horizontalLayout_7.addWidget(self.labelEventID)
        self.comboBoxEventID = QtGui.QComboBox(self.layoutWidget)
        self.comboBoxEventID.setObjectName(_fromUtf8("comboBoxEventID"))
        self.horizontalLayout_7.addWidget(self.comboBoxEventID)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.pushButtonAdd = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.horizontalLayout_9.addWidget(self.pushButtonAdd)
        self.pushButtonRemove = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonRemove.setEnabled(False)
        self.pushButtonRemove.setObjectName(_fromUtf8("pushButtonRemove"))
        self.horizontalLayout_9.addWidget(self.pushButtonRemove)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelCollectionName = QtGui.QLabel(self.layoutWidget)
        self.labelCollectionName.setObjectName(_fromUtf8("labelCollectionName"))
        self.horizontalLayout.addWidget(self.labelCollectionName)
        self.lineEditCollectionName = QtGui.QLineEdit(self.layoutWidget)
        self.lineEditCollectionName.setObjectName(_fromUtf8("lineEditCollectionName"))
        self.horizontalLayout.addWidget(self.lineEditCollectionName)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_11.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelTmin = QtGui.QLabel(self.layoutWidget)
        self.labelTmin.setObjectName(_fromUtf8("labelTmin"))
        self.horizontalLayout_2.addWidget(self.labelTmin)
        self.doubleSpinBoxTmin = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxTmin.setDecimals(3)
        self.doubleSpinBoxTmin.setMinimum(-10.0)
        self.doubleSpinBoxTmin.setSingleStep(0.1)
        self.doubleSpinBoxTmin.setProperty("value", -0.2)
        self.doubleSpinBoxTmin.setObjectName(_fromUtf8("doubleSpinBoxTmin"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxTmin)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelTmax = QtGui.QLabel(self.layoutWidget)
        self.labelTmax.setObjectName(_fromUtf8("labelTmax"))
        self.horizontalLayout_3.addWidget(self.labelTmax)
        self.doubleSpinBoxTmax = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxTmax.setDecimals(3)
        self.doubleSpinBoxTmax.setMaximum(9.9)
        self.doubleSpinBoxTmax.setSingleStep(0.1)
        self.doubleSpinBoxTmax.setProperty("value", 0.5)
        self.doubleSpinBoxTmax.setObjectName(_fromUtf8("doubleSpinBoxTmax"))
        self.horizontalLayout_3.addWidget(self.doubleSpinBoxTmax)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.checkBoxMag = QtGui.QCheckBox(self.layoutWidget)
        self.checkBoxMag.setChecked(True)
        self.checkBoxMag.setObjectName(_fromUtf8("checkBoxMag"))
        self.horizontalLayout_6.addWidget(self.checkBoxMag)
        self.checkBoxGrad = QtGui.QCheckBox(self.layoutWidget)
        self.checkBoxGrad.setChecked(True)
        self.checkBoxGrad.setObjectName(_fromUtf8("checkBoxGrad"))
        self.horizontalLayout_6.addWidget(self.checkBoxGrad)
        self.checkBoxEeg = QtGui.QCheckBox(self.layoutWidget)
        self.checkBoxEeg.setChecked(False)
        self.checkBoxEeg.setObjectName(_fromUtf8("checkBoxEeg"))
        self.horizontalLayout_6.addWidget(self.checkBoxEeg)
        self.checkBoxStim = QtGui.QCheckBox(self.layoutWidget)
        self.checkBoxStim.setChecked(False)
        self.checkBoxStim.setObjectName(_fromUtf8("checkBoxStim"))
        self.horizontalLayout_6.addWidget(self.checkBoxStim)
        self.checkBoxEog = QtGui.QCheckBox(self.layoutWidget)
        self.checkBoxEog.setChecked(False)
        self.checkBoxEog.setObjectName(_fromUtf8("checkBoxEog"))
        self.horizontalLayout_6.addWidget(self.checkBoxEog)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_9)
        self.verticalLayout_11.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.labelRejections = QtGui.QLabel(self.layoutWidget)
        self.labelRejections.setObjectName(_fromUtf8("labelRejections"))
        self.verticalLayout_3.addWidget(self.labelRejections)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.labelGradReject_3 = QtGui.QLabel(self.layoutWidget)
        self.labelGradReject_3.setObjectName(_fromUtf8("labelGradReject_3"))
        self.horizontalLayout_31.addWidget(self.labelGradReject_3)
        self.doubleSpinBoxGradReject_3 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxGradReject_3.setPrefix(_fromUtf8(""))
        self.doubleSpinBoxGradReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxGradReject_3.setProperty("value", 3000.0)
        self.doubleSpinBoxGradReject_3.setObjectName(_fromUtf8("doubleSpinBoxGradReject_3"))
        self.horizontalLayout_31.addWidget(self.doubleSpinBoxGradReject_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.labelEegReject_3 = QtGui.QLabel(self.layoutWidget)
        self.labelEegReject_3.setObjectName(_fromUtf8("labelEegReject_3"))
        self.horizontalLayout_32.addWidget(self.labelEegReject_3)
        self.doubleSpinBoxEEGReject_3 = QtGui.QDoubleSpinBox(self.layoutWidget)
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
        self.labelMagReject_3 = QtGui.QLabel(self.layoutWidget)
        self.labelMagReject_3.setObjectName(_fromUtf8("labelMagReject_3"))
        self.horizontalLayout_33.addWidget(self.labelMagReject_3)
        self.doubleSpinBoxMagReject_3 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxMagReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxMagReject_3.setProperty("value", 4000.0)
        self.doubleSpinBoxMagReject_3.setObjectName(_fromUtf8("doubleSpinBoxMagReject_3"))
        self.horizontalLayout_33.addWidget(self.doubleSpinBoxMagReject_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.labelEogReject_3 = QtGui.QLabel(self.layoutWidget)
        self.labelEogReject_3.setObjectName(_fromUtf8("labelEogReject_3"))
        self.horizontalLayout_34.addWidget(self.labelEogReject_3)
        self.doubleSpinBoxEOGReject_3 = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxEOGReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxEOGReject_3.setProperty("value", 250.0)
        self.doubleSpinBoxEOGReject_3.setObjectName(_fromUtf8("doubleSpinBoxEOGReject_3"))
        self.horizontalLayout_34.addWidget(self.doubleSpinBoxEOGReject_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_30.addLayout(self.verticalLayout_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout_30)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_11.addLayout(self.verticalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_11)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.listWidgetEvents = QtGui.QListWidget(self.layoutWidget)
        self.listWidgetEvents.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidgetEvents.setObjectName(_fromUtf8("listWidgetEvents"))
        self.verticalLayout_4.addWidget(self.listWidgetEvents)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.pushButtonSaveEvents = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonSaveEvents.setObjectName(_fromUtf8("pushButtonSaveEvents"))
        self.horizontalLayout_8.addWidget(self.pushButtonSaveEvents)
        self.pushButtonReadEvents = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonReadEvents.setObjectName(_fromUtf8("pushButtonReadEvents"))
        self.horizontalLayout_8.addWidget(self.pushButtonReadEvents)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.retranslateUi(EventSelectionDialog)
        QtCore.QObject.connect(self.pushButtonCreateEpochs, QtCore.SIGNAL(_fromUtf8("clicked()")), EventSelectionDialog.accept)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), EventSelectionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EventSelectionDialog)
        EventSelectionDialog.setTabOrder(self.scrollArea, self.comboBoxEventID)
        EventSelectionDialog.setTabOrder(self.comboBoxEventID, self.lineEditName)
        EventSelectionDialog.setTabOrder(self.lineEditName, self.pushButtonAdd)
        EventSelectionDialog.setTabOrder(self.pushButtonAdd, self.pushButtonRemove)
        EventSelectionDialog.setTabOrder(self.pushButtonRemove, self.lineEditCollectionName)
        EventSelectionDialog.setTabOrder(self.lineEditCollectionName, self.doubleSpinBoxTmin)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxTmin, self.doubleSpinBoxTmax)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxTmax, self.checkBoxMag)
        EventSelectionDialog.setTabOrder(self.checkBoxMag, self.checkBoxGrad)
        EventSelectionDialog.setTabOrder(self.checkBoxGrad, self.checkBoxEeg)
        EventSelectionDialog.setTabOrder(self.checkBoxEeg, self.checkBoxStim)
        EventSelectionDialog.setTabOrder(self.checkBoxStim, self.checkBoxEog)
        EventSelectionDialog.setTabOrder(self.checkBoxEog, self.doubleSpinBoxGradReject_3)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxGradReject_3, self.doubleSpinBoxMagReject_3)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxMagReject_3, self.doubleSpinBoxEEGReject_3)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxEEGReject_3, self.doubleSpinBoxEOGReject_3)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxEOGReject_3, self.pushButtonSaveEvents)
        EventSelectionDialog.setTabOrder(self.pushButtonSaveEvents, self.pushButtonReadEvents)
        EventSelectionDialog.setTabOrder(self.pushButtonReadEvents, self.pushButtonCancel)
        EventSelectionDialog.setTabOrder(self.pushButtonCancel, self.pushButtonCreateEpochs)
        EventSelectionDialog.setTabOrder(self.pushButtonCreateEpochs, self.listWidgetEvents)

    def retranslateUi(self, EventSelectionDialog):
        EventSelectionDialog.setWindowTitle(_translate("EventSelectionDialog", "Meggie - Epoch Creation", None))
        self.pushButtonCancel.setText(_translate("EventSelectionDialog", "Cancel", None))
        self.pushButtonCreateEpochs.setText(_translate("EventSelectionDialog", "Create epochs", None))
        self.labelName.setText(_translate("EventSelectionDialog", "Event name:      ", None))
        self.labelEventID.setText(_translate("EventSelectionDialog", "Event ID:", None))
        self.pushButtonAdd.setText(_translate("EventSelectionDialog", "Add to list >>", None))
        self.pushButtonRemove.setText(_translate("EventSelectionDialog", "<< Remove", None))
        self.labelCollectionName.setText(_translate("EventSelectionDialog", "Collection name:", None))
        self.lineEditCollectionName.setText(_translate("EventSelectionDialog", "Epochs", None))
        self.labelTmin.setText(_translate("EventSelectionDialog", "Start time:", None))
        self.doubleSpinBoxTmin.setSuffix(_translate("EventSelectionDialog", " s", None))
        self.labelTmax.setText(_translate("EventSelectionDialog", "End time:", None))
        self.doubleSpinBoxTmax.setSuffix(_translate("EventSelectionDialog", " s", None))
        self.checkBoxMag.setText(_translate("EventSelectionDialog", "mag", None))
        self.checkBoxGrad.setText(_translate("EventSelectionDialog", "grad", None))
        self.checkBoxEeg.setText(_translate("EventSelectionDialog", "eeg", None))
        self.checkBoxStim.setText(_translate("EventSelectionDialog", "stim", None))
        self.checkBoxEog.setText(_translate("EventSelectionDialog", "eog", None))
        self.labelRejections.setText(_translate("EventSelectionDialog", "Rejection parameters", None))
        self.labelGradReject_3.setText(_translate("EventSelectionDialog", "Grad:", None))
        self.doubleSpinBoxGradReject_3.setSuffix(_translate("EventSelectionDialog", " fT/cm", None))
        self.labelEegReject_3.setText(_translate("EventSelectionDialog", "EEG:", None))
        self.doubleSpinBoxEEGReject_3.setSuffix(_translate("EventSelectionDialog", " uV", None))
        self.labelMagReject_3.setText(_translate("EventSelectionDialog", "Mag:", None))
        self.doubleSpinBoxMagReject_3.setSuffix(_translate("EventSelectionDialog", " fT", None))
        self.labelEogReject_3.setText(_translate("EventSelectionDialog", "EOG:", None))
        self.doubleSpinBoxEOGReject_3.setSuffix(_translate("EventSelectionDialog", " uV", None))
        self.pushButtonSaveEvents.setText(_translate("EventSelectionDialog", "Save events to file...", None))
        self.pushButtonReadEvents.setText(_translate("EventSelectionDialog", "Read events from file...", None))

