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


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'conteхt')
    success_url = reverse_lazy('blog/blog_list.html')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'conteхt')
    success_url = reverse_lazy('blog/blog_list.html')
    context_object_name = 'objects'


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'objects'

class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    context_object_name = 'object'
    success_url = reverse_lazy('blog/blog_list.html')


    def get_object(self, queryset=None):
            self.object = super().get_object(queryset)
            self.object.view_count +=1
            self.object.save()
            return self.object



class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')
    context_object_name = 'objects'
