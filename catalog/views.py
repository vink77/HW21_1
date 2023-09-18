from django.shortcuts import render
from django.urls import reverse_lazy


from catalog.models import Category, Product
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


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
    model = Product, Category
    fields = ('product_name', 'product_description', 'category', 'price', 'quantity_product', 'date_create','date_last_change')
    success_url = reverse_lazy('catalog:create')

class ProductUpdateView(UpdateView):
    model = Product, Category
    fields = ('product_name', 'product_description', 'category', 'price', 'quantity_product', 'date_create','date_last_change')
    success_url = reverse_lazy('catalog:update')

class ProductListView(ListView):
    model = Product
    success_url = reverse_lazy('catalog:detail')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count +=1
        self.object.save()
        return self.object



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')