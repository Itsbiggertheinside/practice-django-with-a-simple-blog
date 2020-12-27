from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    exclude = ('url_text',)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)