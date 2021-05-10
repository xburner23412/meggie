"""
"""
from PyQt5 import QtWidgets

from meggie.utilities.dialogs.shortMessageBoxUi import Ui_shortMessageBox


class shortMessageBox(QtWidgets.QDialog):
    """
    Class for creating simple messageboxes displaying messages
    """

    def __init__(self, message, parent):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_shortMessageBox()
        self.ui.setupUi(self)

        self.setWindowTitle('Meggie - Info')
        self.ui.labelMessage.setText(message)

