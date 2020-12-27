from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from uuid import uuid4
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    post_author = models.ForeignKey('account.Account', on_delete=models.PROTECT, related_name='posts', verbose_name='Yazar')
    post_title = models.CharField(max_length=75, null=False, blank=False, verbose_name='title')
    post_content = RichTextField(null=False, blank=False, verbose_name='content')
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=200, null=False, blank=False, verbose_name='tags')
    url_text = models.SlugField(unique=True, max_length=95)

    def __str__(self):
        return self.post_title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'url_text': self.url_text})

    def get_unique_url(self):
        url_text = slugify(self.post_title.replace('ı', 'i'))
        unique_url = f'{url_text}-{self.post_author}'
        return unique_url

    def save(self, *args, **kwargs):
        if not self.url_text:
            self.url_text = self.get_unique_url()
            return super(Post, self).save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

    def get_tag_list(self):
        tag_list = self.tags.split(',')
        return tag_list

class Comment(models.Model):
    comment_parent = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments', verbose_name='Bağlı olduğu post')
    comment_owner = models.CharField(max_length=35, verbose_name='Yorum sahibi', null=False)
    comment_email = models.EmailField(verbose_name='Yorum sahibi\'nin mail adresi')
    comment = models.TextField(verbose_name='Yorum')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.comment_parent.post_title} - {self.comment[:50]}...'