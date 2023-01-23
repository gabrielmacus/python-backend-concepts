from ..base.model import BaseModel

class Product(BaseModel):
    name:str = None
    description:str = None
    price:float = None