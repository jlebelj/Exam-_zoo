# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_reptile.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(810, 623)
        self.l_titre_reptile = QtWidgets.QLabel(Dialog)
        self.l_titre_reptile.setGeometry(QtCore.QRect(350, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l_titre_reptile.setFont(font)
        self.l_titre_reptile.setObjectName("l_titre_reptile")
        self.l_num_r = QtWidgets.QLabel(Dialog)
        self.l_num_r.setGeometry(QtCore.QRect(10, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_num_r.setFont(font)
        self.l_num_r.setObjectName("l_num_r")
        self.line_num_r = QtWidgets.QLineEdit(Dialog)
        self.line_num_r.setGeometry(QtCore.QRect(10, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_num_r.setFont(font)
        self.line_num_r.setText("")
        self.line_num_r.setObjectName("line_num_r")
        self.line_nom_r = QtWidgets.QLineEdit(Dialog)
        self.line_nom_r.setGeometry(QtCore.QRect(10, 170, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_nom_r.setFont(font)
        self.line_nom_r.setText("")
        self.line_nom_r.setObjectName("line_nom_r")
        self.l_nom_r = QtWidgets.QLabel(Dialog)
        self.l_nom_r.setGeometry(QtCore.QRect(10, 140, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_nom_r.setFont(font)
        self.l_nom_r.setObjectName("l_nom_r")
        self.l_alimentation_r = QtWidgets.QLabel(Dialog)
        self.l_alimentation_r.setGeometry(QtCore.QRect(600, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_alimentation_r.setFont(font)
        self.l_alimentation_r.setObjectName("l_alimentation_r")
        self.CB_alimentation_r = QtWidgets.QComboBox(Dialog)
        self.CB_alimentation_r.setGeometry(QtCore.QRect(600, 50, 181, 41))
        self.CB_alimentation_r.setObjectName("CB_alimentation_r")
        self.l_type_animal_r = QtWidgets.QLabel(Dialog)
        self.l_type_animal_r.setGeometry(QtCore.QRect(600, 140, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_type_animal_r.setFont(font)
        self.l_type_animal_r.setObjectName("l_type_animal_r")
        self.CB_type_animal_r = QtWidgets.QComboBox(Dialog)
        self.CB_type_animal_r.setGeometry(QtCore.QRect(600, 170, 181, 41))
        self.CB_type_animal_r.setObjectName("CB_type_animal_r")
        self.l_enclos_r = QtWidgets.QLabel(Dialog)
        self.l_enclos_r.setGeometry(QtCore.QRect(10, 260, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_enclos_r.setFont(font)
        self.l_enclos_r.setObjectName("l_enclos_r")
        self.CB_enclos_r = QtWidgets.QComboBox(Dialog)
        self.CB_enclos_r.setGeometry(QtCore.QRect(10, 290, 181, 41))
        self.CB_enclos_r.setObjectName("CB_enclos_r")
        self.textBrowser_r = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_r.setGeometry(QtCore.QRect(10, 340, 561, 281))
        self.textBrowser_r.setObjectName("textBrowser_r")
        self.CB_venimeux_r = QtWidgets.QComboBox(Dialog)
        self.CB_venimeux_r.setGeometry(QtCore.QRect(600, 290, 181, 41))
        self.CB_venimeux_r.setObjectName("CB_venimeux_r")
        self.l_venimeux_r = QtWidgets.QLabel(Dialog)
        self.l_venimeux_r.setGeometry(QtCore.QRect(600, 260, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_venimeux_r.setFont(font)
        self.l_venimeux_r.setObjectName("l_venimeux_r")
        self.l_nb_dent_r1 = QtWidgets.QLabel(Dialog)
        self.l_nb_dent_r1.setGeometry(QtCore.QRect(290, 70, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_nb_dent_r1.setFont(font)
        self.l_nb_dent_r1.setObjectName("l_nb_dent_r1")
        self.line_nb_dent_r = QtWidgets.QLineEdit(Dialog)
        self.line_nb_dent_r.setGeometry(QtCore.QRect(310, 120, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_nb_dent_r.setFont(font)
        self.line_nb_dent_r.setText("")
        self.line_nb_dent_r.setObjectName("line_nb_dent_r")
        self.l_nb_dent_r2 = QtWidgets.QLabel(Dialog)
        self.l_nb_dent_r2.setGeometry(QtCore.QRect(310, 90, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_nb_dent_r2.setFont(font)
        self.l_nb_dent_r2.setObjectName("l_nb_dent_r2")
        self.line_temperature_r = QtWidgets.QLineEdit(Dialog)
        self.line_temperature_r.setGeometry(QtCore.QRect(310, 240, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_temperature_r.setFont(font)
        self.line_temperature_r.setText("")
        self.line_temperature_r.setObjectName("line_temperature_r")
        self.l_temperature_r1 = QtWidgets.QLabel(Dialog)
        self.l_temperature_r1.setGeometry(QtCore.QRect(290, 190, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_temperature_r1.setFont(font)
        self.l_temperature_r1.setObjectName("l_temperature_r1")
        self.l_temperature_r2 = QtWidgets.QLabel(Dialog)
        self.l_temperature_r2.setGeometry(QtCore.QRect(350, 210, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_temperature_r2.setFont(font)
        self.l_temperature_r2.setObjectName("l_temperature_r2")
        self.BT_ajouter_r = QtWidgets.QPushButton(Dialog)
        self.BT_ajouter_r.setGeometry(QtCore.QRect(620, 380, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_ajouter_r.setFont(font)
        self.BT_ajouter_r.setObjectName("BT_ajouter_r")
        self.BT_modifier_r = QtWidgets.QPushButton(Dialog)
        self.BT_modifier_r.setGeometry(QtCore.QRect(620, 420, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_modifier_r.setFont(font)
        self.BT_modifier_r.setObjectName("BT_modifier_r")
        self.BT_supprimer_r = QtWidgets.QPushButton(Dialog)
        self.BT_supprimer_r.setGeometry(QtCore.QRect(620, 460, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_supprimer_r.setFont(font)
        self.BT_supprimer_r.setObjectName("BT_supprimer_r")
        self.MS_e_num_existant_r = QtWidgets.QLabel(Dialog)
        self.MS_e_num_existant_r.setEnabled(True)
        self.MS_e_num_existant_r.setGeometry(QtCore.QRect(0, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_num_existant_r.setFont(font)
        self.MS_e_num_existant_r.setObjectName("MS_e_num_existant_r")
        self.BT_serialiser_r = QtWidgets.QPushButton(Dialog)
        self.BT_serialiser_r.setGeometry(QtCore.QRect(620, 500, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_serialiser_r.setFont(font)
        self.BT_serialiser_r.setObjectName("BT_serialiser_r")
        self.BT_deserialiser_r = QtWidgets.QPushButton(Dialog)
        self.BT_deserialiser_r.setGeometry(QtCore.QRect(620, 540, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_deserialiser_r.setFont(font)
        self.BT_deserialiser_r.setObjectName("BT_deserialiser_r")
        self.MS_e_nb_dent_r = QtWidgets.QLabel(Dialog)
        self.MS_e_nb_dent_r.setEnabled(True)
        self.MS_e_nb_dent_r.setGeometry(QtCore.QRect(240, 160, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_nb_dent_r.setFont(font)
        self.MS_e_nb_dent_r.setObjectName("MS_e_nb_dent_r")
        self.MS_e_num_format_r = QtWidgets.QLabel(Dialog)
        self.MS_e_num_format_r.setEnabled(True)
        self.MS_e_num_format_r.setGeometry(QtCore.QRect(0, 110, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_num_format_r.setFont(font)
        self.MS_e_num_format_r.setObjectName("MS_e_num_format_r")
        self.MS_e_nom_lenght_r = QtWidgets.QLabel(Dialog)
        self.MS_e_nom_lenght_r.setEnabled(True)
        self.MS_e_nom_lenght_r.setGeometry(QtCore.QRect(0, 210, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_nom_lenght_r.setFont(font)
        self.MS_e_nom_lenght_r.setObjectName("MS_e_nom_lenght_r")
        self.MS_e_nom_format_r = QtWidgets.QLabel(Dialog)
        self.MS_e_nom_format_r.setEnabled(True)
        self.MS_e_nom_format_r.setGeometry(QtCore.QRect(0, 230, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_nom_format_r.setFont(font)
        self.MS_e_nom_format_r.setObjectName("MS_e_nom_format_r")
        self.MS_e_temperature_sup_r = QtWidgets.QLabel(Dialog)
        self.MS_e_temperature_sup_r.setEnabled(True)
        self.MS_e_temperature_sup_r.setGeometry(QtCore.QRect(250, 280, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_temperature_sup_r.setFont(font)
        self.MS_e_temperature_sup_r.setObjectName("MS_e_temperature_sup_r")
        self.MS_e_temperature_format_r = QtWidgets.QLabel(Dialog)
        self.MS_e_temperature_format_r.setEnabled(True)
        self.MS_e_temperature_format_r.setGeometry(QtCore.QRect(260, 300, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_temperature_format_r.setFont(font)
        self.MS_e_temperature_format_r.setObjectName("MS_e_temperature_format_r")
        self.BT_quitter_r = QtWidgets.QPushButton(Dialog)
        self.BT_quitter_r.setGeometry(QtCore.QRect(620, 590, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_quitter_r.setFont(font)
        self.BT_quitter_r.setObjectName("BT_quitter_r")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.l_titre_reptile.setText(_translate("Dialog", "Reptile"))
        self.l_num_r.setText(_translate("Dialog", "Numero du reptile"))
        self.l_nom_r.setText(_translate("Dialog", "Nom du reptile"))
        self.l_alimentation_r.setText(_translate("Dialog", "Type d\'alimentation"))
        self.l_type_animal_r.setText(_translate("Dialog", "Type d\'animal"))
        self.l_enclos_r.setText(_translate("Dialog", "Enclos du reptile"))
        self.l_venimeux_r.setText(_translate("Dialog", "reptile venimeux"))
        self.l_nb_dent_r1.setText(_translate("Dialog", "Nombre de dents que "))
        self.l_nb_dent_r2.setText(_translate("Dialog", "le reptile possede"))
        self.l_temperature_r1.setText(_translate("Dialog", "temperature moyenne"))
        self.l_temperature_r2.setText(_translate("Dialog", "du reptile"))
        self.BT_ajouter_r.setText(_translate("Dialog", "Ajouter"))
        self.BT_modifier_r.setText(_translate("Dialog", "Modifier"))
        self.BT_supprimer_r.setText(_translate("Dialog", "Supprimer"))
        self.MS_e_num_existant_r.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Ce numero est deja utilise</span></p></body></html>"))
        self.BT_serialiser_r.setText(_translate("Dialog", "Serialiser"))
        self.BT_deserialiser_r.setText(_translate("Dialog", "Deserialiser"))
        self.MS_e_nb_dent_r.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le nombre doit etre superieure a 0 et entier</span></p></body></html>"))
        self.MS_e_num_format_r.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Voici le format a utiliser: 1234</span></p></body></html>"))
        self.MS_e_nom_lenght_r.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le nom doit comporter moins de 25 lettres </span></p></body></html>"))
        self.MS_e_nom_format_r.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le nom est compose de lettre seulement </span></p></body></html>"))
        self.MS_e_temperature_sup_r.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">La temperature doit etre superieure a 0</span></p></body></html>"))
        self.MS_e_temperature_format_r.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">La temperature doit etre un nombre</span></p></body></html>"))
        self.BT_quitter_r.setText(_translate("Dialog", "Quitter"))