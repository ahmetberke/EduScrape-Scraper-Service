from article import Article
from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
  
  def __init__(self, name, link) -> None:
    self.name = name
    self.link = link

  @abstractmethod
  def scraper(self, article : Article) -> Article :
    pass