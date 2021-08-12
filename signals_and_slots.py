#!/usr/bin/python

"""
SUNNY APP PyQt5 tutorial

In this example, we have a class with a function
and use this for create 6 widgets whit label text and ledSensor

Author: Nicolás Silva 
"""
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import (QSize, pyqtSlot, QPoint)
from PyQt5.QtGui import (QPictureIO, QPixmap, QPicture, QPainter)
from PyQt5.QtWidgets import (QHBoxLayout, QPushButton, QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QGridLayout, QLabel, QSizePolicy)

class ledSensor(QWidget):
    def __init__(self,ledColor:str, ):
        super().__init__()  
        self.ledColor = ledColor
        
    def createLed(self):
        
        self.ledSensor = QLabel("",self)
        self.ledSensor.setMinimumSize(80,80)
        self.ledSensor.setMaximumSize(80,80)
        self.ledSensor.setSizePolicy (QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.ledSensor.setStyleSheet(f"border:3px solid black; border-radius: 40px; background-color: {self.ledColor}")   
        return self.ledSensor
      
    def changeStateLed(self,changeFactor:int):
        
        #Se hace la implementacion del cambio de color del led
        self.changeFactor = changeFactor
        self.changeFactorCircle = (self.changeFactor//2) 
        self.ledSensor.setMinimumSize(self.changeFactor,self.changeFactor)
        self.ledSensor.setMaximumSize(self.changeFactor,self.changeFactor)
        self.ledSensor.setSizePolicy (QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.ledSensor.setStyleSheet(f"border:3px solid black; border-radius: {self.changeFactorCircle}px; background-color: {self.ledColor}")   
        
        return self.ledSensor 

class textWidget(QLabel):
    def __init__(self,textWidget:str, ):
        super().__init__()  
        self.textWidget = textWidget
    
    def createText(self):
        
        self.textSensor = QLabel(self.textWidget,self)
        self.textSensor.setSizePolicy (QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.textSensor.setStyleSheet("font: 30px") 
        return self.textSensor  
        
    def changeStateText(self, changeFactor):
        self.changeFactor = (changeFactor//4)+4
        self.textSensor.setSizePolicy (QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.textSensor.setStyleSheet(f"font: bold {self.changeFactor}px")  
        

class widgetGenerator(QWidget):
    
    def __init__(self, text, led:QLabel):
        super().__init__()    
        self.labelText = text 
        self.ledSensor = led
    
    def indicatorWidget(self):
            
        self.sensor_mas_led = QWidget()
        self.sensor_mas_led.layout = QHBoxLayout() 
        self.sensor_mas_led.setLayout(self.sensor_mas_led.layout) 
        self.sensor_mas_led.layout.addWidget(self.labelText)
        self.sensor_mas_led.layout.addWidget(self.ledSensor)
        
        return self.sensor_mas_led
    
    def displayWidget(self,data: str):
        
        self.data = data   
        self.sensor = QLabel(self.labelText,self)
        self.lcd = QLCDNumber()
        self.lcd.display(self.data)
                 
        self.sensor_display = QWidget()
        self.sensor_display.layout = QHBoxLayout() 
        self.sensor_display.setLayout(self.sensor_display.layout) 
        self.sensor_display.layout.addWidget(self.sensor)
        self.sensor_display.layout.addWidget(self.lcd)  
        
        return self.sensor_display

class ExampleDisplay(QWidget):

    def __init__(self):
        super().__init__()
        self.changeFactor = 100
        self.initUI()
        
        
    def resizeEvent(self, a0: QtGui.QResizeEvent):
        
        self.changeFactorWidth = self.frameSize().width()//10
        self.changeFactorHeight = self.frameSize().height()//10
        if self.changeFactorWidth > self.changeFactorHeight:
            self.changeFactor = self.changeFactorWidth
        else: self.changeFactor = self.changeFactorHeight 
        
        self.driverLed.changeStateLed(self.changeFactor)
        self.tempLed.changeStateLed(self.changeFactor)
        self.sensor1Led.changeStateLed(self.changeFactor)
        self.sensor2Led.changeStateLed(self.changeFactor)
        self.sensor3Led.changeStateLed(self.changeFactor)
        self.sensor4Led.changeStateLed(self.changeFactor)
        self.electroValLed.changeStateLed(self.changeFactor)
        
        self.driverText.changeStateText(self.changeFactor)
        self.tempText.changeStateText(self.changeFactor)
        self.sensor1Text.changeStateText(self.changeFactor)
        self.sensor2Text.changeStateText(self.changeFactor)
        self.sensor3Text.changeStateText(self.changeFactor)
        self.sensor4Text.changeStateText(self.changeFactor)
        self.electroValText.changeStateText(self.changeFactor)


    def initUI(self):
        self.resize(1000, 500)
        
        mainLayout = QGridLayout()
        self.change = 1
        self.temperature = 20
        self.humidity = 80
        
        self.driverText = textWidget("Driver Status")
        self.tempText = textWidget("Temperature")
        self.sensor1Text = textWidget("Sensor 1")
        self.sensor2Text = textWidget("Sensor 2")
        self.sensor3Text = textWidget("Sensor 3")
        self.sensor4Text = textWidget("Sensor 4")
        self.electroValText = textWidget("Electro-Valuation Status")
        
        self.driverLed = ledSensor("red")
        self.tempLed = ledSensor("green")
        self.sensor1Led = ledSensor("green")
        self.sensor2Led = ledSensor("green")
        self.sensor3Led = ledSensor("green")
        self.sensor4Led = ledSensor("green")
        self.electroValLed = ledSensor("green")
        
        self.driverStatus = widgetGenerator(self.driverText.createText(), self.driverLed.createLed()).indicatorWidget()
        self.tempStatus = widgetGenerator(self.tempText.createText(), self.tempLed.createLed()).indicatorWidget()
        self.sensor1= widgetGenerator(self.sensor1Text.createText(), self.sensor1Led.createLed()).indicatorWidget()
        self.sensor2= widgetGenerator(self.sensor2Text.createText(), self.sensor2Led.createLed()).indicatorWidget()
        self.sensor3= widgetGenerator(self.sensor3Text.createText(), self.sensor3Led.createLed()).indicatorWidget()
        self.sensor4= widgetGenerator(self.sensor4Text.createText(), self.sensor4Led.createLed()).indicatorWidget()
        self.elvaStatus = widgetGenerator(self.electroValText.createText(), self.electroValLed.createLed()).indicatorWidget()
        self.dataTemp = widgetGenerator("Temp (°C)","white").displayWidget(f"{self.temperature}")
        self.dataHum = widgetGenerator("Humidity (%)","white").displayWidget(f"{self.humidity}")
        
        mainLayout.addWidget(self.driverStatus, 0,0)
        mainLayout.addWidget(self.tempStatus,1,0)
        mainLayout.addWidget(self.elvaStatus,2,0) 
        
        mainLayout.addWidget(self.sensor1, 0,1)
        mainLayout.addWidget(self.sensor2, 1,1)
        
        mainLayout.addWidget(self.sensor3, 0,2)
        mainLayout.addWidget(self.sensor4, 1,2)
        
        mainLayout.addWidget(self.dataTemp, 2,1)
        mainLayout.addWidget(self.dataHum,2,2)
        
               
        
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
