from .models import Produits
from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from products.views import generate_pdf
from .models import Produits, Tests

# Register your models here.

class ProduitAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans l'interface admin
    list_display = ['afficher_image','libelle', 'description', 'prix','promotions_pourcentage','promotions_datedebut','promotions_datefin']

    def afficher_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', "https://dev-passion76.fr/mercadona_publicite/src/" + obj.images.url) if obj.images else None
    afficher_image.short_description = 'Image'

    def promotions_pourcentage(self, obj):
        return obj.promotions.pourcentage if obj.promotions else None
    promotions_pourcentage.short_description = 'Promotion - Pourcentage'

    def promotions_datedebut(self, obj):
        return obj.promotions.datedebut if obj.promotions else None
    promotions_datedebut.short_description = 'Promotion - Date de fin'

    def promotions_datefin(self, obj):
        return obj.promotions.datefin if obj.promotions else None
    promotions_datefin.short_description = 'Promotion - Date de début'

    def download_pdf(self, request, queryset):
        # Créer une réponse HTTP avec le contenu PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="produits.pdf"'

        # Générer le contenu PDF en fusionnant les produits sélectionnés
        pdf_data = b''
        productsInPromotions = Produits.objects.filter(promotions__isnull=False)
        print(productsInPromotions)
        for produit in productsInPromotions:
            pdf_data += generate_pdf(produit)

        response.write(pdf_data)
        return response

    # Configuration du bouton personnalisé
    download_pdf.short_description = "Télécharger les produits sélectionnés en PDF"


    actions = ['download_pdf']


# admin.site.register(Produits)
admin.site.register(Tests)
admin.site.register(Produits, ProduitAdmin)