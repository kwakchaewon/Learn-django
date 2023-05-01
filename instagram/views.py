from django.shortcuts import render
from .models import Post

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