from django.contrib import admin
from .models import Newsletter, Contact


class NewsletterAdmin(admin.ModelAdmin):

    list_display = ["email", "created_date"]

    search_fields = ["email"]

    list_filter = ["created_date"]

    change_list_template = "admin/change_list_filter_sidebar.html"

    date_hierarchy = "created_date"


class ContactAdmin(admin.ModelAdmin):

    fieldsets = (
        ("اطلاعات کاربر", {
            "fields": ("name", "email"),
        }),
        ("پیام کاربر", {
            "fields": ("subject", "message"),
        }),
        ("زمان‌ها", {
            "fields": ("created_date", "updated_date"),
            "classes": ("grp-collapse",),
        }),
    )

    readonly_fields = ("created_date", "updated_date")

    list_display = [
        "name",
        "email",
        "subject",
        "created_date",
    ]

    search_fields = ["name", "email", "subject"]

    list_filter = ["created_date"]

    change_list_template = "admin/change_list_filter_sidebar.html"

    date_hierarchy = "created_date"



admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Contact, ContactAdmin)
