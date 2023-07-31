import os, shutil
from progress.bar import Bar

class NewsScraper:

    def __init__(self, newspaper):
        self.newspaper = newspaper

    def getNews(self):
        articles = self.getArticles()
        nb_articles = len(articles)
        print(f"[{self.newspaper}] There are {nb_articles} articles links in this page")

        self.deleteArticles()
        bar = Bar(self.newspaper, max=nb_articles, suffix="%(percent).1f%% - %(eta)ds")
        for i in range(len(articles)):
            articleUrl = articles[i]
            title, text = self.getArticleText(articleUrl)
            self.saveArticle(title, text)
            bar.next()
        bar.finish()

    def getArticles(self):
        pass

    def getArticleText(self, url):
        pass

    def saveArticle(self, title, text):
        if not os.path.exists('brazilian_media_changes/data/' + self.newspaper):
            os.makedirs('brazilian_media_changes/data/' + self.newspaper)
        with open('brazilian_media_changes/data/'+self.newspaper+'/'+title+'.txt', 'w', encoding='utf-8') as file :
            file.write(text)
    
    def deleteArticles(self):
        if not os.path.exists('brazilian_media_changes/data/'):
            os.makedirs('brazilian_media_changes/data')
        if os.path.exists('brazilian_media_changes/data/' + self.newspaper):
            shutil.rmtree('brazilian_media_changes/data/' + self.newspaper)
        os.makedirs('brazilian_media_changes/data/' + self.newspaper)

