from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):
    # Query set
    qs = Post.objects.all()
    return render(request, 'post_list.html',{'post_list': qs})