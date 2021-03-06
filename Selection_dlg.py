from PyQt5 import QtGui
from PyQt5 import QtWidgets, QtCore

from Selection_Form import Ui_Dialog
from Socket_controller import Socket_controller


class Selection_form(QtWidgets.QDialog):

    def __init__(self, parent: QtWidgets.QWidget, sock: Socket_controller):
        super(Selection_form, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.sock = sock
        self.ui.listWidget.addItems(self.sock.get_notebook_list())
        self.ui.ok_button.clicked.connect(self.ok_button)
        self.ui.new_button.clicked.connect(self.new_button)
        self.file = ''
        self.res = 0

    def ok_button(self):
        self.file = self.ui.listWidget.selectedItems()[0].text()
        self.res = 1
        self.close()

    def new_button(self):
        self.file = self.ui.filename.text()
        self.close()
        self.res = 2
