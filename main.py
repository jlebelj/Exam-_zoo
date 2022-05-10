####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final -  Zoo
###  Nom: Jeremy lebel
###  No étudiant: 2125813
###  No Groupe: ?
###  Description du fichier: classe main fenetre QT
####################################################################################


###  IMPORTATIONS - Portée globale  ###
########+###############################

# Importer le module sys nécessaire à l'exécution.
import sys
# Pour la réinitialisation de la date dans le dateEdit
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate

# Importer Pour le model de la listView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# importer les interfaces graphiques
import interface_graphique
# from
# from
# from
# Importer la classe Etudiant
#from Etudiant import *

###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################




###### DÉFINITIONS DE LA CLASSE fenetrePrincipale ######
########################################################


class fenetre_principale(QtWidgets.QMainWindow, interface_graphique.Ui_MainWindow):
    """
    Nome de la classe : fenetre_principale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interfacegraphique.Ui_MainWindow : classe main window générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interfacegraphique.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(fenetre_principale, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Gestion de scolarité")
        # Cacher tous les labels d'erreur