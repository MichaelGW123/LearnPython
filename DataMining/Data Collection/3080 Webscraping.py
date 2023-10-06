# Michael Williamson
# Web Scraper using bs4 for 3080
# 1/11/2021

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440
websiteURL = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'
print("Scraping data from " + websiteURL)

ua = UserAgent()
header = {'User-Agent': str(ua.chrome), 'authority': 'www.bestbuy.com'}
page = requests.get(websiteURL, headers = header)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup)
