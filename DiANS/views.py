from django.db.models import Q
from django.shortcuts import render, redirect
from itertools import chain


# Create your views here.
from django.views.generic import TemplateView, ListView

from DiANS.models import *


# def index(request):
#     queryset = Product.objects.all()
#     context = {"products": queryset}
#     return render(request, "index.html", context=context)

# class HomePageView(TemplateView):
#     template_name = 'index.html'

class SearchResultsView(ListView):
    model = Product
    template_name = 'index.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        #shop_Queryset = ShopProduct.objects.all()
        #object_list = ShopProduct.objects.all()
        if query:
            object_list = ShopProduct.objects.filter(
            Q(product__product_Name__icontains=query) | Q(shop__shop_Name__icontains=query)
        ).order_by('product__product_Price')
        else:
            object_list = ""


        return object_list