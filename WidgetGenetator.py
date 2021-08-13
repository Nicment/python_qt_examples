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
    
    def __init__(self, topWidget, bottomWidget):
        super().__init__()    
        self.topWidget = topWidget 
        self.bottomWidget = bottomWidget
    
    def VBoxWidget(self):
            
        self.verticalBox = QWidget()
        self.verticalBox.layout = QVBoxLayout()
        self.verticalBox.setLayout(self.verticalBox.layout) 
        self.verticalBox.layout.addWidget(self.topWidget)
        self.verticalBox.layout.addWidget(self.bottomWidget)
        self.verticalBox.layout.setAlignment(Qt.AlignCenter)
        self.verticalBox.setStyleSheet("border:3px solid black;")
        
        
        return self.verticalBox
    
    def HBoxWidget(self):
            
        self.horizontalBox = QWidget()
        self.horizontalBox.layout = QHBoxLayout()
        self.horizontalBox.setLayout(self.horizontalBox.layout) 
        self.horizontalBox.layout.addWidget(self.topWidget)
        self.horizontalBox.layout.addWidget(self.bottomWidget)
        self.horizontalBox.layout.setAlignment(Qt.AlignCenter)
        self.horizontalBox.setStyleSheet("border:3px solid black;")
        
        
        return self.horizontalBox
    
    def displayWidget(self,data: str):
        
        self.data = data   
        self.lcd = QLCDNumber()
        self.lcd.display(self.data)
                 
        self.sensor_display = QWidget()
        self.sensor_display.layout = QHBoxLayout() 
        self.sensor_display.setLayout(self.sensor_display.layout) 
        self.sensor_display.layout.addWidget(self.topWidget)
        self.sensor_display.layout.addWidget(self.lcd)
        self.sensor_display.layout.setAlignment(Qt.AlignCenter)  
        
        return self.sensor_display

class displayWidget(QWidget):
    def __init__(self, data: int):
        super().__init__()    
        self.data = data 
        self.changeFactor = 200   
    def generate(self):               
        self.lcd = QLCDNumber()
        self.lcd.display(self.data)
        self.lcd.setMinimumSize(self.changeFactor,self.changeFactor/2)
        return self.lcd
    def changeSize(self, changeFactor:int):
        self.changeFactor = changeFactor*4 
        self.lcd.setMinimumSize(self.changeFactor,self.changeFactor//2)