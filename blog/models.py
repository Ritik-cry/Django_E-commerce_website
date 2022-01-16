from operator import mod
from django.db import models

# Create your models here.
class Blogpost(models.Model):
    postId = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    heading0 = models.CharField(max_length=300)
    heading0text = models.CharField(max_length=3000)
    heading1 = models.CharField(max_length=300)
    heading1text = models.CharField(max_length=3000)
    heading2 = models.CharField(max_length=300)
    heading2text = models.CharField(max_length=3000)
    date = models.DateField()
    thumbnail = models.ImageField(upload_to="blog/images",default="")

    def __str__(self):
        return self.title