from django.shortcuts import render
from .models import Chef
from django.core.paginator import Paginator


def chefs_view(request,page=1):
    chefs=Chef.objects.filter(status=True)

    paginator = Paginator(chefs, 3)
    page_obj = paginator.get_page(page)
    return render(request, "food/chefs.html",{'page_obj':page_obj , 'chefs':page_obj })

def menu_view(request):
    return render(request, "food/food_menu.html")