from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import AddCommentForm
from posts.models import Post



@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        form = AddCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            return redirect(request.META.get("HTTP_REFERER"))
    else:
        return redirect("/")



@login_required 
def reply_comment(request , post_id , comment_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=post_id)
        form = AddCommentForm(request.POST)
        comment = get_object_or_404(Comment , pk=comment_id)
        if form.is_valid():
            r_comment = form.save(commit=False)
            r_comment.user = request.user
            r_comment.post = post
            r_comment.is_reply = True
            r_comment.reply = comment
            r_comment.save()
            return redirect(request.META.get("HTTP_REFERER"))
