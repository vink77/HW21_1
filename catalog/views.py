from django.shortcuts import render
from catalog.models import Category, Product



# Create your views here.

def index(request):
    products_list = Product.objects.all()
    context = {
        'objects_list': products_list
    }
    return render(request, 'catalog/index.html', context=context)


def info(request):
    return render(request,'catalog/info1.html')