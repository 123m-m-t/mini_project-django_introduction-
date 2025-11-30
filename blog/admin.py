from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = (
        'title',
        'author',
        'counted_views',
        'status',
        'login_require',
        'published_date',
        'created_date'
    )
    list_filter = ('status', 'author')
    search_fields = ['title', 'content']   # CKEditor مشکلی ندارد


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
