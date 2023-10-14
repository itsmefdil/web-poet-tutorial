from web_poet import field, handle_urls, WebPage

from ..items import Book


@handle_urls("books.toscrape.com")
class BookPage(WebPage[Book]):
    @field
    async def title(self):
        return self.css("h1::text").get()

    @field
    async def price(self):
        return float(self.css(".price_color::text").re_first(r"£(\d+\.\d+)"))

    @field
    async def description(self):
        return self.css(".product_page > p::text").get()
