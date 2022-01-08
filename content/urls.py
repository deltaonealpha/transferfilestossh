"""cipherflix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth
from django.conf.urls import url
from filebrowser.sites import site
from content.views import ReadEbook, ShowMovie,PlayMovie,ListAllMovie,aboutlisting,privacypolicylisting,termlisting,PlayTv,PlayEpTv,ListAllTv,search_product,homeindex,profileview,ListWhatsnEw,faqlisting,ListAllEbooks
urlpatterns = [
    path('watch',ShowMovie.as_view(),name='homeindex'),
    path('profile',profileview.as_view(),name='profileview'),
    path('movies',ListAllMovie,name='movieslisting'),
    path('tv',ListAllTv,name='tvlisting'),
    path('ebooks',ListAllEbooks,name='ebookslisting'),
    path('whatsnew',ListWhatsnEw,name='ListWhatsnEw'),
    path('faq',faqlisting.as_view(),name='search'),
    path('contact',search_product,name='search'),
    path('pricing',search_product,name='search'),
    path('search',search_product,name='search'),
    path('about',aboutlisting.as_view(),name='aboutlisting'),
    path('termsofusage',termlisting.as_view(),name='privacypolicylisting'),
    path('faq',faqlisting.as_view(),name='search'),
    path('privacypolicy',privacypolicylisting.as_view(),name='termlisting'),
    path('',homeindex.as_view(),name='homepageintro'),
    url(r'^play/(?P<id>[0-9]+)/$', PlayMovie.as_view(), name = 'playmovie'),
    url(r'^tv/(?P<id>[0-9]+)/$', PlayTv.as_view(), name = 'listtvepisodepage'),
    url(r'^read/(?P<id>[0-9]+)/$', ReadEbook.as_view(), name = 'readebookpage'),
    url(r'^playtv/(?P<id1>[0-9]+)/(?P<id2>[0-9]+)/$', PlayEpTv.as_view(), name = 'listtvepisodepage'),
]
