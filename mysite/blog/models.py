from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Date')
    #content = models.TextField(max_length=10000)
    content = RichTextUploadingField(blank=True, default='', config_name='default')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
