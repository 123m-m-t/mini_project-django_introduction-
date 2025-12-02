from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag("website/index_part/exclusive_item_blog.html")
def index_part_exclusive_item_blog(limit=3):
    posts = Post.objects.filter(status=True).order_by("-created_date")[:limit]
    return {"posts": posts}