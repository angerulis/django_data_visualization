# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm
from django.contrib.auth.models import User


class Analyse(models.Model):
    indicateur = models.OneToOneField('Indicateur', models.DO_NOTHING, primary_key=True)
    axe = models.ForeignKey('Axe', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ANALYSE'
        unique_together = (('indicateur', 'axe'),)


class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TABLE'


class Agreger(models.Model):
    indicateur = models.OneToOneField('Indicateur', models.DO_NOTHING)
    periode = models.ForeignKey('Periode', models.DO_NOTHING)
    agregat_id = models.AutoField(primary_key=True)
    valeur = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agreger'
        unique_together = (('indicateur', 'periode'),)


class Assignation(models.Model):
    utilisateur = models.OneToOneField('Utilisateur', models.DO_NOTHING)
    ecran = models.ForeignKey('Ecran', models.DO_NOTHING)
    assignation_id = models.AutoField(primary_key=True)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    actif = models.BooleanField(blank=True, null=True)

    # inactif = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignation'
        unique_together = (('utilisateur', 'ecran'),)


class Axe(models.Model):
    axe_id = models.AutoField(primary_key=True)
    table = models.ForeignKey(Table, models.DO_NOTHING)
    type_axe = models.ForeignKey('TypeAxe', models.DO_NOTHING)
    axe_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'axe'

    def __str__(self):
        return self.axe_libelle


class Bloc(models.Model):
    bloc_id = models.AutoField(primary_key=True)
    bloc_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bloc'

    def __str__(self):
        return self.bloc_libelle


class BlocEcran(models.Model):
    ecran = models.ForeignKey('Ecran', models.DO_NOTHING)
    bloc = models.OneToOneField(Bloc, models.DO_NOTHING)
    position_id = models.AutoField(primary_key=True)
    x = models.CharField(max_length=100, blank=True, null=True)
    y = models.CharField(max_length=100, blank=True, null=True)
    h = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bloc_ecran'
        unique_together = (('ecran', 'bloc'),)

    def __str__(self):
        return self.y + '-' + self.ecran.ecran_libelle + '-' + self.bloc.bloc_libelle


class Ecran(models.Model):
    ecran_id = models.AutoField(primary_key=True)
    modele = models.ForeignKey('Modele', models.DO_NOTHING)
    ecran_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecran'

    def __str__(self):
        return self.ecran_libelle


class Indicateur(models.Model):
    indicateur_id = models.AutoField(primary_key=True)
    item = models.ForeignKey('Item', models.DO_NOTHING)
    periodicite = models.ForeignKey('Periodicite', models.DO_NOTHING)
    type_indicateur = models.ForeignKey('TypeIndicateur', models.DO_NOTHING)
    indicateur_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indicateur'


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    type_item = models.ForeignKey('TypeItem', models.DO_NOTHING)
    item_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item'

    def __str__(self):
        return self.item_libelle


class ItemBloc(models.Model):
    item = models.OneToOneField(Item, models.DO_NOTHING)
    bloc = models.ForeignKey(Bloc, models.DO_NOTHING)
    position_id = models.AutoField(primary_key=True)
    x = models.CharField(max_length=100, blank=True, null=True)
    y = models.CharField(max_length=100, blank=True, null=True)
    h = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_bloc'
        unique_together = (('item', 'bloc'),)

    def __str__(self):
        return self.x + '-' + self.item.item_libelle + '-' + self.bloc.bloc_libelle


class Modele(models.Model):
    modele_id = models.AutoField(primary_key=True)
    modele_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modele'

    def __str__(self):
        return self.modele_libelle


class Periode(models.Model):
    periode_id = models.AutoField(primary_key=True)
    periodicite = models.ForeignKey('Periodicite', models.DO_NOTHING)
    periode_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periode'

    def __str__(self):
        return self.periode_libelle


class Periodicite(models.Model):
    periodicite_id = models.AutoField(primary_key=True)
    periodicite_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'periodicite'

    def __str__(self):
        return self.periodicite_libelle


class TypeAxe(models.Model):
    type_axe_id = models.AutoField(primary_key=True)
    type_axe_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_axe'

    def __str__(self):
        return self.type_axe_libelle


class TypeIndicateur(models.Model):
    type_indicateur_id = models.AutoField(primary_key=True)
    type_indicateur_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_indicateur'

    def __str__(self):
        return self.type_indicateur_libelle


class TypeItem(models.Model):
    type_item_id = models.AutoField(primary_key=True)
    type_item_libelle = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_item'

    def __str__(self):
        return self.type_item_libelle


class Utilisateur(models.Model):
    utilisateur = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE, primary_key=True)
    utilisateur_nom = models.CharField(max_length=30, verbose_name='Nom', blank=True, null=True)
    utilisateur_prenom = models.CharField(max_length=30, verbose_name='Prénom', blank=True, null=True)
    utilisateur_contact = models.CharField(max_length=20, verbose_name='Contact', blank=True, null=True)
    utilisateur_email = models.CharField(max_length=30, verbose_name='Email', blank=True, null=True)
    utilisateur_fonction = models.CharField(max_length=30, verbose_name='Fonction', blank=True, null=True)

    class Meta:
        verbose_name = "Profile utilisateur"
        managed = False
        db_table = 'utilisateur'

    def __str__(self):
        return self.utilisateur_nom + ' ' + self.utilisateur_prenom
