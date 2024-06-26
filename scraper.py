import requests
import json
from bs4 import BeautifulSoup
from article import Article
from strategies.dergi_park import DergiParkStrategy
from strategy import Strategy

class Scraper():

  searchURL = "https://scholar.google.com/scholar?start=10&q="
  wordCorrectorURL = "https://scholar.google.com/scholar?hl=tr&as_sdt=0%2C5&q="

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

    response = requests.get(self.searchURL + word)

    instance = BeautifulSoup(response.text, "html.parser")
    
    article_htmls = instance.find_all(class_="gs_r gs_or gs_scl")
    for article_html in article_htmls:
      newArticle = Article()

      # Google Scholarda bulunan tüm özellikleri ata
      newArticle.name = article_html.find("h3").text
      
      newArticle.type = "article"
      if newArticle.name.startswith("[ALINTI]"):
        newArticle.type = "quotation"

      ct_field = article_html.find(class_="gs_fl gs_flb").find("a", string=lambda tag: tag and tag.text.startswith("Alıntılanma"))
      newArticle.citationsNumber = int(ct_field.text.split(" ")[2] if ct_field and len(ct_field.text.split(" ")) > 2 else 0)

      newArticle.authors = list(map(lambda tag: tag.text, article_html.find(class_="gs_a").find_all("a")))
      
      url_tag = article_html.find("h3").find("a", href=True)
      newArticle.url = url_tag["href"] if url_tag != None else ""

      summary_tag = article_html.find(class_="gs_rs")
      newArticle.summary = summary_tag.text if summary_tag else ""

      # Google Scholar'dan gelen article linkin strategy managareine gönder
      detailedArticle = self.scrape_detail(newArticle)
      
      articleList.append(detailedArticle)
    
    return articleList
    
  def correctWord(self, word : str) -> (str, bool): # type: ignore

    response = requests.get(self.wordCorrectorURL + word)
    instance = BeautifulSoup(response.text, "html.parser")
    print(instance.prettify())
    mainTag = instance.find(id="gs_res_ccl_top")
    if mainTag == None:
      return "", True
    subTag = mainTag.find("a")
    if subTag == None:
      return "", True
    print(subTag.text)
    return (subTag.text, False) if subTag != None else ("", True)