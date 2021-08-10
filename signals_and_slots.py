#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.

Author: Jan Bodnar
Website: zetcode.com
"""
import sys
from PyQt5.QtCore import (Qt , pyqtSlot)
from PyQt5.QtWidgets import (QPushButton, QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QGridLayout)


class ExampleDisplay(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.resize(800, 600)
        mainLayout = QGridLayout()
        self.change = 1

        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        self.vbox = QWidget()
        self.vbox.layout = QVBoxLayout()
        self.vbox.layout.addWidget(lcd)
        self.vbox.layout.addWidget(sld)
        self.vbox.setLayout(self.vbox.layout)
        sld.valueChanged.connect(lcd.display)
        
        self.lcd1 = QLCDNumber(self)
        sld1 = QSlider(Qt.Horizontal, self)
        button1 = QPushButton("Boton",self)

        self.vbox1 = QWidget()
        self.vbox1.layout = QVBoxLayout()
        self.vbox1.layout.addWidget(self.lcd1)
        self.vbox1.layout.addWidget(sld1)
        self.vbox1.layout.addWidget(button1)
        button1.clicked.connect(self.on_click)
        self.vbox1.setLayout(self.vbox1.layout)
        sld1.valueChanged.connect(self.lcd1.display)

        mainLayout.addWidget(self.vbox1, 0,0)
        mainLayout.addWidget(self.vbox,0,1)
        
        self.setWindowTitle('Signal and slot')
        self.setLayout(mainLayout)
        
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        if self.change:     
            self.lcd1.hide()
            self.change = 0
        else:
            self.lcd1.show()
            self.change = 1
                


def main():
    app = QApplication(sys.argv)
    ex  = ExampleDisplay()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
