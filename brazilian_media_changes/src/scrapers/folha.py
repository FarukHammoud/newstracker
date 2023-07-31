from news_scraper import NewsScraper
import requests
import os
from bs4 import BeautifulSoup

class FolhaScraper(NewsScraper):

    def __init__(self):
        NewsScraper.__init__(self, 'folha')

    def getNews(self):
        return super().getNews()
    
    def getArticles(self):
        folha = "https://www.folha.uol.com.br/"
        res = requests.get(folha)
        soup = BeautifulSoup(res.content, 'html.parser')

        # All links in the page
        links = soup.find_all('a')

        # Get a list of unique articles urls
        articles = {}
        for link in links:
            href = link.get('href')
            if str(href).endswith('.shtml'):
                articles[str(href)] = ''

        return list(articles.keys())
    
    def getArticleText(self, url):
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        divs = soup.find_all('div')

        for div in divs:
            classes = div.get('class')
            if classes != None and 'c-news__body' in classes:
                text = div.get_text()
                text = text.replace('.','.\n')
                text = text.replace(',',',\n')
                title = url.rsplit('/', 1)[-1].split('.')[0]                
                return (title, text)    
        return ("","")          
    