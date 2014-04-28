from django.db import models

#  models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password_hash = models.CharField(max_length=33)

class File2(models.Model):
    filename = models.CharField(max_length=65536)
    user = models.ForeignKey(User)
    thefile = models.FileField(upload_to='documents/')
