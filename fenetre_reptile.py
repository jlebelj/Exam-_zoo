# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# Importer la boite de dialogue
import interface_reptile
# importation classe
from poisson import *
from animal import *
from liste_globale import lst_animal
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
    for elt in lst_animal:
        if elt.Num_animal == p_num.capitalize():
            return True
    return False

def cacher_labels_erreur_reptile(objet):
    """
    Cacher les différents labels d'erreur dans pop up poisson
    """
    objet.MS_e_num_existant_r.setVisible(False)
    objet.MS_e_nb_dent_r.setVisible(False)
    objet.MS_e_nom_format_r.setVisible(False)
    objet.MS_e_nom_lenght_r.setVisible(False)
    objet.MS_e_temperature_format_r.setVisible(False)
    objet.MS_e_num_format_r.setVisible(False)
    objet.MS_e_temperature_sup_r.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
class Fenetre_reptile(QtWidgets.QDialog, interface_reptile.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_reptile, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("reptile")
        cacher_labels_erreur_reptile(self)
        for e in lst_animal:
            if e.Type_animal == "reptile":
                self.textBrowser_r.append(e.__str__())

    @pyqtSlot()
    def on_BT_quitter_r_clicked(self):
        self.close()
