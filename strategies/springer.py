import requests
from bs4 import BeautifulSoup
from article import Article
from strategy import Strategy
import time
import datetime

class Springer(Strategy):

  def __init__(self) -> None:
    super().__init__("springer", "https://link.springer.com")

  def scraper(self, article : Article) -> Article :
    response = requests.get(article.url)
    if (response.status_code != 200):
      return article
  
    soup = BeautifulSoup(response.text, "html.parser")

    return article
