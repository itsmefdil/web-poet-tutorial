import requests
from web_poet import Injectable, HttpResponse


class BookPage(Injectable):
    def __init__(self, response: HttpResponse):
        self.response = response

    def to_item(self) -> dict:
        return {
            "url": self.response.url,
            "title": self.response.css("h1").get(),
        }


def download(url: str) -> Response:
    response = requests.get(url)
    return HttpResponse(
        url=response.url,
        body=response.content,
        headers=response.headers,
    )


url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
response = download(url)
book_page = BookPage(response=response)
item = book_page.to_item()
