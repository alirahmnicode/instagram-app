from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post
from .forms import AddPostForm, EditPostForm
from comment.forms import AddCommentForm
from users.models import Profile

@login_required
def index(request):
    alert = None
    try:
        # get posts that user followed its creator
        # get user follower
        user_followers = request.user.relation.following.all()
        # filter posts
        # get posts that its user id are in user follower list
        posts = Post.objects.filter(
            user__id__in=[user_id.id for user_id in user_followers],
        )
        # get user posts
        posts |= Post.objects.filter(user=request.user)
    except:
        posts = Post.objects.filter(user=request.user)

    if len(posts) == 0:
        alert = "there is not post for you"
    else:
        alert = None

    print(alert)
    profile = Profile.objects.get(user=request.user)
    if profile.image == '':
        ok = False
    else:
        ok = True
    
    # get users for suggestions
    users = User.objects.all().exclude(username=request.user.username)
    # comment form
    form = AddCommentForm()
    context = {"posts": posts, "users": users , 'form':form , 'alert':alert , 'ok':ok}
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


@login_required
def like_unlike(request , post_id):
    post = get_object_or_404(Post , pk=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect(request.META.get('HTTP_REFERER'))