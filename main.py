#!/usr/bin/env python3

class Personnage:
    def __init__(self, nom):
        self.nom = nom
        self.points_de_vie = 10

    def attaquer(self, cible):
        cible.points_de_vie -= 1
        print(f"{self.nom} attaque {cible.nom}! {cible.nom} a maintenant {cible.points_de_vie} points de vie.")

# Création des personnages
personnage1 = Personnage("Héros")
personnage2 = Personnage("Méchant")

# Boucle de combat
while personnage1.points_de_vie > 0 and personnage2.points_de_vie > 0:
    personnage1.attaquer(personnage2)
    if personnage2.points_de_vie > 0:
        personnage2.attaquer(personnage1)

# Annonce du vainqueur
if personnage1.points_de_vie > 0:
    print(f"{personnage1.nom} a gagné!")
else:
    print(f"{personnage2.nom} a gagné!")