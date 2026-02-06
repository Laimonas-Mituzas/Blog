from django.shortcuts import render
from django.views import generic

from .models import Post
import jinja_filters


# Create your views here.
def posts(request):
    context = {
        'posts': Post.objects.order_by('pk'),
    }
    return render(request, 'posts.html', context)

class PostDetailVIew(generic.DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


