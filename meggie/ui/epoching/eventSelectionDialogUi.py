# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eventSelectionDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EventSelectionDialog(object):
    def setupUi(self, EventSelectionDialog):
        EventSelectionDialog.setObjectName("EventSelectionDialog")
        EventSelectionDialog.setWindowModality(QtCore.Qt.WindowModal)
        EventSelectionDialog.resize(763, 977)
        self.gridLayout = QtWidgets.QGridLayout(EventSelectionDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(EventSelectionDialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_10.addWidget(self.pushButtonCancel)
        self.pushButtonComputeBatch = QtWidgets.QPushButton(EventSelectionDialog)
        self.pushButtonComputeBatch.setObjectName("pushButtonComputeBatch")
        self.horizontalLayout_10.addWidget(self.pushButtonComputeBatch)
        self.pushButtonCompute = QtWidgets.QPushButton(EventSelectionDialog)
        self.pushButtonCompute.setObjectName("pushButtonCompute")
        self.horizontalLayout_10.addWidget(self.pushButtonCompute)
        self.gridLayout.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(EventSelectionDialog)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 745, 928))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(700, 850))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.pushButtonFixedLength = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButtonFixedLength.setGeometry(QtCore.QRect(570, 430, 151, 31))
        self.pushButtonFixedLength.setObjectName("pushButtonFixedLength")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(350, 200, 381, 231))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.listWidgetEvents = QtWidgets.QListWidget(self.groupBox)
        self.listWidgetEvents.setObjectName("listWidgetEvents")
        self.gridLayout_3.addWidget(self.listWidgetEvents, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(30, 460, 311, 441))
        self.widget.setObjectName("widget")
        self.groupBoxEvent = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxEvent.setGeometry(QtCore.QRect(10, 200, 331, 181))
        self.groupBoxEvent.setObjectName("groupBoxEvent")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBoxEvent)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonAdd = QtWidgets.QPushButton(self.groupBoxEvent)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.gridLayout_2.addWidget(self.pushButtonAdd, 2, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.spinBoxEventID = QtWidgets.QSpinBox(self.groupBoxEvent)
        self.spinBoxEventID.setMinimum(0)
        self.spinBoxEventID.setMaximum(999999)
        self.spinBoxEventID.setObjectName("spinBoxEventID")
        self.gridLayout_5.addWidget(self.spinBoxEventID, 0, 1, 1, 1)
        self.labelEventID = QtWidgets.QLabel(self.groupBoxEvent)
        self.labelEventID.setObjectName("labelEventID")
        self.gridLayout_5.addWidget(self.labelEventID, 0, 0, 1, 1)
        self.labelMask = QtWidgets.QLabel(self.groupBoxEvent)
        self.labelMask.setObjectName("labelMask")
        self.gridLayout_5.addWidget(self.labelMask, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditMask = QtWidgets.QLineEdit(self.groupBoxEvent)
        self.lineEditMask.setObjectName("lineEditMask")
        self.horizontalLayout_4.addWidget(self.lineEditMask)
        self.gridLayout_5.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.pushButtonEdit = QtWidgets.QPushButton(self.groupBoxEvent)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.gridLayout_5.addWidget(self.pushButtonEdit, 0, 2, 1, 1)
        self.pushButtonHelp = QtWidgets.QPushButton(self.groupBoxEvent)
        self.pushButtonHelp.setObjectName("pushButtonHelp")
        self.gridLayout_5.addWidget(self.pushButtonHelp, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.pushButtonClear = QtWidgets.QPushButton(self.groupBoxEvent)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.gridLayout_2.addWidget(self.pushButtonClear, 3, 0, 1, 1)
        self.groupBoxRejection = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxRejection.setGeometry(QtCore.QRect(350, 10, 381, 191))
        self.groupBoxRejection.setObjectName("groupBoxRejection")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBoxRejection)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.checkBoxGrad = QtWidgets.QCheckBox(self.groupBoxRejection)
        self.checkBoxGrad.setChecked(True)
        self.checkBoxGrad.setObjectName("checkBoxGrad")
        self.horizontalLayout_31.addWidget(self.checkBoxGrad)
        self.doubleSpinBoxGradReject_3 = QtWidgets.QDoubleSpinBox(self.groupBoxRejection)
        self.doubleSpinBoxGradReject_3.setPrefix("")
        self.doubleSpinBoxGradReject_3.setMinimum(-1.0)
        self.doubleSpinBoxGradReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxGradReject_3.setSingleStep(100.0)
        self.doubleSpinBoxGradReject_3.setProperty("value", 3000.0)
        self.doubleSpinBoxGradReject_3.setObjectName("doubleSpinBoxGradReject_3")
        self.horizontalLayout_31.addWidget(self.doubleSpinBoxGradReject_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        self.checkBoxMag = QtWidgets.QCheckBox(self.groupBoxRejection)
        self.checkBoxMag.setChecked(True)
        self.checkBoxMag.setObjectName("checkBoxMag")
        self.horizontalLayout_33.addWidget(self.checkBoxMag)
        self.doubleSpinBoxMagReject_3 = QtWidgets.QDoubleSpinBox(self.groupBoxRejection)
        self.doubleSpinBoxMagReject_3.setMinimum(-1.0)
        self.doubleSpinBoxMagReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxMagReject_3.setSingleStep(100.0)
        self.doubleSpinBoxMagReject_3.setProperty("value", 4000.0)
        self.doubleSpinBoxMagReject_3.setObjectName("doubleSpinBoxMagReject_3")
        self.horizontalLayout_33.addWidget(self.doubleSpinBoxMagReject_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_33)
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.checkBoxEeg = QtWidgets.QCheckBox(self.groupBoxRejection)
        self.checkBoxEeg.setChecked(False)
        self.checkBoxEeg.setObjectName("checkBoxEeg")
        self.horizontalLayout_32.addWidget(self.checkBoxEeg)
        self.doubleSpinBoxEEGReject_3 = QtWidgets.QDoubleSpinBox(self.groupBoxRejection)
        self.doubleSpinBoxEEGReject_3.setEnabled(False)
        self.doubleSpinBoxEEGReject_3.setMinimum(-1.0)
        self.doubleSpinBoxEEGReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxEEGReject_3.setProperty("value", 70.0)
        self.doubleSpinBoxEEGReject_3.setObjectName("doubleSpinBoxEEGReject_3")
        self.horizontalLayout_32.addWidget(self.doubleSpinBoxEEGReject_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        self.checkBoxEog = QtWidgets.QCheckBox(self.groupBoxRejection)
        self.checkBoxEog.setChecked(False)
        self.checkBoxEog.setObjectName("checkBoxEog")
        self.horizontalLayout_34.addWidget(self.checkBoxEog)
        self.doubleSpinBoxEOGReject_3 = QtWidgets.QDoubleSpinBox(self.groupBoxRejection)
        self.doubleSpinBoxEOGReject_3.setEnabled(False)
        self.doubleSpinBoxEOGReject_3.setMinimum(-1.0)
        self.doubleSpinBoxEOGReject_3.setMaximum(1000000000.0)
        self.doubleSpinBoxEOGReject_3.setProperty("value", 250.0)
        self.doubleSpinBoxEOGReject_3.setObjectName("doubleSpinBoxEOGReject_3")
        self.horizontalLayout_34.addWidget(self.doubleSpinBoxEOGReject_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_34)
        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.groupBoxEpoch = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBoxEpoch.setGeometry(QtCore.QRect(12, 8, 331, 191))
        self.groupBoxEpoch.setObjectName("groupBoxEpoch")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBoxEpoch)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelCollectionName = QtWidgets.QLabel(self.groupBoxEpoch)
        self.labelCollectionName.setObjectName("labelCollectionName")
        self.horizontalLayout.addWidget(self.labelCollectionName)
        self.lineEditCollectionName = QtWidgets.QLineEdit(self.groupBoxEpoch)
        self.lineEditCollectionName.setObjectName("lineEditCollectionName")
        self.horizontalLayout.addWidget(self.lineEditCollectionName)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTmin = QtWidgets.QLabel(self.groupBoxEpoch)
        self.labelTmin.setObjectName("labelTmin")
        self.horizontalLayout_2.addWidget(self.labelTmin)
        self.doubleSpinBoxTmin = QtWidgets.QDoubleSpinBox(self.groupBoxEpoch)
        self.doubleSpinBoxTmin.setDecimals(3)
        self.doubleSpinBoxTmin.setMinimum(-10.0)
        self.doubleSpinBoxTmin.setSingleStep(0.1)
        self.doubleSpinBoxTmin.setProperty("value", -0.2)
        self.doubleSpinBoxTmin.setObjectName("doubleSpinBoxTmin")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxTmin)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelTmax = QtWidgets.QLabel(self.groupBoxEpoch)
        self.labelTmax.setObjectName("labelTmax")
        self.horizontalLayout_3.addWidget(self.labelTmax)
        self.doubleSpinBoxTmax = QtWidgets.QDoubleSpinBox(self.groupBoxEpoch)
        self.doubleSpinBoxTmax.setDecimals(3)
        self.doubleSpinBoxTmax.setMaximum(9.9)
        self.doubleSpinBoxTmax.setSingleStep(0.1)
        self.doubleSpinBoxTmax.setProperty("value", 0.5)
        self.doubleSpinBoxTmax.setObjectName("doubleSpinBoxTmax")
        self.horizontalLayout_3.addWidget(self.doubleSpinBoxTmax)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelBaselineStart = QtWidgets.QLabel(self.groupBoxEpoch)
        self.labelBaselineStart.setObjectName("labelBaselineStart")
        self.horizontalLayout_5.addWidget(self.labelBaselineStart)
        self.doubleSpinBoxBaselineStart = QtWidgets.QDoubleSpinBox(self.groupBoxEpoch)
        self.doubleSpinBoxBaselineStart.setDecimals(3)
        self.doubleSpinBoxBaselineStart.setMinimum(-10.0)
        self.doubleSpinBoxBaselineStart.setProperty("value", -0.2)
        self.doubleSpinBoxBaselineStart.setObjectName("doubleSpinBoxBaselineStart")
        self.horizontalLayout_5.addWidget(self.doubleSpinBoxBaselineStart)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelBaselineEnd = QtWidgets.QLabel(self.groupBoxEpoch)
        self.labelBaselineEnd.setObjectName("labelBaselineEnd")
        self.horizontalLayout_6.addWidget(self.labelBaselineEnd)
        self.doubleSpinBoxBaselineEnd = QtWidgets.QDoubleSpinBox(self.groupBoxEpoch)
        self.doubleSpinBoxBaselineEnd.setDecimals(3)
        self.doubleSpinBoxBaselineEnd.setMinimum(-10.0)
        self.doubleSpinBoxBaselineEnd.setProperty("value", 0.0)
        self.doubleSpinBoxBaselineEnd.setObjectName("doubleSpinBoxBaselineEnd")
        self.horizontalLayout_6.addWidget(self.doubleSpinBoxBaselineEnd)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.groupBox.raise_()
        self.widget.raise_()
        self.groupBoxEvent.raise_()
        self.groupBoxRejection.raise_()
        self.groupBoxEpoch.raise_()
        self.pushButtonFixedLength.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(EventSelectionDialog)
        self.pushButtonCompute.clicked.connect(EventSelectionDialog.accept)
        self.pushButtonCancel.clicked.connect(EventSelectionDialog.reject)
        self.checkBoxGrad.toggled['bool'].connect(self.doubleSpinBoxGradReject_3.setEnabled)
        self.checkBoxMag.toggled['bool'].connect(self.doubleSpinBoxMagReject_3.setEnabled)
        self.checkBoxEeg.toggled['bool'].connect(self.doubleSpinBoxEEGReject_3.setEnabled)
        self.checkBoxEog.toggled['bool'].connect(self.doubleSpinBoxEOGReject_3.setEnabled)
        self.pushButtonComputeBatch.clicked.connect(EventSelectionDialog.acceptBatch)
        QtCore.QMetaObject.connectSlotsByName(EventSelectionDialog)
        EventSelectionDialog.setTabOrder(self.scrollArea, self.lineEditCollectionName)
        EventSelectionDialog.setTabOrder(self.lineEditCollectionName, self.doubleSpinBoxTmin)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxTmin, self.doubleSpinBoxTmax)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxTmax, self.checkBoxGrad)
        EventSelectionDialog.setTabOrder(self.checkBoxGrad, self.doubleSpinBoxGradReject_3)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxGradReject_3, self.checkBoxMag)
        EventSelectionDialog.setTabOrder(self.checkBoxMag, self.doubleSpinBoxMagReject_3)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxMagReject_3, self.checkBoxEeg)
        EventSelectionDialog.setTabOrder(self.checkBoxEeg, self.doubleSpinBoxEEGReject_3)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxEEGReject_3, self.checkBoxEog)
        EventSelectionDialog.setTabOrder(self.checkBoxEog, self.doubleSpinBoxEOGReject_3)
        EventSelectionDialog.setTabOrder(self.doubleSpinBoxEOGReject_3, self.pushButtonCancel)
        EventSelectionDialog.setTabOrder(self.pushButtonCancel, self.pushButtonCompute)

    def retranslateUi(self, EventSelectionDialog):
        _translate = QtCore.QCoreApplication.translate
        EventSelectionDialog.setWindowTitle(_translate("EventSelectionDialog", "Meggie - Epoch Creation"))
        self.pushButtonCancel.setText(_translate("EventSelectionDialog", "Cancel"))
        self.pushButtonComputeBatch.setText(_translate("EventSelectionDialog", "Batch epochs"))
        self.pushButtonCompute.setText(_translate("EventSelectionDialog", "Create epochs"))
        self.pushButtonFixedLength.setText(_translate("EventSelectionDialog", "Fixed length events..."))
        self.groupBox.setTitle(_translate("EventSelectionDialog", "List of given <event ID>, <event name>"))
        self.groupBoxEvent.setTitle(_translate("EventSelectionDialog", "Select events to include in epoch collection"))
        self.pushButtonAdd.setText(_translate("EventSelectionDialog", "Add to list >>"))
        self.labelEventID.setText(_translate("EventSelectionDialog", "Event ID:"))
        self.labelMask.setText(_translate("EventSelectionDialog", "Mask:"))
        self.lineEditMask.setText(_translate("EventSelectionDialog", "0"))
        self.pushButtonEdit.setText(_translate("EventSelectionDialog", "Edit..."))
        self.pushButtonHelp.setText(_translate("EventSelectionDialog", "Help..."))
        self.pushButtonClear.setText(_translate("EventSelectionDialog", "Clear list <<"))
        self.groupBoxRejection.setTitle(_translate("EventSelectionDialog", "Rejection parameters"))
        self.checkBoxGrad.setToolTip(_translate("EventSelectionDialog", "Include or exclude grad channels"))
        self.checkBoxGrad.setText(_translate("EventSelectionDialog", "Grad"))
        self.doubleSpinBoxGradReject_3.setSuffix(_translate("EventSelectionDialog", " fT/cm"))
        self.checkBoxMag.setToolTip(_translate("EventSelectionDialog", "Include or exclude mag channels"))
        self.checkBoxMag.setText(_translate("EventSelectionDialog", "Mag"))
        self.doubleSpinBoxMagReject_3.setSuffix(_translate("EventSelectionDialog", " fT"))
        self.checkBoxEeg.setToolTip(_translate("EventSelectionDialog", "Include or exclude eeg channels"))
        self.checkBoxEeg.setText(_translate("EventSelectionDialog", "EEG"))
        self.doubleSpinBoxEEGReject_3.setSuffix(_translate("EventSelectionDialog", " uV"))
        self.checkBoxEog.setToolTip(_translate("EventSelectionDialog", "Include or exclude eog channels"))
        self.checkBoxEog.setText(_translate("EventSelectionDialog", "EOG"))
        self.doubleSpinBoxEOGReject_3.setSuffix(_translate("EventSelectionDialog", " uV"))
        self.groupBoxEpoch.setTitle(_translate("EventSelectionDialog", "Epoch collection"))
        self.labelCollectionName.setText(_translate("EventSelectionDialog", "Collection name:"))
        self.lineEditCollectionName.setText(_translate("EventSelectionDialog", "Epochs"))
        self.labelTmin.setText(_translate("EventSelectionDialog", "Start time:"))
        self.doubleSpinBoxTmin.setSuffix(_translate("EventSelectionDialog", " s"))
        self.labelTmax.setText(_translate("EventSelectionDialog", "End time:"))
        self.doubleSpinBoxTmax.setSuffix(_translate("EventSelectionDialog", " s"))
        self.labelBaselineStart.setText(_translate("EventSelectionDialog", "Baseline start:"))
        self.doubleSpinBoxBaselineStart.setSuffix(_translate("EventSelectionDialog", "s"))
        self.labelBaselineEnd.setText(_translate("EventSelectionDialog", "Baseline end:"))
        self.doubleSpinBoxBaselineEnd.setSuffix(_translate("EventSelectionDialog", "s"))

