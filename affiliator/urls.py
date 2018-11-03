"""affiliator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

app_name = 'first'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^man$', views.man, name='man'),
    url(r'^woman$', views.woman, name='woman'),
    url(r'^geek$', views.geek, name='geek'),
    url(r'^kids$', views.kids, name='kids'),
	url(r'^dbupdate$', views.dbupdate, name='dbupdate'),
    #url(r'^search$', views.search, name='search'),
    # url(r'^(?P<who>[a-zA-Z]+)/newsort$', views.newsort, name='newsort'),
    # url(r'^(?P<who>[a-zA-Z]+)/popularsort$', views.popularsort, name='popularsort'),
    # url(r'^(?P<who>[a-zA-Z]+)/pricesort$', views.pricesort, name='pricesort'),
    # url(r'^newsort$', views.newsort, name='newsort'),
    # url(r'^popularsort$', views.popularsort, name='popularsort'),
    # url(r'^pricesort$', views.pricesort, name='pricesort'),
    url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)