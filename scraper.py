import requests
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
      # Google Scholarda bulunan tüm özellikleri ata

      # Google Scholar'dan gelen article linkin strategy managareine gönder
      
      articleList.append(newArticle)
    
    for article in articleList:
      print("> ", article.name)

    