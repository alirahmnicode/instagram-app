from django.urls import path
from . import views


app_name = 'comment'

urlpatterns = [
    path('add/<int:post_id>/' , views.add_comment , name="add"),
    path('reply/<int:comment_id>/<int:post_id>/' , views.reply_comment , name="reply"),
]