from dataclasses import dataclass


@dataclass
class ProductItem:
    name: str
    stock: int
    shop: str
    price: int
