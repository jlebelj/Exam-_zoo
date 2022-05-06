####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final -  Zoo
###  Nom: Jeremy lebel
###  No étudiant: 2125813
###  No Groupe: ?
###  Description du fichier: Classe Piosson
####################################################################################

# importation de classes
from animal import  *
from enclos import *
# instanciation

# importation de fonction speciale
import json


class Poisson(Animal):
    """
    Classe Enclos
    """

    #      MÉTHODE CONSTRUCTEUR       #
    ###################################
    def __init__(self, p_num_animal = "", p_nom_animal = "", p_Type_alimentation = "", p_Type_animal = "",
                p_enclos = Enclos(), p_longueur = "", p_Type_eau = ""):
        Animal.__init__(self, p_num_animal, p_nom_animal, p_Type_alimentation, p_Type_animal, p_enclos = Enclos())
        self.__longueur = p_longueur
        self.Type_eau = p_Type_eau

    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    def get_longueur(self):
        return self.__longueur
    def set_longueur(self, p_longueur):
        if p_longueur.isnumeric() and p_longueur > 0:
            self.__longueur = p_longueur


    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self) :
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        output = ("*************************\n")
        output += (f"Nom de l'animal: {self.__nom_animal}\n")
        output += (f"Numero de l'animal: {self.__num_animal}\n")
        output += (f"Prenom: {self.Type_animal}\n")
        output += (f"Type d'alimentation: {self.Type_alimentation}\n")
        output += (f"Numero de l'enclos: {self.enclos.__str__()}\n")
        output += (f"Longueur du poisson: {self.__longueur}\n")
        output += (f"Type d'eau: {self.Type_eau}\n")
        output += ("*************************\n")
        return output


    #####          Autres MÉTHODES         #####
    ############################################

    def serialiser(self, p_fichier):
        """
        Méthode permttant de sérialiser un objet de la classe Etudiant
        ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
        :: return : retourne 0 si le fichier est ouvert et les informations y sont écrites,
        1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture

        """

        try:
            with open(p_fichier, "w") as fichier:
                try:
                    #json.dump(self.__dict__, fichier)
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2
























