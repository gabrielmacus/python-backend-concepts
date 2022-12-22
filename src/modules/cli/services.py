import os
from ..products.model import Product

class CLIServices:
    def prompt_product(self) -> Product:
        """Prompts fields to instantiate Product

        Returns:
            Product: Product instance
        """
        product = Product()
        product.name = input("Name: ")
        product.description = input("Description: ")
        product.price = float(input("Price ($): "))
        return product

    def clear(self):
        """Clears console
        """
        os.system('clear' if os.name == 'posix' else 'cls')