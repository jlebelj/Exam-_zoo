####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final -  Zoo
###  Nom: Jeremy lebel
###  No étudiant: 2125813
###  No Groupe: ?
###  Description du fichier: Classe Piosson
####################################################################################

# importation de classes
from animal import *
from enclos import *
from liste_globale import lst_enclos
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
                p_enclos = Enclos(), p_longueur = 0, p_Type_eau = ""):
        Animal.__init__(self, p_num_animal, p_nom_animal, p_Type_alimentation, p_Type_animal, p_enclos)
        self.__longueur = p_longueur
        self.Type_eau = p_Type_eau

    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    def get_longueur(self):
        """
        Accesseur de l'attribut privé  __longueur
        """
        return self.__longueur
    def set_longueur(self, p_longueur):
        """
        Mutateur de l'attribut privé __longueur
        """
        if p_longueur.isnumeric():
            p_longueur = int(p_longueur)
            if p_longueur > 0:
                self.__longueur = p_longueur
    Longueur_poisson = property(get_longueur, set_longueur)


    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self) :
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        output = (f"Nom de l'animal: {self.Nom_animal}\n")
        output += (f"Numero de l'animal: {self.Num_animal}\n")
        output += (f"Type d'animal: {self.Type_animal}\n")
        output += (f"Type d'alimentation: {self.Type_alimentation}\n")
        output += (f"Longueur du poisson: {self.__longueur}\n")
        output += (f"Type d'eau: {self.Type_eau}\n")
        output += (f"{self.enclos.__str__()}\n")
        return output

    #####          Autres MÉTHODES         #####
    ############################################

    def serialiser(self, p_fichier):
        """
        Méthode permttant de sérialiser un objet de la classe Reptile
        ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
        :: return : retourne 0 si le fichier est ouvert et les informations y sont écrites,
        1 s'il y a erreur d'écriture et 2 s'il y a erreur d'ouverture
        """
        try:
            with open(p_fichier, "w") as fichier:
                try:
                    for enc in lst_enclos:
                        if enc.Num_enclos == self.__dict__["enclos"]:
                            self.__dict__["enclos"] = enc.__dict__
                    json.dump(self.__dict__, fichier)
                    return 0
                except:
                    return 1
        except:
            return 2

    def deserialiser(self, p_fichier):
        """
            Méthode permttant de désérialiser un objet de la classe Reptile
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
                """
        try:
            with open(p_fichier, "r") as fichier:
                try:
                    self.__dict__ = json.load(fichier)
                    # print(self.enclos.__dict__) #= {'Type_enclos': '', 'Emplacement': '', '_Enclos__num_enclos': '', 'lst_animal': []}\
                    #print(self.__dict__["enclos"]) #= {'Type_enclos': 'Terrarium', 'Emplacement': 'sous_sol', '_Enclos__num_enclos': '1234', 'lst_animal': []}
                    # self.__dict__["enclos"] = "a"
                    #print(self.enclos["_Enclos__num_enclos"]) #= 1234
                    # faire for loop parcourant liste enclos reperant lobjet enclos associer au num

                except:
                    return 1
        except:
            return 2

