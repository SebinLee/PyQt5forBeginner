import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("pixmapTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    def loadImageFromFile(self) :
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load("testImage.jpg")
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(600)
        self.lbl_picture.setPixmap(self.qPixmapFileVar)

    def loadImageFromWeb(self) :

        #Web에서 Image 정보 로드
        urlString = "https://avatars1.githubusercontent.com/u/44885477?s=460&v=4"
        imageFromWeb = urllib.request.urlopen(urlString).read()

        #웹에서 Load한 Image를 QPixmap 객체로 만들고, Label을 이용하여 화면에 표시
        self.qPixmapWebVar = QPixmap()
        self.qPixmapWebVar.loadFromData(imageFromWeb)
        self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(600)
        self.lbl_picture.setPixmap(self.qPixmapWebVar)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 