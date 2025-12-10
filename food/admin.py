from django.contrib import admin
from .models import Menu,Category,Chef,Reservation
from django.utils.html import format_html
from grappelli.forms import GrappelliSortableHiddenMixin
from .forms import ReservationAdminForm


# Register your models here.

class MenuAdmin(admin.ModelAdmin):

    empty_value_display = '-empty-'

    list_display = [
        'image_tag',
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

    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": ("name", "price", "status")
        }),
        ("دسته‌بندی‌ها", {
            "fields": ("category",),
        }),
        ("توضیحات", {
            "fields": ("description", "image"),
            "classes": ("grp-collapse",),
        }),
    )

    autocomplete_fields = ["category"]

    change_list_template = "admin/change_list_filter_sidebar.html"

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:50px; height:50px; border-radius:4px;" />', obj.image.url)
        return "-"

    image_tag.short_description = "picture"



class ChefAdmin(admin.ModelAdmin):
    fieldsets = (
        ("اطلاعات فردی", {
            "fields": ("name", "title", "status")
        }),
        ("تصویر", {
            "fields": ("image",),
            "classes": ("grp-collapse",),
        }),
    )
    list_filter = ["status"]

    empty_value_display = '-empty-'

    list_display = [
        'name',
        'title',
        'status',
    ]

class ReservationAdmin(admin.ModelAdmin):

    form = ReservationAdminForm

    fieldsets = (
        ("اطلاعات رزروکننده", {
            "fields": ("name", "email", "phone")
        }),
        ("جزئیات رزرو", {
            "fields": ("persons", "date", "time_slot"),
        }),
        ("توضیحات", {
            "fields": ("note",),
            "classes": ("grp-collapse",),
        }),
    )
    readonly_fields = ["persons"]

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
    list_filter = ["date", "persons"]

    search_fields = ["name", "email", "phone"]


class CategoryAdmin(GrappelliSortableHiddenMixin,admin.ModelAdmin):


    search_fields = ["name"]

    list_display = ["name"]



admin.site.register(Menu, MenuAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Category,CategoryAdmin)