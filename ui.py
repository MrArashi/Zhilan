# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\python\gui\test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(477, 228)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 461, 141))
        self.label.setStyleSheet("font: 20pt \"Times New Roman\";\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 170, 471, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"font: 14pt \"Times New Roman\";\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align:center;\n"
"background-color:white;\n"
"}\n"
"QPushButton:hover {\n"
"font: 14pt \"Times New Roman\";\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align:center;\n"
"background-color:gray;\n"
"}\n"
"QPushButton:pressed {\n"
"font: 14pt \"Times New Roman\";\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align:center;\n"
"background-color:silver;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("QPushButton{\n"
"font: 14pt \"Times New Roman\";\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align:center;\n"
"background-color:white;\n"
"}\n"
"QPushButton:hover {\n"
"font: 14pt \"Times New Roman\";\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align:center;\n"
"background-color:gray;\n"
"}\n"
"QPushButton:pressed {\n"
"font: 14pt \"Times New Roman\";\n"
"border:none;\n"
"font-weight:bold;\n"
"text-align:center;\n"
"background-color:silver;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Hello, Python in interface? lol", "Hello, Python in interface? lol"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Hello, User!</span></p><p align=\"center\"><span style=\" font-size:22pt;\">Я наконец то починил этого червя</span></p><p align=\"center\"><span style=\" font-size:22pt;\">И да GO LOL ZOEBAL</span></p><p><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Да го "))
        self.pushButton.setText(_translate("Dialog", "Да заебал я, го"))



