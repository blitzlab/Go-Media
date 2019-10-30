from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UserProfile(models.Model):
    COUNTRY = [
        ('NG', 'Nigeria'),
        ('GH', 'Ghana'),
        ('SA', 'South Africa'),
        ('UG', 'Uganda'),
    ]
    user = models.OneToOneField(User, related_name = 'profile', on_delete = models.CASCADE)
    about = models.TextField(blank = True)
    nationality = models.CharField(max_length = 50, choices = COUNTRY, blank = True)
    profession = models.CharField(max_length = 100, blank = True)
    Address = models.CharField(max_length = 400, blank = True)
    profile_pic = models.ImageField(upload_to = 'images/profile_picture', blank = True,)
    date_joined = models.DateTimeField(auto_now = True)



    def get_absolute_url(self):
        return reverse('userprofile:profile')

    def __str__(self):
        return self.user.username
