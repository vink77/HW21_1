from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contacts, info1

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contact'),
    path('info1/', info1, name='info1'),

]