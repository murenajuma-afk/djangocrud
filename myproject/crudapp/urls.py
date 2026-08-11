from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('products/', views.admin, name='products'),
    path('add_product/', views.add_product, name='add_product'),
]