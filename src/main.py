import pymysql
from typing import List
import os
from modules.products.model import Product
from modules.products.services import ProductServices
from modules.products.repository import ProductsRepository
from modules.db.services import DBServices
from modules.cli.services import CLIServices


option:int = -1
cli_services = CLIServices()
db_services = DBServices()
products_services = ProductServices()
products_repository = ProductsRepository(db_services, products_services)


while option != 0:
    try:
        cli_services.clear()
        print("Select an option:")
        print("1 - Create product")
        print("2 - Read products")
        print("3 - Update product")
        print("4 - Delete product")
        print("0 - Exit")

        option = int(input("Choose an option: "))
        if option == 1:
            product = cli_services.prompt_product()
            products_repository.create(product)

        elif option == 2:
            print("Creating product")
            products = products_repository.read()
            for product in products:
                print(str(product))

        elif option == 3:
            print("Editing product")
            id = int(input("Id:"))
            product = cli_services.prompt_product()
            products_repository.update(id, product)

        elif option == 4:
            print("Deleting product")
            id = int(input("Id:"))
            products_repository.delete(id)
        
        if option != 0:
            input("Press any key to go back...")
    except Exception as e:
        print("ERROR!\n")
        print(str(e))
        input("\nPress Enter to continue...")
        pass
