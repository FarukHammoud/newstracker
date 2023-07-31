import requests
from bs4 import BeautifulSoup
from database import Database

database = Database()
database.create()

def find_articles():
    folha = "https://www.folha.uol.com.br/"
    res = requests.get(folha)
    soup = BeautifulSoup(res.content, 'html.parser')

    # The title of the page as string
    print(soup.title.string)

    # All links in the page
    links = soup.find_all('a')
    nb_links = len(links)
    print(f"There are {nb_links} links in this page")
    articles = {}
    for link in links:
        href = link.get('href')
        if str(href).endswith('.shtml'):
            articles[str(href)] = ''

    nb_articles = len(articles)
    print(f"There are {nb_articles} articles links in this page")

    print(articles.keys())
    return articles.keys()


article = "https://www1.folha.uol.com.br/colunas/becky-korich/2023/07/adolescentes-vao-sonambulos-para-a-escola.shtml"
res = requests.get(article)
soup = BeautifulSoup(res.content, 'html.parser')
divs = soup.find_all('div')
for div in divs:
    classes = div.get('class')
    if classes != None and 'c-news__body' in classes:
        print('eureka')
        print(div.get_text())