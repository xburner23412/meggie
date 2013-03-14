  # -*- coding: utf-8 -*-
 
 
import os,sys
from root.controller.file import File
from infodialog_main import InfoDialog
#from Project import Project
 
from PyQt4 import QtCore,QtGui
 
# Import the pyuic4-compiled main UI module 
from CreateProjectDialog_Ui import Ui_CreateProjectDialog
 
# Create a dialog main window
class CreateProjectDialog(QtGui.QDialog):
    fname = ''
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.fname = ''
        """
        Reference to main dialog window
        """       
        self.ui = Ui_CreateProjectDialog() # Refers to class in file CreateProjecDialog
        self.ui.setupUi(self)
 
    
    def on_browseButton_clicked(self, checked=None):
        if checked is None: return # Standard for file dialog opening twice
        # Jaakko koodaa: vaihdoin fnamen attribuutiksi
        self.fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        print self.fname
        
        
        """
        Jaakko koodaa: tästä alkaa 
        """
        self.ui.FilePathLineEdit.setText(self.fname)
        
    def on_showFileInfoButton_clicked(self):
        f = File()
        raw = f.open_raw(self.fname)
        self.infoDialog = InfoDialog(raw)
        self.infoDialog.show()
                
        """
        Jaakko koodaa: tähän loppuu
        """
          
    
def main(): 
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main() 