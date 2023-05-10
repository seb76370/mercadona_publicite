from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import UsersAccount
@csrf_exempt
def sign_in(request):
    print("HH"*10)
    print("#"*10)
    if request.method == ("POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if user := authenticate(username=username, password=password):

            userConnected = User.objects.get(username = user)
            userAccount = UsersAccount.objects.get(account_id=userConnected.id)
            if userAccount.is_product_admin:
                login(request,user)
            
    return redirect('index')
