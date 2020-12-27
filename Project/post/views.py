from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from account.models import Account
from .forms import PostWrite, CommentWrite
# from taggit.models import Tag

# Create your views here.
def post_detail(request, url_text):
    post = get_object_or_404(Post, url_text=url_text)
    owner = get_object_or_404(Account, username=post.post_author)
    tags = post.get_tag_list()
    comment_form = CommentWrite(request.POST)
    comments = post.comments.all()

    if request.method == 'POST':
        if request.POST.get('like'):
            owner.total_likes += 1
            owner.save()
        elif request.POST.get('unlike'):
            owner.total_likes -= 1
            owner.save()

        elif request.POST.get('send_comment'):
            comment_owner = request.POST.get('comment_owner')
            comment_email = request.POST.get('comment_email')
            comment = request.POST.get('comment')
            comment_for_post = Comment(
                comment_parent=post, 
                comment_owner=comment_owner, 
                comment_email=comment_email, 
                comment=comment
                )
            comment_for_post.save()
            return redirect(post.get_absolute_url())
        elif request.POST.get('send_comment_2'):
            comment_owner = request.POST.get('comment_owner_auth')
            comment_email = request.POST.get('comment_email_auth')
            comment = request.POST.get('comment')
            comment_for_post = Comment(
                comment_parent=post, 
                comment_owner=request.user, 
                comment_email=request.user.email, 
                comment=comment
                )
            request.user.total_comments += 1
            request.user.save()
            comment_for_post.save()
            return redirect(post.get_absolute_url())
            

    context = {
        'post': post,
        'tags': tags,
        'comments': comments,
        'comment_form': comment_form,
        'owner': owner
    }

    return render(request, 'post/detail.html', context)

@login_required(login_url='login')
def post_write(request):
    form = PostWrite(request.POST or None)

    if form.is_valid():
        post_author = request.user
        post_title = form.cleaned_data.get('post_title')
        post_content = form.cleaned_data.get('post_content')
        tags = form.cleaned_data.get('tags')
        post = Post(post_author=post_author, post_title=post_title, tags=tags, post_content=post_content)
        post.save()

        return redirect('home')


    context = {'form': form}
    return render(request, 'post/write.html', context)

@login_required(login_url='login')
def post_update(request, url_text):
    post = get_object_or_404(Post, url_text=url_text)
    form = PostWrite(request.POST or None, instance=post)

    if form.is_valid():
        # post_author = request.user
        # post_title = form.cleaned_data.get('post_title')
        # post_content = form.cleaned_data.get('post_content')
        # post_tags = form.cleaned_data.get('tags')
        # post = Post(post_author=post_author, post_title=post_title, post_content=post_content, tags=post_tags)
        # post.save()
        post = form.save()
        print(post.post_content)
        return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'post/re_write.html', context)

# @login_required(login_url='login')
# def post_delete(request, url_text):
#     post = get_object_or_404(Post, url_text=url_text)

#     if request.method == 'POST':
#         if request.POST.get('yaziyi_ucur'):
#             pass