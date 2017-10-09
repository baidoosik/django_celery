from celery import shared_task
import requests as req
from bs4 import BeautifulSoup as bfs
from .models import CrawlingList


@shared_task(max_entries=2, default_retry_delay=60*60)
def startup_news_crawling():
    url = 'http://www.doosikbae.com'
    params = {
        'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'),
        'Referer': 'http://myjorney.tistory.com',
    }

    html = req.get(url=url, params=params).text

    soup = bfs(html, 'html.parser')

    for tag in soup.select('#wrapper #main .tiles a'):
        CrawlingList.objects.create(description=tag.text,
                                    url='www.doosikbae.com' + tag['href'])




