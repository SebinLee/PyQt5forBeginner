import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("dateTimeEditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    """
    QDateTimeEdit
    - date()
    - dateTime()

    - clearMaximumDate, DateTime, Time
    - clearMinumumDate, DateTime, Time

    """

    def displayDateTime(self) :
        self.datetimeedit_Test.dateTime()

        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 