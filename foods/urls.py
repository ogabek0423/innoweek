from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('food/', views.food_list, name='food_list'),
    path('food/<int:food_id>/', views.food_detail, name='food_detail'),
    path('products/', ProductListView.as_view(), name='products'),
    path('salats/', views.salat_list, name='salat_list'),
    path('salats/<int:food_id>/', views.salat_detail, name='salat_detail'),
    path('tushlik/', views.tush_list, name='tush_list'),
    path('tushlik/<int:food_id>', views.tush_detail, name='tush_detail'),
    path('non/', views.non_list, name='non_list'),
    path('non/<int:food_id>', views.non_detail, name='non_detail'),
    path('drinks/', views.drinks, name='drink_list')
]
