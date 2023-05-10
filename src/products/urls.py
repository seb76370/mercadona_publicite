"""mercadona_publicite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from products.views import add_cat,add_product,delete_product,update_product,list_product
from products.views import list_categorie

urlpatterns = [
    path('add_categorie/', add_cat,name="add_cat"),
    path('add_product/', add_product,name="add_product"),
    path('list_product/<int:categorie_selected>', list_product,name="list_product"),
    path('list_product/', list_product,name="list_product"),
    path('update_product/<int:id>', update_product,name="update_product"),
    path('delete_product/<int:id>', delete_product,name="delete_product"),
    path('list_categorie/', list_categorie,name="list_cat"),
]
