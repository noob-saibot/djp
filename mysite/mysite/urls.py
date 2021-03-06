"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include

######
# Redirect
from django.core.urlresolvers import reverse
from django.views.generic.base import RedirectView
######

from django.contrib import admin
admin.autodiscover()

######
#api
######

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', RedirectView.as_view(url='/blog/')),
    url(r'^api/', include('snippets.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
