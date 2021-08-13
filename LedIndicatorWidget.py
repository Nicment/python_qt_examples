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
        
        
        #self.colorOperator = QColor(60,30,60)

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