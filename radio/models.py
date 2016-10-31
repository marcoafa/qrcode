from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    attach = models.FileField()
    message = models.CharField(max_length=250)

    def __unicode__(self):
        return "%s"%(self.email)

class Us(models.Model):
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    valid = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s"%(self.user)
