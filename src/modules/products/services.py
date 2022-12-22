from .model import Product

class ProductServices:
    def parse_row(self,product:Product) -> str:
        """Generates SQL query from Product instance, using fields set in object

        Args:
            product (Product): Product instance

        Returns:
            str: SQL query
        """
        sql = "SET "
        sql += f"name = '{product.name}',"
        sql += f"description = '{product.description}',"
        sql += f"price = '{product.price}'"
        return sql

    def parse_product(self,row:dict) -> Product:
        """Generates a Product instance from db row

        Args:
            row (dict): Db row

        Returns:
            Product: Product instance
        """
        product = Product()
        product.id = row["id"]
        product.name = row["name"]
        product.price = row["price"]
        product.description = row["description"]
        return product