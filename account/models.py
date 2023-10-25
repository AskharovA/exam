from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                blank=True,
                                null=True)
    first_name = models.CharField(max_length=255, blank=True, default='')
    last_name = models.CharField(max_length=255, blank=True, default='')
    avatar = models.ImageField(upload_to='profile_avatars', default='default_avatar.jpg')
    email = models.EmailField(blank=True, null=True)
