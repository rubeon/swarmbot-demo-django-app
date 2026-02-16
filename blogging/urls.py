from django.urls import path
from .views import blog_list, blog_detail, post_detail

urlpatterns = [
    path('', blog_list, name='blog_list'),
    path('<str:blog_slug>/', blog_detail, name='blog_detail'),
    path('<str:blog_slug>/<str:post_slug>/', post_detail, name='post_detail'),
]
