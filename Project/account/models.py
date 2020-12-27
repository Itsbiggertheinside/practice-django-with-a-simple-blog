from django.db import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import AbstractUser
from post.models import Post

# Create your models here.
# class Stats(models.Model):
#     user = models.ForeignKey('Account', on_delete=models.CASCADE)
#     likes = models.IntegerField(default=0)
#     comments = models.IntegerField(default=0)
#     posts = models.IntegerField(default=0)

class Account(AbstractUser):
    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'

    def upload_to_path(self, filename):
        return 'profiles/%s/%s/' % (self.username, filename)

    pic = models.ImageField(null=True, blank=True, upload_to=upload_to_path, default='default-profile-img.png')
    city = models.CharField(max_length=21, null=True, blank=True)
    three_word = models.CharField(max_length=35, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    webpage = models.CharField(max_length=150, null=True, blank=True)

    total_likes = models.IntegerField(default=0)
    total_comments = models.IntegerField(default=0)
    total_posts = models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def get_number_of_posts(self):
        posts = Post.objects.filter(post_author=self.id)
        return len(posts)

    # def get_number_of_likes(self):
    #     posts = Post.objects.filter(post_author=self.id)
    #     for post in posts:
    #         return post.likes
        
    # def get_number_of_comments(self):
    #     account = get_object_or_404(Account, id=self.id)
    #     posts = account.posts.filter()
    #     return len(posts)
