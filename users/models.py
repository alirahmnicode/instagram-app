from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(blank=True , upload_to="profile")
    phone = models.IntegerField(unique=True , null="True" , blank=True)



def crete_profile(sender , **kwargs):
    if kwargs['created']:
        p = Profile(user = kwargs['instance'])
        p.save()

post_save.connect(crete_profile , sender=User)


