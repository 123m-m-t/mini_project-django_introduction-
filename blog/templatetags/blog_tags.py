from django import template
from blog.models import Post, Category
from taggit.models import Tag
from django.db.models import Count

register = template.Library()


# ----------------------
#  SEARCH (ثابت)
# ----------------------
@register.inclusion_tag("blog/sidebar/search.html")
def sidebar_search():
    return {}


# ----------------------
#  CATEGORIES (داینامیک)
# ----------------------
@register.inclusion_tag("blog/sidebar/categories.html")
def sidebar_categories():
    categories = Category.objects.annotate(post_count=Count("post"))
    return {"categories": categories}


# ----------------------
#  INSTAGRAM (ثابت)
# ----------------------
@register.inclusion_tag("blog/sidebar/instagram.html")
def sidebar_instagram():
    posts = Post.objects.filter(status=True).order_by("-created_date")[:6]
    return {"posts": posts}



# ----------------------
#  NEWSLETTER (ثابت)
# ----------------------
@register.inclusion_tag("blog/sidebar/newsletter.html")
def sidebar_newsletter():
    return {}


# ----------------------
#  POPULAR POSTS (داینامیک)
# ----------------------
@register.inclusion_tag("blog/sidebar/popular.html")
def sidebar_popular(limit=4):
    posts = Post.objects.filter(status=True).order_by("-counted_views")[:limit]
    return {"posts": posts}


# ----------------------
#  TAG CLOUD (داینامیک)
# ----------------------
@register.inclusion_tag("blog/sidebar/tags.html")
def sidebar_tags():
    tags = Tag.objects.all()
    return {"tags": tags}

@register.simple_tag(takes_context=True)
def post_navigation(context, pid):
    prev_post = Post.objects.filter(status=True, id__lt=pid).order_by('-id').first()
    next_post = Post.objects.filter(status=True, id__gt=pid).order_by('id').first()

    # متغیرها را به context اصلی اضافه می‌کنیم
    context["prev_post"] = prev_post
    context["next_post"] = next_post

    return ""   # خروجی لازم نیست چون در صفحه از context استفاده می‌کنی



