from django.shortcuts import render

def chefs_view(request):
    return render(request, "food/chefs.html")

def menu_view(request):
    return render(request, "food/food_menu.html")