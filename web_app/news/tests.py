from requests_html import HTMLSession

from django.test import TestCase
from news.crawlers.bbc_crawler import run
from news.models import Article


class AnimalTestCase(TestCase):

    def test_run_crawler(self):
        run()
        article = Article.objects.all()
        article = [x for x in article]
        self.assertTrue(len(article) < 300)

    def test_is_goodreads_available(self):
        url='https://www.bbc.com/news/technology'
        with HTMLSession() as session:
            response = session.get(url)
        self.assertTrue(response.status_code == 200)



