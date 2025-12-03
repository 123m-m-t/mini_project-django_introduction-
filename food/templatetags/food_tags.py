from django import template
from food.models import Category, Menu

register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_menu_by_category(category):
    return Menu.objects.filter(category=category)

