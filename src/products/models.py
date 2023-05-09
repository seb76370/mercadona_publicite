from django.db import models

class Categories(models.Model):
    Libelle = models.CharField(max_length=50)

class Promotions(models.Model):
    datedebut = models.DateField()
    datefin = models.DateField()
    pourcentage = models.IntegerField(default=0)

class Produits(models.Model):
    promotions = models.ForeignKey(Promotions, on_delete=models.CASCADE, related_name='Produits_Promotions',null = False, default =None)
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='Produits_Categories',null = False, default =None)
    libelle = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    prix = models.FloatField(default=0.0)
    images = models.FileField(upload_to='uploads/%Y/%m/%d/')