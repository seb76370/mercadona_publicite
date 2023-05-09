from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    print("*"*20)
    print("index")
    return HttpResponse("Welcome to Mercadona Publicity")