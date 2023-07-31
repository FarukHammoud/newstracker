from scrapers.folha import FolhaScraper
from scrapers.g1 import G1Scraper
from git_db import GitDatabase

scrapers = [FolhaScraper(), G1Scraper()]
gitdb = GitDatabase()

for scraper in scrapers:
    scraper.getNews() 
    gitdb.commit()