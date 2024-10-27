from django.shortcuts import render, get_object_or_404, redirect
from .models import Livre, DVD, CD, JeuDePlateau, Emprunteur


# index.html
def index(request):
    return render(request, 'bibliothecaires/index.html')


# liste_medias.html
def liste_medias(request):
    livres = Livre.objects.all()
    dvds = DVD.objects.all()
    cds = CD.objects.all()
    jeux = JeuDePlateau.objects.all()
    return render(request, 'bibliothecaires/liste_medias.html', {'livres': livres, 'dvds': dvds, 'cds': cds, 'jeux': jeux})


# ajouter_media.html
def ajouter_media(request):
    if request.method == 'POST':
        media_type = request.POST.get('media_type')

        if media_type == 'livre':
            auteur = request.POST.get('livre_auteur')
            name = request.POST.get('livre_name')
            if name and auteur:
                Livre.objects.create(name=name, auteur=auteur)
            else:
                return render(request, 'bibliothecaires/ajouter_media.html', {'error': 'Veuillez remplir tous les champs.'})

        elif media_type == 'dvd':
            realisateur = request.POST.get('dvd_realisateur')
            name = request.POST.get('dvd_name')
            if name and realisateur:
                DVD.objects.create(name=name, realisateur=realisateur)
            else:
                return render(request, 'bibliothecaires/ajouter_media.html', {'error': 'Veuillez remplir tous les champs.'})

        elif media_type == 'cd':
            artiste = request.POST.get('cd_artiste')
            name = request.POST.get('cd_name')
            if name and artiste:
                CD.objects.create(name=name, artiste=artiste)
            else:
                return render(request, 'bibliothecaires/ajouter_media.html', {'error': 'Veuillez remplir tous les champs.'})

        elif media_type == 'jeu':
            editeur = request.POST.get('jeu_editeur')
            name = request.POST.get('jeu_name')
            if name and editeur:
                JeuDePlateau.objects.create(name=name, editeur=editeur)
            else:
                return render(request, 'bibliothecaires/ajouter_media.html', {'error': 'Veuillez remplir tous les champs.'})

        return redirect('liste_medias')

    return render(request, 'bibliothecaires/ajouter_media.html')


# creer_membre.html
def creer_membre(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Emprunteur.objects.create(name=name)
        return redirect('liste_membres')

    return render(request, 'bibliothecaires/creer_membre.html')


# liste_membres.html
def liste_membres(request):
    emprunteurs = Emprunteur.objects.all()
    return render(request, 'bibliothecaires/liste_membres.html', {'emprunteurs': emprunteurs})


# mettre_a_jour_membres.html
def mettre_a_jour_membre(request, emprunteur_id):
    emprunteur = get_object_or_404(Emprunteur, id=emprunteur_id)

    if request.method == 'POST':
        emprunteur.name = request.POST.get('name')
        emprunteur.bloque = request.POST.get('bloque') == 'on'
        emprunteur.save()
        return redirect('liste_membres')

    return render(request, 'bibliothecaires/mettre_a_jour_membres.html', {'emprunteur': emprunteur})


# creer_emprunt.html
def creer_emprunt(request):
    livres = Livre.objects.filter(disponible=True)
    dvds = DVD.objects.filter(disponible=True)
    cds = CD.objects.filter(disponible=True)
    emprunteurs = Emprunteur.objects.filter(bloque=False)

    if request.method == 'POST':
        media_id = request.POST.get('media_id')
        emprunteur_id = request.POST.get('emprunteur_id')

        media = None
        try:
            media = Livre.objects.get(id=media_id)
        except Livre.DoesNotExist:
            try:
                media = DVD.objects.get(id=media_id)
            except DVD.DoesNotExist:
                media = CD.objects.get(id=media_id)

        emprunteur = get_object_or_404(Emprunteur, id=emprunteur_id)

        try:
            media.emprunter(emprunteur)
            return redirect('liste_medias')
        except ValueError as e:
            return render(request, 'bibliothecaires/erreur.html', {'message': str(e)})

    return render(request, 'bibliothecaires/creer_emprunt.html', {'livres': livres, 'dvds': dvds, 'cds': cds, 'emprunteurs': emprunteurs})


# rentrer_emprunt.html
def rentrer_emprunt(request):
    livres = Livre.objects.filter(disponible=False)
    dvds = DVD.objects.filter(disponible=False)
    cds = CD.objects.filter(disponible=False)

    if request.method == 'POST':
        media_id = request.POST.get('media_id')

        try:
            media = Livre.objects.get(id=media_id)
        except Livre.DoesNotExist:
            try:
                media = DVD.objects.get(id=media_id)
            except DVD.DoesNotExist:
                media = CD.objects.get(id=media_id)

        try:
            media.retourner()
            return redirect('liste_medias')
        except ValueError as e:
            return render(request, 'bibliothecaires/erreur.html', {'message': str(e)})

    return render(request, 'bibliothecaires/rentrer_emprunt.html', {'livres': livres, 'dvds': dvds, 'cds': cds})
