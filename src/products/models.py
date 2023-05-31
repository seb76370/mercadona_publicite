from django.db import models
from django.http import HttpResponse

class Categories(models.Model):
    libelle = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return str(self.libelle)

class Promotions(models.Model):
    datedebut = models.DateField()
    datefin = models.DateField()
    pourcentage = models.IntegerField(default=0)


class Produits(models.Model):
    promotions = models.ForeignKey(Promotions, on_delete=models.CASCADE, related_name='Produits_Promotions',null = True, default =None)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='Produits_Categories',null = True, default =None)
    libelle = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    prix = models.FloatField(default=0.0)
    images = models.FileField(upload_to='uploads/%Y/%m/%d/')

class Tests(models.Model):
    libelle = models.CharField(max_length=50)
    description = models.CharField(max_length=100,default="")
    result = models.BooleanField(default=False)

