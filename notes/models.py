from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField(max_length=200)
    article = models.TextField()
    auther = models.CharField(max_length=200)
    userid = models.ForeignKey(User,on_delete=models.CASCADE)

