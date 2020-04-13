# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 280, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.l_email = QtWidgets.QLabel(self.centralwidget)
        self.l_email.setGeometry(QtCore.QRect(170, 110, 67, 17))
        self.l_email.setObjectName("l_email")
        self.l_password = QtWidgets.QLabel(self.centralwidget)
        self.l_password.setGeometry(QtCore.QRect(170, 170, 67, 17))
        self.l_password.setObjectName("l_password")
        self.i_email = QtWidgets.QLineEdit(self.centralwidget)
        self.i_email.setGeometry(QtCore.QRect(290, 110, 113, 25))
        self.i_email.setObjectName("i_email")
        self.i_password = QtWidgets.QLineEdit(self.centralwidget)
        self.i_password.setGeometry(QtCore.QRect(290, 160, 113, 25))
        self.i_password.setObjectName("i_password")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera"))
        self.pushButton.setText(_translate("MainWindow", "Program"))
        self.l_email.setText(_translate("MainWindow", "Email:"))
        self.l_password.setText(_translate("MainWindow", "Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

