from datetime import date
from django import forms
from django.http import FileResponse, HttpResponse, HttpResponseRedirect, JsonResponse
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

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph,Image as RLImage,PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

import io
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



def generate_pdf(request):
     buf = io.BytesIO()
     c = canvas.Canvas(buf,pagesize=letter)
     urlbase = "https://dev-passion76.fr/mercadona_publicite/src"
     url="https://camo.githubusercontent.com/290dfc007c9a10e82af412f0e2a1cd3ec8378d1e8adf1e4f868af367349bacd1/68747470733a2f2f74616c656e74706f72747567616c2e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032322f30312f6d65726361646f6e615f656d707265676f5f74726162616c686f5f6573746167696f5f63616e64696461747572615f6573706f6e74616e65615f74616c656e745f706f72747567616c5f6571756970615f62616e6e65722d373638783336382e6a706567"
     c.drawInlineImage(url, 0, 600, width=650,height=200)

     data = []
     data.append(["Libelle","Description","Prix en €","Date de début","Date de fin","Pourcentage","image"])
     for i, produit in enumerate(Produits.objects.filter(promotions__isnull=False), start=1):
        image = RLImage(urlbase+ produit.images.url, width=80, height=80)
        data.append([produit.libelle,produit.description,str(produit.prix) + "€",str(produit.promotions.datedebut),str(produit.promotions.datefin),str(produit.promotions.pourcentage) + "%",image])


     styles = getSampleStyleSheet()
     style = styles["BodyText"]
     # header = Paragraph("<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><bold><font size=18>Produit en Promotion</font></bold>", style)

     t = Table(data)
     t.setStyle(TableStyle([
          ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
          ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
          ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
          ('VALIGN', (0, 0), (-1, -1), 'MIDDLE') 
     ]))
     data_len = len(data)

     for each in range(data_len):
          if each % 2 == 0:
               bg_color = colors.whitesmoke
          else:
               bg_color = colors.lightgrey

          t.setStyle(TableStyle([('BACKGROUND', (0, each), (-1, each), bg_color)]))

     aW = 1340
     aH = 450

     w, h = t.wrap(aW, aH)
     t.drawOn(c, 10, aH-(len(data)-1)*100)

     c.save()
     buf.seek(0)
     return FileResponse(buf,as_attachment=True,filename="ProduitsPromotions.pdf")

