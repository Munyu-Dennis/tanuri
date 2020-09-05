from django.db import models
from django.utils import timezone

class Comments(models.Model):
    from home.models import Blog
    Title = models.ForeignKey(Blog, on_delete=models.CASCADE)
    Name = models.CharField(max_length=150)
    Message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    
