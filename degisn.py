# -*- coding: utf-8 -*-                           

# Form implementation generated from reading ui file 'c:\Users\Yahia Shamaa\Documents\PyQt\tictsctoe.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(0, 60, 121, 121))
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(120, 60, 121, 121))
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(240, 60, 121, 121))
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(240, 180, 121, 121))
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(0, 180, 121, 121))
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(120, 180, 121, 121))
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.b10 = QtWidgets.QPushButton(self.centralwidget)
        self.b10.setGeometry(QtCore.QRect(240, 300, 121, 121))
        self.b10.setText("")
        self.b10.setObjectName("b10")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(0, 300, 121, 121))
        self.b8.setText("")
        self.b8.setObjectName("b8")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(120, 300, 121, 121))
        self.b9.setText("")
        self.b9.setObjectName("b9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "O\'s Turn"))