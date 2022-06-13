import json
import sys
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from Dnevnik import DnevnikRu

from ui.MainUi import Ui_MainWindow
from ui.DateUi import Ui_Dialog
from ui.LoginUi import Ui_Dialog2
from ui.MarksUi import Ui_Dialog3

dnevnik = DnevnikRu()


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.FirstStartFlag = True
        self.login = ""
        self.password = ""
        self.date = QtCore.QDate.currentDate().toPyDate()
        self.homeworkBrowser.setStyleSheet('color: blue')
        self.homeworkBrowser.setFont(QtGui.QFont("Monospace"))

        if not os.path.exists("settings.json"):
            self.homeworkBrowser.setText("Please LogIn")
        else:
            with open("settings.json", "r") as f:
                settings = json.load(f)
                self.password = settings["password"]
                self.login = settings["login"]
                dnevnik.login(login=self.login, password=self.password)
                self.change_browser_content()

        self.actionChangeDate.triggered.connect(self.changedate)
        self.actionLogin_2.triggered.connect(self.loginfunc)
        self.actionMarks.triggered.connect(self.marks)

    def change_browser_content(self):
        date = f"{self.date.day + 1}.{self.date.month}.{self.date.year}"
        res = f'{date}\n'

        homework = dnevnik.homework({self.date.year}, f"{date}", f"{date}")
        if homework is not None:
            for i in homework:
                res += f"{i[0]}: {i[1]}\n\n"
        else:
            res += "НЕТ ДОМАШНЕГО ЗАДАНИЯ"
        self.homeworkBrowser.setText(str(res))

    def changedate(self):
        dialog = ChangeDateDialog(self)
        dialog.exec()
        self.date = dialog.ui.get_date().toPyDate()
        self.change_browser_content()

    def loginfunc(self):
        dialog = LoginDialog(self)
        dialog.exec()
        self.login = dialog.ui.lineEdit.text()
        self.password = dialog.ui.lineEdit_2.text()
        if dnevnik.login(login=self.login.strip(), password=self.password.strip()) is not None:
            settings = {"password": self.password, "login": self.login}
            with open("settings.json", "w") as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)
            self.change_browser_content()

    def marks(self):
        dialog = MarksDialog(self)
        dialog.exec()


class ChangeDateDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self)


class MarksDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self)
        self.mk1 = dnevnik.marks(period="0")
        self.mk2 = dnevnik.marks(period="1")
        self.changeTable()
        self.ui.comboBox.activated[str].connect(self.changeTable)

    def changeTable(self, text="1 семестр"):
        if text == "1 семестр":
            mk = self.mk1
        else:
            mk = self.mk2
        self.ui.tableWidget.setRowCount(len(mk))
        self.ui.tableWidget.setColumnCount(len(mk[0]))
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['№', 'Предметы', 'Оценки', 'Опоздания', 'Пропуски всего/', '/по болезни', 'Средний балл',
             'Итог'])
        # self.ui.tableWidget.setHorizontHeaderLabels()
        for row in mk:
            for col in enumerate(row):
                item = QTableWidgetItem(col[1])
                self.ui.tableWidget.setItem(int(row[0]) - 1, col[0], item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
