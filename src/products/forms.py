
from django import forms
from .models import Categories, Produits

class CategoriesForm(forms.ModelForm):
    class Meta:     
        model = Categories
        fields = ('Libelle',)        