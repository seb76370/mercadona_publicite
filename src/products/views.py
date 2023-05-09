from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from products.forms import CategoriesForm

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
