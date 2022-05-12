# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# Importer la boite de dialogue
import interface_enclos
# importation classe
from poisson import *
from animal import *
from liste_globale import lst_enclos
# definition


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def verifier_animal_liste(p_num):
    """
        Vérifie si l'étudiant existe dans la liste des étudiants
            :param p_num:  le numéro d'étudiant
            :return: True si l'étudiant est trouvé dans la liste des étudiants et False sinon
    """
    for elt in lst_enclos:
        if elt.Num_enclos == p_num.capitalize():
            return True
    return False

def cacher_labels_erreur_poisson(objet):
    """
    Cacher les différents labels d'erreur dans pop up poisson
    """
    objet.MS_e_num_format_e.setVisible(False)
    objet.MS_e_num_existant_e.setVisible(False)


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
class Fenetre_enclos(QtWidgets.QDialog, interface_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_enclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("enclos")
        cacher_labels_erreur_poisson(self)
        for e in lst_enclos:
            self.textBrowser_e.append(e.__str__())

            self.textBrowser_e.append("")

    @pyqtSlot()
    def on_BT_quitter_e_clicked(self):
        self.close()













