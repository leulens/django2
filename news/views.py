from django.shortcuts import render
from django.db.models import Count

from .models import Article, Category

def index_hendler(request):
    last_articles = Article.objects.all().order_by(
        '-pub_date')[:3].prefetch_related('categories')

    cat_list = Category.objects.annotate(
        count=Count('article__id')).order_by('count')[:5]

    context = {'last_articles': last_articles,
               'menu_categories': cat_list
    }

    return render(request, 'news/index.html', context)


def blog_hendler(request):
    last_articles = Article.objects.all().order_by(
        '-pub_date')[:6].prefetch_related('categories')
    context = {'last_articles':last_articles}
    return render(request, 'news/blog.html', context)


def category_hendler(request, cat_slug):
    context = {}
    return render(request, 'news/blog.html', context)


# отдельная страница блога: blog-details
def blog_details_hendler(request, post_slug):
    context = {}
    return render(request, 'news/blog-details.html', context)


# страница контактов contact
def contact_hendler(request):
    context = {}
    return render(request, 'news/contact.html', context)


# страница вопросов и ответов faq
def faq_hendler(request):
    context = {}
    return render(request, 'news/faq.html', context)


def robots_hendler(request):
    context = {}
    return render(request, 'news/robots.txt', context, content_type='text/plain')