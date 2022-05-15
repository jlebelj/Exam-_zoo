# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer l'interface de la page enclos
import interface_enclos
# importation des classes et liste necessaire
from reptile import *
from liste_globale import lst_enclos
#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################
def verifier_enclos_liste(p_num):
    """
        Vérifie si l'enclos existe dans la liste des enclos
            :param p_num:  le numéro de l'enclos
            :return: True si l'enclos est trouvé dans la liste des enclos et False sinon
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
    objet.MS_e_num_inex.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
class Fenetre_enclos(QtWidgets.QDialog, interface_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_enclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("enclos")
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur_poisson(self)
        # afficher les enclos deja creer dansle text browser
        for e in lst_enclos:
            self.textBrowser_e.append(e.__str__())
            # Spacer pour que ce sois plus claire
            self.textBrowser_e.append("")

    @pyqtSlot() # Bouton pour quitter la page enclos
    def on_BT_quitter_e_clicked(self):
        self.close()

    @pyqtSlot()
    # Bouton Creer un enclos
    def on_BT_ajouter_enclos_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Creer des enclos
        """
        # Instancier un objet Enclos
        en = Enclos()
        # Entrée de donnée pour les attributs de l'objet Enclos
        en.Num_enclos = self.line_num_e.text().capitalize()
        en.Type_enclos = self.CB_type_enclos_e.currentText()
        en.Emplacement = self.CB_emplacement_e.currentText()
        # True/False qui nous informe si num d'enclos existe ou pas dans liste des enclos
        verifier_enclos = verifier_enclos_liste(en.Num_enclos)
        # Si num d'enclos valide mais existe déjà dans la liste enclos, on ajoute pas
        if verifier_enclos is True:
            self.line_num_e.clear()
            self.MS_e_num_existant_e.setVisible(True)
        if en.Num_enclos == "": # Si le num d'enclos est invalide, effacer lineEdit et afficher message d'erreur
            self.line_num_e.clear()
            self.MS_e_num_format_e.setVisible(True)

        if en.Num_enclos != "" and verifier_enclos is False: # si num est valide et n'existe pas deja on creer
            lst_enclos.append(en) # ajoute a la liste
            self.textBrowser_e.clear() # reinitialisation du text browser
            for enclos in lst_enclos: # Afffichage de tous les enclos dans la liste
                self.textBrowser_e.append(enclos.__str__())
                self.textBrowser_e.append("") # Spacer
            self.line_num_e.clear() # Réinitialiser  lineEdits num et combobox de l'emplacement et du type d'enclos
            self.CB_type_enclos_e.setCurrentText("Terrarium")
            self.CB_emplacement_e.setCurrentText("sous-sol")


    @pyqtSlot()
    # Bouton Ajouter
    def on_BT_modifier_e_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Modifier d'enclos
        """
        # Instancier un objet Enclos
        en = Enclos()
        # Entrée de donnée pour les attributs de l'objet Enclos
        en.Num_enclos = self.line_num_e.text().capitalize()
        en.Type_enclos = self.CB_type_enclos_e.currentText()
        en.Emplacement = self.CB_emplacement_e.currentText()
        # True/False qui nous informe si num d'enclos existe ou pas dans liste des enclos
        verifier_enclos = verifier_enclos_liste(en.Num_enclos)
        # Si num d'enclos valide et existe dans liste enclos on modifie
        if en.Num_enclos == "":
            self.line_num_e.clear()
            self.MS_e_num_format_e.setVisible(True)
        if verifier_enclos is False:
            self.line_num_e.clear()
            self.MS_e_num_inex.setVisible(True)
        if verifier_enclos is True and en.Num_enclos != "": # si num valide et retrouve dans liste, on modifie
            for enclos in lst_enclos:
                if enclos.Num_enclos == en.Num_enclos: # reperer bon objet grace au numero unique de chaque objet enclos
                    enclos.Type_enclos = en.Type_enclos # ici on attribut nouvelle valeur
                    enclos.Emplacement = en.Emplacement #
                    # Clear le textBowser
                    self.textBrowser_e.clear()
                    # Après modifications, réafficher enclos dans le textBrowser
                    for enc in lst_enclos:
                        self.textBrowser_e.append(enc.__str__())
                        self.textBrowser_e.append("")
                    # Réinitialiser les lineEdits du numéro et les combobox de l'emplacement et du type d'enclos
                    self.line_num_e.clear()
                    self.CB_type_enclos_e.setCurrentText("Terrarium")
                    self.CB_emplacement_e.setCurrentText("sous-sol")

    @pyqtSlot()
    # Bouton Ajouter
    def on_BT_supprimer_e_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer d'enclos
        """
        # Instancier un objet Enclos
        en = Enclos()
        # Entrée de donnée pour les attributs de l'objet Enclos
        en.Num_enclos = self.line_num_e.text().capitalize()
        en.Type_enclos = self.CB_type_enclos_e.currentText()
        en.Emplacement = self.CB_emplacement_e.currentText()
        # True/False qui nous informe si num d'enclos existe ou pas dans liste des enclos
        verifier_enclos = verifier_enclos_liste(en.Num_enclos)
        # Si num d'enclos valide et existe dans liste enclos on supprime
        if en.Num_enclos == "":
            self.line_num_e.clear()
            self.MS_e_num_format_e.setVisible(True)
        if verifier_enclos is False: # si num enclos est introuvable
            self.line_num_e.clear()
            self.MS_e_num_inex.setVisible(True)
        if verifier_enclos is True:  # si num retrouve dans liste, on modifie
            for enclos in lst_enclos:
                if enclos.Num_enclos == en.Num_enclos: # reperer bon objet grace au numero unique de chaque objet enclos
                    lst_enclos.remove(enclos) # supprime objet de la liste des enclos
                    # Clear le textBowser
                    self.textBrowser_e.clear()
                    # Après modifications, réafficher tous les étudiants de la liste dans le textBrowser
                    for enc in lst_enclos: # Après modifications, réafficher enclos dans le textBrowser
                        self.textBrowser_e.append(enc.__str__())
                        self.textBrowser_e.append("")
                    # Réinitialiser les lineEdits du numéro et les combobox de l'emplacement et du type d'enclos
                    self.line_num_e.clear()
                    self.CB_type_enclos_e.setCurrentText("Terrarium")
                    self.CB_emplacement_e.setCurrentText("sous-sol")

