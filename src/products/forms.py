
from django import forms
from .models import Categories, Produits

class CategoriesForm(forms.ModelForm):
    class Meta:     
        model = Categories
        fields = ('libelle',)   


class ProduitForm(forms.ModelForm):
    class Meta:     
        model = Produits
        fields = ('libelle','description','prix','images','categorie')