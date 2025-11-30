from django.shortcuts import render,get_object_or_404
from .models import Post,Category
from django.core.paginator import Paginator
from taggit.models import Tag

# Create your views here.

def blog_view(request, page=1, category_slug=None,tag_slug=None):
    posts = Post.objects.filter(status=True)

    # اگر دسته‌ای انتخاب شده باشد
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    # فیلتر تگ
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 2)
    page_obj = paginator.get_page(page)

    return render(request, 'blog/blog.html', {
        'page_obj': page_obj,
        'category_slug': category_slug,
        'tag_slug': tag_slug
    })
def blog_single(request):
    return render(request,'blog/single-blog.html')