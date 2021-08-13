#!/usr/bin/python

"""
SUNNY APP PyQt5 tutorial

In this example, we have a class with a function
and use this for create 6 widgets whit label text and ledSensor

Author: Nicolás Silva 
"""
import sys
from LedIndicatorWidget import *
from PyQt5 import QtGui
from PyQt5.QtCore import (QSize, pyqtSlot, QPoint, Qt)
#from PyQt5.QtGui import (QPictureIO, QPixmap, QPicture, QPainter)
from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QSplitter, QPushButton, QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QGridLayout, QLabel, QSizePolicy,
                             )

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
        
        self.ledSensorContainer = QWidget()
        self.ledSensorContainer.layout = QVBoxLayout()
        self.ledSensorContainer.setLayout(self.ledSensorContainer.layout)
        self.ledSensorContainer.layout.addWidget(self.ledSensor)
        self.ledSensorContainer.setSizePolicy (QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.ledSensorContainer.setStyleSheet("border:0px solid black;")
        self.ledSensorContainer.layout.setAlignment(Qt.AlignCenter)
        
        return self.ledSensorContainer
      
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
        self.textSensor.setSizePolicy (QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.textSensor.setStyleSheet("font: 30px") 
        return self.textSensor  
        
    def changeStateText(self, changeFactor):
        self.changeFactor = (changeFactor//4)+20
        #self.textSensor.setSizePolicy (QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.textSensor.setStyleSheet(f"border:0px solid white; font: {self.changeFactor}px")  
        

class widgetGenerator(QWidget):
    
    def __init__(self, text: QLabel, led:QLabel):
        super().__init__()    
        self.labelText = text 
        self.ledSensor = led
    
    def verticalBoxWidget(self):
            
        self.verticalBox = QWidget()
        self.verticalBox.layout = QVBoxLayout()
        self.verticalBox.setLayout(self.verticalBox.layout) 
        self.verticalBox.layout.addWidget(self.ledSensor)
        self.verticalBox.layout.addWidget(self.labelText)
        self.verticalBox.layout.setAlignment(Qt.AlignCenter)
        self.verticalBox.setStyleSheet("border:3px solid black;")
        
        
        return self.verticalBox
    
    def displayWidget(self,data: str):
        
        self.data = data   
        self.lcd = QLCDNumber()
        self.lcd.display(self.data)
                 
        self.sensor_display = QWidget()
        self.sensor_display.layout = QHBoxLayout() 
        self.sensor_display.setLayout(self.sensor_display.layout) 
        self.sensor_display.layout.addWidget(self.labelText)
        self.sensor_display.layout.addWidget(self.lcd)  
        
        return self.sensor_display

class displayWidget(QWidget):
    def __init__(self, data: int):
        super().__init__()    
        self.data = data    
    def generate(self):               
        self.lcd = QLCDNumber()
        self.lcd.display(self.data)
        return self.lcd

class ExampleDisplay(QWidget):

    def __init__(self):
        super().__init__()
        self.changeFactor = 100
        self.initUI()
        
        
    def resizeEvent(self, a0: QtGui.QResizeEvent):
        
        self.changeFactorWidth = self.frameSize().width()//20
        self.changeFactorHeight = self.frameSize().height()//20
        if self.changeFactorWidth > self.changeFactorHeight:
            self.changeFactor = self.changeFactorWidth
        else: self.changeFactor = self.changeFactorHeight 
        
        self.driverLed.setFactorResize(self.changeFactor)
        self.tempLed.setFactorResize(self.changeFactor)
        self.sensor1Led.setFactorResize(self.changeFactor)
        self.sensor2Led.setFactorResize(self.changeFactor)
        self.sensor3Led.setFactorResize(self.changeFactor)
        self.sensor4Led.setFactorResize(self.changeFactor)
        self.electroValLed.setFactorResize(self.changeFactor)
        #self.electroValLed.setColor("purple")
        
        self.driverText.changeStateText(self.changeFactor)
        self.tempText.changeStateText(self.changeFactor)
        self.sensor1Text.changeStateText(self.changeFactor)
        self.sensor2Text.changeStateText(self.changeFactor)
        self.sensor3Text.changeStateText(self.changeFactor)
        self.sensor4Text.changeStateText(self.changeFactor)
        self.electroValText.changeStateText(self.changeFactor)
        #self.led.setFactorResize(self.changeFactor)


    def initUI(self):
        self.resize(1000, 500)
        
        mainLayout = QGridLayout()
        self.change = 1
        self.temperature = 20
        self.humidity = 80
        
        #self.led = LedIndicator("red")
        #self.led.setDisabled(True)  # Make the led non clickable

        
        self.driverText = textWidget("D Status")
        self.tempText = textWidget("T Status")
        self.electroValText = textWidget("E Status")
        
        self.sensor1Text = textWidget("Sensor 1")
        self.sensor2Text = textWidget("Sensor 2")
        self.sensor3Text = textWidget("Sensor 3")
        self.sensor4Text = textWidget("Sensor 4")
        
        self.displayTemperatureText = textWidget("Temp (°C)")
        self.displayHumidityText = textWidget("Humidity (%)")
        self.displayVelocityText = textWidget("Velocity (rpm)")
                
        self.driverLed = LedIndicator("red")
        self.tempLed = LedIndicator("red")
        self.sensor1Led = LedIndicator("green")
        self.sensor2Led = LedIndicator("red")
        self.sensor3Led = LedIndicator("green")
        self.sensor4Led = LedIndicator("red")
        self.electroValLed = LedIndicator("green")
        
        self.displayTemperature = displayWidget(self.temperature).generate()
        self.displayHumidity = displayWidget(self.humidity).generate()
        
        self.driverStatus = widgetGenerator(self.driverText.createText(), self.driverLed).verticalBoxWidget()
        self.tempStatus = widgetGenerator(self.tempText.createText(), self.tempLed).verticalBoxWidget()
        self.elvaStatus = widgetGenerator(self.electroValText.createText(), self.electroValLed).verticalBoxWidget()
        
        self.sensor1= widgetGenerator(self.sensor1Text.createText(), self.sensor1Led).verticalBoxWidget()
        self.sensor2= widgetGenerator(self.sensor2Text.createText(), self.sensor2Led).verticalBoxWidget()
        #self.packSensor1 = widgetGenerator(self.sensor2, self.sensor1).verticalBoxWidget()
        
        self.sensor3= widgetGenerator(self.sensor3Text.createText(), self.sensor3Led).verticalBoxWidget()
        self.sensor4= widgetGenerator(self.sensor4Text.createText(), self.sensor4Led).verticalBoxWidget()
        #self.packSensor2 = widgetGenerator(self.sensor3,self.sensor4).verticalBoxWidget()
        
        self.dataTemp = widgetGenerator(self.displayTemperatureText,"white").displayWidget(f"{self.temperature}")
        self.dataHum = widgetGenerator(self.displayHumidityText,"white").displayWidget(f"{self.humidity}")
        
        self.sensores = QWidget()
        self.sensores.layout = QHBoxLayout()
        self.sensores.setLayout(self.sensores.layout) 
        self.sensores.layout.addWidget(self.sensor1)
        self.sensores.layout.addWidget(self.sensor2)
        self.sensores.layout.addWidget(self.sensor3)
        self.sensores.layout.addWidget(self.sensor4)
        self.sensores.layout.setAlignment(Qt.AlignCenter)
        self.sensores.setStyleSheet("border:0px solid black;")
        
        self.dataState = QWidget()
        self.dataState.layout = QHBoxLayout()
        self.dataState.setLayout(self.dataState.layout) 
        self.dataState.layout.addWidget(self.driverStatus)
        self.dataState.layout.addWidget(self.tempStatus)
        self.dataState.layout.addWidget(self.elvaStatus)
        self.dataState.layout.setAlignment(Qt.AlignCenter)
        self.dataState.setStyleSheet("border:0px solid black;")
        
        hbox = QHBoxLayout(self)
        
        topTop = QFrame(self)
        topTop.setFrameShape(QFrame.StyledPanel)
        
        topleft = self.dataState

        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)

        bottom = self.sensores

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(topTop)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        
        mainLayout.addWidget(self.dataState, 0,0)
        mainLayout.addWidget(self.sensores,1,0)
        #mainLayout.addWidget(self.elvaStatus,2,0) 
        
        #mainLayout.addWidget(self.elvaStatus, 0,1)
        #mainLayout.addWidget(self.sensor2, 1,1)
        
        #mainLayout.addWidget(self.packSensor1, 0,2)
        #mainLayout.addWidget(self.sensor2, 1,2)
        
        #mainLayout.addWidget(self.packSensor2, 0,3)
        #mainLayout.addWidget(self.sensor4, 1,3)
        
        #mainLayout.addWidget(self.dataTemp, 2,1)
        #mainLayout.addWidget(self.dataHum,2,2)
        
               
        
        self.setWindowTitle('Signal and slot')
        self.setLayout(hbox)
        
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
