from article import Article
from abc import ABC

class Strategy(metaclass=ABC):
  
  def __init__(self, name, link) -> None:
    self.name = name
    self.link = link

  @abstractmethod
  def scraper(article : Article) -> Article :
    pass