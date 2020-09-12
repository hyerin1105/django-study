from django.db import models

# Create your models here.
from django.db import models

class Post2(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()