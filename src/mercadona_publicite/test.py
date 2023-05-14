
import datetime
from django.test import TestCase
from products.models import Categories, Produits, Promotions

class ProductTestCase(TestCase):
    def test_create_product(self):
        nbr_produits_before_add = Produits.objects.count()
        cat = Categories(libelle="testcat")
        cat.save()
        p = Produits(
            libelle="test",
            description="test",
            categorie = cat,
            images="test.jpg"
        )
        p.save()

        nbr_produits_after_add = Produits.objects.count()

        self.assertTrue(nbr_produits_after_add == nbr_produits_before_add + 1)

    def test_add_promotions(self):
        cat = Categories(libelle="testcat")
        cat.save()
        p = Produits(
            libelle="test",
            description="test",
            categorie = cat,
            images="test.jpg"
        )

        p.save()

        current_date = datetime.date.today()
        future_date = current_date + datetime.timedelta(days=15)

        promo = Promotions(
            datedebut=current_date,
            datefin=future_date,
            pourcentage = 10
        )

        promo.save()

        p.promotions = promo
        p.save()
        
        self.assertTrue(p.id == promo.id)

    def test_delete_product(self):
        nbr_produits_before_add = Produits.objects.count()
        cat = Categories(libelle="testcat")
        cat.save()
        p = Produits(
            libelle="test",
            description="test",
            categorie = cat,
            images="test.jpg"
        )
        p.save()

        p.delete()

        nbr_produits_after_add = Produits.objects.count()

        self.assertTrue(nbr_produits_after_add == nbr_produits_before_add)    

    def test_create_categorie(self):
        nbr_cat_after_add = Categories.objects.count()
        cat = Categories(libelle="testcat")
        cat.save()
        nbr_cat_before_add = Categories.objects.count()

        self.assertTrue(nbr_cat_before_add == nbr_cat_after_add + 1)

