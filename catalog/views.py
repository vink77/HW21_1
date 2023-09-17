from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Category, Product
from django.views.generic import CreateView, ListView


# Create your views here.

def index(request):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list
    }
    return render(request, 'catalog/index.html', context=context)


def contacts(request):
    return render(request,'catalog/contacts.html')

def info1(request):
    return render(request,'catalog/info1.html')

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'product_description', 'price','date_create','date_last_change')
    success_url = reverse_lazy('catalog:create_product')

class ProductListView(ListView):
    model = Product