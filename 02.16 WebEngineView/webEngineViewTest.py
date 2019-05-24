import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("webEngineViewTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #WebEngineView의 시그널
        self.webEngineView_Test.loadStarted.connect(self.printLoadStart)
        self.webEngineView_Test.loadProgress.connect(self.printLoading)
        self.webEngineView_Test.loadFinished.connect(self.printLoadFinished)
        self.webEngineView_Test.urlChanged.connect(self.urlChangedFunction)

        #버튼들에 기능을 연결
        self.btn_setUrl.clicked.connect(self.urlGo)
        self.btn_back.clicked.connect(self.btnBackFunc)
        self.btn_forward.clicked.connect(self.btnForwardFunc)
        self.btn_reload.clicked.connect(self.btnRelaodFunc)
        self.btn_stop.clicked.connect(self.btnStopFunc)

    #WebEngineView의 시그널에 연결된 함수들
    def printLoadStart(self) : print("Start Loading")
    def printLoading(self) : print("Loading")
    def printLoadFinished(self) : print("Load Finished")

    def urlChangedFunction(self) :
        self.line_url.setText(self.webEngineView_Test.url().toString())
        print("Url Changed")

    #버튼을 눌렀을 때 실행될 함수들
    def urlGo(self) :
        self.webEngineView_Test.load(QUrl(self.line_url.text()))

    def btnBackFunc(self) :
        self.webEngineView_Test.back()

    def btnForwardFunc(self) :
        self.webEngineView_Test.forward()

    def btnRelaodFunc(self) :
        self.webEngineView_Test.reload()

    def btnStopFunc(self) :
        self.webEngineView_Test.stop()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()