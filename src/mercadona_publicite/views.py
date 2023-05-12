import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from products.forms import CategoriesForm
from products.models import Categories, Produits, Promotions
from products.serializers import CategorieSerializers, ProductsSerializers, PromotionsSerializers
from products.views import list_product
from pprint import pprint
# Create your views here.

def index(request):
    ListCats=[]
    cats = Categories.objects.all()
    ListCats.append({"id":0,"libelle":"tous"})
    for cat in cats:
        ListCats.append({"id":cat.id,"libelle":cat.libelle})

    # print(ListCats)
    products = Produits.objects.all()
    dateday = datetime.date.today()
    for p in products:

        if p.promotions:
            print(p.promotions.datedebut,dateday,p.promotions.datefin)
            if p.promotions.datedebut < dateday or  dateday > p.promotions.datefin:
                print("promotions hors date")
                old_promo = p.promotions
                p.promotions = None
                p.save()
                if old_promo:
                    old_promo.delete()

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
            s['promotions']["newprix"] = s['prix'] - (s['prix']*s['promotions']['pourcentage'])/100
    # ,"ListCats":ListCats}
    return render(request, "mercadona_publicite/index.html", context ={"cards":list(serializer.data),"base_url":"https://dev-passion76.fr/","ListCats":ListCats})
                                                                       
