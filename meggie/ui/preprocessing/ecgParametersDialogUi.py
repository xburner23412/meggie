# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ecgParametersDialogBatch.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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
        Dialog.resize(634, 968)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 616, 911))
        self.scrollAreaWidgetContents_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.tabWidgetECGSettings = QtGui.QTabWidget(self.scrollAreaWidgetContents_2)
        self.tabWidgetECGSettings.setGeometry(QtCore.QRect(0, 0, 591, 571))
        self.tabWidgetECGSettings.setObjectName(_fromUtf8("tabWidgetECGSettings"))
        self.tabECG1 = QtGui.QWidget()
        self.tabECG1.setObjectName(_fromUtf8("tabECG1"))
        self.widget = QtGui.QWidget(self.tabECG1)
        self.widget.setGeometry(QtCore.QRect(9, 9, 568, 470))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.labelECGChannel = QtGui.QLabel(self.widget)
        self.labelECGChannel.setObjectName(_fromUtf8("labelECGChannel"))
        self.horizontalLayout_10.addWidget(self.labelECGChannel)
        self.comboBoxECGChannel = QtGui.QComboBox(self.widget)
        self.comboBoxECGChannel.setObjectName(_fromUtf8("comboBoxECGChannel"))
        self.horizontalLayout_10.addWidget(self.comboBoxECGChannel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.groupBoxEvent = QtGui.QGroupBox(self.widget)
        self.groupBoxEvent.setObjectName(_fromUtf8("groupBoxEvent"))
        self.formLayout_4 = QtGui.QFormLayout(self.groupBoxEvent)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.frame = QtGui.QFrame(self.groupBoxEvent)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout_3 = QtGui.QFormLayout(self.frame)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelTmin = QtGui.QLabel(self.frame)
        self.labelTmin.setObjectName(_fromUtf8("labelTmin"))
        self.horizontalLayout.addWidget(self.labelTmin)
        self.doubleSpinBoxTmin = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxTmin.setDecimals(3)
        self.doubleSpinBoxTmin.setMinimum(-99.99)
        self.doubleSpinBoxTmin.setSingleStep(0.05)
        self.doubleSpinBoxTmin.setProperty("value", -0.2)
        self.doubleSpinBoxTmin.setObjectName(_fromUtf8("doubleSpinBoxTmin"))
        self.horizontalLayout.addWidget(self.doubleSpinBoxTmin)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelTmax = QtGui.QLabel(self.frame)
        self.labelTmax.setObjectName(_fromUtf8("labelTmax"))
        self.horizontalLayout_2.addWidget(self.labelTmax)
        self.doubleSpinBoxTmax = QtGui.QDoubleSpinBox(self.frame)
        self.doubleSpinBoxTmax.setDecimals(3)
        self.doubleSpinBoxTmax.setMinimum(-99.99)
        self.doubleSpinBoxTmax.setSingleStep(0.05)
        self.doubleSpinBoxTmax.setProperty("value", 0.4)
        self.doubleSpinBoxTmax.setObjectName(_fromUtf8("doubleSpinBoxTmax"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxTmax)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.labelEventID = QtGui.QLabel(self.frame)
        self.labelEventID.setObjectName(_fromUtf8("labelEventID"))
        self.horizontalLayout_6.addWidget(self.labelEventID)
        self.spinBoxEventsID = QtGui.QSpinBox(self.frame)
        self.spinBoxEventsID.setMaximum(10000)
        self.spinBoxEventsID.setProperty("value", 998)
        self.spinBoxEventsID.setObjectName(_fromUtf8("spinBoxEventsID"))
        self.horizontalLayout_6.addWidget(self.spinBoxEventsID)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)
        self.formLayout_3.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout_8)
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.frame)
        self.verticalLayout_5.addWidget(self.groupBoxEvent)
        self.groupBoxFilteringECG = QtGui.QGroupBox(self.widget)
        self.groupBoxFilteringECG.setObjectName(_fromUtf8("groupBoxFilteringECG"))
        self.formLayout_5 = QtGui.QFormLayout(self.groupBoxFilteringECG)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.frame_6 = QtGui.QFrame(self.groupBoxFilteringECG)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.labelLowPass = QtGui.QLabel(self.frame_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLowPass.sizePolicy().hasHeightForWidth())
        self.labelLowPass.setSizePolicy(sizePolicy)
        self.labelLowPass.setObjectName(_fromUtf8("labelLowPass"))
        self.horizontalLayout_23.addWidget(self.labelLowPass)
        self.spinBoxLowPass = QtGui.QSpinBox(self.frame_6)
        self.spinBoxLowPass.setMaximum(1000000)
        self.spinBoxLowPass.setProperty("value", 1)
        self.spinBoxLowPass.setObjectName(_fromUtf8("spinBoxLowPass"))
        self.horizontalLayout_23.addWidget(self.spinBoxLowPass)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.labelHighPass = QtGui.QLabel(self.frame_6)
        self.labelHighPass.setObjectName(_fromUtf8("labelHighPass"))
        self.horizontalLayout_24.addWidget(self.labelHighPass)
        self.spinBoxHighPass = QtGui.QSpinBox(self.frame_6)
        self.spinBoxHighPass.setMaximum(1000000000)
        self.spinBoxHighPass.setProperty("value", 40)
        self.spinBoxHighPass.setObjectName(_fromUtf8("spinBoxHighPass"))
        self.horizontalLayout_24.addWidget(self.spinBoxHighPass)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_24)
        self.gridLayout_3.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.frame_6)
        self.verticalLayout_5.addWidget(self.groupBoxFilteringECG)
        self.groupBoxFilter = QtGui.QGroupBox(self.widget)
        self.groupBoxFilter.setObjectName(_fromUtf8("groupBoxFilter"))
        self.formLayout_6 = QtGui.QFormLayout(self.groupBoxFilter)
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.frame_7 = QtGui.QFrame(self.groupBoxFilter)
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_7)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.labelLow = QtGui.QLabel(self.frame_7)
        self.labelLow.setObjectName(_fromUtf8("labelLow"))
        self.horizontalLayout_26.addWidget(self.labelLow)
        self.spinBoxLow = QtGui.QSpinBox(self.frame_7)
        self.spinBoxLow.setProperty("value", 1)
        self.spinBoxLow.setObjectName(_fromUtf8("spinBoxLow"))
        self.horizontalLayout_26.addWidget(self.spinBoxLow)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.labelHigh = QtGui.QLabel(self.frame_7)
        self.labelHigh.setObjectName(_fromUtf8("labelHigh"))
        self.horizontalLayout_27.addWidget(self.labelHigh)
        self.spinBoxHigh = QtGui.QSpinBox(self.frame_7)
        self.spinBoxHigh.setMaximum(1000)
        self.spinBoxHigh.setProperty("value", 100)
        self.spinBoxHigh.setObjectName(_fromUtf8("spinBoxHigh"))
        self.horizontalLayout_27.addWidget(self.spinBoxHigh)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_27)
        self.gridLayout_6.addLayout(self.horizontalLayout_25, 0, 0, 1, 1)
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.frame_7)
        self.verticalLayout_5.addWidget(self.groupBoxFilter)
        self.groupBoxSSP = QtGui.QGroupBox(self.widget)
        self.groupBoxSSP.setObjectName(_fromUtf8("groupBoxSSP"))
        self.formLayout_7 = QtGui.QFormLayout(self.groupBoxSSP)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.frame_2 = QtGui.QFrame(self.groupBoxSSP)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelGrad = QtGui.QLabel(self.frame_2)
        self.labelGrad.setObjectName(_fromUtf8("labelGrad"))
        self.horizontalLayout_3.addWidget(self.labelGrad)
        self.spinBoxGrad = QtGui.QSpinBox(self.frame_2)
        self.spinBoxGrad.setProperty("value", 2)
        self.spinBoxGrad.setObjectName(_fromUtf8("spinBoxGrad"))
        self.horizontalLayout_3.addWidget(self.spinBoxGrad)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelMag = QtGui.QLabel(self.frame_2)
        self.labelMag.setObjectName(_fromUtf8("labelMag"))
        self.horizontalLayout_4.addWidget(self.labelMag)
        self.spinBoxMag = QtGui.QSpinBox(self.frame_2)
        self.spinBoxMag.setProperty("value", 2)
        self.spinBoxMag.setObjectName(_fromUtf8("spinBoxMag"))
        self.horizontalLayout_4.addWidget(self.spinBoxMag)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.labelEeg = QtGui.QLabel(self.frame_2)
        self.labelEeg.setObjectName(_fromUtf8("labelEeg"))
        self.horizontalLayout_5.addWidget(self.labelEeg)
        self.spinBoxEeg = QtGui.QSpinBox(self.frame_2)
        self.spinBoxEeg.setProperty("value", 2)
        self.spinBoxEeg.setObjectName(_fromUtf8("spinBoxEeg"))
        self.horizontalLayout_5.addWidget(self.spinBoxEeg)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        self.gridLayout_5.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.frame_2)
        self.verticalLayout_5.addWidget(self.groupBoxSSP)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_17.addWidget(self.label)
        self.doubleSpinBoxQrs = QtGui.QDoubleSpinBox(self.widget)
        self.doubleSpinBoxQrs.setMaximum(1.0)
        self.doubleSpinBoxQrs.setSingleStep(0.1)
        self.doubleSpinBoxQrs.setProperty("value", 0.6)
        self.doubleSpinBoxQrs.setObjectName(_fromUtf8("doubleSpinBoxQrs"))
        self.horizontalLayout_17.addWidget(self.doubleSpinBoxQrs)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.tabWidgetECGSettings.addTab(self.tabECG1, _fromUtf8(""))
        self.tabECG2 = QtGui.QWidget()
        self.tabECG2.setObjectName(_fromUtf8("tabECG2"))
        self.horizontalLayoutWidget_17 = QtGui.QWidget(self.tabECG2)
        self.horizontalLayoutWidget_17.setGeometry(QtCore.QRect(10, 60, 364, 41))
        self.horizontalLayoutWidget_17.setObjectName(_fromUtf8("horizontalLayoutWidget_17"))
        self.horizontalLayout_21 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.labelStart1 = QtGui.QLabel(self.horizontalLayoutWidget_17)
        self.labelStart1.setObjectName(_fromUtf8("labelStart1"))
        self.horizontalLayout_21.addWidget(self.labelStart1)
        self.spinBoxStart = QtGui.QSpinBox(self.horizontalLayoutWidget_17)
        self.spinBoxStart.setMaximum(10000)
        self.spinBoxStart.setProperty("value", 5)
        self.spinBoxStart.setObjectName(_fromUtf8("spinBoxStart"))
        self.horizontalLayout_21.addWidget(self.spinBoxStart)
        self.labelStart2 = QtGui.QLabel(self.horizontalLayoutWidget_17)
        self.labelStart2.setObjectName(_fromUtf8("labelStart2"))
        self.horizontalLayout_21.addWidget(self.labelStart2)
        self.horizontalLayoutWidget = QtGui.QWidget(self.tabECG2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 160, 310, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.labelJobs = QtGui.QLabel(self.horizontalLayoutWidget)
        self.labelJobs.setObjectName(_fromUtf8("labelJobs"))
        self.horizontalLayout_7.addWidget(self.labelJobs)
        self.spinBoxJobs = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.spinBoxJobs.setProperty("value", 1)
        self.spinBoxJobs.setObjectName(_fromUtf8("spinBoxJobs"))
        self.horizontalLayout_7.addWidget(self.spinBoxJobs)
        self.layoutWidget = QtGui.QWidget(self.tabECG2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 341, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.labelTaps = QtGui.QLabel(self.layoutWidget)
        self.labelTaps.setObjectName(_fromUtf8("labelTaps"))
        self.horizontalLayout_22.addWidget(self.labelTaps)
        self.spinBoxTaps = QtGui.QSpinBox(self.layoutWidget)
        self.spinBoxTaps.setMaximum(10000)
        self.spinBoxTaps.setProperty("value", 2048)
        self.spinBoxTaps.setObjectName(_fromUtf8("spinBoxTaps"))
        self.horizontalLayout_22.addWidget(self.spinBoxTaps)
        self.verticalLayoutWidget = QtGui.QWidget(self.tabECG2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 389, 111))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.checkBoxEEGProj = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxEEGProj.setObjectName(_fromUtf8("checkBoxEEGProj"))
        self.verticalLayout.addWidget(self.checkBoxEEGProj)
        self.checkBoxSSPProj = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxSSPProj.setEnabled(True)
        self.checkBoxSSPProj.setChecked(True)
        self.checkBoxSSPProj.setObjectName(_fromUtf8("checkBoxSSPProj"))
        self.verticalLayout.addWidget(self.checkBoxSSPProj)
        self.checkBoxSSPCompute = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxSSPCompute.setChecked(True)
        self.checkBoxSSPCompute.setObjectName(_fromUtf8("checkBoxSSPCompute"))
        self.verticalLayout.addWidget(self.checkBoxSSPCompute)
        self.layoutWidget_2 = QtGui.QWidget(self.tabECG2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 531, 41))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_29 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.labelBad = QtGui.QLabel(self.layoutWidget_2)
        self.labelBad.setObjectName(_fromUtf8("labelBad"))
        self.horizontalLayout_29.addWidget(self.labelBad)
        self.lineEditBad = QtGui.QLineEdit(self.layoutWidget_2)
        self.lineEditBad.setObjectName(_fromUtf8("lineEditBad"))
        self.horizontalLayout_29.addWidget(self.lineEditBad)
        self.groupBox = QtGui.QGroupBox(self.tabECG2)
        self.groupBox.setGeometry(QtCore.QRect(10, 400, 520, 132))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.frameEpochRejection = QtGui.QFrame(self.groupBox)
        self.frameEpochRejection.setEnabled(True)
        self.frameEpochRejection.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameEpochRejection.setFrameShadow(QtGui.QFrame.Raised)
        self.frameEpochRejection.setObjectName(_fromUtf8("frameEpochRejection"))
        self.formLayout = QtGui.QFormLayout(self.frameEpochRejection)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.labelGradReject = QtGui.QLabel(self.frameEpochRejection)
        self.labelGradReject.setObjectName(_fromUtf8("labelGradReject"))
        self.horizontalLayout_14.addWidget(self.labelGradReject)
        self.doubleSpinBoxGradReject = QtGui.QDoubleSpinBox(self.frameEpochRejection)
        self.doubleSpinBoxGradReject.setMaximum(1000000000.0)
        self.doubleSpinBoxGradReject.setProperty("value", 3000.0)
        self.doubleSpinBoxGradReject.setObjectName(_fromUtf8("doubleSpinBoxGradReject"))
        self.horizontalLayout_14.addWidget(self.doubleSpinBoxGradReject)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.labelEegReject = QtGui.QLabel(self.frameEpochRejection)
        self.labelEegReject.setObjectName(_fromUtf8("labelEegReject"))
        self.horizontalLayout_11.addWidget(self.labelEegReject)
        self.doubleSpinBoxEEGReject = QtGui.QDoubleSpinBox(self.frameEpochRejection)
        self.doubleSpinBoxEEGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEEGReject.setProperty("value", 100.0)
        self.doubleSpinBoxEEGReject.setObjectName(_fromUtf8("doubleSpinBoxEEGReject"))
        self.horizontalLayout_11.addWidget(self.doubleSpinBoxEEGReject)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.labelMagReject = QtGui.QLabel(self.frameEpochRejection)
        self.labelMagReject.setObjectName(_fromUtf8("labelMagReject"))
        self.horizontalLayout_13.addWidget(self.labelMagReject)
        self.doubleSpinBoxMagReject = QtGui.QDoubleSpinBox(self.frameEpochRejection)
        self.doubleSpinBoxMagReject.setMaximum(1000000000.0)
        self.doubleSpinBoxMagReject.setProperty("value", 4000.0)
        self.doubleSpinBoxMagReject.setObjectName(_fromUtf8("doubleSpinBoxMagReject"))
        self.horizontalLayout_13.addWidget(self.doubleSpinBoxMagReject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.labelEOGReject = QtGui.QLabel(self.frameEpochRejection)
        self.labelEOGReject.setObjectName(_fromUtf8("labelEOGReject"))
        self.horizontalLayout_15.addWidget(self.labelEOGReject)
        self.doubleSpinBoxEOGReject = QtGui.QDoubleSpinBox(self.frameEpochRejection)
        self.doubleSpinBoxEOGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEOGReject.setProperty("value", 250.0)
        self.doubleSpinBoxEOGReject.setObjectName(_fromUtf8("doubleSpinBoxEOGReject"))
        self.horizontalLayout_15.addWidget(self.doubleSpinBoxEOGReject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout_12)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.frameEpochRejection)
        self.tabWidgetECGSettings.addTab(self.tabECG2, _fromUtf8(""))
        self.widget1 = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        self.widget1.setGeometry(QtCore.QRect(0, 580, 591, 311))
        self.widget1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_19.addWidget(self.pushButtonCancel)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_19.addWidget(self.pushButton)
        self.pushButtonCompute = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCompute.sizePolicy().hasHeightForWidth())
        self.pushButtonCompute.setSizePolicy(sizePolicy)
        self.pushButtonCompute.setObjectName(_fromUtf8("pushButtonCompute"))
        self.horizontalLayout_19.addWidget(self.pushButtonCompute)
        self.gridLayout.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidgetECGSettings.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.acceptBatch)
        QtCore.QObject.connect(self.pushButtonCompute, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.tabWidgetECGSettings, self.comboBoxECGChannel)
        Dialog.setTabOrder(self.comboBoxECGChannel, self.doubleSpinBoxTmin)
        Dialog.setTabOrder(self.doubleSpinBoxTmin, self.doubleSpinBoxTmax)
        Dialog.setTabOrder(self.doubleSpinBoxTmax, self.spinBoxEventsID)
        Dialog.setTabOrder(self.spinBoxEventsID, self.spinBoxLowPass)
        Dialog.setTabOrder(self.spinBoxLowPass, self.spinBoxHighPass)
        Dialog.setTabOrder(self.spinBoxHighPass, self.spinBoxLow)
        Dialog.setTabOrder(self.spinBoxLow, self.spinBoxHigh)
        Dialog.setTabOrder(self.spinBoxHigh, self.spinBoxGrad)
        Dialog.setTabOrder(self.spinBoxGrad, self.spinBoxMag)
        Dialog.setTabOrder(self.spinBoxMag, self.spinBoxEeg)
        Dialog.setTabOrder(self.spinBoxEeg, self.doubleSpinBoxQrs)
        Dialog.setTabOrder(self.doubleSpinBoxQrs, self.lineEditBad)
        Dialog.setTabOrder(self.lineEditBad, self.spinBoxStart)
        Dialog.setTabOrder(self.spinBoxStart, self.spinBoxTaps)
        Dialog.setTabOrder(self.spinBoxTaps, self.spinBoxJobs)
        Dialog.setTabOrder(self.spinBoxJobs, self.checkBoxEEGProj)
        Dialog.setTabOrder(self.checkBoxEEGProj, self.checkBoxSSPProj)
        Dialog.setTabOrder(self.checkBoxSSPProj, self.checkBoxSSPCompute)
        Dialog.setTabOrder(self.checkBoxSSPCompute, self.doubleSpinBoxGradReject)
        Dialog.setTabOrder(self.doubleSpinBoxGradReject, self.doubleSpinBoxMagReject)
        Dialog.setTabOrder(self.doubleSpinBoxMagReject, self.doubleSpinBoxEEGReject)
        Dialog.setTabOrder(self.doubleSpinBoxEEGReject, self.doubleSpinBoxEOGReject)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Meggie - Compute ECG projections", None))
        self.labelECGChannel.setText(_translate("Dialog", "Channel to use for ECG detection:", None))
        self.groupBoxEvent.setTitle(_translate("Dialog", "Events", None))
        self.labelTmin.setText(_translate("Dialog", "Start time:", None))
        self.doubleSpinBoxTmin.setSuffix(_translate("Dialog", " s", None))
        self.labelTmax.setText(_translate("Dialog", "End time:", None))
        self.doubleSpinBoxTmax.setSuffix(_translate("Dialog", " s", None))
        self.labelEventID.setText(_translate("Dialog", "Events ID:", None))
        self.groupBoxFilteringECG.setTitle(_translate("Dialog", "Filter cut-off frequencies for ECG channel:", None))
        self.labelLowPass.setText(_translate("Dialog", "Low:", None))
        self.spinBoxLowPass.setSuffix(_translate("Dialog", " Hz", None))
        self.labelHighPass.setText(_translate("Dialog", "High:", None))
        self.spinBoxHighPass.setSuffix(_translate("Dialog", " Hz", None))
        self.groupBoxFilter.setTitle(_translate("Dialog", "Filtering cut-off frequencies for data:", None))
        self.labelLow.setText(_translate("Dialog", "Low:", None))
        self.spinBoxLow.setSuffix(_translate("Dialog", " Hz", None))
        self.labelHigh.setText(_translate("Dialog", "High:", None))
        self.spinBoxHigh.setSuffix(_translate("Dialog", " Hz", None))
        self.groupBoxSSP.setTitle(_translate("Dialog", "Number of SSP vectors", None))
        self.labelGrad.setText(_translate("Dialog", "Grad:", None))
        self.labelMag.setText(_translate("Dialog", "Mag:", None))
        self.labelEeg.setText(_translate("Dialog", "EEG:", None))
        self.label.setText(_translate("Dialog", "QRS detection threshold (between 0 and 1):", None))
        self.tabWidgetECGSettings.setTabText(self.tabWidgetECGSettings.indexOf(self.tabECG1), _translate("Dialog", "ECG settings", None))
        self.labelStart1.setText(_translate("Dialog", "Start artifact detection after", None))
        self.labelStart2.setText(_translate("Dialog", "seconds.", None))
        self.labelJobs.setText(_translate("Dialog", "Number of jobs to run in parallel:", None))
        self.labelTaps.setText(_translate("Dialog", "Number of taps to use for filtering:", None))
        self.checkBoxEEGProj.setText(_translate("Dialog", "Add EEG average reference proj.", None))
        self.checkBoxSSPProj.setText(_translate("Dialog", "Exclude the SSP projectors currently in the fiff file", None))
        self.checkBoxSSPCompute.setText(_translate("Dialog", "Compute SSP after averaging", None))
        self.labelBad.setText(_translate("Dialog", "Bad channels (eg. MEG 2443, MEG 1531):", None))
        self.groupBox.setTitle(_translate("Dialog", "Epoch rejection", None))
        self.labelGradReject.setText(_translate("Dialog", "Grad:", None))
        self.doubleSpinBoxGradReject.setSuffix(_translate("Dialog", " fT/cm", None))
        self.labelEegReject.setText(_translate("Dialog", "EEG:", None))
        self.doubleSpinBoxEEGReject.setSuffix(_translate("Dialog", " uV", None))
        self.labelMagReject.setText(_translate("Dialog", "Mag:", None))
        self.doubleSpinBoxMagReject.setSuffix(_translate("Dialog", " fT", None))
        self.labelEOGReject.setText(_translate("Dialog", "EOG:", None))
        self.doubleSpinBoxEOGReject.setSuffix(_translate("Dialog", " uV", None))
        self.tabWidgetECGSettings.setTabText(self.tabWidgetECGSettings.indexOf(self.tabECG2), _translate("Dialog", "Bads etc.", None))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel", None))
        self.pushButton.setText(_translate("Dialog", "Compute Batch", None))
        self.pushButtonCompute.setText(_translate("Dialog", "Compute", None))

