from django.db import models
from django.contrib.auth.models import User

# # nouvelle class utlisateur on y ajoute le champ admin_produit
class UsersAccount(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    is_product_admin = models.BooleanField(default=False)
