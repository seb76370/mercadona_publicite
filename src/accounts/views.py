from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import UsersAccount
@csrf_exempt
def sign_in(request):
    if request.method == ("POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(username=username, password=password):
            login(request,user)
            userConnected = User.objects.get(username = user)
            userAccount = UsersAccount.objects.get(account_id=userConnected.id)
            return JsonResponse({"message":"success","is_product_admin":userAccount.is_product_admin})

        return JsonResponse({"message":"fail","error":"error d'authentification"})