import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("dateTimeEditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #프로그램이 실행되면 DateTimeEdit의 값이 현재 날짜/시간으로 설정되게 하기
        self.currentDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit_Test.setDateTime(self.currentDateTime)

        #버튼들에 기능 할당
        self.btn_displayDateTime.clicked.connect(self.displayDateTime)
        self.btn_enterDateTime.clicked.connect(self.enterDateTimeFunc)
        self.btn_enterDate.clicked.connect(self.enterDateFunc)
        self.btn_enterTime.clicked.connect(self.enterTimeFunc)
        self.btn_changeFormat.clicked.connect(self.changeDisplayFormat)
        self.btn_showRange.clicked.connect(self.showRangeFunc)
        self.btn_editMaximum.clicked.connect(self.extendMaximum)
        self.btn_editMinimum.clicked.connect(self.extendMinimum)

    def displayDateTime(self) :
        #DateTimeEdit의 값을 사용할 때는 아래와 같이 객체를 만들고, 그 객체에 값을 저장한 후 사용해야 합니다.
        self.displayDateTimeVar = self.dateTimeEdit_Test.dateTime()
        self.displayDateVar = self.dateTimeEdit_Test.date()
        self.displayTimeVar = self.dateTimeEdit_Test.time()

        #QDateTime, QDate, QTime 객체들의 값을 Label에 표시합니다.
        #toString 함수는 02.12QDateTimeEdit의 하위페이지에 있는 QDateTime, QDate, QTime 함수를 참고하시기 바랍니다.
        self.lbl_displayDateTime.setText(self.displayDateTimeVar.toString("yyyy-MM-dd AP hh:mm:ss"))
        self.lbl_displayDate.setText(self.displayDateVar.toString("yyyy-MM-dd"))
        self.lbl_displayTime.setText(self.displayTimeVar.toString("AP hh:mm:ss"))

    def enterDateTimeFunc(self) :
        #LineEdit에서 글자를 가져온 후, fromString 함수를 이용해서 QDateTime객체를 만듭니다.
        #그 후, setDateTime 함수를 이용해 DateTimeEdit에 적용합니다.
        self.enterDateTimeText = self.line_dateTime.text()
        self.enterDateTimeVar = QDateTime.fromString(self.enterDateTimeText, "yyyy-MM-dd AP hh:mm:ss")
        self.dateTimeEdit_Test.setDateTime(self.enterDateTimeVar)

    def enterDateFunc(self) :
        #LineEdit에서 글자를 가져온 후, fromString 함수를 이용해서 QDate객체를 만듭니다.
        #그 후, setDate 함수를 이용해 DateTimeEdit에 적용합니다.
        self.enterDateText = self.line_date.text()
        self.enterDateVar = QDate.fromString(self.enterDateText, "yyyy-MM-dd")
        self.dateTimeEdit_Test.setDate(self.enterDateVar)

    def enterTimeFunc(self) :
        #LineEdit에서 글자를 가져온 후, fromString 함수를 이용해서 QTime객체를 만듭니다.
        #그 후, setTime 함수를 이용해 DateTimeEdit에 적용합니다.
        self.enterTimeText = self.line_time.text()
        self.enterTimeVar = QTime.fromString(self.enterTimeText, "AP hh:mm:ss")
        self.dateTimeEdit_Test.setTime(self.enterTimeVar)
    
    def changeDisplayFormat(self) :
        #LineEdit에서 글자를 가져온 후, 그 글자를 DateTimeEdit의 형식문자로 지정합니다.
        self.displayFormatText = self.line_displayFormat.text()
        self.dateTimeEdit_Test.setDisplayFormat(self.displayFormatText)

    def showRangeFunc(self) :
        print(self.dateTimeEdit_Test.minimumDateTime())
        print(self.dateTimeEdit_Test.maximumDateTime())

    def extendMaximum(self) :
        #DateTimeEdit의 현재 maximumDateTime을 가져옵니다.
        #그 후 addDays 함수를 이용하여 최댓값을 10일 연장시킨 후, setMaximumDateTime을 이용하여 DateTimeEdit에 적용시킵니다.
        self.currentMaximumDateTime = self.dateTimeEdit_Test.maximumDateTime()
        self.currentMaximumDateTime = self.currentMaximumDateTime.addDays(10)
        self.dateTimeEdit_Test.setMaximumDateTime(self.currentMaximumDateTime)

    def extendMinimum(self) :
        #DateTimeEdit의 현재 minimumDateTime을 가져옵니다.
        #그 후 addDays 함수를 이용하여 최솟값을 10일 뒤로 미룬 후, setMinimumDateTime을 이용하여 DateTimeEdit에 적용시킵니다.
        self.currentMinimumDateTime = self.dateTimeEdit_Test.minimumDateTime()
        self.currentMinimumDateTime = self.currentMinimumDateTime.addDays(-10)
        self.dateTimeEdit_Test.setMinimumDateTime(self.currentMinimumDateTime)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 