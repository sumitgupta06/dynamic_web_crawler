#a dynamic web crawler would work for an entire website instead of specifing a page
#it also collects all the nesecarry info form the linked pages(like all the links on the linked page) of the website
import requests
from bs4 import BeautifulSoup


def spider(max_pages):
    page = 1
    while page <= max_pages:
        url = "https://buckysroom.org/trade/search.php?page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class': 'item-name'}):
            href = "https://buckysroom.org" + link.get('href')
            title = link.string
            print(href)
            print(title)
            get_single_item_date(href)
        page += 1


def get_single_item_date(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div', {'class': 'i-name'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = "https://buckysroom.org" + link.get('href')
        print(href)

spider(3)
