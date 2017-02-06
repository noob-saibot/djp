from django.contrib import admin
from blog.models import Post, WikiInform, Charts
from django import forms
from ckeditor.widgets import CKEditorWidget
import blog.wiki_parser as wiki


class PostAdmin(admin.ModelAdmin):
    actions = ['to_draft', 'to_prod']
    list_display = ['title', 'is_draft']
    def to_prod(self, request, queryset):
        queryset.update(is_draft=False)

    def to_draft(self, request, queryset):
        queryset.update(is_draft=True)

class WikiAdmin(admin.ModelAdmin):
    list_display = ['title', 'post_id']
    actions = ['create_or_refill_wiki']

    def create_or_refill_wiki(self, request, queryset):
        for i in Post.objects.all():
            if not WikiInform.objects.filter(title=i.title).update(post_id=i.id, content=wiki.Inform(i.content).links(), datetime=i.datetime):
                notes = WikiInform(title=i.title, post_id=i.id, content=wiki.Inform(i.content).links(), datetime=i.datetime)
                notes.save()

class ChartsAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Post, PostAdmin)
admin.site.register(WikiInform, WikiAdmin)
admin.site.register(Charts, ChartsAdmin)
