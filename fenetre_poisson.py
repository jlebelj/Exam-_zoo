# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# Importer la boite de dialogue
import interface_poisson
# importation classe
from poisson import *
from animal import *
from liste_globale import lst_animal_globale
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
    for elt in lst_animal_globale:
        if elt.Num_animal == p_num.capitalize():
            return True
    return False

def cacher_labels_erreur_poisson(objet):
    """
    Cacher les différents labels d'erreur dans pop up poisson
    """
    objet.MS_e_num_format_p.setVisible(False)
    objet.MS_e_nom_format_p.setVisible(False)
    objet.MS_e_nom_lenght_p.setVisible(False)
    objet.MS_e_num_existant_p.setVisible(False)
    objet.MS_e_longueur_sup_p.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
class Fenetre_poisson(QtWidgets.QDialog, interface_poisson.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_poisson, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("poisson")
        cacher_labels_erreur_poisson(self)
        for e in lst_animal_globale:
            if e.Type_animal == "poisson":
                self.textBrowser_p.append(e.__str__())
                self.textBrowser_p.append("")

    @pyqtSlot()
    def on_BT_quitter_p_clicked(self):
        self.close()



