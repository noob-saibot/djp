from __future__ import unicode_literals

from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from tastypie.utils.timezone import now
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Date')
    is_draft = models.BooleanField(default=True)
    content = RichTextUploadingField(blank=True, default='', config_name='default')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/main/%i/" % self.id

class WikiInform(models.Model):
    title = models.CharField(max_length=255)
    post_id = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Date')
    content = models.TextField()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
