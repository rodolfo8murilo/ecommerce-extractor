import logging
from scrapy.exceptions import DropItem
from crawler.database import ProductRepository

logging.basicConfig(level=logging.DEBUG)
    
class CleanDataPipeline:

    def process_item(self, item, spider):

        item["product_name"] = item["product_name"].strip()

        return item    



class ValidatePipeline:

    def process_item(self, item, spider):

        if not item.get("product_id"):
            logging.info("Missing product_id")
            raise DropItem("Missing product_id")

        if not item.get("price"):
            logging.info("Missing price")
            raise DropItem("Missing price")
        
        if not item.get("product_url"):
            logging.info("Missing product_url")
            raise DropItem("Missing product_url")
        
        if not item.get("company_id"):
            logging.info("Missing company_id")
            raise DropItem("Missing company_id")
        
        if not item.get("company_name"):
            logging.info("Missing company_name")
            raise DropItem("Missing company_name")

        return item
    
class DuplicatesPipeline:

    def open_spider(self, spider):
        self.repo = ProductRepository()

    def process_item(self, item, spider):
        if self.repo.get_product_by_id(item["product_id"]) != None:
            logging.info("Missing company_name")
            raise DropItem("Duplicate item")
        return item

class SaveToDatabasePipeline:

    def open_spider(self, spider):
        self.repo = ProductRepository()

    def process_item(self, item, spider):

        self.repo.insert_product(
            product_id=item["product_id"],
            product_name=item["product_name"],
            price=item["price"],
            price_with_discount=item["price_with_discount"],
            old_price=item["old_price"],
            product_url=item["product_url"],
            company_id=item['company_id'],
            company_name=item['company_name']
        )
        
        return item

    def close_spider(self, spider):
        self.repo.close()
    