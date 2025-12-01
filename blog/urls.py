from django.urls import path, include
from .views import blog_view, blog_single, blog_search

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('page/<int:page>/', blog_view, name='blog_page'),
    path('single/<int:pid>/', blog_single, name='single'),
    path('blog/category/<slug:category_slug>/', blog_view, name='blog_category'),
    path('blog/category/<slug:category_slug>/page/<int:page>/', blog_view, name='blog_category_page'),
    # path('tag/<str:tag_name>' ,blog_view,name='tag'),
    # path('author/<str:author_username>',blog_view,name='author'),
    path('search/',blog_search,name='search'),
    path('blog/tag/<slug:tag_slug>/', blog_view, name='blog_tag'),
    path('blog/tag/<slug:tag_slug>/page/<int:page>/', blog_view, name='blog_tag_page'),

]
