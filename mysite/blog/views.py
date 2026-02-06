from django.shortcuts import render
from django.views import generic
from .models import Post
from django.core.paginator import Paginator
import jinja_filters
from django.db.models import Q


# Create your views here.
def posts(request):
    posts = Post.objects.order_by('pk')
    paginator = Paginator(posts, per_page=2)
    page_number = request.GET.get('page')
    paged_posts = paginator.get_page(page_number)

    context = {
        'posts': paged_posts,
    }
    return render(request, 'posts.html', context)

class PostDetailVIew(generic.DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


def search(request):
    query = request.GET.get('query')
    posts_search_results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))

    context = {
        "query": query,
        "posts": posts_search_results,
    }
    return render(request, template_name="search.html", context=context)


