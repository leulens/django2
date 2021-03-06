"""super_news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import debug_toolbar

from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap, index
from news import views, sitemaps


urlpatterns = [
    path('', cache_page(60*60)(views.IndexView.as_view()), name='homepage'),

    path('blog/', views.BlogListView.as_view(), name='blog'),

    path('post/<post_slug>', cache_page(60*60)(views.PageDetailView.as_view()), name='page'),
    path('tag/<slug>/', cache_page(60*60)(views.TagListView.as_view()), name='tag'),
    path('category/<cat_slug>/', cache_page(60*60)(views.CategoryListView.as_view()), name='category'),

    path('contact/', cache_page(60*60)(views.ContactView.as_view()), name='contact'),
    path('faq/', cache_page(60*60)(views.FaqView.as_view()), name='faq'),
    path('search/', views.SearchView.as_view(), name='search'),

    path('robots.txt', views.RobotsView.as_view()),
    path('sitemap.xml', cache_page(86400)(index), {'sitemaps': sitemaps.sitemaps}),
    path('sitemap-<section>.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps.sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),


    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),

    path('accounts/', include('authors.urls')),


    # grappelli URLS
    path('grappelli/', include('grappelli.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)