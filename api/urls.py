from django.urls import path
from . import views


app_name = "api"

urlpatterns = [
    path('all_posts' , views.all_posts , name="posts"),
]