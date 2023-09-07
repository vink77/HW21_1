from django.urls import path

from catalog.views import index, info

urlpatterns = [
    path('', index),
    path('info1/', info),

]