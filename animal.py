####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final -  Zoo
###  Nom: Jeremy lebel
###  No étudiant: 2125813
###  No Groupe: ?
###  Description du fichier: Classe Animal
####################################################################################










class Animal:
    """
    Classe Animal (classe mere de poisson et reptile)
    """

    #      MÉTHODE CONSTRUCTEUR       #
    ###################################
    def __init__(self, p_num_animal = "", p_nom_animal = "", p_Type_alimentation = "", p_Type_animal = "", p_enclos = Enclos()):
        self.__num_animal = p_num_animal
        self.__nom_animal = p_nom_animal
        self.Type_alimentation = p_Type_alimentation
        self.Type_animal = p_Type_animal
        self.enclos = p_enclos


    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    def get_num_animal(self):
        """
        Accesseur de l'attribut privé  __num_animal
        """
        return self.__num_animal
    def set_num_animal(self, p_num):
        """
        Mutateur de l'attribut privé  __num_animal
        """
        if len(p_num) == 5:
            if p_num[0].isalpha() and p_num[1:].isnumeric():
                self.__num_animal = p_num
    Num_animal = property(get_num_animal, set_num_animal)


    def get_nom_animal(self):
        """
        Accesseur de l'attribut privé  __nom_animal
        """
        return self.__nom_animal
    def set_nom_animal(self, p_nom):
        """
        Mutateur de l'attribut privé __nom_animal
        """
        if len(p_nom) <= 25 and p_nom.isalpha():
            self.__nom_animal = p_nom
    Nom_animal = property(get_nom_animal, set_nom_animal)


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
        output += (f"Type d'animal: {self.Type_animal}\n")
        output += (f"Type d'alimentation: {self.Type_alimentation}\n")
        output += (f"Numero de l'enclos: {self.enclos.__str__()}\n")
        output += ("*************************\n")
        return output













