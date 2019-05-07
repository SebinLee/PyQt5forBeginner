import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("spinboxTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.spinbox_Test.valueChanged.connect(self.printValue)
        self.btn_showInfo.clicked.connect(self.printInfo)
        self.btn_changeRangeStep.clicked.connect(self.changeRangeStep)

        self.doublespinbox_Test.valueChanged.connect(self.printDoubleValue)
        self.btn_doubleShowInfo.clicked.connect(self.printDoubleInfo)
        self.btn_doubleChangeRangeStep.clicked.connect(self.doubleChangeRangeStep)


    def printValue(self) :
        print(self.spinbox_Test.value())
    
    def printInfo(self) :
        print("Maximum value is",self.spinbox_Test.maximum())
        print("Minimum value is",self.spinbox_Test.minimum())
        print("Step Size is",self.spinbox_Test.singleStep())

    def changeRangeStep(self) :
        self.spinbox_Test.setRange(0,1000)
        self.spinbox_Test.setStep(10)

    def printDoubleValue(self) :
        print(self.doublespinbox_Test.value())

    def printDoubleInfo(self) :
        print("Maximum value is",self.doublespinbox_Test.maximum())
        print("Minimum value is",self.doublespinbox_Test.minimum())
        print("Step Size is",self.doublespinbox_Test.singleStep())
    
    def doubleChangeRangeStep(self) :
        self.doublespinbox_Test.setRange(0,1000)
        self.doublespinbox_Test.setStep(1.5)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 