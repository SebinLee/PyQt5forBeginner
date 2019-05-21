import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("dateEditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #프로그램이 실행되면 DateEdit의 값이 현재 날짜/시간으로 설정되게 하기
        self.currentDate = QDate.currentDate()
        self.dateEdit_Test.setDate(self.currentDate)

        #버튼들에 기능 할당
        self.btn_displayDate.clicked.connect(self.displayDate)
        self.btn_enterDate.clicked.connect(self.enterDateFunc)
        self.btn_changeFormat.clicked.connect(self.changeDisplayFormat)
        self.btn_showRange.clicked.connect(self.showRangeFunc)
        self.btn_editMaximum.clicked.connect(self.extendMaximum)
        self.btn_editMinimum.clicked.connect(self.extendMinimum)

    def displayDate(self) :
        self.displayDateVar = self.dateEdit_Test.date()
        self.lbl_displayDate.setText(self.displayDateVar.toString("yyyy-MM-dd"))

    def enterDateFunc(self) :
        #LineEdit에서 글자를 가져온 후, fromString 함수를 이용해서 QDate객체를 만듭니다.
        #그 후, setDate 함수를 이용해 DateEdit에 적용합니다.
        self.enterDateText = self.line_date.text()
        self.enterDateVar = QDate.fromString(self.enterDateText, "yyyy-MM-dd")
        self.dateEdit_Test.setDate(self.enterDateVar)
    
    def changeDisplayFormat(self) :
        #LineEdit에서 글자를 가져온 후, 그 글자를 DateEdit의 형식문자로 지정합니다.
        self.displayFormatText = self.line_displayFormat.text()
        self.dateEdit_Test.setDisplayFormat(self.displayFormatText)

    def showRangeFunc(self) :
        print(self.dateEdit_Test.minimumDate())
        print(self.dateEdit_Test.maximumDate())

    def extendMaximum(self) :
        #DateEdit의 현재 maximumDate을 가져옵니다.
        #그 후 addDays 함수를 이용하여 최댓값을 10일 연장시킨 후, setMaximumDate을 이용하여 DateEdit에 적용시킵니다.
        self.currentMaximumDate = self.dateEdit_Test.maximumDate()
        self.currentMaximumDate = self.currentMaximumDate.addDays(10)
        self.dateEdit_Test.setMaximumDate(self.currentMaximumDate)

    def extendMinimum(self) :
        #DateEdit의 현재 minimumDate을 가져옵니다.
        #그 후 addDays 함수를 이용하여 최솟값을 10일 뒤로 미룬 후, setMinimumDate을 이용하여 DateEdit에 적용시킵니다.
        self.currentMinimumDate = self.dateEdit_Test.minimumDate()
        self.currentMinimumDate = self.currentMinimumDate.addDays(-10)
        self.dateEdit_Test.setMinimumDate(self.currentMinimumDate)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 