# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\中期项目\helloworld\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow1(object):

    def setupUi1(self, MainWindow):
        MainWindow.setObjectName("陈亮")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushButton.setObjectName("点击次数加一")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi1(MainWindow)
        #self.pushButton.clicked.connect(MainWindow.close)#将BtnClose的clicked信号和MainWindow的close槽连接
        self.pushButton.clicked.connect(self.clickTime1)#换成绑定自己编写的函数   <-----------
        self.clickCnt = 0#记录点击次数                                         <-----------
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi1(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "陈亮"))
        self.pushButton.setText(_translate("MainWindow", "点击次数加一"))
        
    def clickTime1(self):
        self.clickCnt+=1#点击次数递增
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("MainWindow", "点击次数 %d"%self.clickCnt))

    # @classmethod
    # def kaishi(self):
    #     import sys
    #     app=QtWidgets.QApplication(sys.argv)
    #     formObj=QtWidgets.QMainWindow()  #注意，这里和我们一开始创建窗体时使用的界面类型相同
    #     ui=Ui_MainWindow1()
    #     ui.setupUi1(formObj)
    #     formObj.show()
    #     app.exec_()

if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)
    formObj=QtWidgets.QMainWindow()  #注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui=Ui_MainWindow1()
    ui.setupUi1(formObj)
    formObj.show()
    sys.exit(app.exec_())

# import sys  
# app=QtWidgets.QApplication(sys.argv)  
# formObj=QtWidgets.QMainWindow()  #注意，这里和我们一开始创建窗体时使用的界面类型相同
# ui=Ui_MainWindow1()  
# ui.setupUi1(formObj)  
# formObj.show()  
# sys.exit(app.exec_())