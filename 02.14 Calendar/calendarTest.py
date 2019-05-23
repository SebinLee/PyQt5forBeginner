import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("calendarTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #QCalendarWidget의 시그널
        self.calendarWidget_Test.clicked.connect(self.calendarClicked)
        self.calendarWidget_Test.currentPageChanged.connect(self.calendarPageChanged)
        self.calendarWidget_Test.selectionChanged.connect(self.calendarSelectionChanged)        

        #QCalendarWidget이 자동으로 오늘 날짜가 있는 달력을 보여주게 설정
        self.todayDate = QDate.currentDate()
        self.calendarWidget_Test.setCurrentPage(self.todayDate.year(), self.todayDate.month())

        #버튼에 기능 연결
        self.btn_prevMonth.clicked.connect(self.prevMonth)
        self.btn_nextMonth.clicked.connect(self.nextMonth)
        self.btn_today.clicked.connect(self.today)

    #CalendarWidget의 시그널에 연결된 함수들
    def calendarClicked(self) :
        print(self.calendarWidget_Test.selectedDate())

    def calendarPageChanged(self) :
        self.year = str(self.calendarWidget_Test.yearShown()) + "년"
        self.month = str(self.calendarWidget_Test.monthShown()) + "월"
        self.lbl_currentPage.setText(self.year + " " + self.month)

    def calendarSelectionChanged(self) :
        self.selectedDateVar = self.calendarWidget_Test.selectedDate()
        self.lbl_selectedDate.setText(self.selectedDateVar.toString())

    #버튼에 연결된 함수들
    def prevMonth(self) :
        self.calendarWidget_Test.showPreviousMonth()

    def nextMonth(self) :
        self.calendarWidget_Test.showNextMonth()

    def today(self) :
        self.calendarWidget_Test.showToday()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 