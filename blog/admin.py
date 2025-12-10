from django.contrib import admin
from .models import Post, Category, Comment
from django.utils.html import format_html
from .forms import PostAdminForm



class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ("نام دسته‌بندی", {
            "fields": ("name",)
        }),
        ("اطلاعات سیستم", {
            "fields": ("slug",),
            "classes": ("grp-collapse",),
        }),
    )

    readonly_fields = ("slug",)
    search_fields = ["name"]


class PostAdmin(admin.ModelAdmin):

    fieldsets = (
        ("اطلاعات اصلی", {
            "fields": ("title", "author", "category", "tags")
        }),
        ("محتوا", {
            "fields": ("content",),
        }),
        ("نمایش", {
            "fields": ("image_tag" , "counted_views"),
            "classes": ("grp-collapse",),
        }),
        ("تنظیمات انتشار", {
            "fields": ("status", "login_require", "published_date"),
            "classes": ("grp-collapse",),
        }),
        ("زمان‌ها", {
            "fields": ("created_date", "updated_date"),
            "classes": ("grp-collapse",),
        }),
    )

    readonly_fields = ("created_date", "image_tag","updated_date")

    autocomplete_fields = ['author', 'category']

    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = (
        'image_tag',
        'title',
        'author',
        'counted_views',
        'status',
        'login_require',
        'published_date',
        'created_date'
    )
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']

    change_list_template = "admin/change_list_filter_sidebar.html"

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width:80px; height:60px; border-radius:4px;" />', obj.image.url)
        return "-"

    image_tag.short_description = "picture"

    form = PostAdminForm


class CommentAdmin(admin.ModelAdmin):

    autocomplete_fields = ['post']

    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date', 'subject')
    list_filter = ['approved', 'created_date']
    list_editable = ['approved']
    search_fields = ['name', 'email', 'subject']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
