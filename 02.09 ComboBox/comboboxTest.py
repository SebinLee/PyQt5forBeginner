import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("comboboxTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.syncComboBox()

        self.cmb_Test.currentIndexChanged.connect(self.comboBoxFunction)
        self.btn_addItem.clicked.connect(self.addComboBoxItem)
        self.btn_deleteItem.clicked.connect(self.deleteComboBoxItem)
        self.btn_clearItem.clicked.connect(self.clearComboBoxItem)

    def syncComboBox(self) :
        for i in range(0,self.cmb_Test.count()) :
            self.cmb_deleteItem.addItem(self.cmb_Test.itemText(i))

    def comboBoxFunction(self) :
        self.lbl_display.setText(self.cmb_Test.currentText())

    def addComboBoxItem(self) :
        self.cmb_Test.addItem(self.lineedit_addItem.text())
        self.cmb_deleteItem.addItem(self.lineedit_addItem.text())
        print("Item Added")

    def deleteComboBoxItem(self) :
        self.delidx = self.cmb_deleteItem.currentIndex()
        self.cmb_Test.removeItem(self.delidx)
        self.cmb_deleteItem.removeItem(self.delidx)
        print("Item Deleted")

    def clearComboBoxItem(self) :
        self.cmb_Test.clear()
        self.cmb_deleteItem.clear()
    

    


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 
