from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User
from blog.models import Post, WikiInform

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets')

class WikiSerializer(serializers.HyperlinkedModelSerializer):
    #content = serializers.HyperlinkedRelatedField(many=True, view_name='wiki_notes', read_only=True)

    class Meta:
        model = WikiInform
        fields = ('id', 'post_id', 'content')


owner = serializers.ReadOnlyField(source='owner.username')
