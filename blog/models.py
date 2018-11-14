from django.db import models
from django.utils import timezone
from django.conf import settings
from askcompany.utils import uuid_upload_to

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_post_set")
    title = models.CharField(max_length=200)
    text = models.TextField()
    photo = models.ImageField(upload_to=uuid_upload_to)
    created_date = models.DateTimeField(
        default = timezone.now
    )
    published_date = models.DateTimeField(
        blank = True, null = True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    message = models.TextField()