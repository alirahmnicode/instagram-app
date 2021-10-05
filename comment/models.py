from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_comments')
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='post_comments')
    reply = models.ForeignKey('self' , on_delete=models.CASCADE , null=True , blank=True , related_name='reply_comments')
    is_reply = models.BooleanField(default=False)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}-{self.body[:30]}'
    
    class Meta:
        ordering = ('-created',)