import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("dateTimeEditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.btn_displayDateTime.clicked.connect(self.displayDateTime)
        self.dateTimeEdit.dateChanged.connect(self.printFunc)

    def displayDateTime(self) :

        """
        minDateTimeVar = QDateTime.currentDateTime()
        maxDateTimeVar = QDateTime.currentDateTime()
        maxDateTimeVar = maxDateTimeVar.addDays(100)

        self.dateTimeEdit.setDateTimeRange(minDateTimeVar, maxDateTimeVar)
        print(self.dateTimeEdit.minimumDate())
        print(self.dateTimeEdit.maximumDate())

        self.dateTimeEdit.clearMaximumDateTime()
        self.dateTimeEdit.clearMinimumDateTime()
        print(self.dateTimeEdit.maximumDateTime())
        print(self.dateTimeEdit.minimumDateTime())
        """

        if self.dateTimeEdit.calendarPopup() : self.dateTimeEdit.setCalendarPopup(False)
        else  : self.dateTimeEdit.setCalendarPopup(True)

    def printFunc(self) :
        print("DateChanged")
        

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 