from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('like-unlike/<int:post_id>/' , views.like_unlike , name="like_unlike"),
    path('' , views.index , name="home"),
    path('<str:slug>/<int:pk>/' , views.post_detail , name="post_detail"),
    path('add_post/' , views.add_post , name="add_post"),
    path('delete/<int:post_id>/<int:post_user_id>/' , views.delete_post , name="delete"),
    path('edit/<int:post_id>/<int:post_user_id>/' , views.edit_post , name="edit"),
]