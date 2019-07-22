from django.db import models


# Create your models here.

class Ostad(models.Model):
    name = models.CharField(max_length=50)
    sid = models.CharField(max_length=20)
    gid = models.CharField(max_length=20, null=True)
    university = models.CharField(max_length=20, default='sharif')
    city = models.CharField(max_length=20, default='Tehran')
