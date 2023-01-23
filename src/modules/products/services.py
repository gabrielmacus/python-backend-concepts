from ..base.services import BaseServices
from .model import Product

class ProductServices(BaseServices):

    def __init__(self):
        pass

    def item_to_row(self,item:Product) -> dict:
        data = BaseServices.item_to_row(self,item)
        data['name'] = f"'{item.name}'"
        data['description'] = f"'{item.description}'"
        data['price'] = f"{item.price}"
        return data

    def row_to_item(self,row:dict) -> Product:
        item:Product = BaseServices.row_to_item(self,row)
        item.name = row['name']
        item.description = row['description']
        item.price = row['price']
        return item