from django.shortcuts import render , get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import PostsSerializer
from posts.models import Post



@api_view()
def all_posts(request):
    posts = Post.objects.all()
    posts_ser = PostsSerializer(posts , many=True)
    return Response(posts_ser.data)


@api_view()
def post(request , slug , pk):
    post = get_object_or_404(Post , slug=slug , pk=pk)
    post_ser = PostsSerializer(post)
    return Response(post_ser.data)
