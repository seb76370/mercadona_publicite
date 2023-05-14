import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from products.models import Categories, Produits, Promotions, Tests
from products.serializers import CategorieSerializers, ProductsSerializers, PromotionsSerializers
from products.views import list_product
from pprint import pprint
from django.views.generic import TemplateView


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
           if p.promotions.datedebut < dateday or  dateday > p.promotions.datefin:
                old_promo = p.promotions
                p.promotions = None
                p.save()
                # if old_promo:
                #     old_promo.delete()

    serializer = ProductsSerializers(products, many=True)

    for s in serializer.data:
        if s['categorie']:
            cat = Categories.objects.get(pk=s['categorie'])
            serializerCat = CategorieSerializers(cat)
            s['categorie'] = serializerCat.data
        if s['promotions']:
            # print("promooo")
            promo = Promotions.objects.get(pk=s['promotions'])
            # print(promo.datedebut,dateday)
            # print(promo.datefin,dateday)
            if promo.datedebut <= dateday <= promo.datefin:
                serializerPromo = PromotionsSerializers(promo)
                s['promotions'] = serializerPromo.data
                s['promotions']["newprix"] = s['prix'] - (s['prix']*s['promotions']['pourcentage'])/100
            else:
                s['promotions'] = None
    return render(request, "mercadona_publicite/index.html", context ={"cards":list(serializer.data),"base_url":"https://dev-passion76.fr/mercadona_publicite/src/","ListCats":ListCats})
                                                                       
def tuto(request):
    return render(request, "mercadona_publicite/tuto.html")

def test(request):
    return render(request, "tests/test.html")

class EditorChartView(TemplateView):
    template_name = 'tests/test.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Tests.objects.all()
        return context

