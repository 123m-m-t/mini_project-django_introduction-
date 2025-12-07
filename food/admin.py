from django.contrib import admin
from .models import Menu,Category,Chef,Reservation
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

class ChefAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [
        'name',
        'title',
        'status',
    ]

class ReservationAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = [
        'name',
        'email',
        'phone',
        'persons',
        'date',
        'time_slot',
        'note',
    ]

admin.site.register(Menu, MenuAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Category)