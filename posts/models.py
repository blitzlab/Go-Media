from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from userprofile.models import UserProfile

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(allow_unicode = True, unique = True)
    text = models.TextField()
    featured_image = models.ImageField(upload_to = 'images', default='/images/gig.png')
    publish_date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name = 'posts', null = True, on_delete=models.CASCADE)

    def __str__(self):
        self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['-publish_date']
