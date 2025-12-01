from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category
from django.core.paginator import Paginator
from taggit.models import Tag

# Create your views here.

def blog_view(request,page=1, category_slug=None,tag_slug=None):
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
        'tag_slug': tag_slug,
        'posts': posts
    })
def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status=True)

    # افزایش بازدید
    post.counted_views += 1
    post.save()

    return render(request, "blog/single-blog.html", {
        "post": post,
    })

def blog_search(request):
    query = request.GET.get("q", "").strip()

    if query:
        # 1. اول جستجو با عبارت کامل (کاملاً شبیه عنوان)
        exact_posts = Post.objects.filter(title__iexact=query, status=True)
        if exact_posts.exists():
            return redirect("blog:single", pid=exact_posts.first().id)

        # 2. اگر نبود: جستجو با startswith
        starts_posts = Post.objects.filter(title__istartswith=query, status=True)
        if starts_posts.exists():
            return redirect("blog:single", pid=starts_posts.first().id)

        # 3. اگر نبود: contains معمولی
        contains_posts = Post.objects.filter(title__icontains=query, status=True)
        if contains_posts.exists():
            return redirect("blog:single", pid=contains_posts.first().id)

    # نتیجه پیدا نشد
    return redirect("blog:home")