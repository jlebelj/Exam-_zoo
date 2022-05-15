from poisson import *
from enclos import *
from reptile import *

###  instanciation objet pour test  ###
#######################################
A1 = Enclos("Terrarium", "sous_sol", "1234", [])
r1 = Reptile("B1234", "gecko", "Omnivore", "Reptile", A1, "23", 30, True)
A1.lst_animal.append(r1)

A2 = Enclos("Aquarium", "premier etage", "4321", [])
p2 = Poisson("C1234", "achigan", "carnivore", "Poisson", A2, "6", "douce")
p1 = Poisson("A1234", "brochet", "carnivore", "Poisson", A2, "10", "sale")

A2.lst_animal.append(p1)
A2.lst_animal.append(p2)
#       liste
####################
lst_animal_globale = []
lst_enclos = []

lst_animal_globale.append(r1)
lst_animal_globale.append(p2)
lst_animal_globale.append(p1)

lst_enclos.append(A1)
lst_enclos.append(A2)