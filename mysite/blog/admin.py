from django.contrib import admin
from blog.models import Post
from django import forms
from redactor.widgets import RedactorEditor
from ckeditor.widgets import CKEditorWidget

admin.site.register(Post)
