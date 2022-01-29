import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem, QTableWidget
from PyQt5.uic import loadUi
from prog import Main

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('untitled.ui', self)
        conn = sqlite3.connect('coffee.sqlite')
        cur = conn.cursor()
        a = 0
        for i in cur.execute('SELECT * FROM NIGGER').fetchall():
            self.table.insertRow(a)
            self.table.setItem(a, 0, QTableWidgetItem(i[0]))
            self.table.setItem(a, 1, QTableWidgetItem(i[1]))
            self.table.setItem(a, 2, QTableWidgetItem(i[2]))
            self.table.setItem(a, 3, QTableWidgetItem(i[3]))
            self.table.setItem(a, 4, QTableWidgetItem(i[4]))
            self.table.setItem(a, 5, QTableWidgetItem(i[5]))
            a += 1
            print(i)

        self.table.itemDoubleClicked.connect(self.nigger)


        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("id"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("название"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem("степень прожарки"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem("Молотый/в зернах"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem("цена"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem("объем упаковки"))

    def nigger(self, item):
        w = Main()
        w.exec_()
        item.setText(w.change)

def start():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


start()