import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('untitled2.ui', self)
        self.pushButton.clicked.connect(self.end)

    def end(self):
        self.change = self.lineEdit.text()
        self.close()



def start():
    app = QApplication(sys.argv)
    w = Main()
    w.exec_()
    sys.exit(app.exec_())


#start()