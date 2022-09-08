from django.db import models


# Create your models here.


class Education(models.Model):
    code = models.CharField(max_length=255, null=False, primary_key=True)
    rubrique = models.CharField(max_length=255, null=False)
    _2010 = models.IntegerField()
    _2011 = models.IntegerField()
    _2012 = models.IntegerField()
    _2013 = models.IntegerField()
    _2014 = models.IntegerField()
    _2015 = models.IntegerField()
    _2016 = models.IntegerField()
    _2017 = models.IntegerField()
    _2018 = models.IntegerField()
    _2019 = models.IntegerField()
    _2020 = models.IntegerField()
    _2021 = models.IntegerField()
    _2022 = models.IntegerField()
    _2023 = models.IntegerField()
    _2024 = models.IntegerField()
    _2025 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bd_database_presidence"."_education'

    def __str__(self):
        return self.code



class Transport(models.Model):
    filename = models.CharField(max_length=255, null=False)
    code = models.CharField(primary_key=True, max_length=255, null=False)
    rubrique = models.CharField(max_length=255, null=False)
    annee = models.IntegerField()
    janvier = models.IntegerField()
    fevrier = models.IntegerField()
    mars = models.IntegerField()
    avril = models.IntegerField()
    mai = models.IntegerField()
    juin = models.IntegerField()
    juillet = models.IntegerField()
    aout = models.IntegerField()
    septembre = models.IntegerField()
    octobre = models.IntegerField()
    novembre = models.IntegerField()
    decembre = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bd_database_presidence"."transport'

    def __str__(self):
        return self.code


class Trytable(models.Model):
    name = models.CharField(max_length=255, null=False)
    number = models.IntegerField(primary_key=True)

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return str(self.name)

    class Meta:
        managed = False
        db_table = 'trytable'
