import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("texteditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #PlainTextEdit과 관련된 버튼에 기능 연결
        self.btn_printPlainTextEdit.clicked.connect(self.printPlainTextEdit)
        self.btn_clearPlainTextEdit.clicked.connect(self.clearPlainTextEdit)

        #PlainTextEdit에 기능 연결
        self.plaintextedit_Test.textChanged.connect(self.showPlainTextEdit)

    #PlainTextEdit과 관련된 함수
    def printPlainTextEdit(self) :
        print(self.plaintextedit_Test.toPlainText())

    def clearPlainTextEdit(self) :
        self.plaintextedit_Test.clear()

    def showPlainTextEdit(self) :
        self.textBrowser.setText(self.plaintextedit_Test.toPlainText())


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 