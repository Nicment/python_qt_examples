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
from WidgetGenetator import*
from PyQt5.QtCore import (pyqtSlot, Qt)
#from PyQt5.QtGui import (QPictureIO, QPixmap, QPicture, QPainter)
from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QSplitter, QWidget, QLCDNumber,
                             QVBoxLayout, QApplication, QGridLayout, QLabel)

 
class signalsStateWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.changeFactor = 100
        self.initUI()
        
    def initUI(self):
        self.resize(1000, 500)
        
        self.change = 1
        self.temperature = 20
        self.humidity = 80
        
        """-------------- Definicion de los Textos  ----------------------"""  
                
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
        
        self.checkSensorText = textWidget("Check")
        
        """-------------- Definicion de los Leds  ----------------------"""  
              
        self.driverLed = LedIndicator("red")
        self.tempLed = LedIndicator("red")
        self.electroValLed = LedIndicator("green")
        
        self.sensor1Led = LedIndicator("green")
        self.sensor2Led = LedIndicator("red")
        self.sensor3Led = LedIndicator("green")
        self.sensor4Led = LedIndicator("red")
        
        self.checkSensorLed = LedIndicator("green")
        
        self.displayTemperature = displayWidget(self.temperature).generate()
        self.displayHumidity = displayWidget(self.humidity).generate()
        
        self.driverStatus = widgetGenerator(self.driverText.createText(), self.driverLed).verticalBoxWidget()
        self.tempStatus = widgetGenerator(self.tempText.createText(), self.tempLed).verticalBoxWidget()
        self.elvaStatus = widgetGenerator(self.electroValText.createText(), self.electroValLed).verticalBoxWidget()
        
        self.sensor1= widgetGenerator(self.sensor1Text.createText(), self.sensor1Led).verticalBoxWidget()
        self.sensor2= widgetGenerator(self.sensor2Text.createText(), self.sensor2Led).verticalBoxWidget()
        
        self.sensor3= widgetGenerator(self.sensor3Text.createText(), self.sensor3Led).verticalBoxWidget()
        self.sensor4= widgetGenerator(self.sensor4Text.createText(), self.sensor4Led).verticalBoxWidget()
        
        self.dataTemp = widgetGenerator(self.displayTemperatureText,"white").displayWidget(f"{self.temperature}")
        self.dataHum = widgetGenerator(self.displayHumidityText,"white").displayWidget(f"{self.humidity}")
        
        
        #self.checkSensor = widgetGenerator(self.checkSensorText,self.checkSensorLed).verticalBoxWidget()
        
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
        
        self.checkSensorState = QWidget()
        self.checkSensorState.layout = QVBoxLayout()
        self.checkSensorState.setLayout(self.checkSensorState.layout) 
        self.checkSensorState.layout.addWidget(self.checkSensorLed)
        self.checkSensorState.layout.addWidget(self.checkSensorText.createText())
        self.checkSensorState.layout.setAlignment(Qt.AlignCenter)
        self.checkSensorState.setStyleSheet("border:0px solid black;")
        
        hbox = QHBoxLayout(self)
        
        topTop = QFrame(self)
        topTop.setFrameShape(QFrame.StyledPanel)
        
        topleft = self.dataState

        topright = self.checkSensorState

        bottom = self.sensores

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(topTop)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        
        self.setWindowTitle('Status Sensors')
        self.setLayout(hbox)
        
        self.show()
            
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
        self.checkSensorLed.setFactorResize(self.changeFactor*2)
        
        self.driverText.changeStateText(self.changeFactor)
        self.tempText.changeStateText(self.changeFactor)
        self.sensor1Text.changeStateText(self.changeFactor)
        self.sensor2Text.changeStateText(self.changeFactor)
        self.sensor3Text.changeStateText(self.changeFactor)
        self.sensor4Text.changeStateText(self.changeFactor)
        self.electroValText.changeStateText(self.changeFactor)
        self.checkSensorText.changeStateText(self.changeFactor)
                
