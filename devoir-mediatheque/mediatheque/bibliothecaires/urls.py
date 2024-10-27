from django.urls import path
from . import views

urlpatterns = [
    path('liste_medias/', views.liste_medias, name='liste_medias'),
    path('ajouter_media/', views.ajouter_media, name='ajouter_media'),
    path('creer_membre/', views.creer_membre, name='creer_membre'),
    path('liste_membres/', views.liste_membres, name='liste_membres'),
    path('mettre_a_jour_membre/<int:emprunteur_id>/', views.mettre_a_jour_membre, name='mettre_a_jour_membre'),
    path('creer_emprunt/', views.creer_emprunt, name='creer_emprunt'),
    path('rentrer_emprunt/', views.rentrer_emprunt, name='rentrer_emprunt'),
]
