from django.db import models
from django.utils import timezone
from datetime import timedelta


# Classe Emprunteur
class Emprunteur(models.Model):
    name = models.CharField(max_length=1000)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Classe Media
class Media(models.Model):
    name = models.CharField(max_length=1000)
    disponible = models.BooleanField(default=True)
    dateEmprunt = models.DateTimeField(null=True, blank=True)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

    def emprunter(self, emprunteur):
        if self.disponible and not emprunteur.bloque and emprunteur.nb_emprunts() < 3:
            self.disponible = False
            self.dateEmprunt = timezone.now()
            self.emprunteur = emprunteur
            self.save()
        else:
            raise ValueError("Impossible d'emprunter ce média.")

    def retourner(self):
        self.disponible = True
        self.dateEmprunt = None
        self.emprunteur = None
        self.save()

    def est_en_retard(self):
        if self.dateEmprunt:
            return timezone.now() > self.dateEmprunt + timedelta(days=7)
        return False


# Types de médias (Livre, DVD, CD)
class Livre(Media):
    objects = None
    auteur = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} - {self.auteur}"

class DVD(Media):
    objects = None
    realisateur = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} - {self.realisateur}"

class CD(Media):
    objects = None
    artiste = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} - {self.artiste}"


# Classe JeuDePlateau
class JeuDePlateau(models.Model):
    objects = None
    name = models.CharField(max_length=1000)
    editeur = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.name} - {self.editeur}"


def nb_emprunts(self):
    emprunts_livres = Livre.objects.filter(emprunteur=self, disponible=False).count()
    emprunts_dvds = DVD.objects.filter(emprunteur=self, disponible=False).count()
    emprunts_cds = CD.objects.filter(emprunteur=self, disponible=False).count()
    return emprunts_livres + emprunts_dvds + emprunts_cds
Emprunteur.add_to_class('nb_emprunts', nb_emprunts)
