from django.shortcuts import render
from .models import Post
import jinja_filters


# Create your views here.
def posts(request):
    context = {
        'posts': Post.objects.order_by('pk'),
    }
    return render(request, 'posts.html', context)