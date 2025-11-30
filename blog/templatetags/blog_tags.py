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
    return {}


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

