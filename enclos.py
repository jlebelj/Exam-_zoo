####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Examen final -  Zoo
###  Nom: Jeremy lebel
###  No étudiant: 2125813
###  No Groupe: ?
###  Description du fichier: Classe Enclos
####################################################################################

class Enclos:
    """
    Classe Enclos
    """

    #      MÉTHODE CONSTRUCTEUR       #
    ###################################
    def __init__(self, p_Type_enclos = "", p_emplacement = "", p_num_enclos = "", p_lst_animal = [] ):
        self.Type_enclos = p_Type_enclos
        self.Emplacement = p_emplacement
        self.__num_enclos = p_num_enclos
        self.lst_animal = p_lst_animal


    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    def get_num_enclos(self):
        """
        Accesseur de l'attribut privé  __num_animal
        """
        return self.__num_enclos
    def set_num_enclos(self, p_num):
        """
        Mutateur de l'attribut privé __nom_animal
        """
        if p_num.isnumeric() and len(p_num) == 4:
            self.__num_enclos = p_num
    Num_enclos = property(get_num_enclos, set_num_enclos)


    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################
    def __str__(self) :
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        output = (f"Numero de l'enclos: {self.__num_enclos}\n")
        output += (f"Type de l'enclos: {self.Type_enclos}\n")
        output += (f"Emplacement de l'enclos: {self.Emplacement}\n")
        chaine = ""
        for x in self.lst_animal:
            print(self.lst_animal)
            chaine += "\n" + x.Num_animal+": " + x.Nom_animal
        output += (f"Animal/Animaux dans cet enclos: {chaine}")
        return output

    def format_serialiser(self):
        """
        Méthode spéciale d'affichage utilise seulement lorsqu'on serialise pour bien formater les donnees
        :return: Chaine utlilise dans le fichier json
        """
        return self.__dict__









