from django.contrib import admin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ('total_likes', 'total_comments', 'total_posts',)

admin.site.register(Account, AccountAdmin)