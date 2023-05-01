from django.urls import path
from . import views

urlpatterns = [
    path('', views.insta_post, name = "insta_post")
]
