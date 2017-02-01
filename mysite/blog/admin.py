from django.contrib import admin
from blog.models import Post, WikiInform
from django import forms
#from redactor.widgets import RedactorEditor
from ckeditor.widgets import CKEditorWidget

class PostAdmin(admin.ModelAdmin):
    actions = ['to_draft', 'to_prod']
    list_display = ['title', 'is_draft']
    def to_prod(self, request, queryset):
        queryset.update(is_draft=False)

    def to_draft(self, request, queryset):
        queryset.update(is_draft=True)

class WikiAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_id']

admin.site.register(Post, PostAdmin)
admin.site.register(WikiInform, WikiAdmin)
