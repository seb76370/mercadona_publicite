from django.db import models
from django.contrib.auth.models import AbstractUser

# nouvelle class utlisateur on y ajoute le champ admin_produit
class Accounts(AbstractUser):
    is_admin_product = models.BooleanField(default=False)
