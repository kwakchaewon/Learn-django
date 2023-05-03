from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView

# Create your views here.

def insta_post(request):
    qs = Post.objects.all()
    q = request.GET.get('q','')
    
    if q:
        qs = qs.filter(message__icontains=q)
    
    print(q)
    
    # instagram/templates/instagram/post_list.html
    return render(request, 'insta_post.html', {
        'post_list':qs,
        'q':q,
    })
    
    
def post_detail(request, pk):
    response = HttpResponse("hellow")
    return response


# Generic view 예시
# /instagram/post_list.html
post_list = ListView.as_view(model=Post)


