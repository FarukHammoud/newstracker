from news_scraper import NewsScraper
import requests
from bs4 import BeautifulSoup
import re

class G1Scraper(NewsScraper):

    def __init__(self):
        NewsScraper.__init__(self, 'g1')

    def getNews(self):
        return super().getNews()
    
    def getArticles(self):
        g1 = "https://g1.globo.com/"
        res = requests.get(g1)

        # All links in the page (using inverted regex)
        inverted_source = str(res.content)[::-1]
        inverted_links = re.findall("lmthg.*?sptth", inverted_source)

        # Get a list of unique articles urls
        articles = {}
        for inverted_link in inverted_links:
            link = inverted_link[::-1]
            if 'noticia' in link.split('/') or 'blog' in link.split('/'):
                articles[link] = ''
                
        return list(articles.keys())
    
    def getArticleText(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        divs = soup.find_all('div')

        for div in divs:
            classes = div.get('class')
            if classes != None and 'mc-article-body' in classes:
                text = div.get_text()
                text = text.replace('.','.\n')
                text = text.replace(',',',\n')
                title = url.rsplit('/', 1)[-1].split('.')[0]          
                return (title, text)  
        return ("","")              
    