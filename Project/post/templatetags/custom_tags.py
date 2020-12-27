from django import template
from post.models import Post


register = template.Library()

@register.simple_tag
def show_latest_posts(count):
    return Post.objects.order_by('-created_at')[:count]
