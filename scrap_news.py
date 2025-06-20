import requests
from bs4 import BeautifulSoup


def financial_express(session=None):
    url = "https://economictimes.indiatimes.com/?from=mdr"
    if not session:
        session = requests.Session()

    session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36'})
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_news_elem = soup.find_all(class_="storyItem")
    return [ news.text for news in all_news_elem ]
        