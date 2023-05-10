from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    cards = [

        {"libelle":"basket nike",
         "description":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum ab libero
                        rem. Vero facere facilis possimus autem id, illum reiciendis, perspiciatis
                        ullam itaque enim nobis sapiente corrupti, molestiae nulla non?""",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion":True},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},{"libelle":"basket nike",
         "description":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum ab libero
                        rem. Vero facere facilis possimus autem id, illum reiciendis, perspiciatis
                        ullam itaque enim nobis sapiente corrupti, molestiae nulla non?""",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion":True},
         {"libelle":"basket nike",
         "description":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum ab libero
                        rem. Vero facere facilis possimus autem id, illum reiciendis, perspiciatis
                        ullam itaque enim nobis sapiente corrupti, molestiae nulla non?""",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion":True}, {"libelle":"basket nike",
         "description":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum ab libero
                        rem. Vero facere facilis possimus autem id, illum reiciendis, perspiciatis
                        ullam itaque enim nobis sapiente corrupti, molestiae nulla non?""",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion":True},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},
        {"libelle":"basket adidas",
         "description":"basket toto",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion" :False},{"libelle":"basket nike",
         "description":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum ab libero
                        rem. Vero facere facilis possimus autem id, illum reiciendis, perspiciatis
                        ullam itaque enim nobis sapiente corrupti, molestiae nulla non?""",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion":True},
         {"libelle":"basket nike",
         "description":"""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum ab libero
                        rem. Vero facere facilis possimus autem id, illum reiciendis, perspiciatis
                        ullam itaque enim nobis sapiente corrupti, molestiae nulla non?""",
         "image":"https://assets.laboutiqueofficielle.com/w_450,q_auto,f_auto/media/products/2021/05/31/reebok_268771_FAB_GW8357_TPDT_20210615T073244_01.jpg",
         "promotion":True}]
    
    return render(request, "mercadona_publicite/index.html", context ={"cards":cards})
    