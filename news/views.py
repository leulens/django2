from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Article, Category


def index_hendler(request):
    last_articles = Article.objects.all().order_by(
        '-pub_date')[:3].prefetch_related('categories')
    context = {'last_articles': last_articles,
    }
    return render(request, 'news/index.html', context)


def blog_hendler(request, **kwargs):
    cat_slug = kwargs.get('cat_slug')
    if cat_slug:
        category = Category.objects.get(slug=cat_slug)
        last_articles = Article.objects.filter(
            categories__slug=cat_slug).order_by(
            '-pub_date')[:6].prefetch_related('categories')
    else:
        last_articles = Article.objects.all().order_by(
        '-pub_date')[:6].prefetch_related('categories')
        category = None
    context = {
        'last_articles':last_articles,
        'category': category,
        }
    return render(request, 'news/blog.html', context)



# отдельная страница блога: blog-details
def blog_details_hendler(request, post_slug):
    main_article = Article.objects.get(slug=post_slug)
    try:
        prev_article = Article.objects.get(id = main_article.id - 1)
    except:
        prev_article = None

    try:
        next_article = Article.objects.get(id = main_article.id + 1)
    except:
        next_article = None
    context = {
        'article': main_article,
        'prev_article': prev_article,
        'next_article': next_article,
    }
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