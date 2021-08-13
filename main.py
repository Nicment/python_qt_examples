import sys
import indicator_window
from LedIndicatorWidget import *
from PyQt5.QtWidgets import (QApplication)

def main():
    app = QApplication(sys.argv)
    ex  = indicator_window.signalsStateWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()