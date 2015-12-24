# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test3.ui'
#
# Created: Fri Apr 10 21:34:29 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.pushButton1 = QtGui.QPushButton(Dialog)
        self.pushButton1.setGeometry(QtCore.QRect(280, 30, 75, 23))
        self.pushButton1.setObjectName(_fromUtf8("pushButton1"))
        self.pushButton2 = QtGui.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(280, 140, 75, 23))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButtonup = QtGui.QPushButton(Dialog)
        self.pushButtonup.setGeometry(QtCore.QRect(280, 60, 75, 23))
        self.pushButtonup.setObjectName(_fromUtf8("pushButtonup"))
        self.pushButtondown = QtGui.QPushButton(Dialog)
        self.pushButtondown.setGeometry(QtCore.QRect(280, 100, 75, 23))
        self.pushButtondown.setObjectName(_fromUtf8("pushButtondown"))
        self.listWidget = QtGui.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 256, 231))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "工具", None))
        self.pushButton1.setText(_translate("Dialog", "打开", None))
        self.pushButton2.setText(_translate("Dialog", "保存", None))
        self.pushButtonup.setText(_translate("Dialog", "上", None))
        self.pushButtondown.setText(_translate("Dialog", "下", None))

