from importlib._common import _

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Utilisateur, Assignation, Modele, Ecran, BlocEcran, Bloc, ItemBloc, Item, TypeItem

admin.site.register([Assignation, Modele, Ecran, BlocEcran, Bloc, ItemBloc, Item, TypeItem])


# Define an inline admin descriptor for Utilisateur model
# which acts a bit like a singleton
class UtilisateurInline(admin.StackedInline):
    model = Utilisateur
    can_delete = False
    verbose_name_plural = 'utilisateurs'


# Define a new User admin
class MyUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    inlines = (UtilisateurInline,)


class UserCred(admin.ModelAdmin):
    fields = ('', 'title', 'content')


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
