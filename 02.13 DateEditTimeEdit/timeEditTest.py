import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("TimeEditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #프로그램이 실행되면 TimeEdit의 값이 현재 날짜/시간으로 설정되게 하기
        self.currentTime = QTime.currentTime()
        self.timeEdit_Test.setTime(self.currentTime)

        #버튼들에 기능 할당
        self.btn_displayTime.clicked.connect(self.displayTime)
        self.btn_enterTime.clicked.connect(self.enterTimeFunc)
        self.btn_changeFormat.clicked.connect(self.changeDisplayFormat)

    def displayTime(self) :
        self.displayTimeVar = self.timeEdit_Test.time()
        self.lbl_displayTime.setText(self.displayTimeVar.toString("AP hh:mm:ss"))

    def enterTimeFunc(self) :
        #LineEdit에서 글자를 가져온 후, fromString 함수를 이용해서 QTime객체를 만듭니다.
        #그 후, setTime 함수를 이용해 TimeEdit에 적용합니다.
        self.enterTimeText = self.line_time.text()
        self.enterTimeVar = QTime.fromString(self.enterTimeText, "AP hh:mm:ss")
        self.timeEdit_Test.setTime(self.enterTimeVar)
    
    def changeDisplayFormat(self) :
        #LineEdit에서 글자를 가져온 후, 그 글자를 TimeEdit의 형식문자로 지정합니다.
        self.displayFormatText = self.line_displayFormat.text()
        self.timeEdit_Test.setDisplayFormat(self.displayFormatText)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 