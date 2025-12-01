from django.contrib import admin
from .models import Post, Category, Comment


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

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post','approved','created_date')
    list_filter = ('post','approved')
    search_fields = ['name','post']


admin.site.register(Comment,CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
