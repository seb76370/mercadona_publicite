from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from .models import Categories
from products.forms import CategoriesForm, ProduitForm

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

class list_categorie(ListView):
     model = Categories
     context_object_name = 'list_cat'
     template_name = 'testlist.html'


