import logging
import sqlite3


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class ProductRepository:
    def __init__(self, db_path: str = "products.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INT NOT NULL UNIQUE,
                product_name TEXT NOT NULL,
                price REAL,
                price_with_discount REAL,
                old_price REAL,
                product_url TEXT,
                company_id TEXT,
                company_name TEXT
            )
            """
        )
        self.conn.commit()

    def insert_product(
        self,
        product
    ):
        try:
            product_id = product['product_id']
            product_name = product['product_name']
            product_url = str(product['product_url'])

            raw_price = product.get("price")
            price = raw_price if raw_price is not None else None

            raw_price_with_discount = product.get("price_with_discount")
            raw_old_price = product.get("old_price")

            price_with_discount = (
                raw_price_with_discount
                if raw_price_with_discount is not None
                else None
            )

            old_price = (
                float(raw_old_price)
                if raw_old_price is not None
                else None
            )

            company_id = product['company_id']
            company_name = product['company_name']

            query = """
            INSERT INTO products (
                product_id,
                product_name,
                price,
                price_with_discount,
                old_price,
                product_url,
                company_id,
                company_name
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """

            self.cursor.execute(
                query,
                (
                    product_id,
                    product_name,
                    price,
                    price_with_discount,
                    old_price,
                    product_url,
                    company_id,
                    company_name,
                ),
            )
            self.conn.commit()

        except (ValueError, sqlite3.DatabaseError) as error:
            logger.error("Error inserting product: %s", error)

    def get_product_by_id(self, product_id: str):
        query = """
        SELECT
            product_id,
            product_name,
            price,
            price_with_discount,
            old_price,
            product_url,
            company_id,
            company_name
        FROM products
        WHERE product_id = ?
        """

        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()
