from django.urls import path, include
from .views import blog_view, blog_single, blog_search, blog_by_date

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('page/<int:page>/', blog_view, name='blog_page'),
    path('single/<int:pid>/', blog_single, name='single'),
    path('blog/category/<slug:category_slug>/', blog_view, name='blog_category'),
    path('blog/category/<slug:category_slug>/page/<int:page>/', blog_view, name='blog_category_page'),
    # path('tag/<str:tag_name>' ,blog_view,name='tag'),
    path('author/<str:author_username>',blog_view,name='author'),
    path('author/<str:author_username>/page/<int:page>', blog_view, name='author_page'),
    path('search/',blog_search,name='search'),
    path('blog/tag/<slug:tag_slug>/', blog_view, name='blog_tag'),
    path('blog/tag/<slug:tag_slug>/page/<int:page>/', blog_view, name='blog_tag_page'),
    path("date/<int:year>/<int:month>/<int:day>/", blog_by_date, name="blog_date"),
    path("date/<int:year>/<int:month>/<int:day>/page/<int:page>/", blog_by_date, name="blog_date_page"),
]
