# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ecgParametersDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(524, 931)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.pushButtonPlotEvents = QtWidgets.QPushButton(Dialog)
        self.pushButtonPlotEvents.setObjectName("pushButtonPlotEvents")
        self.horizontalLayout_19.addWidget(self.pushButtonPlotEvents)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_19.addWidget(self.pushButtonCancel)
        self.pushButtonComputeBatch = QtWidgets.QPushButton(Dialog)
        self.pushButtonComputeBatch.setObjectName("pushButtonComputeBatch")
        self.horizontalLayout_19.addWidget(self.pushButtonComputeBatch)
        self.pushButtonCompute = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCompute.sizePolicy().hasHeightForWidth())
        self.pushButtonCompute.setSizePolicy(sizePolicy)
        self.pushButtonCompute.setObjectName("pushButtonCompute")
        self.horizontalLayout_19.addWidget(self.pushButtonCompute)
        self.gridLayout.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 506, 874))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(500, 860))
        self.scrollAreaWidgetContents_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.tabWidgetECGSettings = QtWidgets.QTabWidget(self.scrollAreaWidgetContents_2)
        self.tabWidgetECGSettings.setGeometry(QtCore.QRect(0, 0, 501, 471))
        self.tabWidgetECGSettings.setObjectName("tabWidgetECGSettings")
        self.tabECG1 = QtWidgets.QWidget()
        self.tabECG1.setObjectName("tabECG1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tabECG1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.labelECGChannel = QtWidgets.QLabel(self.tabECG1)
        self.labelECGChannel.setObjectName("labelECGChannel")
        self.horizontalLayout_10.addWidget(self.labelECGChannel)
        self.comboBoxECGChannel = QtWidgets.QComboBox(self.tabECG1)
        self.comboBoxECGChannel.setObjectName("comboBoxECGChannel")
        self.horizontalLayout_10.addWidget(self.comboBoxECGChannel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.groupBoxEvent = QtWidgets.QGroupBox(self.tabECG1)
        self.groupBoxEvent.setObjectName("groupBoxEvent")
        self.formLayout_4 = QtWidgets.QFormLayout(self.groupBoxEvent)
        self.formLayout_4.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName("formLayout_4")
        self.frame = QtWidgets.QFrame(self.groupBoxEvent)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame)
        self.formLayout_3.setObjectName("formLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelTmin = QtWidgets.QLabel(self.frame)
        self.labelTmin.setObjectName("labelTmin")
        self.horizontalLayout.addWidget(self.labelTmin)
        self.doubleSpinBoxTmin = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxTmin.setDecimals(3)
        self.doubleSpinBoxTmin.setMinimum(-99.99)
        self.doubleSpinBoxTmin.setSingleStep(0.05)
        self.doubleSpinBoxTmin.setProperty("value", -0.1)
        self.doubleSpinBoxTmin.setObjectName("doubleSpinBoxTmin")
        self.horizontalLayout.addWidget(self.doubleSpinBoxTmin)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTmax = QtWidgets.QLabel(self.frame)
        self.labelTmax.setObjectName("labelTmax")
        self.horizontalLayout_2.addWidget(self.labelTmax)
        self.doubleSpinBoxTmax = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxTmax.setDecimals(3)
        self.doubleSpinBoxTmax.setMinimum(-99.99)
        self.doubleSpinBoxTmax.setSingleStep(0.05)
        self.doubleSpinBoxTmax.setProperty("value", 0.1)
        self.doubleSpinBoxTmax.setObjectName("doubleSpinBoxTmax")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxTmax)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_8)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame)
        self.verticalLayout_5.addWidget(self.groupBoxEvent)
        self.groupBoxFilteringECG = QtWidgets.QGroupBox(self.tabECG1)
        self.groupBoxFilteringECG.setObjectName("groupBoxFilteringECG")
        self.formLayout_5 = QtWidgets.QFormLayout(self.groupBoxFilteringECG)
        self.formLayout_5.setObjectName("formLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.groupBoxFilteringECG)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.labelLowPass = QtWidgets.QLabel(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLowPass.sizePolicy().hasHeightForWidth())
        self.labelLowPass.setSizePolicy(sizePolicy)
        self.labelLowPass.setObjectName("labelLowPass")
        self.horizontalLayout_23.addWidget(self.labelLowPass)
        self.spinBoxLowPass = QtWidgets.QSpinBox(self.frame_6)
        self.spinBoxLowPass.setMaximum(1000000)
        self.spinBoxLowPass.setProperty("value", 5)
        self.spinBoxLowPass.setObjectName("spinBoxLowPass")
        self.horizontalLayout_23.addWidget(self.spinBoxLowPass)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.labelHighPass = QtWidgets.QLabel(self.frame_6)
        self.labelHighPass.setObjectName("labelHighPass")
        self.horizontalLayout_24.addWidget(self.labelHighPass)
        self.spinBoxHighPass = QtWidgets.QSpinBox(self.frame_6)
        self.spinBoxHighPass.setMaximum(1000000000)
        self.spinBoxHighPass.setProperty("value", 35)
        self.spinBoxHighPass.setObjectName("spinBoxHighPass")
        self.horizontalLayout_24.addWidget(self.spinBoxHighPass)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_24)
        self.gridLayout_3.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_6)
        self.verticalLayout_5.addWidget(self.groupBoxFilteringECG)
        self.groupBoxSSP = QtWidgets.QGroupBox(self.tabECG1)
        self.groupBoxSSP.setObjectName("groupBoxSSP")
        self.formLayout_7 = QtWidgets.QFormLayout(self.groupBoxSSP)
        self.formLayout_7.setObjectName("formLayout_7")
        self.frame_2 = QtWidgets.QFrame(self.groupBoxSSP)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelGrad = QtWidgets.QLabel(self.frame_2)
        self.labelGrad.setObjectName("labelGrad")
        self.horizontalLayout_3.addWidget(self.labelGrad)
        self.spinBoxGrad = QtWidgets.QSpinBox(self.frame_2)
        self.spinBoxGrad.setProperty("value", 2)
        self.spinBoxGrad.setObjectName("spinBoxGrad")
        self.horizontalLayout_3.addWidget(self.spinBoxGrad)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelMag = QtWidgets.QLabel(self.frame_2)
        self.labelMag.setObjectName("labelMag")
        self.horizontalLayout_4.addWidget(self.labelMag)
        self.spinBoxMag = QtWidgets.QSpinBox(self.frame_2)
        self.spinBoxMag.setProperty("value", 2)
        self.spinBoxMag.setObjectName("spinBoxMag")
        self.horizontalLayout_4.addWidget(self.spinBoxMag)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelEeg = QtWidgets.QLabel(self.frame_2)
        self.labelEeg.setObjectName("labelEeg")
        self.horizontalLayout_5.addWidget(self.labelEeg)
        self.spinBoxEeg = QtWidgets.QSpinBox(self.frame_2)
        self.spinBoxEeg.setProperty("value", 2)
        self.spinBoxEeg.setObjectName("spinBoxEeg")
        self.horizontalLayout_5.addWidget(self.spinBoxEeg)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_2)
        self.verticalLayout_5.addWidget(self.groupBoxSSP)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.tabWidgetECGSettings.addTab(self.tabECG1, "")
        self.tabECG2 = QtWidgets.QWidget()
        self.tabECG2.setObjectName("tabECG2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tabECG2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 179))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelStart2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelStart2.setObjectName("labelStart2")
        self.gridLayout_2.addWidget(self.labelStart2, 0, 2, 1, 1)
        self.spinBoxStart = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxStart.setMaximum(10000)
        self.spinBoxStart.setProperty("value", 5)
        self.spinBoxStart.setObjectName("spinBoxStart")
        self.gridLayout_2.addWidget(self.spinBoxStart, 0, 1, 1, 1)
        self.checkBoxSSPProj = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.checkBoxSSPProj.setChecked(True)
        self.checkBoxSSPProj.setObjectName("checkBoxSSPProj")
        self.gridLayout_2.addWidget(self.checkBoxSSPProj, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxSSPCompute = QtWidgets.QCheckBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxSSPCompute.sizePolicy().hasHeightForWidth())
        self.checkBoxSSPCompute.setSizePolicy(sizePolicy)
        self.checkBoxSSPCompute.setChecked(True)
        self.checkBoxSSPCompute.setObjectName("checkBoxSSPCompute")
        self.verticalLayout.addWidget(self.checkBoxSSPCompute)
        self.gridLayout_2.addLayout(self.verticalLayout, 4, 0, 1, 1)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.labelStart1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelStart1.setObjectName("labelStart1")
        self.horizontalLayout_21.addWidget(self.labelStart1)
        self.gridLayout_2.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.labelTaps = QtWidgets.QLabel(self.gridLayoutWidget)
        self.labelTaps.setObjectName("labelTaps")
        self.horizontalLayout_22.addWidget(self.labelTaps)
        self.gridLayout_2.addLayout(self.horizontalLayout_22, 1, 0, 1, 1)
        self.spinBoxTaps = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBoxTaps.setMaximum(10000)
        self.spinBoxTaps.setProperty("value", 2048)
        self.spinBoxTaps.setObjectName("spinBoxTaps")
        self.gridLayout_2.addWidget(self.spinBoxTaps, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.doubleSpinBoxQrs = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        self.doubleSpinBoxQrs.setMaximum(1.0)
        self.doubleSpinBoxQrs.setSingleStep(0.1)
        self.doubleSpinBoxQrs.setProperty("value", 0.6)
        self.doubleSpinBoxQrs.setObjectName("doubleSpinBoxQrs")
        self.gridLayout_2.addWidget(self.doubleSpinBoxQrs, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tabECG2)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 487, 136))
        self.groupBox.setObjectName("groupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.frameEpochRejection = QtWidgets.QFrame(self.groupBox)
        self.frameEpochRejection.setEnabled(True)
        self.frameEpochRejection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameEpochRejection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameEpochRejection.setObjectName("frameEpochRejection")
        self.formLayout = QtWidgets.QFormLayout(self.frameEpochRejection)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.labelGradReject = QtWidgets.QLabel(self.frameEpochRejection)
        self.labelGradReject.setObjectName("labelGradReject")
        self.horizontalLayout_14.addWidget(self.labelGradReject)
        self.doubleSpinBoxGradReject = QtWidgets.QDoubleSpinBox(self.frameEpochRejection)
        self.doubleSpinBoxGradReject.setMaximum(1000000000.0)
        self.doubleSpinBoxGradReject.setProperty("value", 3000.0)
        self.doubleSpinBoxGradReject.setObjectName("doubleSpinBoxGradReject")
        self.horizontalLayout_14.addWidget(self.doubleSpinBoxGradReject)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.labelEegReject = QtWidgets.QLabel(self.frameEpochRejection)
        self.labelEegReject.setObjectName("labelEegReject")
        self.horizontalLayout_11.addWidget(self.labelEegReject)
        self.doubleSpinBoxEEGReject = QtWidgets.QDoubleSpinBox(self.frameEpochRejection)
        self.doubleSpinBoxEEGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEEGReject.setProperty("value", 100.0)
        self.doubleSpinBoxEEGReject.setObjectName("doubleSpinBoxEEGReject")
        self.horizontalLayout_11.addWidget(self.doubleSpinBoxEEGReject)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelMagReject = QtWidgets.QLabel(self.frameEpochRejection)
        self.labelMagReject.setObjectName("labelMagReject")
        self.horizontalLayout_13.addWidget(self.labelMagReject)
        self.doubleSpinBoxMagReject = QtWidgets.QDoubleSpinBox(self.frameEpochRejection)
        self.doubleSpinBoxMagReject.setMaximum(1000000000.0)
        self.doubleSpinBoxMagReject.setProperty("value", 4000.0)
        self.doubleSpinBoxMagReject.setObjectName("doubleSpinBoxMagReject")
        self.horizontalLayout_13.addWidget(self.doubleSpinBoxMagReject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.labelEOGReject = QtWidgets.QLabel(self.frameEpochRejection)
        self.labelEOGReject.setObjectName("labelEOGReject")
        self.horizontalLayout_15.addWidget(self.labelEOGReject)
        self.doubleSpinBoxEOGReject = QtWidgets.QDoubleSpinBox(self.frameEpochRejection)
        self.doubleSpinBoxEOGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEOGReject.setProperty("value", 250.0)
        self.doubleSpinBoxEOGReject.setObjectName("doubleSpinBoxEOGReject")
        self.horizontalLayout_15.addWidget(self.doubleSpinBoxEOGReject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_12)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frameEpochRejection)
        self.groupBoxFilter = QtWidgets.QGroupBox(self.tabECG2)
        self.groupBoxFilter.setGeometry(QtCore.QRect(10, 340, 566, 103))
        self.groupBoxFilter.setObjectName("groupBoxFilter")
        self.formLayout_6 = QtWidgets.QFormLayout(self.groupBoxFilter)
        self.formLayout_6.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName("formLayout_6")
        self.frame_7 = QtWidgets.QFrame(self.groupBoxFilter)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.labelLow = QtWidgets.QLabel(self.frame_7)
        self.labelLow.setObjectName("labelLow")
        self.horizontalLayout_26.addWidget(self.labelLow)
        self.spinBoxLow = QtWidgets.QSpinBox(self.frame_7)
        self.spinBoxLow.setProperty("value", 1)
        self.spinBoxLow.setObjectName("spinBoxLow")
        self.horizontalLayout_26.addWidget(self.spinBoxLow)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.labelHigh = QtWidgets.QLabel(self.frame_7)
        self.labelHigh.setObjectName("labelHigh")
        self.horizontalLayout_27.addWidget(self.labelHigh)
        self.spinBoxHigh = QtWidgets.QSpinBox(self.frame_7)
        self.spinBoxHigh.setMaximum(1000)
        self.spinBoxHigh.setProperty("value", 35)
        self.spinBoxHigh.setObjectName("spinBoxHigh")
        self.horizontalLayout_27.addWidget(self.spinBoxHigh)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_27)
        self.gridLayout_6.addLayout(self.horizontalLayout_25, 0, 0, 1, 1)
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.frame_7)
        self.tabWidgetECGSettings.addTab(self.tabECG2, "")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget.setGeometry(QtCore.QRect(0, 480, 301, 371))
        self.widget.setObjectName("widget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidgetECGSettings.setCurrentIndex(0)
        self.pushButtonCancel.clicked.connect(Dialog.reject)
        self.pushButtonComputeBatch.clicked.connect(Dialog.acceptBatch)
        self.pushButtonCompute.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidgetECGSettings, self.comboBoxECGChannel)
        Dialog.setTabOrder(self.comboBoxECGChannel, self.doubleSpinBoxTmin)
        Dialog.setTabOrder(self.doubleSpinBoxTmin, self.doubleSpinBoxTmax)
        Dialog.setTabOrder(self.doubleSpinBoxTmax, self.spinBoxLowPass)
        Dialog.setTabOrder(self.spinBoxLowPass, self.spinBoxHighPass)
        Dialog.setTabOrder(self.spinBoxHighPass, self.spinBoxLow)
        Dialog.setTabOrder(self.spinBoxLow, self.spinBoxHigh)
        Dialog.setTabOrder(self.spinBoxHigh, self.doubleSpinBoxGradReject)
        Dialog.setTabOrder(self.doubleSpinBoxGradReject, self.doubleSpinBoxMagReject)
        Dialog.setTabOrder(self.doubleSpinBoxMagReject, self.doubleSpinBoxEEGReject)
        Dialog.setTabOrder(self.doubleSpinBoxEEGReject, self.doubleSpinBoxEOGReject)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Meggie - Compute ECG projections"))
        self.pushButtonPlotEvents.setText(_translate("Dialog", "Plot events"))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel"))
        self.pushButtonComputeBatch.setText(_translate("Dialog", "Compute Batch"))
        self.pushButtonCompute.setText(_translate("Dialog", "Compute"))
        self.labelECGChannel.setText(_translate("Dialog", "Channel to use for ECG detection:"))
        self.groupBoxEvent.setTitle(_translate("Dialog", "Events"))
        self.labelTmin.setText(_translate("Dialog", "Start time:"))
        self.doubleSpinBoxTmin.setSuffix(_translate("Dialog", " s"))
        self.labelTmax.setText(_translate("Dialog", "End time:"))
        self.doubleSpinBoxTmax.setSuffix(_translate("Dialog", " s"))
        self.groupBoxFilteringECG.setTitle(_translate("Dialog", "Filter cut-off frequencies for ECG channel:"))
        self.labelLowPass.setText(_translate("Dialog", "Low:"))
        self.spinBoxLowPass.setSuffix(_translate("Dialog", " Hz"))
        self.labelHighPass.setText(_translate("Dialog", "High:"))
        self.spinBoxHighPass.setSuffix(_translate("Dialog", " Hz"))
        self.groupBoxSSP.setTitle(_translate("Dialog", "Number of SSP vectors"))
        self.labelGrad.setText(_translate("Dialog", "Grad:"))
        self.labelMag.setText(_translate("Dialog", "Mag:"))
        self.labelEeg.setText(_translate("Dialog", "EEG:"))
        self.tabWidgetECGSettings.setTabText(self.tabWidgetECGSettings.indexOf(self.tabECG1), _translate("Dialog", "ECG settings"))
        self.labelStart2.setText(_translate("Dialog", "seconds."))
        self.checkBoxSSPProj.setText(_translate("Dialog", "Exclude SSP projections currently in the file"))
        self.checkBoxSSPCompute.setText(_translate("Dialog", "Compute SSP after averaging"))
        self.labelStart1.setText(_translate("Dialog", "Start artifact detection after"))
        self.labelTaps.setText(_translate("Dialog", "Number of taps to use for filtering:"))
        self.label.setText(_translate("Dialog", "QRS detection threshold (between 0 and 1):"))
        self.groupBox.setTitle(_translate("Dialog", "Epoch rejection"))
        self.labelGradReject.setText(_translate("Dialog", "Grad:"))
        self.doubleSpinBoxGradReject.setSuffix(_translate("Dialog", " fT/cm"))
        self.labelEegReject.setText(_translate("Dialog", "EEG:"))
        self.doubleSpinBoxEEGReject.setSuffix(_translate("Dialog", " uV"))
        self.labelMagReject.setText(_translate("Dialog", "Mag:"))
        self.doubleSpinBoxMagReject.setSuffix(_translate("Dialog", " fT"))
        self.labelEOGReject.setText(_translate("Dialog", "EOG:"))
        self.doubleSpinBoxEOGReject.setSuffix(_translate("Dialog", " uV"))
        self.groupBoxFilter.setTitle(_translate("Dialog", "Filtering cut-off frequencies for the data"))
        self.labelLow.setText(_translate("Dialog", "Low:"))
        self.spinBoxLow.setSuffix(_translate("Dialog", " Hz"))
        self.labelHigh.setText(_translate("Dialog", "High:"))
        self.spinBoxHigh.setSuffix(_translate("Dialog", " Hz"))
        self.tabWidgetECGSettings.setTabText(self.tabWidgetECGSettings.indexOf(self.tabECG2), _translate("Dialog", "Advanced"))

