# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created: Thu May 30 15:15:38 2013
#      by: PyQt4 UI code generator 4.10
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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(784, 540)
        self.textBrowser = QtGui.QTextBrowser(About)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 761, 521))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "Dialog", None))
        self.textBrowser.setHtml(_translate("About", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This is a prototype version of Meggie,  a graphical user interface for preprocessing and analyzing MEG-measurement data. Meggie utilizes external modules such as the MNE software package and MaxFilter.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Meggie is realeased under the Simplified BSD lisence:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">Copyright (c) &lt;2013&gt;, &lt;Kari Aliranta, Jaakko Leppäkangas, Janne Pesonen and Atte Rautio&gt;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">All rights reserved.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">Redistribution and use in source and binary forms, with or without</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">modification, are permitted provided that the following conditions are met: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">1. Redistributions of source code must retain the above copyright notice, this</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">   list of conditions and the following disclaimer. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">2. Redistributions in binary form must reproduce the above copyright notice,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">   this list of conditions and the following disclaimer in the documentation</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">   and/or other materials provided with the distribution. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">The views and conclusions contained in the software and documentation are those</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">of the authors and should not be interpreted as representing official policies, </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#f9f9f9;\"><span style=\" font-family:\'monospace,Courier\'; font-size:8pt; color:#000000; background-color:#f9f9f9;\">either expressed or implied, of the FreeBSD Project.</span></p></body></html>", None))

