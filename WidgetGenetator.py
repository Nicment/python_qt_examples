import sys
from LedIndicatorWidget import *
from PyQt5 import QtGui
from PyQt5.QtCore import (QSize, pyqtSlot, QPoint, Qt)
#from PyQt5.QtGui import (QPictureIO, QPixmap, QPicture, QPainter)
from PyQt5.QtWidgets import (QHBoxLayout, QFrame, QSplitter, QPushButton, QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication, QGridLayout, QLabel, QSizePolicy,
                             )

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