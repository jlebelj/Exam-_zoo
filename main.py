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
from PyQt5.QtCore import QDate, pyqtSlot

# Importer Pour le model de la listView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# importer les interfaces graphiques
import interface_graphique_zoo
import interface_liste_animaux
# importer classe
from liste_globale import lst_enclos
from liste_globale import lst_animal_globale
from fenetre_reptile import *
from fenetre_poisson import *
from fenetre_enclos import *
from fenetre_liste import *
from reptile import *
from poisson import *
# instanciation d'objet pour des test
A1 = Enclos("Terrarium", "sous_sol", "1234", [])
r1 = Reptile("B1234", "gecko", "Omnivore", "Reptile", A1, 23, 30, "Non")
r2 = Reptile("B4321", "dragon barbu", "Omnivore", "Reptile", A1, 35, 20, "Non")
A1.lst_animal.append(r1)
A1.lst_animal.append(r2)
A2 = Enclos("Aquarium", "premier etage", "4321", [])
p2 = Poisson("C1234", "achigan", "carnivore", "Poisson", A2, "6", "douce")
p1 = Poisson("A1234", "brochet", "carnivore", "Poisson", A2, "10", "sale")

A2.lst_animal.append(p1)
A2.lst_animal.append(p2)

lst_animal_globale.append(r1)
lst_animal_globale.append(p2)
lst_animal_globale.append(p1)
lst_animal_globale.append(r2)

lst_enclos.append(A1)
lst_enclos.append(A2)

#######################################################
###### DÉFINITIONS DE LA CLASSE fenetrePrincipale ######
########################################################
class Fenetre_principale(QtWidgets.QMainWindow, interface_graphique_zoo.Ui_MainWindow):
    """
    Nome de la classe : fenetrePrincipale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interfacegraphique.Ui_MainWindow : Ma classe générée avec QtDesigner
    """
    def __init__(self, parent=None):

        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interfacegraphique.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(Fenetre_principale, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Zoo")
        # Cacher tous les labels d'erreur

                        ###  Bouton  ###
    ##########################################################

    @pyqtSlot()
    # Bouton poisson pour ouvrir pop up poisson
    def on_BT_poisson_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetre_poisson()  # nom de la classe du pop up
        # Préparer la listview
        # Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()

    @pyqtSlot()
    # Bouton poisson pour ouvrir pop up poisson
    def on_BT_reptile_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetre_reptile()  # nom de la classe du pop up
        # Préparer la listview
        # Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()

    @pyqtSlot()
    # Bouton poisson pour ouvrir pop up poisson
    def on_BT_enclos_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetre_enclos()  # nom de la classe du pop up
        # Préparer la listview
        # Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()

    @pyqtSlot()
    # Bouton poisson pour ouvrir pop up poisson
    def on_BT_afficher_animaux_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetre_liste()  # nom de la classe du pop up
        # Préparer la listview
        # Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()

    @pyqtSlot()
    def on_BT_quitter_m_clicked(self):
        self.close()


def main():
    """
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = Fenetre_principale()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()

if __name__ == "__main__":
    main()

