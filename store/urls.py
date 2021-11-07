from os import name
from django.urls import path
from django.conf.urls import url
from .import views
urlpatterns = [
    path('', views.Store, name='store'),
    path('category/<slug:category_slug>/', views.Store, name='product_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/', views.search, name='search'),
    
]