import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel 
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Image Viewer"
        self.setWindowTitle(self.title)

        label = QLabel(self)
        pixmap = QPixmap('red.png')
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
        self.resize(pixmap.width(), pixmap.height())


app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())