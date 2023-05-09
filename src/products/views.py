from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView

import products
from .models import Categories
from products.forms import CategoriesForm, ProduitForm
from .models import Produits

@csrf_exempt
def add_cat(request):
    if request.method != "POST":
         return HttpResponse("Erreur de requete")
    
    form = CategoriesForm(request.POST)
    if form.is_valid():
          form.save() 
          return JsonResponse({"message":"success"})
    else:
          errors = form.errors.as_data()
          errors_text = str(errors['Libelle'][0])
          return JsonResponse({"message":"fail","error":errors_text})
    
@csrf_exempt
def add_product(request):
    if request.method != "POST":
         return HttpResponse("Erreur de requete")
    
    form = ProduitForm(request.POST, request.FILES)
    if form.is_valid():
          form.save() 
          return JsonResponse({"message":"success"})
    else:
          errors = form.errors.as_data()
          print(errors)
          # errors_text = str(errors['Libelle'][0])
          return JsonResponse({"message":"fail","error":"eee"})
    
@csrf_exempt
def delete_product(request,id):
     if request.method != "DELETE":
          return HttpResponse("Erreur de requete")

     product = Produits.objects.filter(pk=id)
     for p in product:
          promo = p.promotions
          promo.delete()
     
     product.delete()

     return JsonResponse({"message":"success"})


class list_categorie(ListView):
     model = Categories
     context_object_name = 'list_cat'
     template_name = 'testlist.html'


