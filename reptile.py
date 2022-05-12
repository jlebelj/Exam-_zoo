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


class Reptile(Animal):
    """
    Classe Enclos
    """

    #      MÉTHODE CONSTRUCTEUR       #
    ###################################
    def __init__(self, p_num_animal = "", p_nom_animal = "", p_Type_alimentation = "", p_Type_animal = "",
                p_enclos = Enclos(), p_nb_dent = "", p_temperature_moyenne = 0, p_Venimeux = False):
        Animal.__init__(self, p_num_animal, p_nom_animal, p_Type_alimentation, p_Type_animal, p_enclos)
        self.__nb_dent = p_nb_dent
        self.__temperature_moyenne = p_temperature_moyenne
        self.Venimeux = p_Venimeux


    ###   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    def get_nb_dent(self):
        """
        Accesseur de l'attribut privé  __nb_dent
        """
        return self.__nb_dent
    def set_nb_dent(self, p_nb):
        """
        Mutateur de l'attribut privé __nb_dent
        """
        if p_nb.isnumeric() and p_nb > 0:
            self.__nb_dent = p_nb
    Nb_dent = property(get_nb_dent, set_nb_dent)

    def get_temperature_moyenne(self):
        """
        Accesseur de l'attribut privé  __temperature_moyenne
        """
        return self.__temperature_moyenne
    def set_temperature_moyenne(self, p_temp):
        if p_temp.isnumeric() and p_temp > 0:
            self.__temperature_moyenne = p_temp
    Temperature_moyenne = property(get_temperature_moyenne, set_temperature_moyenne)

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
        output += (f"{self.enclos.__str__()}\n")
        output += (f"Nombre de dents: {self.__nb_dent}\n")
        output += (f"emperature moyenne corporelle: {self.__temperature_moyenne}\n")
        output += (f"Reptile venimeux?: {self.Venimeux}\n")
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
                self.__dict__["enclos"] = self.enclos.__dict__
                try:
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
            with open(p_fichier , "r") as fichier :
                try:
                    self.__dict__ = json.load(fichier)
                    return 0
                except:
                    return 1
        except:
            return 2

A1 = Enclos("Terrarium", "sous_sol", "1234")

l1 = Reptile("A1111", "gecko", "Omnivore", "reptile", A1, "10", 35, False)

l2 = Reptile()

l2.deserialiser("test2")

l1.serialiser("test2")

#q1.serialiser("test2")
#q1.serialiser("test2")

l3 = Reptile()

l3.deserialiser("test2")






