from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy


from blog.models import Blog
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


# Create your views here.

#def index(request):
#    product_list = Product.objects.all()
#    context = {
#        'objects_list': product_list
#    }
#    return render(request, 'catalog/index.html', context=context)


def contacts(request):
    return render(request,'Blog/contacts.html')

def info1(request):

    return render(request,'Blog/info1.html')

class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'conteхt', 'date_create', 'is_published', 'date_create','date_last_change')
    success_url = reverse_lazy('Blog:create')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('product_name', 'product_description', 'category', 'price', 'quantity_product', 'date_create','date_last_change')
    success_url = reverse_lazy('Blog:update')

class BlogListView(ListView):
    model = Blog
    success_url = reverse_lazy('Blog:list')
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'


def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count +=1
        self.object.save()
        return self.object



class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('Blog:list')