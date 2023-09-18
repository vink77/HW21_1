from django.shortcuts import render
from django.urls import reverse_lazy


from catalog.models import Category, Product
from django.views.generic import CreateView, ListView, DetailView, UpdateView


# Create your views here.

#def index(request):
#    product_list = Product.objects.all()
#    context = {
#        'objects_list': product_list
#    }
#    return render(request, 'catalog/index.html', context=context)


def contacts(request):
    return render(request,'catalog/contacts.html')

def info1(request):
    return render(request,'catalog/info1.html')

class ProductCreateView(CreateView):
    model = Product
    fields = ('product_name', 'product_description', 'price', 'quantity_product', 'date_create','date_last_change')
    success_url = reverse_lazy('catalog:create_product')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_name', 'product_description', 'price', 'quantity_product', 'date_create','date_last_change')
    success_url = reverse_lazy('catalog:create_product')

class ProductListView(ListView):
    model = Product
    success_url = reverse_lazy('catalog:product_detail')

class ProductDetailView(DetailView):
    model = Product
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count +=1
        self.object.save()
        return self.object