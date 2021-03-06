from django.shortcuts import render

# Create your views here.
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, WikiSerializer, UserSerializer
from rest_framework import generics, permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import detail_route, api_view
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.reverse import reverse
from blog.models import Post, WikiInform
import django_filters.rest_framework

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)

class WikiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WikiInform.objects.all()
    serializer_class = WikiSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_fields = ('post_id',)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        'wiki_notes_id': reverse('wiki-list', request=request, format=format),
        'charts': reverse('chart-list', request=request, format=format),
    })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

