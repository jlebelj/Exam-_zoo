# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(286, 315)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.l_zoo = QtWidgets.QLabel(self.centralwidget)
        self.l_zoo.setGeometry(QtCore.QRect(120, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.l_zoo.setFont(font)
        self.l_zoo.setObjectName("l_zoo")
        self.BT_poisson = QtWidgets.QPushButton(self.centralwidget)
        self.BT_poisson.setGeometry(QtCore.QRect(50, 90, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_poisson.setFont(font)
        self.BT_poisson.setObjectName("BT_poisson")
        self.BT_reptile = QtWidgets.QPushButton(self.centralwidget)
        self.BT_reptile.setGeometry(QtCore.QRect(50, 130, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_reptile.setFont(font)
        self.BT_reptile.setObjectName("BT_reptile")
        self.BT_enclos = QtWidgets.QPushButton(self.centralwidget)
        self.BT_enclos.setGeometry(QtCore.QRect(50, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_enclos.setFont(font)
        self.BT_enclos.setObjectName("BT_enclos")
        self.BT_afficher_animaux = QtWidgets.QPushButton(self.centralwidget)
        self.BT_afficher_animaux.setGeometry(QtCore.QRect(50, 170, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_afficher_animaux.setFont(font)
        self.BT_afficher_animaux.setObjectName("BT_afficher_animaux")
        self.BT_quitter_m = QtWidgets.QPushButton(self.centralwidget)
        self.BT_quitter_m.setGeometry(QtCore.QRect(50, 210, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_quitter_m.setFont(font)
        self.BT_quitter_m.setObjectName("BT_quitter_m")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 286, 26))
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
        self.l_zoo.setText(_translate("MainWindow", "Zoo"))
        self.BT_poisson.setText(_translate("MainWindow", "Poisson"))
        self.BT_reptile.setText(_translate("MainWindow", "Reptile"))
        self.BT_enclos.setText(_translate("MainWindow", "Enclos"))
        self.BT_afficher_animaux.setText(_translate("MainWindow", "Afficher animaux"))
        self.BT_quitter_m.setText(_translate("MainWindow", "Quitter"))
