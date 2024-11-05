from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)