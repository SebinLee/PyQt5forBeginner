import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("progressbarTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #ProgressBar의 시그널
        self.progressBar_Test.valueChanged.connect(self.printValue)

        #QTimer를 이용하여 매초마다 ProgressBar의 값이 1씩 늘어나게 설정합니다.
        #QTimer객체를 만들고, Interval을 1000으로 설정한 후, ProgrssBar의 값이 늘어나게 하는 함수를 연결하고 QTimer를 시작합니다.
        #QTimer에 대한 설명은 02.17.01 QTimer에서 보실 수 있습니다.
        self.timerVar = QTimer()
        self.timerVar.setInterval(1000)
        self.timerVar.timeout.connect(self.progressBarTimer)
        self.timerVar.start()

    def progressBarTimer(self) :
        self.time = self.progressBar_Test.value()
        self.time += 1
        self.progressBar_Test.setValue(self.time)

        #ProgressBar의 값이 progressBar의 최댓값 이상이 되면 Timer를 중단시켜 ProgressBar의 값이 더이상 증가하지 않게 합니다.
        if self.time >= self.progressBar_Test.maximum() :
            self.timerVar.stop()

    def printValue(self) :
        print(self.progressBar_Test.value())
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()