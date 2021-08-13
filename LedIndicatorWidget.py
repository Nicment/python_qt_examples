from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class LedIndicator(QAbstractButton):
    scaledSize = 1000.0

    def __init__(self, color: str):
        QAbstractButton.__init__(self)
        
        self.color = color
        
        self.setMinimumSize(80, 80)
        print(self.minimumSize())
        
        self.setCheckable(True)
        self.setDisabled(True)

    def resizeEvent(self, QResizeEvent):
        self.update()
        
    def setFactorResize(self, factor):
        self.factorResize = factor
        
    def setColor(self, setColorValue:str):
        self.color =  setColorValue
        
    def paintEvent(self, QPaintEvent):
        self.off_color_1 = QColor(self.color).lighter(200)
        self.off_color_2 = QColor(self.color).darker(100)
        
        realSize = min(self.width(), self.height())
        self.setMinimumSize(self.factorResize, self.factorResize)

        painter = QPainter(self)
        pen = QPen(Qt.black)
        pen.setWidth(1)

        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(realSize / self.scaledSize, realSize / self.scaledSize)

        gradient = QRadialGradient(QPointF(-500, -500), 1500, QPointF(-500, -500))
        gradient.setColorAt(0, QColor(224, 224, 224))
        gradient.setColorAt(1, QColor(28, 28, 28))
        painter.setPen(pen)
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(QPointF(0, 0), 500, 500)

        gradient = QRadialGradient(QPointF(500, 500), 1500, QPointF(500, 500))
        gradient.setColorAt(0, QColor(224, 224, 224))
        gradient.setColorAt(1, QColor(28, 28, 28))
        painter.setPen(pen)
        painter.setBrush(QBrush(gradient))
        painter.drawEllipse(QPointF(0, 0), 450, 450)

        gradient = QRadialGradient(QPointF(500, 500), 1500, QPointF(500, 500))
        gradient.setColorAt(0, self.off_color_1)
        gradient.setColorAt(1, self.off_color_2)

        painter.setBrush(gradient)
        painter.drawEllipse(QPointF(0, 0), 400, 400)
        
"""
    Codigo de la Version 1.0 funcional de una implementacion para
    de un Led para mostrar en la ventana principal

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
        
        return self.ledSensor"""