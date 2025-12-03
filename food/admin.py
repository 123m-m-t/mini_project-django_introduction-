from django.contrib import admin
from .models import Menu,Category
# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [
        'name',
        'status',
        'price',
        'description',
    ]
    list_filter = [
        'status',
        'price',
        'category',
    ]
    search_fields = [
        'name',
    ]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Category)