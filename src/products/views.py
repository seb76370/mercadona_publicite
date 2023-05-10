from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from rest_framework.response import Response

from .serializers import  CategorieSerializers, ProductsSerializers, PromotionsSerializers
from .models import Categories, Promotions
from .forms import CategoriesForm, ProduitForm
from .models import Produits

from pprint import pprint

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
          errors_text = str(errors['libelle'][0])
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
          # errors_text = str(errors['libelle'][0])
          return JsonResponse({"message":"fail","error":"error"})
    
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

@csrf_exempt
def update_product(request,id):
     if request.method != "POST":
          return HttpResponse("Erreur de requete")

     product = Produits.objects.get(pk=id)
   
     if not product:
        return JsonResponse({"message":"fail","error":"Produit inconnu"})
  
     form = ProduitForm(request.POST, request.FILES, instance=product)

     if form.is_valid():
          form.save() 
          return JsonResponse({"message":"success"})
     else:
          errors = form.errors.as_data()
          print(errors)
          return JsonResponse({"message":"fail","error":"eee"})

@csrf_exempt
def list_product(request,categorie_selected = None):
     if request.method != "GET":
          return HttpResponse("Erreur de requete")

     products = Produits.objects.all()

     if categorie_selected:
          products = products.filter(categorie = categorie_selected)

     serializer = ProductsSerializers(products, many=True)

     for s in serializer.data:
          if s['categorie']:
               cat = Categories.objects.get(pk=s['categorie'])
               serializerCat = CategorieSerializers(cat)
               s['categorie'] = serializerCat.data

          if s['promotions']:
               promo = Promotions.objects.get(pk=s['promotions'])
               serializerPromo = PromotionsSerializers(promo)
               s['promotions'] = serializerPromo.data
     return JsonResponse({"products":serializer.data})
  

def list_categorie(request):
     if request.method != "GET":
          return HttpResponse("Erreur de requete")

     categories = Categories.objects.all()
     serializer = CategorieSerializers(categories, many=True)
     return JsonResponse({"categorie":serializer.data})

def pageproduct(request):
     return render(request, "mercadona_publicite/pageproduct.html")