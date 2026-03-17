import sqlite3
import logging
from typing import Optional


class ProductRepository:
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, db_path: str = "products.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute("""
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
        """)
        self.conn.commit()

    def insert_product(
        self,
        product_id: int,
        product_name: str,
        price: float,
        price_with_discount: Optional[float],
        old_price: Optional[float],
        product_url: str,
        company_id: str,
        company_name: str,
    ):
        try:
            # validação de tipos
            product_id = str(product_id)
            product_name = str(product_name)
            product_url = str(product_url)
            
            price_with_discount = float(price_with_discount)
            old_price = float(old_price)
            if price is not None:
                price = float(price)
            company_id = str(company_id)
            company_name = str(company_name)
            query = """
            INSERT INTO products (product_id, product_name, price, price_with_discount, old_price, product_url, company_id, company_name)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """

            self.cursor.execute(query, (product_id, product_name, price, price_with_discount, old_price, product_url, company_id, company_name))
            self.conn.commit()

        except (ValueError, sqlite3.DatabaseError) as e:
            logging.error(f"Error Insert product: {e}")

    def get_product_by_id(self, product_id: str):
        query = """
        SELECT product_id, product_name, price, price_with_discount, old_price, product_url, company_id, company_name 
        FROM products
        WHERE product_id = ?
        """

        self.cursor.execute(query, (product_id,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()