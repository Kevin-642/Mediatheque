from django.urls import path
from . import views

urlpatterns = [
    path('liste_medias_emprunteurs/', views.liste_medias_emprunteurs, name='liste_medias_emprunteurs'),
]
