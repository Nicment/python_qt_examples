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
from PyQt5.QtGui import QPainter, QBrush, QPen  
from PyQt5.QtWidgets import (QHBoxLayout, QPushButton, QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QGridLayout, QLabel)


class widgetGenerator(QWidget):
    
    def __init__(self, labelText:str, ledColor:str):
        super().__init__()    
        self.labelText = labelText 
        self.ledColor = ledColor
    
    def sensorWidget(self):

        self.sensor = QLabel(self.labelText,self)
        
        self.ledSensor = QLabel("",self) 
        self.ledSensor.setStyleSheet(f"border:3px solid black; border-radius: 40px; background-color: {self.ledColor}")   
                
        self.sensor_mas_led = QWidget()
        self.sensor_mas_led.layout = QHBoxLayout() 
        self.sensor_mas_led.setLayout(self.sensor_mas_led.layout) 
        self.sensor_mas_led.layout.addWidget(self.sensor)
        self.sensor_mas_led.layout.addWidget(self.ledSensor)
        
        return self.sensor_mas_led
    

class ExampleDisplay(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.resize(800, 600)
        mainLayout = QGridLayout()
        #internalLayout = QGridLayout()
        self.change = 1
        
        self.driverStatus = widgetGenerator("Driver Status","green").sensorWidget()
        self.tempStatus = widgetGenerator("Temp Status", "red").sensorWidget()
        self.sensor1= widgetGenerator("Sensor 1","red").sensorWidget()
        self.sensor2= widgetGenerator("Sensor 2", "green").sensorWidget()
        self.sensor3= widgetGenerator("sensor 3", "blue").sensorWidget()
        self.sensor4= widgetGenerator("sensor 4", "green").sensorWidget()
        
        
        mainLayout.addWidget(self.driverStatus, 0,0)
        mainLayout.addWidget(self.tempStatus,1,0)
        
        mainLayout.addWidget(self.sensor1, 0,1)
        mainLayout.addWidget(self.sensor2, 1,1)
        
        mainLayout.addWidget(self.sensor3, 0,2)
        mainLayout.addWidget(self.sensor4, 1,2)
        
        
        self.setWindowTitle('Signal and slot')
        self.setLayout(mainLayout)
        
        self.show()
             
        
        
    @pyqtSlot()
    def on_click(self):
        if self.change:     
            print("Hola Mundo")
            self.change = 0
        else:
            print("Adios mundo")
            self.change = 1
                


def main():
    app = QApplication(sys.argv)
    ex  = ExampleDisplay()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
