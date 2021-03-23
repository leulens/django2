from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Category, Author, Comment, Newsletter, Tag


class ArticleAdmin(SummernoteModelAdmin): #настройка для администрирования раздела статей
    summernote_fields = ('content', 'short_description') #поля, к которым будет применен редактор


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Newsletter)
admin.site.register(Tag)
