from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget

class PostWrite(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post_title', 'tags', 'post_content')

    post_title = forms.CharField(label = 'Başlık: ')
    tags = forms.CharField(label = 'Etiketler: ')
    post_content = forms.CharField(widget = CKEditorWidget(), label = 'İçerik: ')

class CommentWrite(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
