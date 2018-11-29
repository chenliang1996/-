# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\中期项目\helloworld\xinchuang.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")

    def retranslateUi(self, Form):
        self.pushButton.setText(_translate("MainWindow", "点击次数加一"))
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "chenliang"))

if __name__=="__main__":  
    import sys  
    app=QtWidgets.QApplication(sys.argv)
    formObj=QtWidgets.QMainWindow()  #注意，这里和我们一开始创建窗体时使用的界面类型相同
    ui=Ui_Form()
    ui.setupUi(formObj)  
    formObj.show()  
    sys.exit(app.exec_())

