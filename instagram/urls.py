from django.urls import path
from . import views

urlpatterns = [
    path('', views.insta_post, name = "insta_post"),
    path('/<int:pk>/', views.post_detail,name='post_detail'),
    path('/post_list/', views.post_list, name='post_list'),
    path('/read_excel', views.read_excel)
]
