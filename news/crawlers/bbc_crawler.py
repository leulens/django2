from datetime import datetime

from slugify import slugify
from requests_html import HTMLSession

from concurrent.futures import ThreadPoolExecutor

from news.models import Article, Author, Category

try:
    author = Author.objects.get(id=3)
except:
    print('Создайте сначала автора, а потом запускайте парсер!')

def crawl_one(url):

    with HTMLSession() as session:
        response = session.get(url)

    name = response.html.xpath('//h1')[0].text
    content = response.html.xpath('//article//p')
    image_url = response.html.xpath('//figure//img/@src')[0]
    pub_date = response.html.xpath('//time/@datetime')
    cats = response.html.xpath('//article//div[@class="ssrcss-1emjddl-Cluster e1ihwmse0"]//ul//li')


    my_content = ''
    short_description = ''

    for element in content:
        my_content += f'<{element.tag}>' + element.text + f'<{element.tag}>'
        if len(short_description) < 200:
            short_description += element.text + ' '

    image_name = slugify(name)
    img_type = image_url.split('.')[-1]

    img_path = f'images/{image_name}.{img_type}'

    with open(f'media/{img_path}', 'wb') as f:
        with HTMLSession() as session:
            response = session.get(image_url)
            f.write(response.content)

    pub_date = datetime.strptime(pub_date[0][0:10], '%Y-%m-%d')

    categories = []

    for cat in cats:
        categories.append(
            {
                 'name': cat.text.strip(),
                 'slug': slugify(cat.text)
             }
        )

    article = {
        'name': name,
        'slug': slugify(name),
        'content': my_content,
        'short_description': short_description.strip(),
        'main_image': img_path,
        'pub_date': pub_date,
        'author': author,
    }

    article, created = Article.objects.get_or_create(**article)

    for category in categories:
        cat, created = Category.objects.get_or_create(**category)

        article.categories.add(cat)

    print(article)


def get_fresh_news():
    base_url = 'https://www.bbc.com/news/technology'

    with HTMLSession() as session:
        response = session.get(base_url)

    links =response.html.absolute_links

    # fresh_news = [lnk for lnk in links if '/news/technology' in lnk]

    fresh_news = []

    for link in links:
        try:
            if link.split('-')[-1].isdigit():
                fresh_news.append(link)
        except:
            pass

    return fresh_news

def run():

    fresh_news = get_fresh_news()
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(crawl_one, fresh_news)