import sys
import threading
import time
import traceback

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QIODevice
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
import schedule

thr_stop = 0


class MainWindow(QMainWindow):
    portlist = QSerialPortInfo().availablePorts()
    serial = QSerialPort()
    serial.setBaudRate(9600)

    curport = 'none'

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('Arduino.ui', self)
        for i in self.portlist:
            self.ports.addItem(i.portName())
        self.con.clicked.connect(self.connect)
        self.portclose.clicked.connect(self.close)
        self.serial.readyRead.connect(self.updateInfo)

    def food(self):
        if self.curport == 'none':
            return
        self.serial.write(b'1')
        print('вода залита')

    def trash(self):
        if self.curport == 'none':
            return
        self.serial.write(b'2')
        print('вода выведена')

    def gas(self):
        if self.curport == 'none':
            return
        self.serial.write(b'0')
        print('газ подкачен')

    def lightup(self):
        if self.curport == 'none':
            return
        self.serial.write(b'3')
        self.serial.write(b'1')
        print('свет включен')

    def lightdown(self):
        if self.curport == 'none':
            return
        self.serial.write(b'3')
        self.serial.write(b'0')
        print('свет выключен')

    def schedfunc(self):
        global thr_stop
        self.w_time.setText()
        while 1:
            if thr_stop:
                break
            schedule.run_pending()
            time.sleep(0.5)

    def updateInfo(self):
        try:
            tip, data = str(self.serial.readLine(), 'utf-8').split()
        except:
            self.malf.setText('Нет доступа к устройству, проверьте подключение')
        self.malf.setText('Не обнаружены')
        if tip == '0':
            if data == '1':
                self.alarm.setText('Норма')
            elif data == '2':
                self.alarm.setText('Мало воды')
            else:
                self.alarm.setText('ПЕРЕПОЛНЕНИЕ!')

    def connect(self):
        if self.ports.currentText() == 'none' or self.curport == self.ports.currentText():
            return
        self.curport = self.ports.currentText()
        self.portlabel.setText(f"Подключенный порт: {self.ports.currentText()}")
        self.serial.setPortName(self.ports.currentText())
        self.serial.open(QIODevice.ReadWrite)
        self.serial.write(b'1')
        print(self.serial.portName())

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.trash()
        global thr_stop
        thr_stop = 1

    def close(self):
        self.serial.close()
        self.portlabel.setText(f"Подключенный порт: none")


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)


sys.excepthook = excepthook

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    schedule.every(12).days.do(w.food)
    schedule.every(12).days.do(w.trash)
    schedule.every(1).days.do(w.gas)
    schedule.every().day.at("06:30").do(w.lightup)
    schedule.every().day.at("21:00").do(w.lightdown)
    thr = threading.Thread(target=w.schedfunc, name='thr-1')
    thr.start()
    w.show()
    sys.exit(app.exec_())
