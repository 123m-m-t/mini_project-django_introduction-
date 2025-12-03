from django.urls import path, include
from .views import chefs_view, menu_view

app_name = 'food'

urlpatterns = [
    path('chefs/', chefs_view, name='chefs'),
    path('chefs/<int:page>', chefs_view, name='chefs_page'),
    path('menu/', menu_view, name='menu'),
]