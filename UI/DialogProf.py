# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogProf.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogProf(object):
    def setupUi(self, DialogProf):
        DialogProf.setObjectName("DialogProf")
        DialogProf.resize(400, 300)
        self.label = QtWidgets.QLabel(DialogProf)
        self.label.setGeometry(QtCore.QRect(20, 30, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DialogProf)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(DialogProf)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lineEditProfNome = QtWidgets.QLineEdit(DialogProf)
        self.lineEditProfNome.setGeometry(QtCore.QRect(70, 30, 201, 21))
        self.lineEditProfNome.setObjectName("lineEditProfNome")
        self.lineEditProfTelefone = QtWidgets.QLineEdit(DialogProf)
        self.lineEditProfTelefone.setGeometry(QtCore.QRect(80, 80, 131, 21))
        self.lineEditProfTelefone.setObjectName("lineEditProfTelefone")
        self.lineEditProfEmail = QtWidgets.QLineEdit(DialogProf)
        self.lineEditProfEmail.setGeometry(QtCore.QRect(80, 130, 181, 21))
        self.lineEditProfEmail.setObjectName("lineEditProfEmail")
        self.pushButtonOK = QtWidgets.QPushButton(DialogProf)
        self.pushButtonOK.setGeometry(QtCore.QRect(40, 220, 113, 32))
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.pushButtonCancel = QtWidgets.QPushButton(DialogProf)
        self.pushButtonCancel.setGeometry(QtCore.QRect(200, 220, 113, 32))
        self.pushButtonCancel.setObjectName("pushButtonCancel")

        self.retranslateUi(DialogProf)
        QtCore.QMetaObject.connectSlotsByName(DialogProf)

    def retranslateUi(self, DialogProf):
        _translate = QtCore.QCoreApplication.translate
        DialogProf.setWindowTitle(_translate("DialogProf", "Dialog"))
        self.label.setText(_translate("DialogProf", "Nome:"))
        self.label_2.setText(_translate("DialogProf", "Telefone:"))
        self.label_3.setText(_translate("DialogProf", "Email:"))
        self.pushButtonOK.setText(_translate("DialogProf", "OK"))
        self.pushButtonCancel.setText(_translate("DialogProf", "Cancel"))

