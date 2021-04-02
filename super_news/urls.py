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

from django.conf import settings
from django.conf.urls.static import static

from news import views


urlpatterns = [
    path('', views.index_hendler, name='homepage'),

    path('blog/', views.blog_hendler, name='blog'),
    path('blog/page/<number>/', views.blog_hendler, name='blog_pager'),

    path('<cat_slug>', views.blog_hendler, name='category'),
    path('<cat_slug>/page/<number>/', views.blog_hendler, name='category_pager'),

    path('post/<post_slug>', views.blog_details_hendler, name='page'),

    path('contact/', views.contact_hendler, name='contact'),
    path('faq/', views.faq_hendler, name='faq'),

    path('robots.txt', views.robots_hendler),

    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)