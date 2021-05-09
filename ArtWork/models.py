from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
  Name = models.CharField( max_length=100)
  UploadDate = models.DateTimeField(auto_now=True, auto_now_add=False)
  Owner = models.ForeignKey(User, on_delete=models.CASCADE)
  File = models.FileField(upload_to='Media', max_length=200)