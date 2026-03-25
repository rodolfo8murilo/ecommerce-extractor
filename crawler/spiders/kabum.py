import uuid
from scrapy import Spider, Request
from pydantic import ValidationError
from crawler.items import ProductItem


class KabumSpider(Spider):
    name = "kabum"
    allowed_domains = ["servicespub.prod.api.aws.grupokabum.com.br"]
    BASE_URL_API = (
        "https://servicespub.prod.api.aws.grupokabum.com.br"
        "/catalog/v2/products-by-category/"
    )
    BASE_NAME = "Kabum"
    BASE_URL = "https://www.kabum.com.br"

    CATEGORIES = ["hardware", "perifericos", "computadores"]

    def __init__(self, *args, pages=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = int(pages) if pages else None

    async def start(self):
        for category in self.CATEGORIES:
            url = f"{self.BASE_URL_API}{category}?page_number=1&page_size=100"

            yield Request(
                url=url,
                callback=self.parse,
                meta={"category": category},
            )

    def parse(self, response):
        products = response.json()
        category = response.meta["category"]
        total_page = products["meta"]["total_pages_count"]
        current_page = products["meta"]["page"]["number"]

        if self.pages:
            total_page = self.pages

        for product in products["data"]:
            product_url = self.BASE_URL + f"/produto/{product['id']}"
            product_fields = {
                "product_id": product["id"],
                "product_name": product["attributes"]["title"],
                "price": product["attributes"]["price"],
                "price_with_discount": product["attributes"]["price_with_discount"],
                "old_price": product["attributes"]["old_price"],
                "product_url": product_url,
                "company_id": str(uuid.uuid5(uuid.NAMESPACE_DNS, self.name)),
                "company_name": self.BASE_NAME,
            }
            try:
                product = ProductItem(**product_fields)
                yield product.model_dump()
            except ValidationError:
                self.logger.error("Product Attribute required.")

        if current_page < total_page:
            next_url = f"{self.BASE_URL_API}{category}?page_number={current_page + 1}&page_size=100"
            yield Request(
                url=next_url, callback=self.parse, meta={"category": category}
            )
