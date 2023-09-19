from django.urls import path
from blog.apps import BlogModelConfig
from django.conf import settings

from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView
from . import views

app_name = BlogModelConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('detail/<pk>/', BlogDetailView.as_view(), name='detail'),
    path('update/<pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<pk>/', BlogDeleteView.as_view(), name='delete'),

]