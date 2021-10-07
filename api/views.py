from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post


@api_view(['GET' , 'POST'])
def all_posts(request):
    posts = Post.objects.all()