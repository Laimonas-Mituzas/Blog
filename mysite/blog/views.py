from django.shortcuts import render
from django.views import generic
from .models import Post
from django.core.paginator import Paginator
import jinja_filters


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


