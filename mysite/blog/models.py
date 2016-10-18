from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(u'Date')
    content = models.TextField(max_length=10000)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


#####################################
#Add imagekit
#####################################
import PIL
from PIL import Image
from imagekit.models.fields import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust,ResizeToFill

class Jobseeker(models.Model):
    def get_file_path(self, filename):
        extension = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), extension)
        return os.path.join("images", filename)
        ...
        photo = models.ImageField(verbose_name=u'Poster',upload_to=get_file_path,max_length=256, blank=True, null=True)
        photo_small =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFill(50, 50)], image_field='photo',
            format='JPEG', options={'quality': 90})
        photo_medium =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFit(300, 200)], image_field='photo',
            format='JPEG', options={'quality': 90})
       photo_big =ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
            ResizeToFit(640, 480)], image_field='photo',
            format='JPEG', options={'quality': 90})
