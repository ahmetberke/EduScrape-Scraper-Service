from article import Article
from strategy import Strategy

class DergiParkStrategy(Strategy):

  def __init__(self) -> None:
    super().__init__("dergipark", "")

  def scraper(article : Article) -> Article:



    return Article(
      name="",
      authors=[],
      type="",
      publishedDate="",
      publisherName="",
      browserKeyWords="",
      articleKeyWords="",
      summary="",
      references="",
      citationsNumber=0,
      doi="",
      url=""
    )