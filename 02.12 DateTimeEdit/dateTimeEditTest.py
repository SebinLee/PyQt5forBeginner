import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("dateTimeEditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.currentDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit_Test.setDateTime(self.currentDateTime)


        self.btn_displayDateTime.clicked.connect(self.displayDateTime)
        self.btn_enterDateTime.clicked.connect(self.enterDateTimeFunc)
        self.btn_enterDate.clicked.connect(self.enterDateFunc)
        self.btn_enterTime.clicked.connect(self.enterTimeFunc)

        self.btn_changeFormat.clicked.connect(self.changeDisplayFormat)

        self.btn_showRange.clicked.connect(self.showRangeFunc)

        """
        self.btn_editMaximum.clicked.connect(self.extendMaximum)
        self.btn_editMinimum.clicked.connect(self.extendMinimum)
        """


    def displayDateTime(self) :
        self.displayDateTimeVar = self.dateTimeEdit_Test.dateTime()
        self.displayDateVar = self.dateTimeEdit_Test.date()
        self.displayTimeVar = self.dateTimeEdit_Test.time()

        self.lbl_displayDateTime.setText(self.displayDateTimeVar.toString("yyyy-MM-dd AP hh:mm:ss"))
        self.lbl_displayDate.setText(self.displayDateVar.toString("yyyy-MM-dd"))
        self.lbl_displayTime.setText(self.displayTimeVar.toString("AP hh:mm:ss"))

    def enterDateTimeFunc(self) :
        self.enterDateTimeText = self.line_dateTime.text()
        self.enterDateTimeVar = QDateTime.fromString(self.enterDateTimeText, "yyyy-MM-dd AP hh:mm:ss")
        self.dateTimeEdit_Test.setDateTime(self.enterDateTimeVar)

    def enterDateFunc(self) :
        self.enterDateText = self.line_date.text()
        self.enterDateVar = QDate.fromString(self.enterDateText, "yyyy-MM-dd")
        self.dateTimeEdit_Test.setDate(self.enterDateVar)

    def enterTimeFunc(self) :
        self.enterTimeText = self.line_time.text()
        self.enterTimeVar = QTime.fromString(self.enterTimeText, "AP hh:mm:ss")
        self.dateTimeEdit_Test.setTime(self.enterTimeVar)
    
    def changeDisplayFormat(self) :
        self.displayFormatText = self.line_displayFormat.text()
        self.dateTimeEdit_Test.setDisplayFormat(self.displayFormatText)

    def showRangeFunc(self) :
        print(self.dateTimeEdit_Test.minimumDateTime())
        print(self.dateTimeEdit_Test.maximumDateTime())

    """
    def extendMaximum(self) :
        self.currentMaximumDateTime = self.dateTimeEdit_Test.maximumDateTime()
        self.currentMaximumDateTime = self.currentMaximumDateTime.addDays(10)
        self.dateTimeEdit_Test.setMinimumDateTime(self.currentMaximumDateTime)

    def extendMinimum(self) :
        self.currentMinimumDateTime = self.dateTimeEdit_Test.minimumDateTime()
        self.currentMinimumDateTime = self.currentMinimumDateTime.addDays(-10)
        self.dateTimeEdit_Test.setMinimumDateTime(self.currentMinimumDateTime)
    """

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 