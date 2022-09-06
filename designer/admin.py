from django.contrib import admin

from .models import Utilisateur, Assignation, Modele, Ecran, BlocEcran, Bloc, ItemBloc, Item, TypeItem

admin.site.register([ Utilisateur, Assignation, Modele, Ecran, BlocEcran, Bloc, ItemBloc, Item, TypeItem])