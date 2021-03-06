# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pop_poisson.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(818, 628)
        self.BT_serialiser_p = QtWidgets.QPushButton(Dialog)
        self.BT_serialiser_p.setGeometry(QtCore.QRect(630, 500, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_serialiser_p.setFont(font)
        self.BT_serialiser_p.setObjectName("BT_serialiser_p")
        self.CB_eau_p = QtWidgets.QComboBox(Dialog)
        self.CB_eau_p.setGeometry(QtCore.QRect(610, 290, 181, 41))
        self.CB_eau_p.setObjectName("CB_eau_p")
        self.CB_eau_p.addItem("")
        self.CB_eau_p.addItem("")
        self.CB_eau_p.addItem("")
        self.l_enclo_p = QtWidgets.QLabel(Dialog)
        self.l_enclo_p.setGeometry(QtCore.QRect(20, 260, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_enclo_p.setFont(font)
        self.l_enclo_p.setObjectName("l_enclo_p")
        self.CB_type_animal_p = QtWidgets.QComboBox(Dialog)
        self.CB_type_animal_p.setGeometry(QtCore.QRect(610, 180, 181, 41))
        self.CB_type_animal_p.setObjectName("CB_type_animal_p")
        self.CB_type_animal_p.addItem("")
        self.l_eau_p = QtWidgets.QLabel(Dialog)
        self.l_eau_p.setGeometry(QtCore.QRect(610, 260, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_eau_p.setFont(font)
        self.l_eau_p.setObjectName("l_eau_p")
        self.l_type_animal_p = QtWidgets.QLabel(Dialog)
        self.l_type_animal_p.setGeometry(QtCore.QRect(610, 150, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_type_animal_p.setFont(font)
        self.l_type_animal_p.setObjectName("l_type_animal_p")
        self.l_num_p = QtWidgets.QLabel(Dialog)
        self.l_num_p.setGeometry(QtCore.QRect(10, 0, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_num_p.setFont(font)
        self.l_num_p.setObjectName("l_num_p")
        self.l_longueur_p = QtWidgets.QLabel(Dialog)
        self.l_longueur_p.setGeometry(QtCore.QRect(310, 100, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_longueur_p.setFont(font)
        self.l_longueur_p.setObjectName("l_longueur_p")
        self.l_alimen_p = QtWidgets.QLabel(Dialog)
        self.l_alimen_p.setGeometry(QtCore.QRect(610, 20, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_alimen_p.setFont(font)
        self.l_alimen_p.setObjectName("l_alimen_p")
        self.line_longueur_p = QtWidgets.QLineEdit(Dialog)
        self.line_longueur_p.setGeometry(QtCore.QRect(320, 140, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_longueur_p.setFont(font)
        self.line_longueur_p.setText("")
        self.line_longueur_p.setObjectName("line_longueur_p")
        self.BT_modifier_p = QtWidgets.QPushButton(Dialog)
        self.BT_modifier_p.setGeometry(QtCore.QRect(630, 420, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_modifier_p.setFont(font)
        self.BT_modifier_p.setObjectName("BT_modifier_p")
        self.BT_deserialiser_p = QtWidgets.QPushButton(Dialog)
        self.BT_deserialiser_p.setGeometry(QtCore.QRect(630, 540, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_deserialiser_p.setFont(font)
        self.BT_deserialiser_p.setObjectName("BT_deserialiser_p")
        self.l_titre_poisson = QtWidgets.QLabel(Dialog)
        self.l_titre_poisson.setGeometry(QtCore.QRect(360, 0, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.l_titre_poisson.setFont(font)
        self.l_titre_poisson.setObjectName("l_titre_poisson")
        self.BT_ajouter_p = QtWidgets.QPushButton(Dialog)
        self.BT_ajouter_p.setGeometry(QtCore.QRect(630, 380, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_ajouter_p.setFont(font)
        self.BT_ajouter_p.setObjectName("BT_ajouter_p")
        self.l_nom_p = QtWidgets.QLabel(Dialog)
        self.l_nom_p.setGeometry(QtCore.QRect(20, 140, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_nom_p.setFont(font)
        self.l_nom_p.setObjectName("l_nom_p")
        self.MS_e_num_format_p = QtWidgets.QLabel(Dialog)
        self.MS_e_num_format_p.setEnabled(True)
        self.MS_e_num_format_p.setGeometry(QtCore.QRect(10, 110, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_num_format_p.setFont(font)
        self.MS_e_num_format_p.setObjectName("MS_e_num_format_p")
        self.line_nom_p = QtWidgets.QLineEdit(Dialog)
        self.line_nom_p.setGeometry(QtCore.QRect(20, 170, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_nom_p.setFont(font)
        self.line_nom_p.setText("")
        self.line_nom_p.setObjectName("line_nom_p")
        self.MS_e_nom_format_p = QtWidgets.QLabel(Dialog)
        self.MS_e_nom_format_p.setEnabled(True)
        self.MS_e_nom_format_p.setGeometry(QtCore.QRect(10, 230, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_nom_format_p.setFont(font)
        self.MS_e_nom_format_p.setObjectName("MS_e_nom_format_p")
        self.CB_alimentation_p = QtWidgets.QComboBox(Dialog)
        self.CB_alimentation_p.setGeometry(QtCore.QRect(610, 50, 181, 41))
        self.CB_alimentation_p.setObjectName("CB_alimentation_p")
        self.CB_alimentation_p.addItem("")
        self.CB_alimentation_p.addItem("")
        self.CB_alimentation_p.addItem("")
        self.MS_e_nom_lenght_p = QtWidgets.QLabel(Dialog)
        self.MS_e_nom_lenght_p.setEnabled(True)
        self.MS_e_nom_lenght_p.setGeometry(QtCore.QRect(10, 210, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_nom_lenght_p.setFont(font)
        self.MS_e_nom_lenght_p.setObjectName("MS_e_nom_lenght_p")
        self.CB_enclos_p = QtWidgets.QComboBox(Dialog)
        self.CB_enclos_p.setGeometry(QtCore.QRect(20, 290, 181, 41))
        self.CB_enclos_p.setObjectName("CB_enclos_p")
        self.MS_e_num_existant_p = QtWidgets.QLabel(Dialog)
        self.MS_e_num_existant_p.setEnabled(True)
        self.MS_e_num_existant_p.setGeometry(QtCore.QRect(10, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_num_existant_p.setFont(font)
        self.MS_e_num_existant_p.setObjectName("MS_e_num_existant_p")
        self.textBrowser_p = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_p.setGeometry(QtCore.QRect(20, 340, 591, 281))
        self.textBrowser_p.setObjectName("textBrowser_p")
        self.BT_supprimer_p = QtWidgets.QPushButton(Dialog)
        self.BT_supprimer_p.setGeometry(QtCore.QRect(630, 460, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_supprimer_p.setFont(font)
        self.BT_supprimer_p.setObjectName("BT_supprimer_p")
        self.MS_e_longueur_sup_p = QtWidgets.QLabel(Dialog)
        self.MS_e_longueur_sup_p.setEnabled(True)
        self.MS_e_longueur_sup_p.setGeometry(QtCore.QRect(280, 180, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_longueur_sup_p.setFont(font)
        self.MS_e_longueur_sup_p.setObjectName("MS_e_longueur_sup_p")
        self.line_num_p = QtWidgets.QLineEdit(Dialog)
        self.line_num_p.setGeometry(QtCore.QRect(10, 30, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line_num_p.setFont(font)
        self.line_num_p.setText("")
        self.line_num_p.setObjectName("line_num_p")
        self.BT_quitter_p = QtWidgets.QPushButton(Dialog)
        self.BT_quitter_p.setGeometry(QtCore.QRect(630, 590, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.BT_quitter_p.setFont(font)
        self.BT_quitter_p.setObjectName("BT_quitter_p")
        self.MS_e_num_inex_p = QtWidgets.QLabel(Dialog)
        self.MS_e_num_inex_p.setEnabled(True)
        self.MS_e_num_inex_p.setGeometry(QtCore.QRect(10, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_num_inex_p.setFont(font)
        self.MS_e_num_inex_p.setObjectName("MS_e_num_inex_p")
        self.MS_e_serialiser_p = QtWidgets.QLabel(Dialog)
        self.MS_e_serialiser_p.setEnabled(True)
        self.MS_e_serialiser_p.setGeometry(QtCore.QRect(210, 310, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_serialiser_p.setFont(font)
        self.MS_e_serialiser_p.setObjectName("MS_e_serialiser_p")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.BT_serialiser_p.setText(_translate("Dialog", "Serialiser"))
        self.CB_eau_p.setItemText(0, _translate("Dialog", "Sal??"))
        self.CB_eau_p.setItemText(1, _translate("Dialog", "Douce"))
        self.CB_eau_p.setItemText(2, _translate("Dialog", "M??lang??e"))
        self.l_enclo_p.setText(_translate("Dialog", "Enclos du poisson"))
        self.CB_type_animal_p.setItemText(0, _translate("Dialog", "Poisson"))
        self.l_eau_p.setText(_translate("Dialog", "Type d\'eau "))
        self.l_type_animal_p.setText(_translate("Dialog", "Type d\'animal"))
        self.l_num_p.setText(_translate("Dialog", "Numero du poisson"))
        self.l_longueur_p.setText(_translate("Dialog", "Longueur du poisson"))
        self.l_alimen_p.setText(_translate("Dialog", "Type d\'alimentation"))
        self.BT_modifier_p.setText(_translate("Dialog", "Modifier"))
        self.BT_deserialiser_p.setText(_translate("Dialog", "Deserialiser"))
        self.l_titre_poisson.setText(_translate("Dialog", "Poisson"))
        self.BT_ajouter_p.setText(_translate("Dialog", "Ajouter"))
        self.l_nom_p.setText(_translate("Dialog", "Nom du poisson"))
        self.MS_e_num_format_p.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Voici le format a utiliser: a1234</span></p></body></html>"))
        self.MS_e_nom_format_p.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le nom est compose de lettres seulement </span></p></body></html>"))
        self.CB_alimentation_p.setItemText(0, _translate("Dialog", "Herbivore"))
        self.CB_alimentation_p.setItemText(1, _translate("Dialog", "Carnivore"))
        self.CB_alimentation_p.setItemText(2, _translate("Dialog", "Omnivore"))
        self.MS_e_nom_lenght_p.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le nom doit comporter moins de 25 lettres </span></p></body></html>"))
        self.MS_e_num_existant_p.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Ce numero est deja utilise</span></p></body></html>"))
        self.BT_supprimer_p.setText(_translate("Dialog", "Supprimer"))
        self.MS_e_longueur_sup_p.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Le nombre doit etre superieure a 0</span></p></body></html>"))
        self.BT_quitter_p.setText(_translate("Dialog", "Quitter"))
        self.MS_e_num_inex_p.setText(_translate("Dialog", "<html><head/><body><p><span style=\" color:#ff0000;\">Ce numero est inexistant</span></p></body></html>"))
        self.MS_e_serialiser_p.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
