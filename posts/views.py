from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import AddPostForm, EditPostForm
from comment.forms import AddCommentForm


def index(request):
    posts = Post.objects.all()
    # get users for suggestions
    users = User.objects.all().exclude(username=request.user.username)
    context = {"posts": posts , 'users':users}
    return render(request, "index.html", context)


@login_required
def post_detail(request, slug, pk):
    post = Post.objects.get(slug=slug, pk=pk)
    # comments = Comment.objects.filter(is_reply=False, post=post)
    comment_form = AddCommentForm()
    context = {"post": post, "comment_form": comment_form}
    return render(request, "post/post_detail.html", context)


@login_required
def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.slug = slugify(form.cleaned_data["descriptions"][:30])
            new_post.save()
            return redirect("/")
    else:
        form = AddPostForm()
    return render(request, "post/add_post.html", {"form": form})


# delete post
@login_required
def delete_post(request, post_user_id, post_id):
    if request.user.id == post_user_id:
        post = get_object_or_404(Post, pk=post_id)
        post.delete()
        return redirect("/")
    else:
        return redirect(
            "users:profile", pk=request.user.pk, username=request.user.username
        )


@login_required
def edit_post(request, post_user_id, post_id):
    if request.user.id == post_user_id:
        post = get_object_or_404(Post, pk=post_id)
        if request.method == "POST":
            form = EditPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                new_post = form.save(commit=False)
                new_post.slug = slugify(form.cleaned_data["descriptions"][:30])
                new_post.save()
                return redirect("/")
        else:
            form = EditPostForm(instance=post)
            return render(request, "post/edit_post.html", {"form": form})
    else:
        return redirect(
            "users:profile", pk=request.user.pk, username=request.user.username
        )


