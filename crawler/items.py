from pydantic import BaseModel, Field, HttpUrl
from typing import Optional

class ProductItem(BaseModel):

    product_id: int = Field(required=True)
    product_name : str = Field(required=True)
    price : float = Field(required=True)
    price_with_discount : Optional[float] = None
    old_price : Optional[float] = None
    product_url : HttpUrl = Field(required=True)
    company_id: str = Field(required=True)
    company_name: str = Field(required=True)