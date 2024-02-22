import json

class Article:
  def __init__(self,
                name : str = "", 
                authors : list[str] = [], 
                type: str = "", 
                publishedDate : str = "",
                publisherName : str = "",
                browserKeyWords : list[str] = [],
                articleKeyWords : list[str] = [],
                summary: str = [],
                references : list[str] = [],
                citationsNumber : int = 0,
                doi : str = "",
                url : str = "" 
              ) -> None:

    self.name = name
    self.authors = authors
    self.type = type
    self.publishedDate = publishedDate
    self.publisherName = publisherName
    self.browserKeyWords = browserKeyWords
    self.articleKeyWords = articleKeyWords
    self.summary = summary
    self.references = references
    self.citationsNumber = citationsNumber
    self.doi = doi
    self.url = url

    pass

  def JSON(self):
    return json.dumps(self.__dict__).encode('utf8')