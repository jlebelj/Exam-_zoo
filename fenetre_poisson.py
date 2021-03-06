# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import interface_poisson
# importation classe
from poisson import *
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

def verifier_animal_est_poisson(p_type):
    """
        Vérifie si le type d'animal choisit est le bon dependemment du pop up choisit
            :param p_type:  le numéro d'étudiant
            :return: True si l'étudiant est trouvé dans la liste des étudiants et False sinon
    """
    if p_type == "Poisson":
            return True
    return False

def cacher_labels_erreur_poisson(objet):
    """
    Cacher les différents labels d'erreur dans pop up poisson
    """
    objet.MS_e_num_inex_p.setVisible(False)
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
        self.setWindowTitle("Poisson")
        cacher_labels_erreur_poisson(self)
        for e in lst_animal_globale:
            if e.Type_animal == "Poisson":
                self.textBrowser_p.append(e.__str__())
                self.textBrowser_p.append("")
        for enc in lst_enclos:
            self.CB_enclos_p.addItem(enc.Num_enclos)

    @pyqtSlot()
    def on_BT_quitter_p_clicked(self): # quitter page poisson
        self.close()

    @pyqtSlot()
    # Bouton ajouter pour Poisson
    def on_BT_ajouter_p_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton ajouter un poisson
        """
        # Instancier un objet Enclos
        po = Poisson()
        # Entrée de donnée pour les attributs de l'objet Poisson
        po.Num_animal = self.line_num_p.text().capitalize()
        po.Nom_animal = self.line_nom_p.text()
        po.Longueur_poisson = self.line_longueur_p.text()
        po.Type_animal = self.CB_type_animal_p.currentText()
        po.Type_eau = self.CB_eau_p.currentText()
        po.Type_alimentation = self.CB_alimentation_p.currentText()
        po.enclos = self.CB_enclos_p.currentText()
        # True/False qui nous informe si num existe ou pas dans liste + si type
        verifier_animal = verifier_animal_liste(po.Num_animal)
        verifier_type_animal = verifier_animal_est_poisson(po.Type_animal)
        # Si num d'enclos valide mais existe déjà dans la liste enclos, on ajoute pas
        if verifier_animal is True:
            self.line_num_p.clear()
            self.MS_e_num_existant_p.setVisible(True)
        if verifier_type_animal is False:
            self.MS_e_type_p.setVisible(True)
        if po.Num_animal == "":  # Si le num d'enclos est invalide, effacer lineEdit et afficher message d'erreur
            self.line_num_p.clear()
            self.MS_e_num_format_p.setVisible(True)
        if po.Nom_animal == "":
            self.MS_e_nom_format_p.setVisible(True)
            self.MS_e_nom_lenght_p.setVisible(True)
            self.line_nom_p.clear()
        if po.Longueur_poisson == 0:
            self.line_longueur_p.clear()
            self.MS_e_longueur_sup_p.setVisible(True)
            # si num est valide et n'existe pas deja on creer
        if po.Num_animal != "" and po.Nom_animal != "" and po.Longueur_poisson != 0 and verifier_type_animal is True \
                and verifier_animal is False:
            lst_animal_globale.append(po)  # ajoute a la liste
            for a in lst_animal_globale:
                if a.Num_animal == po.Num_animal:
                    for encl in lst_enclos:
                        if encl.Num_enclos == po.enclos:
                            a.enclos = encl
            for enclo in lst_enclos:
                if enclo.Num_enclos == self.CB_enclos_p.currentText():
                    enclo.lst_animal.append(po)
            #self.textBrowser_p.clear()  # reinitialisation du text browser
            self.textBrowser_p.clear()
            for animaux in lst_animal_globale:
                if animaux.Type_animal == "Poisson":
                    self.textBrowser_p.append(animaux.__str__()) # Affichage de tous les poissons dans la liste
                    self.textBrowser_p.append("")# Spacer
            self.line_num_p.clear()  # Réinitialiser lineEdits num et combobox de l'emplacement et du type d'enclos
            self.CB_eau_p.setCurrentText("Salé")
            self.CB_alimentation_p.setCurrentText("Herbivore")
            self.line_nom_p.clear()
            self.line_longueur_p.clear()
            self.CB_type_animal_p.setCurrentText("Poisson")

    @pyqtSlot()
    # Bouton modifier pour Poisson
    def on_BT_modifier_p_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton ajouter un poisson
        """
        # Instancier un objet Enclos
        po = Poisson()
        # Entrée de donnée pour les attributs de l'objet Poisson
        po.Num_animal = self.line_num_p.text().capitalize()
        po.Nom_animal = self.line_nom_p.text()
        po.Longueur_poisson = self.line_longueur_p.text()
        po.Type_animal = self.CB_type_animal_p.currentText()
        po.Type_eau = self.CB_eau_p.currentText()
        po.Type_alimentation = self.CB_alimentation_p.currentText()
        po.enclos = self.CB_enclos_p.currentText()
        # True/False qui nous informe si num d'enclos existe ou pas dans liste des enclos + si type st == poisson
        verifier_animal = verifier_animal_liste(po.Num_animal)
        verifier_type_animal = verifier_animal_est_poisson(po.Type_animal)
        # Si num d'enclos valide mais existe pas dans la liste enclos, message d'erreur
        if verifier_animal is False:
            self.line_num_p.clear()
            self.MS_e_num_inex_p.setVisible(True)
        if verifier_type_animal is False:
            self.MS_e_type_p.setVisible(True)
        if po.Num_animal == "":  # Si le num est invalide, effacer lineEdit et afficher message d'erreur
            self.line_num_p.clear()
            self.MS_e_num_format_p.setVisible(True)
        if po.Nom_animal == "": # Si le nom est invalide, effacer lineEdit et afficher message d'erreur
            self.MS_e_nom_format_p.setVisible(True)
            self.MS_e_nom_lenght_p.setVisible(True)
            self.line_nom_p.clear()
        if po.Longueur_poisson == 0: # Si longueur est invalide, effacer lineEdit et afficher message d'erreur
            self.line_longueur_p.clear()
            self.MS_e_longueur_sup_p.setVisible(True)
            # si num est valide et n'existe pas deja on creer
        if po.Num_animal != "" and po.Nom_animal != "" and po.Longueur_poisson != 0 and verifier_type_animal is True \
                and verifier_animal is True: # Si toutes valeurs sont correctes
            for a in lst_animal_globale:
                if a.Num_animal == po.Num_animal: # identifie l'objet poisson correspondant au num entre
                    for enc in lst_enclos:
                        if enc.Num_enclos == a.enclos.Num_enclos: # identifie l'objet poisson correspondant a ancien poisson
                            enc.lst_animal.remove(a) # on supprime l'ancien poisson de son enclos
                    a.Nom_animal = self.line_nom_p.text()
                    a.Longueur_poisson = self.line_longueur_p.text()
                    a.Type_animal = self.CB_type_animal_p.currentText() # associe new valeur au bon objet poisson
                    a.Type_alimentation = self.CB_alimentation_p.currentText()
                    a.Type_eau = self.CB_eau_p.currentText()
                    for encl in lst_enclos:
                        if encl.Num_enclos == po.enclos:
                            a.enclos = encl # modifie l'enclos pour sa nouvelle valeur
            for enclo in lst_enclos:
                if enclo.Num_enclos == self.CB_enclos_p.currentText():
                    enclo.lst_animal.append(po) # ajoute poisson maintenant modifie dans la liste d'animaux de l'enclos
            self.textBrowser_p.clear() # reinitialisation du text browser
            for animaux in lst_animal_globale:
                if animaux.Type_animal == "Poisson": # affiche seulement poisson dans page poisson
                    self.textBrowser_p.append(animaux.__str__())  # Afffichage de tous les poisons dans la liste
                    self.textBrowser_p.append("")  # Spacer
            self.line_num_p.clear()  # Réinitialiser lineEdits num et combobox de pop up poisson
            self.CB_eau_p.setCurrentText("Salé")
            self.CB_alimentation_p.setCurrentText("Herbivore")
            self.line_nom_p.clear()
            self.line_longueur_p.clear()
            self.CB_type_animal_p.setCurrentText("Poisson")

    @pyqtSlot()
    # Bouton supprimer pour Poisson
    def on_BT_supprimer_p_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton ajouter un poisson
        """
        # Instancier un objet Enclos
        po = Poisson()
        # Entrée de donnée pour les attributs de l'objet Poisson
        po.Num_animal = self.line_num_p.text().capitalize()
        po.Type_animal = self.CB_type_animal_p.currentText()
        # True/False qui nous informe si num d'enclos existe ou pas dans liste des enclos + si type st == poisson
        verifier_animal = verifier_animal_liste(po.Num_animal)
        verifier_type_animal = verifier_animal_est_poisson(po.Type_animal)
        # Si num valide mais existe pas dans liste, message d'erreur
        if verifier_animal is False:
            self.line_num_p.clear()
            self.MS_e_num_inex_p.setVisible(True)
        if verifier_type_animal is False:
            self.MS_e_type_p.setVisible(True)
        if po.Num_animal == "":  # Si le num est invalide, effacer lineEdit et afficher message d'erreur
            self.line_num_p.clear()
            self.MS_e_num_format_p.setVisible(True)
        if verifier_type_animal is True and verifier_animal is True:  # Si toutes valeurs sont correctes
            for a in lst_animal_globale:
                if a.Num_animal == po.Num_animal:  # identifie l'objet poisson correspondant au num entre
                    lst_animal_globale.remove(a)
                    for enc in lst_enclos:
                        if enc.Num_enclos == a.enclos.Num_enclos: # identifie l'objet poisson correspondant au num entre
                            enc.lst_animal.remove(a)  # on supprime poisson de son enclos
            self.textBrowser_p.clear()  # reinitialisation du text browser
            for animaux in lst_animal_globale:
                if animaux.Type_animal == "Poisson":  # affiche seulement poisson dans page poisson
                    self.textBrowser_p.append(animaux.__str__())  # Afffichage de tous les poisons dans la liste
                    self.textBrowser_p.append("")  # Spacer
            self.line_num_p.clear()  # Réinitialiser lineEdits num et combobox de pop up poisson
            self.CB_eau_p.setCurrentText("Salé")
            self.CB_alimentation_p.setCurrentText("Herbivore")
            self.line_nom_p.clear()
            self.line_longueur_p.clear()
            self.CB_type_animal_p.setCurrentText("Poisson")

    @pyqtSlot()
    # Bouton supprimer pour Poisson
    def on_BT_serialiser_p_clicked(self):
        # Cacher les labels qui affichent les différentes erreurs
        # Instancier un objet reptile
        po = Poisson()
        # Entrée de donnée pour les attributs de l'objet poisson
        po.Num_animal = self.line_num_p.text().capitalize()
        po.Nom_animal = self.line_nom_p.text()
        po.Longueur_poisson = self.line_longueur_p.text()
        po.Type_animal = self.CB_type_animal_p.currentText()
        po.Type_eau = self.CB_eau_p.currentText()
        po.Type_alimentation = self.CB_alimentation_p.currentText()
        po.enclos = self.CB_enclos_p.currentText()
        # Si tout est valide on serialise
        if po.Num_animal != "" and po.Nom_animal != "" and po.Longueur_poisson != 0:
            # Séréaliser cet objet
            result = po.serialiser(po.Nom_animal + "_" + po.Num_animal + ".json")
            # Si la séréalisation a marché
            if result == 0:
                # Réinitialiser lineEdits num et combobox de pop up poisson
                self.line_num_p.clear()
                self.CB_eau_p.setCurrentText("Salé")
                self.CB_alimentation_p.setCurrentText("Herbivore")
                self.line_nom_p.clear()
                self.line_longueur_p.clear()
                self.CB_type_animal_p.setCurrentText("Poisson")
            # sinon afficher des messages d'erreur
            elif result == 1:
                # Afficher le message d'erreur d'écriture dans le fichier
                self.MS_e_serialiser_p.setText("<font color=\"#ff0000\">Erreur d'écriture dans le fichier</font>")
            else:
                # Afficher le message d'erreur d'ouverture du fichier
                self.MS_e_serialiser_p.setText("<font color=\"#ff0000\">Erreur d'ouverture du fichier</font>")
        # si le nom est invalide, afficher un message d'erreur
        if po.Nom_animal == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setVisible(True)
        # Si le donnees invalide, effacer le lineEdit et afficher un message d'erreur
        if po.Num_animal == "":
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setVisible(True)
            # Si longueur pas bon clear lineedit et message erreur
        if po.Longueur_poisson == "":
            self.line_longueur_p.clear()
            self.label_erreur_date.setVisible(True)

