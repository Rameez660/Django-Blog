from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content =models.TextField()
    author = models.CharField(max_length=70, default="")
    slug = models.CharField(max_length=130, default="")
    timeStamp = models.DateTimeField(blank=True)
    # thumbnail = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return "Name is:- "+self.title +" by "+self.author