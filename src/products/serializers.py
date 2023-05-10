from rest_framework import serializers

from .models import Categories, Produits, Promotions

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Produits
        fields = ['id','libelle','description','prix','images','categorie','promotions']
        read_only_fields = ['id','libelle','description','prix','images','categorie','promotions']        

class CategorieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','libelle']
        read_only_fields = ['id','libelle']        

class PromotionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields = ['id','datedebut','datefin','pourcentage']
        read_only_fields = ['id','datedebut','datefin','pourcentage']  