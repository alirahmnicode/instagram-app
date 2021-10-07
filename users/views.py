from django.shortcuts import render, redirect, get_object_or_404 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from posts.models import Post
from .forms import UserLoginForm, UserRegisterForm, EditProfileForm
from .models import Profile , Relation


def user_login(request):
    next_url = request.GET.get("next")
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                login(request, user)
                messages.success(request, "you logged in successfully", "success")
                if next_url:
                    return redirect(next_url)
                return redirect("/")
            else:
                messages.error(request, "wrong username or password", "warning")
    else:
        form = UserLoginForm()
    return render(request, "account/login.html", {"form": form})


def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd["username"], cd["email"], cd["password"])
            login(request, user)
            messages.success(request, "you are registered successfully", "success")
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "account/signup.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.success(request, "you are logged out successfully", "success")
    return redirect("/")


# user profile
@login_required
def user_profile(request, pk, username):
    user = get_object_or_404(User, pk=pk, username=username)
    posts = Post.objects.filter(user=user)
    try:
        profile = Profile.objects.get(user=user)
        is_profile = True
    except:
        is_profile = False
    context = {"posts": posts, "user": user , "is_profile":is_profile}
    return render(request, "account/profile.html", context)


@login_required
def edit_profile(request, username):
    if request.user.username == username:
        user = get_object_or_404(User, username=username)
        profile = get_object_or_404(Profile, user=user)
        if request.method == "POST":
            form = EditProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                user.email = form.cleaned_data["email"]
                user.save()
                return redirect(
                    "users:profile", pk=request.user.pk, username=request.user.username
                )
        else:
            form = EditProfileForm(
                instance=profile, initial={"email": request.user.email}
            )
        context = {"form": form}
        return render(request, "account/edit_profile.html", context)
    else:
        return redirect(
            "users:profile", pk=request.user.pk, username=request.user.username
        )


@login_required
def follow_unfollow(request , user_id):
    user = get_object_or_404(User , pk=user_id)
    # get or create relation object for add follower for user
    obj_user, created_user_r = Relation.objects.get_or_create(user=user)
    # get or create relation object for add following for user that send request
    obj_request_user, created_r_user_r = Relation.objects.get_or_create(user=request.user)

    # add following for user that send request
    if created_r_user_r == True:
        obj_request_user.following.add(user)
    
    # add folower for user
    if created_user_r == True:
        obj_user.follower.add(request.user)
    elif request.user in obj_user.follower.all():
        # unfollow user
        obj_user.follower.remove(request.user)
        obj_request_user.following.remove(user)
    else:
        # follow user 
        obj_user.follower.add(request.user)
        obj_request_user.following.add(user)

    return redirect(request.META.get('HTTP_REFERER'))

    
