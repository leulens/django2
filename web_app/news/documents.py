from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Article



html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@registry.register_document
class ArticleDocument(Document):

    content = fields.TextField(analyzer=html_strip)

    class Index:
        name = 'articles'

    class Django:
        model = Article  # The model associated with this Document

        fields = [
            'name',
            'pub_date'
        ]
