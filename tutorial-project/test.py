import requests
from parsel import Selector


def parse(response: requests.Response) -> dict:
    selector = Selector(response.text)
    return {
        "url": response.url,
        "title": selector.css("h1").get(),
    }


def download(url: str) -> requests.Response:
    return requests.get(url)


url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = download(url)
item = parse(response)

print(item)
