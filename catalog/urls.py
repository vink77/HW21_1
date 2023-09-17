from django.urls import path
from django.contrib import admin
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, info1, ProductCreateView
from django.conf.urls.static import static
from django.conf import settings

app_name = CatalogConfig.name





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contact'),
    path('info1/', info1, name='info1'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)