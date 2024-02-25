from typing import Union
from fastapi import FastAPI

from scraper import Scraper

app = FastAPI()

scraper = Scraper()

@app.get("/article")
def read_article(search : Union[str, None] = None):
  
  if (search == ""):
    return []
  
  articles = scraper.scrap(search)

  return articles
