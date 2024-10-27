from django.contrib import admin
from .models import Livre, CD, DVD, JeuDePlateau, Emprunteur

admin.site.register(Livre)
admin.site.register(CD)
admin.site.register(DVD)
admin.site.register(JeuDePlateau)
admin.site.register(Emprunteur)