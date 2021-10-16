from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'posts')
    descriptions = models.TextField()
    slug = models.SlugField()
    likes = models.ManyToManyField(User , related_name='likes' , blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descriptions[:30]

    def get_absolut_url(self):
        return reverse('post:post_detail' , kwargs={'slug':self.slug , 'pk':self.pk})
    
    class Meta:
        ordering = ('-create',)


