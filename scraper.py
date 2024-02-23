import requests
import json
from bs4 import BeautifulSoup
from article import Article
from strategies.dergi_park import DergiParkStrategy
from strategy import Strategy

class Scraper():

  searchURL = "https://scholar.google.com/scholar?start=10&q="

  def __init__(self) -> None:
    self.strategies : list[Strategy]  = [
      DergiParkStrategy()
    ]
    pass

  def operate_strategy(self, article : Article) -> Strategy:
    filteredStrategies = [s for s in self.strategies if article.url.startswith(s.link)]
    return filteredStrategies[0] if len(filteredStrategies) > 0 else None

  def scrape_detail(self, article : Article) -> Article:
    strategy = self.operate_strategy(article)
    return strategy.scraper(article) if strategy != None else article

  def scrap(self, word : str) -> list[Article] :

    articleList : list[Article] = []

    response = requests.get(self.searchURL + word.replace(" ", "+"))
    instance = BeautifulSoup(response.text, "html.parser")
    
    article_htmls = instance.find_all(class_="gs_r gs_or gs_scl")
    for article_html in article_htmls:
      newArticle = Article()

      # Google Scholarda bulunan tüm özellikleri ata
      newArticle.name = article_html.find("h3").text
      newArticle.citationsNumber = int(article_html.find(class_="gs_fl gs_flb").find_all("a")[2].text.split(" ")[2])
      newArticle.authors = list(map(lambda tag: tag.text, article_html.find(class_="gs_a").find_all("a")))
      url_tag = article_html.find("h3").find("a", href=True)
      newArticle.url = url_tag["href"] if url_tag != None else ""

      # Google Scholar'dan gelen article linkin strategy managareine gönder
      detailedArticle = self.scrape_detail(newArticle)
      
      articleList.append(detailedArticle)
    
    return articleList
    