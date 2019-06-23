import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import QMessageBox

from ui import HomeUI, PayUI

import time

class HomeWindow(QtWidgets.QMainWindow):

    def __init__(self):
    
        super(HomeWindow, self).__init__()
        
        self.ui = HomeUI()
        self.ui.setupUi(self)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)


        self.showTime()

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString("hh:mm")
        if time.second() % 2 == 0:
            text = text[:2] + " " + text[3:]

        self.ui.lcdNumber.display(text)


class PayWindow(QtWidgets.QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
    
        super(PayWindow, self).__init__()
        
        self.ui = PayUI()
        self.ui.setupUi(self)

        # NOTE: no button needed yet
        # self.ui.pushButton.clicked.connect(self.switch)

    def switch(self):
        print("Switch window")
        self.switch_window.emit()


class MyGui:

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        self.homewindow = HomeWindow()
        self.paywindow = PayWindow()
        # NOTE: no button needed yet
        # self.paywindow.switch_window.connect(self.show_home)
        
        pass

    def show_home(self):
        self.paywindow.hide()
        self.homewindow.show()

    def show_pay(self):
        self.homewindow.hide()
        self.paywindow.show()

    def display_ordernumber(self, val):
        self.homewindow.ui.order_number.setText(val)

    def display_validpage(self, val)
        self.paywindow.ui.lblbarcode(val[0])
        self.paywindow.ui.lblmasuk(val[1])
        self.paywindow.ui.lblkeluar(val[2])
        self.paywindow.ui.lbldurasi(val[3])
        self.paywindow.ui.lblHarga("<html><head/><body><p><span style=\" color:#fc0107;\">Rp%s,00</span></p></body></html>" % val[4])

    def start(self):
        sys.exit(self.app.exec_())


if __name__ == '__main__':
    mygui = MyGui()
    controller = MyGui()
    controller.show_pay()
    print("fsd")
    mygui.start()