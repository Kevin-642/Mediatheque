from django.shortcuts import render
from bibliothecaires.models import Livre, DVD, CD, JeuDePlateau

def liste_medias_emprunteurs(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'membres/liste_medias_emprunteurs.html', {'livres': livres, 'dvds': dvds, 'cds': cds, 'jeux': jeux})
