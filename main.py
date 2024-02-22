import requests
from bs4 import BeautifulSoup
from scraper import Scraper

if __name__ == "__main__":
  scrapper = Scraper()
  scrapper.scrap("makine öğrenmesi")
