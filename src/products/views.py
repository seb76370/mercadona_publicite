from datetime import date
from django import forms
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from rest_framework.response import Response

from .serializers import  CategorieSerializers, ProductsSerializers, PromotionsSerializers
from .models import Categories, Promotions
from .forms import CategoriesForm,  ProductAddForm, ProduitForm
from .models import Produits

from pprint import pprint


def add_cat(request):

    if request.method != "POST":
     return HttpResponse("Erreur de requete")
    form = CategoriesForm(request.POST)

    if form.is_valid():
     print('################')
     cat = form.save()
     print("newcat",cat.id) 
    else:
     errors = form.errors.as_data() 
     print(errors)

    try:
     return redirect(request.META.get('HTTP_REFERER'))
    except:
     # version postman tets api
     return JsonResponse({"status":"sucess","catID":cat.id})    

# sert a l'ajout et la mise an jour
def add_product(request):

    if request.method != "POST":
     return redirect('pageproduct')
    
    product_id = request.POST.get('product_id', 0)

    if str(product_id) != "0":   

     ProduitToupdate = Produits.objects.get(pk=product_id)
     form = ProductAddForm(request.POST, request.FILES,instance=ProduitToupdate)
    else:
     form = ProductAddForm(request.POST, request.FILES)
    if form.is_valid():
     # on ajoute la promo si necessaire
     if request.POST.get('promo', 'no') == 'yes':
          promo = Promotions(
          datedebut=request.POST.get('datedebut'),
          datefin=request.POST.get('datefin'),
          pourcentage=request.POST.get('pourcentage')
          )
          promo.save()
     
     # Sauvegarde Produit
     product = form.save()

     # on ajoute la promotion precedement créer
     if request.POST.get('promo', 'no') == 'yes':
          product.promotions = promo
          product.save()
     else:
          old_promo = product.promotions
          product.promotions = None
          product.save()
          # if old_promo:
          #     old_promo.delete()

    else:
     errors = form.errors.as_data() 
     return HttpResponse(f"Formulaire Invalide {errors}")

    if request.POST.get('test', "no") == "yes":
     return JsonResponse({"status":"sucess","id":product.id}) 
     
    return redirect('pageproduct')


def delete_product(request,id):
     product = Produits.objects.filter(pk=id)
     for p in product:
          promo = p.promotions
          if promo:
               promo.delete()

     product.delete()
     if request.GET.get('test','no') == "yes":
          return JsonResponse({"status":"sucess"})
      
     return redirect('index')


def update_product(request,id):
     product = Produits.objects.get(pk=id)
     ProduitPromo = {
     'promo':False,
     'datedebut':"",
     'datefin':"",
     'pourcentage':"",
     }

     print("product.promotions",product.promotions)

     if product.promotions:
         promo = Promotions.objects.get(pk=product.promotions.id)
         ProduitPromo = {
          'promo':True,
          'datedebut':promo.datedebut,
          'datefin':promo.datefin,
          'pourcentage':promo.pourcentage,
          }
     print("promotionssss")
     print(ProduitPromo)
     form = ProductAddForm(instance = product)
     context ={
          'forms':form,
          'promo':ProduitPromo,
          'id':id
     }
     return render(request, "mercadona_publicite/pageproduct.html",context)


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
     form = ProductAddForm()
     context ={
          'forms':form,
          'id':0
     }
     return render(request, "mercadona_publicite/pageproduct.html",context)

