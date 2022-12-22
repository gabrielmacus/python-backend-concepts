from .model import Product
from ..db.services import DBServices
from .services import ProductServices
from typing import List



class ProductsRepository:
    module_services:ProductServices = None
    db_services:DBServices = None

    def __init__(self, db_services:DBServices, module_services:ProductServices) -> None:
        self.db_services = db_services
        self.module_services = module_services

    def create(self,product:Product) -> int:
        """Inserts product instance into db

        Args:
            product (Product): Product instance

        Returns:
            int: Created products
        """
        row = self.module_services.parse_row(product)
        return self.db_services.execute_db(f"INSERT INTO products {row}")
        
    def read(self) -> List[Product]:
        """Reads products from db

        Returns:
            List[Product]: Products list
        """
        products:List[Product] = []
        rows = self.db_services.query_db("SELECT * FROM products")
        for row in rows:
            products.append(self.module_services.parse_product(row))
        return products

    def update(self, id:int, product:Product) -> int:
        """Updates product from database

        Args:
            id (int): Id of the product to be updated
            product (Product): Product instance

        Returns:
            int: Updated rows. Should be 1
        """
        row = self.module_services.parse_row(product)
        return self.db_services.execute_db(f"UPDATE products {row} WHERE id = {id}")

    def delete(self,id:int):
        self.db_services.execute_db(f"DELETE FROM products WHERE id = {id}")