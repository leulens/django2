from django.contrib import admin
from django.utils.html import format_html

from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Category, Author, Comment, Newsletter, Tag


def count_words(modeladmin, request, queryset):
    for object in queryset:
        text = object.content.replace('<p>', '').replace('</p>', '')
        words = text.split()
        object.content_words_count = len(words)
        object.save()

count_words.short_description = "Count words in article"


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', 'short_description')
    list_display = ('name', 'image_code', 'pub_date', 'author', 'content_words_count', 'count_unique_words')
    list_filter = ('author', 'pub_date', 'categories')
    search_fields = ('name', 'author')
    actions = (count_words, )

    def image_code(self, object):
        return format_html(
            '<img src="{}" width="100">',
            object.main_image.url
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'in_menu', 'order', 'articles_count')
    list_filter = ('in_menu', )
    search_fields = ('name', )
    list_editable = ('order', 'in_menu')
    readonly_fields = ('order', )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('article_set')

    def articles_count(self, object):
        return object.article_set.all().count()


class AuthorArticleInLine(admin.TabularInline):
    model = Article
    exclude = ('content', 'short_description')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'ava')
    search_fields = ('name', )
    inlines = (AuthorArticleInLine, )

    def ava(self, object):
        return format_html(
            '<img src="{}" width="70">',
            object.avatar.url
        )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment)
admin.site.register(Newsletter)
admin.site.register(Tag)

