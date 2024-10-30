from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from .models import Emprunteur, Livre, CD, DVD, JeuDePlateau, Emprunteur


# Test pour la création d'un emprunteur
class TestCreateEmprunteur(TestCase):
    def setUp(self):
        Emprunteur.objects.create(name="Test Emprunteur", bloque=False)

    def test_create_emprunteur(self):
        emprunteur = Emprunteur.objects.get(name="Test Emprunteur")
        self.assertEqual(emprunteur.name, "Test Emprunteur")
        self.assertFalse(emprunteur.bloque)

# Test pour la création d'un livre
class TestCreateLivre(TestCase):
    def setUp(self):
        Livre.objects.create(name="Test Livre", auteur="Auteur Test", disponible=True)

    def test_livre_creation(self):
        livre = Livre.objects.get(name="Test Livre")
        self.assertEqual(livre.auteur, "Auteur Test")
        self.assertTrue(livre.disponible)

# Test pour la création d'un CD
class TestCreateCd(TestCase):
    def setUp(self):
        CD.objects.create(name="Test CD", artiste="Artiste Test", disponible=True)

    def test_cd_creation(self):
        cd = CD.objects.get(name="Test CD")
        self.assertEqual(cd.artiste, "Artiste Test")
        self.assertTrue(cd.disponible)

# Test pour la création d'un CD
class TestCreateDvd(TestCase):
    def setUp(self):
        DVD.objects.create(name="Test DVD", realisateur="Realisateur Test", disponible=True)

    def test_dvd_creation(self):
        dvd = DVD.objects.get(name="Test DVD")
        self.assertEqual(dvd.realisateur, "Realisateur Test")
        self.assertTrue(dvd.disponible)

# Test pour la création d'un Jeu de plateau
class TestCreateJeu(TestCase):
    def setUp(self):
        JeuDePlateau.objects.create(name="Test Jeu", createur="Createur Test")

    def test_jeu_creation(self):
        jeu = JeuDePlateau.objects.get(name="Test Jeu")
        self.assertEqual(jeu.createur, "Createur Test")

# Test pour vérifier la limite de 3 emprunts par emprunteur
class TestLimiteEmprunt(TestCase):
    def setUp(self):
        self.emprunteur = Emprunteur.objects.create(name="John Doe")
        self.livre1 = Livre.objects.create(name="Livre 1", disponible=True)
        self.livre2 = Livre.objects.create(name="Livre 2", disponible=True)
        self.livre3 = Livre.objects.create(name="Livre 3", disponible=True)

    def test_emprunteur_bloque_apres_trois_emprunts(self):
        # Crée les trois emprunts pour l'emprunteur
        Emprunteur.objects.create(emprunteur=self.emprunteur, livre=self.livre1, date_emprunt=timezone.now())
        Emprunteur.objects.create(emprunteur=self.emprunteur, livre=self.livre2, date_emprunt=timezone.now())
        Emprunteur.objects.create(emprunteur=self.emprunteur, livre=self.livre3, date_emprunt=timezone.now())

        self.emprunteur.check_bloque()

        self.assertTrue(self.emprunteur.bloque, "L'emprunteur est bloqué après 3 emprunts.")


class TestBloquageEmpruntSeptJours(TestCase):
    def setUp(self):
        self.emprunteur = Emprunteur.objects.create(name="Jane Doe")
        self.livre = Livre.objects.create(name="Livre Test", disponible=True)

    def test_emprunteur_bloque_emprunt_7_jours(self):
        emprunt = Emprunteur.objects.create(
            emprunteur=self.emprunteur,
            livre=self.livre,
            date_emprunt=timezone.now() - timedelta(days=8)
        )

        self.emprunteur.check_bloque()


        self.emprunteur.refresh_from_db()

        self.assertTrue(self.emprunteur.bloque,
                        "L'emprunteur est bloqué après un emprunt de plus de 7 jours.")