import requests
from bs4 import BeautifulSoup
from article import Article
from strategy import Strategy

class DergiParkStrategy(Strategy):

  def __init__(self) -> None:
    super().__init__("dergipark", "https://dergipark.org.tr")

  def scraper(self, article : Article) -> Article :
    response = requests.get(article.url)
    if (response.status_code != 200):
      return article
  
    soup = BeautifulSoup(response.text, "html.parser")
    
    doi_a_tag = soup.find("a", class_="doi-link")
    article.doi = doi_a_tag.text if doi_a_tag != None else ""

    summary_div = soup.find("div", class_="article-abstract data-section")
    if summary_div:
      article.summary = summary_div.find("p").text if summary_div.find("p") != None else ""

    keywords_div = soup.find("div", class_="article-keywords data-section")
    if keywords_div:
      article.articleKeyWords = list(map(lambda tag: tag.text, keywords_div.find_all("a")))

    references_div = soup.find("div", class_="article-citations data-section")
    if references_div:
      article.references = list(map(lambda tag: tag.text, references_div.find_all("li")))

    publication_date_title = soup.find("th", string="Publication Date")
    if publication_date_title:
      publication_date_value = publication_date_title.parent.find("td")
      article.publishedDate = publication_date_value.text if publication_date_value else ""


    return article

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