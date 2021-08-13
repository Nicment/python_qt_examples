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
        
        self.mainWindow = QGridLayout()
        self.change = 1
        self.temperature = 20
        self.humidity = 80
        self.velocity = -5500
        
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
              
        self.driverLed = LedIndicator("green")
        self.tempLed = LedIndicator("green")
        self.electroValLed = LedIndicator("green")
        
        self.sensor1Led = LedIndicator("green")
        self.sensor2Led = LedIndicator("green")
        self.sensor3Led = LedIndicator("green")
        self.sensor4Led = LedIndicator("green")
        
        self.checkSensorLed = LedIndicator("green")
        
        self.temperatureDisplay = displayWidget(self.temperature)
        self.humidityDisplay = displayWidget(self.humidity)
        self.velocityDisplay = displayWidget(self.velocity)
        
        """----Se crean todos los sensores y estados que queremos mostrar------"""
        
        self.dataTemp = widgetGenerator(self.temperatureDisplay.generate(),self.displayTemperatureText.createText()).VBoxWidget()
        self.dataHum = widgetGenerator(self.humidityDisplay.generate(),self.displayHumidityText.createText()).VBoxWidget()
        self.dataVel = widgetGenerator(self.velocityDisplay.generate(),self.displayVelocityText.createText()).VBoxWidget()
    
        self.driverStatus = widgetGenerator(self.driverLed, self.driverText.createText()).VBoxWidget()
        self.tempStatus = widgetGenerator(self.tempLed, self.tempText.createText()).VBoxWidget()
        self.elvaStatus = widgetGenerator(self.electroValLed, self.electroValText.createText(), ).VBoxWidget()
        self.checkSensor = widgetGenerator(self.checkSensorLed,self.checkSensorText.createText()).VBoxWidget()
        
        self.sensor1= widgetGenerator(self.sensor1Led , self.sensor1Text.createText()).VBoxWidget()
        self.sensor2= widgetGenerator(self.sensor2Led , self.sensor2Text.createText()).VBoxWidget()
        self.sensor3= widgetGenerator(self.sensor3Led , self.sensor3Text.createText()).VBoxWidget()
        self.sensor4= widgetGenerator(self.sensor4Led , self.sensor4Text.createText()).VBoxWidget()
        """-----------------------------------------------------------------------------------------"""
        """Se hace la organización de los Displays que mostraran la informacion de los sensores"""
        
        self.displays = QWidget()
        self.displays.layout = QHBoxLayout()
        self.displays.setLayout(self.displays.layout) 
        self.displays.layout.addWidget(self.dataTemp)
        self.displays.layout.addWidget(self.dataHum)
        self.displays.layout.addWidget(self.dataVel)
        self.displays.layout.setAlignment(Qt.AlignCenter)
        
        """-----------------------------------------------------------------------------------------"""
        
        """Se montan todos los sensores en una caja 
        horizontal para facilitar su acomodacion
        en la pestaña principal"""
        
        self.sensores = QWidget()
        self.sensores.layout = QHBoxLayout()
        self.sensores.setLayout(self.sensores.layout) 
        self.sensores.layout.addWidget(self.sensor1)
        self.sensores.layout.addWidget(self.sensor2)
        self.sensores.layout.addWidget(self.sensor3)
        self.sensores.layout.addWidget(self.sensor4)
        self.sensores.layout.setAlignment(Qt.AlignCenter)
        
        """-----------------------------------------------------------------------------------------"""
        
        """Se montan todos los estados de los sensores principales
        en una caja horizontal para facilitar su acomodacion
        en la pestaña principal"""
        
        self.dataState = QWidget()
        self.dataState.layout = QHBoxLayout()
        self.dataState.setLayout(self.dataState.layout) 
        self.dataState.layout.addWidget(self.driverStatus)
        self.dataState.layout.addWidget(self.tempStatus)
        self.dataState.layout.addWidget(self.elvaStatus)
        self.dataState.layout.setAlignment(Qt.AlignCenter)
        
        """---------------------------------------------------------------------------------------------"""
        
        """
        * Se agregan los Widgets que se quieren mostrar 
        * al mainWindow 
        """
        self.topWidget = self.displays
        self.middleWidget = widgetGenerator(self.dataState, self.checkSensor).HBoxWidget()
        self.middleWidget.setStyleSheet("border:0px solid black;")
        self.bottonWidget = self.sensores
        
        self.mainWindow.addWidget(self.topWidget, 0,0)
        self.mainWindow.addWidget(self.middleWidget, 1,0)
        self.mainWindow.addWidget(self.bottonWidget,2,0)
        
        """
        *------------------------------------------------------------
        """
        
        self.setWindowTitle('Status Sensors')
        self.setLayout(self.mainWindow)
        
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
        self.checkSensorText.changeStateText(self.changeFactor*2)
        
        self.displayTemperatureText.changeStateText(self.changeFactor)
        self.displayHumidityText.changeStateText(self.changeFactor)
        self.displayVelocityText.changeStateText(self.changeFactor)
        
        self.temperatureDisplay.changeSize(self.changeFactor)
        self.humidityDisplay.changeSize(self.changeFactor)
        self.velocityDisplay.changeSize(self.changeFactor)
        print (self.changeFactor)
                
