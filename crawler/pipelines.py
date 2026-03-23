# pylint: disable=too-few-public-methods

import logging

from scrapy.exceptions import DropItem

from crawler.database import ProductRepository


logger = logging.getLogger(__name__)


class CleanDataPipeline:
    def process_item(self, item):
        item["product_name"] = item["product_name"].strip()
        return item


class ValidatePipeline:
    def process_item(self, item):
        if not item.get("product_id"):
            logger.info("Missing product_id")
            raise DropItem("Missing product_id")

        if not item.get("price"):
            logger.info("Missing price")
            raise DropItem("Missing price")

        if not item.get("product_url"):
            logger.info("Missing product_url")
            raise DropItem("Missing product_url")

        if not item.get("company_id"):
            logger.info("Missing company_id")
            raise DropItem("Missing company_id")

        if not item.get("company_name"):
            logger.info("Missing company_name")
            raise DropItem("Missing company_name")

        return item


class DuplicatesPipeline:
    def __init__(self):
        self.repo = None

    def open_spider(self):
        self.repo = ProductRepository()

    def process_item(self, item):
        if self.repo.get_product_by_id(item["product_id"]) is not None:
            logger.info("Duplicate item")
            raise DropItem("Duplicate item")

        return item


class SaveToDatabasePipeline:
    def __init__(self):
        self.repo = None

    def open_spider(self):
        self.repo = ProductRepository()

    def process_item(self, item):
        self.repo.insert_product(item)
        return item

    def close_spider(self):
        self.repo.close()
