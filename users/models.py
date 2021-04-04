from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.html import mark_safe
import os, random

def image_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    _now = datetime.now()

    return (f"profile_pic/{_now.strftime('%Y')}-{_now.strftime('%m')}-{instance}-{basefilename}-{randomstr}{file_extension}")

now = timezone.now()

class User(models.Model):
    user_fname = models.CharField(max_length=200, verbose_name='First Name')
    user_lname = models.CharField(max_length=200, verbose_name='Last Name')
    user_email = models.EmailField(unique=True, max_length=200, verbose_name='Email')
    user_position = models.CharField(max_length=200, verbose_name='Position')
    pub_date = models.DateField(default=now)
    user_img = models.ImageField(upload_to=image_path, default='profile_pic/default.png')

    def __str__(self):
        return self.user_email
    
    def image_tag(self):
        return mark_safe(f'<img src="/users/media/{self.user_img}" width="50" height="50"/>')

