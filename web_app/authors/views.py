from django.shortcuts import render

from .models import Author


def author_profile_datail(request, **kwargs):
    user = Author.objects.get(user__username=kwargs.get('username'))
    context = {'user':user}
    return render(request, 'authors/base-author.html', context)
