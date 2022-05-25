# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# Importer la boite de dialogue
import interface_reptile
# importation classe
from reptile import *
from animal import *
from liste_globale import lst_animal_globale
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
    for elt in lst_animal_globale:
        if elt.Num_animal == p_num.capitalize():
            return True
    return False

def verifier_animal_est_reptile(p_type):
    """
        Vérifie si le type d'animal choisit est le bon dependemment du pop up choisit
            :param p_num:  le numéro d'étudiant
            :return: True si l'étudiant est trouvé dans la liste des étudiants et False sinon
    """
    if p_type == "Reptile":
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
    objet.MS_e_num_inex_r.setVisible(False)

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################
class Fenetre_reptile(QtWidgets.QDialog, interface_reptile.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_reptile, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("reptile")
        cacher_labels_erreur_reptile(self)
        for e in lst_animal_globale:
            if e.Type_animal == "Reptile":
                self.textBrowser_r.append(e.__str__())
                self.textBrowser_r.append("")
        for enc in lst_enclos:
            self.CB_enclos_r.addItem(enc.Num_enclos)

    @pyqtSlot()
    def on_BT_quitter_r_clicked(self):
        self.close()

    @pyqtSlot()
    # Bouton ajouter pour reptile
    def on_BT_ajouter_r_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton ajouter un reptile
        """
        # Instancier un objet reptile
        rep = Reptile()
        # Entrée de donnée pour les attributs de l'objet reptile
        rep.Num_animal = self.line_num_r.text().capitalize()
        rep.Nom_animal = self.line_nom_r.text()
        rep.Temperature_moyenne = self.line_temperature_r.text()
        rep.Type_animal = self.CB_type_animal_r.currentText()
        rep.Venimeux = self.CB_venimeux_r.currentText()
        rep.Type_alimentation = self.CB_alimentation_r.currentText()
        rep.enclos = self.CB_enclos_r.currentText()
        rep.Nb_dent = self.line_nb_dent_r.text()
        # True/False qui nous informe si num existe ou pas dans liste + si type
        verifier_animal = verifier_animal_liste(rep.Num_animal)
        verifier_type_animal = verifier_animal_est_reptile(rep.Type_animal)
        # Si num valide mais existe déjà dans la liste, on ajoute pas
        if verifier_animal is True:
            self.line_num_e.clear()
            self.MS_e_num_existant_r.setVisible(True)
        if rep.Num_animal == "":  # Si le num est invalide, effacer lineEdit et afficher message d'erreur
            self.line_num_r.clear()
            self.MS_e_num_format_r.setVisible(True)
        if rep.Nom_animal == "":
            self.MS_e_nom_lenght_r.setVisible(True)
            self.MS_e_nom_format_r.setVisible(True)
            self.line_nom_r.clear()
        if rep.Nb_dent == 0:
            self.line_nb_dent_r.clear()
            self.MS_e_nb_dent_r.setVisible(True)
        if rep.Temperature_moyenne == 0:
            self.line_temperature_r.clear()
            self.MS_e_temperature_sup_r.setVisible(True)
            self.MS_e_temperature_format_r.setVisible(True)
            # si num est valide et n'existe pas deja on creer
        if rep.Num_animal != "" and rep.Nom_animal != "" and rep.Nb_dent != 0 and rep.Temperature_moyenne != 0 \
                and verifier_type_animal is True and verifier_animal is False:
            lst_animal_globale.append(rep)  # ajoute a la liste globale d'animaux
            for a in lst_animal_globale:
                if a.Num_animal == rep.Num_animal:
                    for encl in lst_enclos:
                        if encl.Num_enclos == rep.enclos: # association de objet enclos a attribut enclos
                            a.enclos = encl
            for enclo in lst_enclos:
                if enclo.Num_enclos == self.CB_enclos_r.currentText():
                    enclo.lst_animal.append(rep) # ajouter animal a liste d'animaux
            # self.textBrowser_p.clear()  # reinitialisation du text browser
            self.textBrowser_r.clear()
            for animaux in lst_animal_globale:
                if animaux.Type_animal == "Reptile":
                    self.textBrowser_r.append(animaux.__str__())  # Afffichage de tous les reptiles dans la liste
                    self.textBrowser_r.append("")  # Spacer
            self.line_num_r.clear()  # Réinitialiser lineEdits num et combobox de l'emplacement et du type d'enclos
            self.CB_venimeux_r.setCurrentText("Oui")
            self.CB_alimentation_r.setCurrentText("Herbivore")
            self.line_nom_r.clear()
            self.line_temperature_r.clear()
            self.line_nb_dent_r.clear()
            self.CB_type_animal_r.setCurrentText("Poisson")

    @pyqtSlot()
    # Bouton modifier pour reptile
    def on_BT_modifier_r_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton ajouter un reptile
        """
        # Instancier un objet reptile
        rep = Reptile()
        # Entrée de donnée pour les attributs de l'objet reptile
        rep.Num_animal = self.line_num_r.text().capitalize()
        rep.Nom_animal = self.line_nom_r.text()
        rep.Temperature_moyenne = self.line_temperature_r.text()
        rep.Type_animal = self.CB_type_animal_r.currentText()
        rep.Venimeux = self.CB_venimeux_r.currentText()
        rep.Type_alimentation = self.CB_alimentation_r.currentText()
        rep.enclos = self.CB_enclos_r.currentText()
        rep.Nb_dent = self.line_nb_dent_r.text()
        # True/False qui nous informe si num existe ou pas dans liste + si type st == reptile
        verifier_animal = verifier_animal_liste(rep.Num_animal)
        verifier_type_animal = verifier_animal_est_reptile(rep.Type_animal)
        # Si num valide mais existe pas dans liste, message d'erreur
        if verifier_animal is False:
            self.line_num_r.clear()
            self.MS_e_num_inex_r.setVisible(True)
        if rep.Num_animal == "":  # Si le num est invalide, effacer lineEdit et afficher message d'erreur
            self.line_num_r.clear()
            self.MS_e_num_format_r.setVisible(True)
        if rep.Nom_animal == "":
            self.MS_e_nom_lenght_r.setVisible(True)
            self.MS_e_nom_format_r.setVisible(True)
            self.line_nom_r.clear()
        if rep.Nb_dent == 0:
            self.line_nb_dent_r.clear()
            self.MS_e_nb_dent_r.setVisible(True)
        if rep.Temperature_moyenne == 0:
            self.line_temperature_r.clear()
            self.MS_e_temperature_sup_r.setVisible(True)
            self.MS_e_temperature_format_r.setVisible(True)
            # si num est valide et n'existe pas deja on creer
        if rep.Num_animal != "" and rep.Nom_animal != "" and rep.Temperature_moyenne != 0 and rep.Nb_dent != 0 \
                and verifier_type_animal is True and verifier_animal is True:  # Si toutes valeurs sont correctes
            for a in lst_animal_globale:
                if a.Num_animal == rep.Num_animal:  # identifie l'objet poisson correspondant au num entre
                    for enc in lst_enclos:
                        if enc.Num_enclos == a.enclos.Num_enclos:  # identifie l'objet reptile correspondant a ancien reptile
                            enc.lst_animal.remove(a)  # on supprime l'ancien reptile de son enclos
                    a.Nom_animal = self.line_nom_r.text()
                    a.Nb_dent = self.line_nb_dent_r.text()
                    a.Type_animal = self.CB_type_animal_r.currentText() # associe nouvelle valeur au bon objet reptile
                    a.Type_alimentation = self.CB_alimentation_r.currentText()
                    a.Temperature_moyenne = self.line_temperature_r.text()
                    a.Venimeux = self.CB_venimeux_r.currentText()
                    for encl in lst_enclos:
                        if encl.Num_enclos == rep.enclos:
                            a.enclos = encl  # modifie l'enclos pour sa nouvelle valeur
            for enclo in lst_enclos:
                if enclo.Num_enclos == self.CB_enclos_r.currentText():
                    enclo.lst_animal.append(rep)  # ajoute reptile maintenant modifie dans la liste d'animaux de l'enclos
            self.textBrowser_r.clear()  # reinitialisation du text browser
            for animaux in lst_animal_globale:
                if animaux.Type_animal == "Reptile":  # affiche seulement poisson dans page reptile
                    self.textBrowser_r.append(animaux.__str__())  # Affichage de tous les reptile dans la liste
                    self.textBrowser_r.append("")  # Spacer
            self.line_num_r.clear()  # Réinitialiser lineEdits num et combobox
            self.CB_venimeux_r.setCurrentText("Oui")
            self.CB_alimentation_r.setCurrentText("Herbivore")
            self.line_nom_r.clear()
            self.line_temperature_r.clear()
            self.line_nb_dent_r.clear()
            self.CB_type_animal_r.setCurrentText("Reptile")


    @pyqtSlot()
    # Bouton modifier pour reptile
    def on_BT_supprimer_r_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton ajouter un reptile
        """
        # Instancier un objet reptile
        rep = Reptile()
        # Entrée de donnée pour les attributs de l'objet reptile
        rep.Num_animal = self.line_num_r.text().capitalize()
        rep.Type_animal = self.CB_type_animal_r.currentText()
        # True/False qui nous informe si num existe ou pas dans liste + si type st == reptile
        verifier_animal = verifier_animal_liste(rep.Num_animal)
        verifier_type_animal = verifier_animal_est_reptile(rep.Type_animal)
        # Si num valide mais existe pas dans la liste, message d'erreur
        if rep.Num_animal == "":  # Si le num est invalide, effacer lineEdit et afficher message d'erreur
            self.line_num_r.clear()
            self.MS_e_num_format_r.setVisible(True)
        if verifier_animal is False:
            self.line_num_r.clear()
            self.MS_e_num_inex_r.setVisible(True)
        if verifier_type_animal is True and verifier_animal is True:  # Si toutes valeurs sont correctes
            for a in lst_animal_globale:
                if a.Num_animal == rep.Num_animal:  # identifie l'objet reptile correspondant au num entre
                    lst_animal_globale.remove(a)
                    for enc in lst_enclos:
                        if enc.Num_enclos == a.enclos.Num_enclos:  # identifie l'objet enclos correspondant au num entre
                            enc.lst_animal.remove(a)  # on supprime reptile de son enclos
            self.textBrowser_r.clear()  # reinitialisation du text browser
            for animaux in lst_animal_globale:
                if animaux.Type_animal == "Reptile":  # affiche seulement reptile dans page reptile
                    self.textBrowser_r.append(animaux.__str__())  # Affichage de tous les poisons dans la liste
                    self.textBrowser_r.append("")  # Spacer
            self.line_num_r.clear()  # Réinitialiser lineEdits num et combobox
            self.CB_venimeux_r.setCurrentText("Oui")
            self.CB_alimentation_r.setCurrentText("Herbivore")
            self.line_nom_r.clear()
            self.line_temperature_r.clear()
            self.line_nb_dent_r.clear()
            self.CB_type_animal_r.setCurrentText("Reptile")

    @pyqtSlot()
    # Bouton supprimer pour reptile
    def on_BT_serialiser_r_clicked(self):
        # Cacher les labels qui affichent les différentes erreurs
        # Instancier un objet reptile
        rep = Reptile()
        # Entrée de donnée pour les attributs de l'objet reptile
        rep.Num_animal = self.line_num_r.text().capitalize()
        rep.Nom_animal = self.line_nom_r.text()
        rep.Temperature_moyenne = self.line_temperature_r.text()
        rep.Type_animal = self.CB_type_animal_r.currentText()
        rep.Venimeux = self.CB_venimeux_r.currentText()
        rep.Type_alimentation = self.CB_alimentation_r.currentText()
        rep.enclos = self.CB_enclos_r.currentText()
        rep.Nb_dent = self.line_nb_dent_r.text()
        # Si donnees sont valides :
        if rep.Num_animal != "" and rep.Nom_animal != "" and rep.Temperature_moyenne != 0 and rep.Nb_dent != 0:
            # Séréaliser cet objet
            result = rep.serialiser(rep.Nom_animal + "_" + rep.Num_animal + ".json")
            # Si la séréalisation a marché
            if result == 0:
                # Réinitialiser lineEdits num et combobox
                self.line_num_r.clear()
                self.CB_venimeux_r.setCurrentText("Oui")
                self.CB_alimentation_r.setCurrentText("Herbivore")
                self.line_nom_r.clear()
                self.line_temperature_r.clear()
                self.line_nb_dent_r.clear()
                self.CB_type_animal_r.setCurrentText("Reptile")
            # sinon afficher des messages d'erreur
            elif result == 1:
                # Afficher le message d'erreur d'écriture dans le fichier
                self.MS_e_serialiser_r.setText("<font color=\"#ff0000\">Erreur d'écriture dans le fichier</font>")
            else:
                # Afficher le message d'erreur d'ouverture du fichier
                self.MS_e_serialiser_r.setText("<font color=\"#ff0000\">Erreur d'ouverture du fichier</font>")
        # si le nom est invalide, afficher un message d'erreur
        if rep.Nom_animal == "":
            self.line_nom_r.clear()
            self.MS_e_nom_format_r.setVisible(True)
            self.MS_e_nom_lenght_r.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit et afficher un message d'erreur
        if rep.Num_animal == "":
            self.line_num_r.clear()
            self.MS_e_num_format_r.setVisible(True)
            # Si donnees invalide clear line edit, afficher un message d'erreur
        if rep.Nb_dent == 0:
            self.line_nb_dent_r.clear()
            self.MS_e_nb_dent_r.setVisible(True)
        if rep.Temperature_moyenne == 0:
            self.line_temperature_r.clear()
            self.MS_e_temperature_sup_r.setVisible(True)
            self.MS_e_temperature_format_r.setVisible(True)