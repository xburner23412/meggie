# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eogParametersDialogUi.ui'
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
        Dialog.setEnabled(True)
        Dialog.resize(582, 957)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem)
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.horizontalLayout_13.addWidget(self.pushButtonCancel)
        self.pushButtonComputeBatch = QtGui.QPushButton(Dialog)
        self.pushButtonComputeBatch.setObjectName(_fromUtf8("pushButtonComputeBatch"))
        self.horizontalLayout_13.addWidget(self.pushButtonComputeBatch)
        self.pushButtonCompute = QtGui.QPushButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCompute.sizePolicy().hasHeightForWidth())
        self.pushButtonCompute.setSizePolicy(sizePolicy)
        self.pushButtonCompute.setObjectName(_fromUtf8("pushButtonCompute"))
        self.horizontalLayout_13.addWidget(self.pushButtonCompute)
        self.gridLayout.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 564, 900))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(564, 900))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.tabWidgetEOGSettings = QtGui.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidgetEOGSettings.setGeometry(QtCore.QRect(0, 0, 561, 481))
        self.tabWidgetEOGSettings.setObjectName(_fromUtf8("tabWidgetEOGSettings"))
        self.tabEOG1 = QtGui.QWidget()
        self.tabEOG1.setObjectName(_fromUtf8("tabEOG1"))
        self.groupBoxFilter = QtGui.QGroupBox(self.tabEOG1)
        self.groupBoxFilter.setGeometry(QtCore.QRect(10, 340, 351, 101))
        self.groupBoxFilter.setObjectName(_fromUtf8("groupBoxFilter"))
        self.frame_7 = QtGui.QFrame(self.groupBoxFilter)
        self.frame_7.setGeometry(QtCore.QRect(10, 30, 271, 61))
        self.frame_7.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_7.setObjectName(_fromUtf8("frame_7"))
        self.horizontalLayoutWidget_19 = QtGui.QWidget(self.frame_7)
        self.horizontalLayoutWidget_19.setGeometry(QtCore.QRect(10, 10, 251, 41))
        self.horizontalLayoutWidget_19.setObjectName(_fromUtf8("horizontalLayoutWidget_19"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.labelLow = QtGui.QLabel(self.horizontalLayoutWidget_19)
        self.labelLow.setObjectName(_fromUtf8("labelLow"))
        self.horizontalLayout_26.addWidget(self.labelLow)
        self.spinBoxLow = QtGui.QSpinBox(self.horizontalLayoutWidget_19)
        self.spinBoxLow.setProperty("value", 1)
        self.spinBoxLow.setObjectName(_fromUtf8("spinBoxLow"))
        self.horizontalLayout_26.addWidget(self.spinBoxLow)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.labelHigh = QtGui.QLabel(self.horizontalLayoutWidget_19)
        self.labelHigh.setObjectName(_fromUtf8("labelHigh"))
        self.horizontalLayout_27.addWidget(self.labelHigh)
        self.spinBoxHigh = QtGui.QSpinBox(self.horizontalLayoutWidget_19)
        self.spinBoxHigh.setMaximum(1000)
        self.spinBoxHigh.setProperty("value", 35)
        self.spinBoxHigh.setObjectName(_fromUtf8("spinBoxHigh"))
        self.horizontalLayout_27.addWidget(self.spinBoxHigh)
        self.horizontalLayout_25.addLayout(self.horizontalLayout_27)
        self.groupBoxFilteringEOG = QtGui.QGroupBox(self.tabEOG1)
        self.groupBoxFilteringEOG.setGeometry(QtCore.QRect(10, 120, 491, 101))
        self.groupBoxFilteringEOG.setObjectName(_fromUtf8("groupBoxFilteringEOG"))
        self.frame_6 = QtGui.QFrame(self.groupBoxFilteringEOG)
        self.frame_6.setGeometry(QtCore.QRect(10, 30, 391, 61))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.horizontalLayoutWidget_20 = QtGui.QWidget(self.frame_6)
        self.horizontalLayoutWidget_20.setGeometry(QtCore.QRect(10, 10, 371, 41))
        self.horizontalLayoutWidget_20.setObjectName(_fromUtf8("horizontalLayoutWidget_20"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.labelLowPass = QtGui.QLabel(self.horizontalLayoutWidget_20)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelLowPass.sizePolicy().hasHeightForWidth())
        self.labelLowPass.setSizePolicy(sizePolicy)
        self.labelLowPass.setObjectName(_fromUtf8("labelLowPass"))
        self.horizontalLayout_23.addWidget(self.labelLowPass)
        self.spinBoxLowPass = QtGui.QSpinBox(self.horizontalLayoutWidget_20)
        self.spinBoxLowPass.setProperty("value", 1)
        self.spinBoxLowPass.setObjectName(_fromUtf8("spinBoxLowPass"))
        self.horizontalLayout_23.addWidget(self.spinBoxLowPass)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_23)
        self.horizontalLayout_24 = QtGui.QHBoxLayout()
        self.horizontalLayout_24.setObjectName(_fromUtf8("horizontalLayout_24"))
        self.labelHighPass = QtGui.QLabel(self.horizontalLayoutWidget_20)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHighPass.sizePolicy().hasHeightForWidth())
        self.labelHighPass.setSizePolicy(sizePolicy)
        self.labelHighPass.setObjectName(_fromUtf8("labelHighPass"))
        self.horizontalLayout_24.addWidget(self.labelHighPass)
        self.spinBoxHighPass = QtGui.QSpinBox(self.horizontalLayoutWidget_20)
        self.spinBoxHighPass.setMaximum(1000)
        self.spinBoxHighPass.setProperty("value", 10)
        self.spinBoxHighPass.setObjectName(_fromUtf8("spinBoxHighPass"))
        self.horizontalLayout_24.addWidget(self.spinBoxHighPass)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_24)
        self.groupBoxSSP = QtGui.QGroupBox(self.tabEOG1)
        self.groupBoxSSP.setGeometry(QtCore.QRect(10, 230, 361, 101))
        self.groupBoxSSP.setObjectName(_fromUtf8("groupBoxSSP"))
        self.frame_2 = QtGui.QFrame(self.groupBoxSSP)
        self.frame_2.setGeometry(QtCore.QRect(10, 30, 341, 61))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayoutWidget_9 = QtGui.QWidget(self.frame_2)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 10, 325, 41))
        self.horizontalLayoutWidget_9.setObjectName(_fromUtf8("horizontalLayoutWidget_9"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelGrad = QtGui.QLabel(self.horizontalLayoutWidget_9)
        self.labelGrad.setObjectName(_fromUtf8("labelGrad"))
        self.horizontalLayout_3.addWidget(self.labelGrad)
        self.spinBoxGrad = QtGui.QSpinBox(self.horizontalLayoutWidget_9)
        self.spinBoxGrad.setProperty("value", 2)
        self.spinBoxGrad.setObjectName(_fromUtf8("spinBoxGrad"))
        self.horizontalLayout_3.addWidget(self.spinBoxGrad)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.labelMag = QtGui.QLabel(self.horizontalLayoutWidget_9)
        self.labelMag.setObjectName(_fromUtf8("labelMag"))
        self.horizontalLayout_4.addWidget(self.labelMag)
        self.spinBoxMag = QtGui.QSpinBox(self.horizontalLayoutWidget_9)
        self.spinBoxMag.setProperty("value", 2)
        self.spinBoxMag.setObjectName(_fromUtf8("spinBoxMag"))
        self.horizontalLayout_4.addWidget(self.spinBoxMag)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.labelEeg = QtGui.QLabel(self.horizontalLayoutWidget_9)
        self.labelEeg.setObjectName(_fromUtf8("labelEeg"))
        self.horizontalLayout_5.addWidget(self.labelEeg)
        self.spinBoxEeg = QtGui.QSpinBox(self.horizontalLayoutWidget_9)
        self.spinBoxEeg.setProperty("value", 2)
        self.spinBoxEeg.setObjectName(_fromUtf8("spinBoxEeg"))
        self.horizontalLayout_5.addWidget(self.spinBoxEeg)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)
        self.groupBoxEvent = QtGui.QGroupBox(self.tabEOG1)
        self.groupBoxEvent.setGeometry(QtCore.QRect(10, 10, 541, 99))
        self.groupBoxEvent.setObjectName(_fromUtf8("groupBoxEvent"))
        self.frame = QtGui.QFrame(self.groupBoxEvent)
        self.frame.setGeometry(QtCore.QRect(10, 30, 531, 61))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayoutWidget_8 = QtGui.QWidget(self.frame)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 10, 508, 41))
        self.horizontalLayoutWidget_8.setObjectName(_fromUtf8("horizontalLayoutWidget_8"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelTmin = QtGui.QLabel(self.horizontalLayoutWidget_8)
        self.labelTmin.setObjectName(_fromUtf8("labelTmin"))
        self.horizontalLayout.addWidget(self.labelTmin)
        self.doubleSpinBoxTmin = QtGui.QDoubleSpinBox(self.horizontalLayoutWidget_8)
        self.doubleSpinBoxTmin.setDecimals(3)
        self.doubleSpinBoxTmin.setMinimum(-99.99)
        self.doubleSpinBoxTmin.setSingleStep(0.05)
        self.doubleSpinBoxTmin.setProperty("value", -0.2)
        self.doubleSpinBoxTmin.setObjectName(_fromUtf8("doubleSpinBoxTmin"))
        self.horizontalLayout.addWidget(self.doubleSpinBoxTmin)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelTmax = QtGui.QLabel(self.horizontalLayoutWidget_8)
        self.labelTmax.setObjectName(_fromUtf8("labelTmax"))
        self.horizontalLayout_2.addWidget(self.labelTmax)
        self.doubleSpinBoxTmax = QtGui.QDoubleSpinBox(self.horizontalLayoutWidget_8)
        self.doubleSpinBoxTmax.setDecimals(3)
        self.doubleSpinBoxTmax.setMinimum(-99.99)
        self.doubleSpinBoxTmax.setSingleStep(0.05)
        self.doubleSpinBoxTmax.setProperty("value", 0.2)
        self.doubleSpinBoxTmax.setObjectName(_fromUtf8("doubleSpinBoxTmax"))
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxTmax)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_2)
        self.tabWidgetEOGSettings.addTab(self.tabEOG1, _fromUtf8(""))
        self.tabEOG2 = QtGui.QWidget()
        self.tabEOG2.setObjectName(_fromUtf8("tabEOG2"))
        self.groupBox = QtGui.QGroupBox(self.tabEOG2)
        self.groupBox.setGeometry(QtCore.QRect(10, 150, 491, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.frameEpochRejection = QtGui.QFrame(self.groupBox)
        self.frameEpochRejection.setEnabled(True)
        self.frameEpochRejection.setGeometry(QtCore.QRect(10, 30, 461, 91))
        self.frameEpochRejection.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameEpochRejection.setFrameShadow(QtGui.QFrame.Raised)
        self.frameEpochRejection.setObjectName(_fromUtf8("frameEpochRejection"))
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.frameEpochRejection)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 441, 80))
        self.horizontalLayoutWidget_4.setObjectName(_fromUtf8("horizontalLayoutWidget_4"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.labelGradReject = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.labelGradReject.setObjectName(_fromUtf8("labelGradReject"))
        self.horizontalLayout_14.addWidget(self.labelGradReject)
        self.doubleSpinBoxGradReject = QtGui.QDoubleSpinBox(self.horizontalLayoutWidget_4)
        self.doubleSpinBoxGradReject.setPrefix(_fromUtf8(""))
        self.doubleSpinBoxGradReject.setMaximum(1000000000.0)
        self.doubleSpinBoxGradReject.setProperty("value", 3000.0)
        self.doubleSpinBoxGradReject.setObjectName(_fromUtf8("doubleSpinBoxGradReject"))
        self.horizontalLayout_14.addWidget(self.doubleSpinBoxGradReject)
        self.verticalLayout_2.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.labelEegReject = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.labelEegReject.setObjectName(_fromUtf8("labelEegReject"))
        self.horizontalLayout_11.addWidget(self.labelEegReject)
        self.doubleSpinBoxEEGReject = QtGui.QDoubleSpinBox(self.horizontalLayoutWidget_4)
        self.doubleSpinBoxEEGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEEGReject.setProperty("value", 100.0)
        self.doubleSpinBoxEEGReject.setObjectName(_fromUtf8("doubleSpinBoxEEGReject"))
        self.horizontalLayout_11.addWidget(self.doubleSpinBoxEEGReject)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.labelMagReject = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.labelMagReject.setObjectName(_fromUtf8("labelMagReject"))
        self.horizontalLayout_10.addWidget(self.labelMagReject)
        self.doubleSpinBoxMagReject = QtGui.QDoubleSpinBox(self.horizontalLayoutWidget_4)
        self.doubleSpinBoxMagReject.setMaximum(1000000000.0)
        self.doubleSpinBoxMagReject.setProperty("value", 4000.0)
        self.doubleSpinBoxMagReject.setObjectName(_fromUtf8("doubleSpinBoxMagReject"))
        self.horizontalLayout_10.addWidget(self.doubleSpinBoxMagReject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.labelEogReject = QtGui.QLabel(self.horizontalLayoutWidget_4)
        self.labelEogReject.setObjectName(_fromUtf8("labelEogReject"))
        self.horizontalLayout_15.addWidget(self.labelEogReject)
        self.doubleSpinBoxEOGReject = QtGui.QDoubleSpinBox(self.horizontalLayoutWidget_4)
        self.doubleSpinBoxEOGReject.setMaximum(1000000000.0)
        self.doubleSpinBoxEOGReject.setProperty("value", 1000000000.0)
        self.doubleSpinBoxEOGReject.setObjectName(_fromUtf8("doubleSpinBoxEOGReject"))
        self.horizontalLayout_15.addWidget(self.doubleSpinBoxEOGReject)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_12.addLayout(self.verticalLayout_3)
        self.gridLayoutWidget = QtGui.QWidget(self.tabEOG2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 138))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.spinBoxStart = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBoxStart.setObjectName(_fromUtf8("spinBoxStart"))
        self.gridLayout_2.addWidget(self.spinBoxStart, 0, 1, 1, 1)
        self.checkBoxSSPCompute = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBoxSSPCompute.setObjectName(_fromUtf8("checkBoxSSPCompute"))
        self.gridLayout_2.addWidget(self.checkBoxSSPCompute, 3, 0, 1, 1)
        self.labelTaps = QtGui.QLabel(self.gridLayoutWidget)
        self.labelTaps.setObjectName(_fromUtf8("labelTaps"))
        self.gridLayout_2.addWidget(self.labelTaps, 1, 0, 1, 1)
        self.labelStart2 = QtGui.QLabel(self.gridLayoutWidget)
        self.labelStart2.setObjectName(_fromUtf8("labelStart2"))
        self.gridLayout_2.addWidget(self.labelStart2, 0, 2, 1, 1)
        self.spinBoxTaps = QtGui.QSpinBox(self.gridLayoutWidget)
        self.spinBoxTaps.setMaximum(10000)
        self.spinBoxTaps.setProperty("value", 2048)
        self.spinBoxTaps.setObjectName(_fromUtf8("spinBoxTaps"))
        self.gridLayout_2.addWidget(self.spinBoxTaps, 1, 1, 1, 1)
        self.labelStart1 = QtGui.QLabel(self.gridLayoutWidget)
        self.labelStart1.setObjectName(_fromUtf8("labelStart1"))
        self.gridLayout_2.addWidget(self.labelStart1, 0, 0, 1, 1)
        self.checkBoxSSPProj = QtGui.QCheckBox(self.gridLayoutWidget)
        self.checkBoxSSPProj.setEnabled(True)
        self.checkBoxSSPProj.setChecked(True)
        self.checkBoxSSPProj.setObjectName(_fromUtf8("checkBoxSSPProj"))
        self.gridLayout_2.addWidget(self.checkBoxSSPProj, 2, 0, 1, 1)
        self.tabWidgetEOGSettings.addTab(self.tabEOG2, _fromUtf8(""))
        self.widget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 490, 301, 371))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidgetEOGSettings.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButtonCompute, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QObject.connect(self.pushButtonComputeBatch, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.acceptBatch)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.scrollArea, self.doubleSpinBoxTmin)
        Dialog.setTabOrder(self.doubleSpinBoxTmin, self.doubleSpinBoxTmax)
        Dialog.setTabOrder(self.doubleSpinBoxTmax, self.spinBoxLowPass)
        Dialog.setTabOrder(self.spinBoxLowPass, self.spinBoxHighPass)
        Dialog.setTabOrder(self.spinBoxHighPass, self.spinBoxGrad)
        Dialog.setTabOrder(self.spinBoxGrad, self.spinBoxMag)
        Dialog.setTabOrder(self.spinBoxMag, self.spinBoxEeg)
        Dialog.setTabOrder(self.spinBoxEeg, self.spinBoxLow)
        Dialog.setTabOrder(self.spinBoxLow, self.spinBoxHigh)
        Dialog.setTabOrder(self.spinBoxHigh, self.pushButtonCancel)
        Dialog.setTabOrder(self.pushButtonCancel, self.pushButtonCompute)
        Dialog.setTabOrder(self.pushButtonCompute, self.tabWidgetEOGSettings)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Meggie - Compute EOG projections", None))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel", None))
        self.pushButtonComputeBatch.setText(_translate("Dialog", "Compute Batch", None))
        self.pushButtonCompute.setText(_translate("Dialog", "Compute", None))
        self.groupBoxFilter.setTitle(_translate("Dialog", "Filtering cut-off frequency", None))
        self.labelLow.setText(_translate("Dialog", "Low:", None))
        self.spinBoxLow.setSuffix(_translate("Dialog", " Hz", None))
        self.labelHigh.setText(_translate("Dialog", "High:", None))
        self.spinBoxHigh.setSuffix(_translate("Dialog", " Hz", None))
        self.groupBoxFilteringEOG.setTitle(_translate("Dialog", "Filter cut-off frequencies for EOG channel", None))
        self.labelLowPass.setText(_translate("Dialog", "Low:", None))
        self.spinBoxLowPass.setSuffix(_translate("Dialog", " Hz", None))
        self.labelHighPass.setText(_translate("Dialog", "High:", None))
        self.spinBoxHighPass.setSuffix(_translate("Dialog", " Hz", None))
        self.groupBoxSSP.setTitle(_translate("Dialog", "Number of SSP vectors", None))
        self.labelGrad.setText(_translate("Dialog", "Grad:", None))
        self.labelMag.setText(_translate("Dialog", "Mag:", None))
        self.labelEeg.setText(_translate("Dialog", "EEG:", None))
        self.groupBoxEvent.setTitle(_translate("Dialog", "Events", None))
        self.labelTmin.setText(_translate("Dialog", "Start time:", None))
        self.doubleSpinBoxTmin.setSuffix(_translate("Dialog", " s", None))
        self.labelTmax.setText(_translate("Dialog", "End time:", None))
        self.doubleSpinBoxTmax.setSuffix(_translate("Dialog", " s", None))
        self.tabWidgetEOGSettings.setTabText(self.tabWidgetEOGSettings.indexOf(self.tabEOG1), _translate("Dialog", "EOG settings", None))
        self.groupBox.setTitle(_translate("Dialog", "Epoch rejection", None))
        self.labelGradReject.setText(_translate("Dialog", "Grad:", None))
        self.doubleSpinBoxGradReject.setSuffix(_translate("Dialog", " fT/cm", None))
        self.labelEegReject.setText(_translate("Dialog", "EEG:", None))
        self.doubleSpinBoxEEGReject.setSuffix(_translate("Dialog", " uV", None))
        self.labelMagReject.setText(_translate("Dialog", "Mag:", None))
        self.doubleSpinBoxMagReject.setSuffix(_translate("Dialog", " fT", None))
        self.labelEogReject.setText(_translate("Dialog", "EOG:", None))
        self.doubleSpinBoxEOGReject.setSuffix(_translate("Dialog", " uV", None))
        self.checkBoxSSPCompute.setText(_translate("Dialog", "Compute SSP after averaging", None))
        self.labelTaps.setText(_translate("Dialog", "Number of taps to use for filtering:", None))
        self.labelStart2.setText(_translate("Dialog", "seconds.", None))
        self.labelStart1.setText(_translate("Dialog", "Start artifact detection after", None))
        self.checkBoxSSPProj.setText(_translate("Dialog", "Exclude SSP projections currently in the file", None))
        self.tabWidgetEOGSettings.setTabText(self.tabWidgetEOGSettings.indexOf(self.tabEOG2), _translate("Dialog", "Advanced", None))

