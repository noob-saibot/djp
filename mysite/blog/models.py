from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Date')
    content = models.TextField(max_length=10000)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
