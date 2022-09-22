from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Utilisateur, Assignation, Modele, Ecran, BlocEcran, Bloc, ItemBloc, Item, TypeItem

admin.site.register([Utilisateur, Assignation, Modele, Ecran, BlocEcran, Bloc, ItemBloc, Item, TypeItem])


# Define an inline admin descriptor for Utilisateur model
# which acts a bit like a singleton
class UtilisateurInline(admin.StackedInline):
    model = Utilisateur
    can_delete = False
    verbose_name_plural = 'utilisateurs'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UtilisateurInline,)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
