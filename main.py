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

@app.get("/word-check")
def read_article(word : Union[str, None] = None):

  res = scraper.correctWord(word)
  print(res)

  return {
    "correctWord" : res[0],
    "isCorrect" : res[1] 
  }
