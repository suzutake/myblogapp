from django.db import models

# Create your models here.
class Post(object):
    """docstring for Post."""
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
