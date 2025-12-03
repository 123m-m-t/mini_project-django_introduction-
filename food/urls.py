from django.urls import path, include
from .views import chefs_view, menu_view

app_name = 'food'

urlpatterns = [
    path('chefs/', chefs_view, name='chefs'),
    path('menu/', menu_view, name='menu'),
]