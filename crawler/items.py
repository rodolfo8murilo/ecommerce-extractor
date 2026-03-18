# pylint: disable=too-few-public-methods

from typing import Optional

from pydantic import BaseModel, HttpUrl


class ProductItem(BaseModel):
    product_id: int
    product_name: str
    price: float
    price_with_discount: Optional[float] = None
    old_price: Optional[float] = None
    product_url: HttpUrl
    company_id: str
    company_name: str
