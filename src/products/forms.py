
from django import forms
from .models import Categories, Produits

class CategoriesForm(forms.ModelForm):
    class Meta:     
        model = Categories
        fields = ('libelle',)

        def __str__(self):
            return self.libelle   


class ProduitForm(forms.ModelForm):
    class Meta:     
        model = Produits
        fields = ('libelle','description','prix','images','categorie')


class ProductAddForm(forms.ModelForm):
    class Meta: 
        model = Produits
        fields = "__all__"


        widgets={
            "libelle": forms.TextInput(),
            "description": forms.Textarea(
            attrs={
                'rows':"2", 
                'cols':"100"
            }
            ),
            "images": forms.ClearableFileInput(attrs={'multiple': False}),
             "categorie": forms.Select(), 
        }
    def __init__(self, *args, **kwargs):
        super(ProductAddForm, self).__init__(*args, **kwargs)
        self.fields['promotions'].required = False

    def clean(self):
        cleaned_data = super().clean()
        prix = cleaned_data.get('prix')

        if prix is not None and prix <= 0:
            self.add_error('prix', "Le prix doit être supérieur à zéro.")

        return cleaned_data