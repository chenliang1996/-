# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\中期项目\helloworld\untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_xinchuang import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 300)
        MainWindow.setMinimumSize(QtCore.QSize(500, 300))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(50, 80, 201, 71))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 190, 75, 23))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setAutoDefault(True)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 80, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(300, 170, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_3.clicked.connect(self.lineEdit.show)
        self.pushButton_4.clicked.connect(self.online)   # connect绑定的事件
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "点击次数加一"))
        self.pushButton_2.setText(_translate("MainWindow", "清除"))
        self.pushButton_3.setText(_translate("MainWindow", "打印"))
        self.pushButton_4.setText(_translate("MainWindow", "打开新的窗口"))

    def online(self):
        formObj=QtWidgets.QDialog()#注意，这里和我们一开始创建窗体时使用的界面类型相同
        ip=Ui_Form()
        ip.setupUi(formObj)
        formObj.show()
        formObj.exec_()

if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)
    formObj=QtWidgets.QMainWindow()  #注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui=Ui_MainWindow()  
    ui.setupUi(formObj)  
    formObj.show()  
    sys.exit(app.exec_())

