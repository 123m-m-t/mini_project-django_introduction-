from django.shortcuts import render, get_object_or_404, redirect,reverse
from .models import Post, Category, Comment
from django.core.paginator import Paginator
from taggit.models import Tag


# Create your views here.

def blog_view(request, page=1, category_slug=None, tag_slug=None, author_username=None):
    posts = Post.objects.filter(status=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    if author_username:
        posts = posts.filter(author__username=author_username)

    paginator = Paginator(posts, 2)
    page_obj = paginator.get_page(page)

    return render(request, 'blog/blog.html', {
        'page_obj': page_obj,
        'category_slug': category_slug,
        'tag_slug': tag_slug,
        'author_username': author_username,
        'posts': posts
    })

def blog_single(request, pid):
    post = get_object_or_404(Post, id=pid, status=True)

    # افزایش بازدید
    post.counted_views += 1
    post.save()

    if post.login_require and not request.user.is_authenticated:
        return redirect(f"{reverse('accounts:auth')}?next={request.path}")

    comments = Comment.objects.filter(post=post, approved=True)

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect(f"{reverse('accounts:auth')}?next={request.path}")

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("comment")
        subject = request.POST.get("subject")

        Comment.objects.create(
            post=post,
            name=name,
            email=email,
            subject=subject if subject else "No subject",
            message=message,
            approved=False,
        )

        return redirect("blog:single", pid=pid)

    return render(request, "blog/single-blog.html", {
        "post": post,
        "comments": comments,
    })


def blog_search(request):
    query = request.GET.get("q", "").strip()

    if query:

        exact_posts = Post.objects.filter(title__iexact=query, status=True)
        if exact_posts.exists():
            return redirect("blog:single", pid=exact_posts.first().id)

        starts_posts = Post.objects.filter(title__istartswith=query, status=True)
        if starts_posts.exists():
            return redirect("blog:single", pid=starts_posts.first().id)

        contains_posts = Post.objects.filter(title__icontains=query, status=True)
        if contains_posts.exists():
            return redirect("blog:single", pid=contains_posts.first().id)

    return redirect("blog:home")

def blog_by_date(request, year, month, day,page=1):
    posts = Post.objects.filter(
        status=True,
        created_date__year=year,
        created_date__month=month,
        created_date__day=day,
    )

    paginator = Paginator(posts, 3)  # هر صفحه ۶ پست، می‌تونی عوضش کنی
    page_obj = paginator.get_page(page)

    return render(request, "blog/blog.html", {
        "page_obj": page_obj,
        "posts": page_obj.object_list,
        "filter_date": {"year": year, "month": month, "day": day},
    })