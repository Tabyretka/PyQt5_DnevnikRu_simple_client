# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\archive\ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 11, 421, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.homeworkBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.homeworkBrowser.setObjectName("homeworkBrowser")
        self.verticalLayout.addWidget(self.homeworkBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menuBar.setObjectName("menuBar")
        self.menumenu = QtWidgets.QMenu(self.menuBar)
        self.menumenu.setObjectName("menumenu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionChange_date = QtWidgets.QAction(MainWindow)
        self.actionChange_date.setObjectName("actionChange_date")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        self.actionLogin.setObjectName("actionLogin")
        self.actionChangeDate = QtWidgets.QAction(MainWindow)
        self.actionChangeDate.setObjectName("actionChangeDate")
        self.actionLogin_2 = QtWidgets.QAction(MainWindow)
        self.actionLogin_2.setObjectName("actionLogin_2")
        self.actionMarks = QtWidgets.QAction(MainWindow)
        self.actionMarks.setObjectName("actionMarks")
        self.menumenu.addAction(self.actionChangeDate)
        self.menumenu.addAction(self.actionLogin_2)
        self.menumenu.addAction(self.actionMarks)
        self.menuBar.addAction(self.menumenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HOMEWORK"))
        self.menumenu.setTitle(_translate("MainWindow", "menu"))
        self.actionChange_date.setText(_translate("MainWindow", "Change date"))
        self.actionLogin.setText(_translate("MainWindow", "Login"))
        self.actionChangeDate.setText(_translate("MainWindow", "Change date"))
        self.actionLogin_2.setText(_translate("MainWindow", "Login"))
        self.actionMarks.setText(_translate("MainWindow", "Marks"))
