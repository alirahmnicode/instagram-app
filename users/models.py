from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True , upload_to="profile")
    phone = models.IntegerField(unique=True , null=True , blank=True)
   

    def imageUrl(self):
        if self.image.url == '':
            return "https://img.icons8.com/ios/50/000000/user--v1.png"
        else:
            return self.image.url

    


def crete_profile(sender , **kwargs):
    if kwargs['created']:
        p = Profile(user = kwargs['instance'])
        p.save()

post_save.connect(crete_profile , sender=User)


class Relation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follower = models.ManyToManyField(User , related_name="follower" , blank=True)
    following = models.ManyToManyField(User , related_name="following" , blank=True)

    def __str__(self):
        return self.user.username
