from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    attach = models.FileField()
    message = models.CharField(max_length=250)
