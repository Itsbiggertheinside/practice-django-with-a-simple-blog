from django.shortcuts import render
from django.db.models import Q, Count, Max
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from post.models import Post

# Create your views here.
def home(request):
    post_list = Post.objects.order_by('-created_at',)
    paginator = Paginator(post_list, 4)
    page = request.GET.get('sayfa')
    top_tags = Post.objects.values('tags').distinct()
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    context = {
        'posts': posts,
        'top_tags': top_tags,
    }

    
    return render(request, 'base/home.html', context)

def search(request):
    if request.method == 'GET':
        if request.GET.get('search_button'):
            query = request.GET.get('query')
            if query:
                posts_after_search = Post.objects.filter(
                    Q(post_author__username__icontains=query) |
                    Q(post_title__icontains=query) | 
                    Q(post_content__icontains=query)
                )
                return render(request, 'base/search.html', context={'posts_after_search': posts_after_search})

    return render(request, 'base/search.html')