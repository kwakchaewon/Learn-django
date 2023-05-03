from django.shortcuts import render
from .models import Post
from django.http import HttpResponse, HttpRequest, FileResponse
from django.views.generic import ListView
from urllib.parse import quote
import pandas as pd

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


#  파일 다운로드 제공
def read_excel(request):
    response = FileResponse(open('sample data.xls','rb'))
    return response