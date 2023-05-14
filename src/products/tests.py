from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from products.models import Produits

class ProductTestCase(TestCase):

    def test_create_product(self):

        # nombre d'element dans notre BDD
        nbr_element_before_add = Produits.objects.count

        # Ajouter un element
        # image_path = './test.jpg'
        # with open(image_path, 'rb') as f:
        #     image_file = SimpleUploadedFile('test.jpg', f.read(), content_type='image/jpeg')

        # Création d'une instance de Produits avec l'image
        new_produit = Produits.objects.create(
            libelle='Nom du produit',
            description='Description du produit',
            prix=9.99,
            images=None
        )

        new_produit.save()

        # verifier que notre BDD est incrementer de 1

        nbr_element_after_add = Produits.objects.count

        self.assertTrue(nbr_element_after_add == nbr_element_before_add +  1)