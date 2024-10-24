#!/usr/bin/env python3

import unittest
from main import Personnage

class TestPersonnage(unittest.TestCase):

    def setUp(self):
        self.hero = Personnage("Héros")
        self.mechant = Personnage("Méchant")

    def test_points_de_vie_initiaux(self):
        self.assertEqual(self.hero.points_de_vie, 10)
        self.assertEqual(self.mechant.points_de_vie, 10)

    def test_attaque(self):
        self.hero.attaquer(self.mechant)
        self.assertEqual(self.mechant.points_de_vie, 9)

    def test_mort(self):
        for _ in range(10):
            self.hero.attaquer(self.mechant)
        self.assertEqual(self.mechant.points_de_vie, 0)

    def test_combat_complet(self):
        while self.hero.points_de_vie > 0 and self.mechant.points_de_vie > 0:
            self.hero.attaquer(self.mechant)
            if self.mechant.points_de_vie > 0:
                self.mechant.attaquer(self.hero)
        self.assertTrue(self.hero.points_de_vie > 0 or self.mechant.points_de_vie > 0)

if __name__ == '__main__':
    unittest.main()