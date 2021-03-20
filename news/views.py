from django.shortcuts import render

# Create your views here.

def blog_hendler(request):
    context = {}
    return render(request, 'news/blog.html', context)

# страница контактов contact
def contact_hendler(request):
    context = {}
    return render(request, 'news/contact.html', context)


# отдельная страница блога: blog-details
def blog_details_hendler(request):
    context = {}
    return render(request, 'news/blog-details.html', context)

# страница вопросов и ответов faq
def faq_hendler(request):
    context = {}
    return render(request, 'news/faq.html', context)

# главная страница index
def index_hendler(request):
    context = {}
    return render(request, 'news/index.html', context)

def robots_hendler(request):
    context = {}
    return render(request, 'news/robots.txt', context, content_type='text/plain')