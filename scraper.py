import requests
import json
from bs4 import BeautifulSoup
from article import Article

class Scraper():

  searchURL = "https://scholar.google.com/scholar?start=10&q="

  def scrap(self, word : str) -> list[Article] :

    articleList : list[Article] = []

    response = requests.get(self.searchURL + word.replace(" ", "+"))
    instance = BeautifulSoup(response.text, "html.parser")
    
    article_htmls = instance.find_all(class_="gs_r gs_or gs_scl")
    for article_html in article_htmls:
      newArticle = Article()
      
      newArticle.name = article_html.find("h3").text
      newArticle.citationsNumber = int(article_html.find(class_="gs_fl gs_flb").find_all("a")[2].text.split(" ")[2])
      newArticle.authors = list(map(lambda tag: tag.text, article_html.find(class_="gs_a").find_all("a")))
      # Google Scholarda bulunan tüm özellikleri ata

      # Google Scholar'dan gelen article linkin strategy managareine gönder
      
      articleList.append(newArticle)
    
    article_jsons = []
    for article in articleList:
      article_jsons.append(article.__dict__)

    print(json.dumps(article_jsons, ensure_ascii=False))
    