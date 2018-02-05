import requests
from bs4 import BeautifulSoup
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_pages(s):
    url = "https://newyork.craigslist.org/search/stp"
    response = requests.get(url, params={'s': s}, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    titles = soup.select(".result-title")

    output = []

    for title in titles:
        clean_title = title.text.strip().encode('utf-8')
        output.append(clean_title)

    return output

start = 0
while start < 1000:
    result = get_pages(start)
    for r in result:
        print r

    time.sleep(0.5)
    start = start + 120
