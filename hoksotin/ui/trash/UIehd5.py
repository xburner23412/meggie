# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UIehdotus5.ui'
#
# Created: Sat Mar 23 12:40:46 2013
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(818, 785)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.metaBox = QtGui.QGroupBox(self.centralwidget)
        self.metaBox.setObjectName(_fromUtf8("metaBox"))
        self.layoutWidget_3 = QtGui.QWidget(self.metaBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(26, 35, 113, 23))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.labelDate = QtGui.QLabel(self.layoutWidget_3)
        self.labelDate.setObjectName(_fromUtf8("labelDate"))
        self.gridLayout_3.addWidget(self.labelDate, 0, 0, 1, 1)
        self.labelDateValue = QtGui.QLabel(self.layoutWidget_3)
        self.labelDateValue.setObjectName(_fromUtf8("labelDateValue"))
        self.gridLayout_3.addWidget(self.labelDateValue, 0, 1, 1, 1)
        self.filtersBox = QtGui.QGroupBox(self.metaBox)
        self.filtersBox.setGeometry(QtCore.QRect(0, 70, 299, 125))
        self.filtersBox.setObjectName(_fromUtf8("filtersBox"))
        self.layoutWidget_4 = QtGui.QWidget(self.filtersBox)
        self.layoutWidget_4.setGeometry(QtCore.QRect(23, 31, 181, 77))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget_4)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.labelLow = QtGui.QLabel(self.layoutWidget_4)
        self.labelLow.setLineWidth(1)
        self.labelLow.setScaledContents(True)
        self.labelLow.setObjectName(_fromUtf8("labelLow"))
        self.gridLayout_2.addWidget(self.labelLow, 0, 0, 1, 1)
        self.labelLowValue = QtGui.QLabel(self.layoutWidget_4)
        self.labelLowValue.setObjectName(_fromUtf8("labelLowValue"))
        self.gridLayout_2.addWidget(self.labelLowValue, 0, 1, 1, 1)
        self.labelHigh = QtGui.QLabel(self.layoutWidget_4)
        self.labelHigh.setObjectName(_fromUtf8("labelHigh"))
        self.gridLayout_2.addWidget(self.labelHigh, 1, 0, 1, 1)
        self.labelHighValue = QtGui.QLabel(self.layoutWidget_4)
        self.labelHighValue.setObjectName(_fromUtf8("labelHighValue"))
        self.gridLayout_2.addWidget(self.labelHighValue, 1, 1, 1, 1)
        self.labelSfreq = QtGui.QLabel(self.layoutWidget_4)
        self.labelSfreq.setObjectName(_fromUtf8("labelSfreq"))
        self.gridLayout_2.addWidget(self.labelSfreq, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.metaBox)
        self.channelsBox = QtGui.QGroupBox(self.centralwidget)
        self.channelsBox.setObjectName(_fromUtf8("channelsBox"))
        self.layoutWidget_5 = QtGui.QWidget(self.channelsBox)
        self.layoutWidget_5.setGeometry(QtCore.QRect(20, 23, 300, 142))
        self.layoutWidget_5.setObjectName(_fromUtf8("layoutWidget_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.layoutWidget_5)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.labelEEG = QtGui.QLabel(self.layoutWidget_5)
        self.labelEEG.setObjectName(_fromUtf8("labelEEG"))
        self.gridLayout_4.addWidget(self.labelEEG, 0, 0, 1, 1)
        self.labelEEGValue = QtGui.QLabel(self.layoutWidget_5)
        self.labelEEGValue.setObjectName(_fromUtf8("labelEEGValue"))
        self.gridLayout_4.addWidget(self.labelEEGValue, 0, 1, 1, 1)
        self.labelGradMEG = QtGui.QLabel(self.layoutWidget_5)
        self.labelGradMEG.setObjectName(_fromUtf8("labelGradMEG"))
        self.gridLayout_4.addWidget(self.labelGradMEG, 1, 0, 1, 1)
        self.labelGradMEGValue = QtGui.QLabel(self.layoutWidget_5)
        self.labelGradMEGValue.setObjectName(_fromUtf8("labelGradMEGValue"))
        self.gridLayout_4.addWidget(self.labelGradMEGValue, 1, 1, 1, 1)
        self.labelMagMEG = QtGui.QLabel(self.layoutWidget_5)
        self.labelMagMEG.setObjectName(_fromUtf8("labelMagMEG"))
        self.gridLayout_4.addWidget(self.labelMagMEG, 2, 0, 1, 1)
        self.labelMagMEGValue = QtGui.QLabel(self.layoutWidget_5)
        self.labelMagMEGValue.setObjectName(_fromUtf8("labelMagMEGValue"))
        self.gridLayout_4.addWidget(self.labelMagMEGValue, 2, 1, 1, 1)
        self.labelSamples = QtGui.QLabel(self.layoutWidget_5)
        self.labelSamples.setObjectName(_fromUtf8("labelSamples"))
        self.gridLayout_4.addWidget(self.labelSamples, 3, 0, 1, 1)
        self.labelSamplesValue = QtGui.QLabel(self.layoutWidget_5)
        self.labelSamplesValue.setObjectName(_fromUtf8("labelSamplesValue"))
        self.gridLayout_4.addWidget(self.labelSamplesValue, 3, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.channelsBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 818, 29))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setMinimumSize(QtCore.QSize(430, 97))
        self.dockWidget.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea|QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.layoutWidget = QtGui.QWidget(self.dockWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 33))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonEpoch = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonEpoch.setObjectName(_fromUtf8("pushButtonEpoch"))
        self.horizontalLayout.addWidget(self.pushButtonEpoch)
        self.pushButtonAverage = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonAverage.setObjectName(_fromUtf8("pushButtonAverage"))
        self.horizontalLayout.addWidget(self.pushButtonAverage)
        self.pushButtonaverage = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonaverage.setObjectName(_fromUtf8("pushButtonaverage"))
        self.horizontalLayout.addWidget(self.pushButtonaverage)
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(20, 130, 364, 571))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabRecommended = QtGui.QWidget()
        self.tabRecommended.setMaximumSize(QtCore.QSize(360, 16777215))
        self.tabRecommended.setAccessibleName(_fromUtf8(""))
        self.tabRecommended.setObjectName(_fromUtf8("tabRecommended"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tabRecommended)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 511))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.listWidgetEpochs = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.listWidgetEpochs.setObjectName(_fromUtf8("listWidgetEpochs"))
        item = QtGui.QListWidgetItem()
        self.listWidgetEpochs.addItem(item)
        self.horizontalLayout_3.addWidget(self.listWidgetEpochs)
        self.tabWidget.addTab(self.tabRecommended, _fromUtf8(""))
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget)
        self.actionLoad_file = QtGui.QAction(MainWindow)
        self.actionLoad_file.setObjectName(_fromUtf8("actionLoad_file"))
        self.actionSave_file = QtGui.QAction(MainWindow)
        self.actionSave_file.setObjectName(_fromUtf8("actionSave_file"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.menuFile.addAction(self.actionLoad_file)
        self.menuFile.addAction(self.actionSave_file)
        self.menuTools.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.metaBox.setTitle(_translate("MainWindow", "Background", None))
        self.labelDate.setText(_translate("MainWindow", "Date:", None))
        self.labelDateValue.setText(_translate("MainWindow", "DateValue", None))
        self.filtersBox.setTitle(_translate("MainWindow", "Filters", None))
        self.labelLow.setText(_translate("MainWindow", "Low-pass:", None))
        self.labelLowValue.setText(_translate("MainWindow", "Low-pass value", None))
        self.labelHigh.setText(_translate("MainWindow", "High-pass:", None))
        self.labelHighValue.setText(_translate("MainWindow", "High-pass value", None))
        self.labelSfreq.setText(_translate("MainWindow", "TextLabel:", None))
        self.label_5.setText(_translate("MainWindow", "TextLabel", None))
        self.channelsBox.setTitle(_translate("MainWindow", "Channels", None))
        self.labelEEG.setText(_translate("MainWindow", "EEG:", None))
        self.labelEEGValue.setText(_translate("MainWindow", "EEG value", None))
        self.labelGradMEG.setText(_translate("MainWindow", "Grad. MEG:", None))
        self.labelGradMEGValue.setText(_translate("MainWindow", "Grad. MEG value", None))
        self.labelMagMEG.setText(_translate("MainWindow", "Mag. MEG:", None))
        self.labelMagMEGValue.setText(_translate("MainWindow", "Mag. MEG value", None))
        self.labelSamples.setText(_translate("MainWindow", "Samples:", None))
        self.labelSamplesValue.setText(_translate("MainWindow", "SamplesValue", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.pushButtonEpoch.setText(_translate("MainWindow", "Epoch", None))
        self.pushButtonAverage.setText(_translate("MainWindow", "Average", None))
        self.pushButtonaverage.setText(_translate("MainWindow", "Visualize", None))
        __sortingEnabled = self.listWidgetEpochs.isSortingEnabled()
        self.listWidgetEpochs.setSortingEnabled(False)
        item = self.listWidgetEpochs.item(0)
        item.setText(_translate("MainWindow", "Epoch", None))
        self.listWidgetEpochs.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRecommended), _translate("MainWindow", "Recommended actions", None))
        self.actionLoad_file.setText(_translate("MainWindow", "Load file", None))
        self.actionSave_file.setText(_translate("MainWindow", "Save file", None))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences", None))
