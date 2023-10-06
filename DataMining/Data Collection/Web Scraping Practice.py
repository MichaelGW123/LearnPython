# Michael Williamson
# Web Scraper using bs4
# 1/2/2021

import requests
from bs4 import BeautifulSoup

#https://realpython.com/beautiful-soup-web-scraper-python/

#https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia
#websiteURL = input("What website would you like to scrape? ")
websiteURL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
print("Scraping data from " + websiteURL)

page = requests.get(websiteURL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')
#print(results.prettify())
software_jobs = results.find_all('h2', string = lambda text: 'software' in text.lower())

job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

print(len(software_jobs))

for s_job in software_jobs:
    link = s_job.find('a')['href']
    print(s_job.text.strip())
    print(f"Apply here: {link}\n")