from django.db import models
# Create your models here.


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    timeStamp = models.DateTimeField(blank=True)
    # timestamp=models.DateField(blank=True)
    # timeStamp =models.DateTimeField(auto_now= True)
    # timeStamp=models.DateTimeField(auto_now_add= True)
    

    def __str__(self):
        return "Name is:- "+self.name +" , "+ "Email is:- " +self.email

