import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("sliderDialTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        """
        QAbstractSlider Singal
        - sliderMoved()
        - valueChanged()
        - rangeChanged()

        QAbstractSlider Description
        - Value : The bounded interger that QAbstractSlider maintains.
        - minumum : The lowest possible value
        - maximum : THe highest possible value.
        - singleStep : The smaller of two natural steps that typically corresponds to the user pressing an arrow key
        - pageStep : The larger of two natural steps thah typically coreesponds to the user pressing PageUp/Down and MousePress

        QAbstractSlider Function & Slot
        - maximum()
        - minimum()
        - pageStep()
        - singleStep()

        - setMaximum()
        - setMinimum()
        - setPageStep()
        - setSingleStep()

        - setRange(min,max)
        - setValue()
        """

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 