from concurrent.futures import ThreadPoolExecutor
import re
import requests
from bs4 import BeautifulSoup

##
# Prints current day list of advertisments in ss.lv for Cesis and Sigulda cities
##

listings = []


def scrapeWebsite(url, region):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ads = soup.find_all(id=re.compile("tr_[0-9]+$"))

    for ad in ads:
        stats = ad.find_all("td", {"class": "msga2-o pp6"})

        formattedStats = [stat.get_text() for stat in stats]

        listings.append('{} | {}'.format(region, ' | '.join(formattedStats)))


websites = {
    "Sigulda": "https://www.ss.lv/lv/real-estate/flats/riga-region/sigulda/today/hand_over/",
    "Cesis": "https://www.ss.lv/lv/real-estate/flats/cesis-and-reg/cesis/today/hand_over/"
}

with ThreadPoolExecutor() as executor:
    for region, url in websites.items():
        executor.submit(scrapeWebsite, url, region)

for listing in listings:
    print(listing)
