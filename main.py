import pymysql
from typing import List
import os
'''
Model
'''
class Product:
    id:int = None
    name:str = None
    description:str = None
    price:float = None

    def __repr__(self) -> str:
        return f"{self.id} - {self.name} - {self.description} - ${str(self.price)}"

'''
DB
'''
def connect_db() -> pymysql.Connection:
    """Establishes connection with mysql db

    Returns:
        pymysql.Connection: DB connection object
    """
    return pymysql.connect(
        host='localhost',
        port=8306,
        user='root',
        password='123456',
        database='python-backend-concepts',
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_db(sql:str) -> int:
    """Executes a write operation in db

    Args:
        sql (str): SQL query

    Returns:
        int: Number of affected rows
    """
    connection = connect_db()
    with connection.cursor() as cursor:
        cursor.execute(sql)
    connection.commit()
    return connection.affected_rows()

def query_db(sql:str) -> List[dict]:
    """Executes a read operation in db

    Args:
        sql (str): SQL query

    Returns:
        List[dict]: Array of fetched rows
    """
    connection = connect_db()
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()

def parse_row_product(product:Product) -> str:
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

def parse_product_row(row:dict) -> Product:
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

'''
CRUD
'''
def create_product(product:Product) -> int:
    """Inserts product instance into db

    Args:
        product (Product): Product instance

    Returns:
        int: Created products
    """
    row = parse_row_product(product)
    return execute_db(f"INSERT INTO products {row}")
    
def read_products() -> List[Product]:
    """Reads products from db

    Returns:
        List[Product]: Products list
    """
    products:List[Product] = []
    rows = query_db("SELECT * FROM products")
    for row in rows:
        products.append(parse_product_row(row))
    return products

def update_product(id:int, product:Product) -> int:
    """Updates product from database

    Args:
        id (int): Id of the product to be updated
        product (Product): Product instance

    Returns:
        int: Updated rows. Should be 1
    """
    row = parse_row_product(product)
    return execute_db(f"UPDATE products {row} WHERE id = {id}")

def delete_product(id:int):
    execute_db(f"DELETE FROM products WHERE id = {id}")


''' Command line interface '''
def prompt_product() -> Product:
    """Prompts fields to instantiate Product

    Returns:
        Product: Product instance
    """
    product = Product()
    product.name = input("Name: ")
    product.description = input("Description: ")
    product.price = float(input("Price ($): "))
    return product

def clear():
    """Clears console
    """
    os.system('clear' if os.name == 'posix' else 'cls')

option:int = -1
while option != 0:
    try:
        clear()
        print("Select an option:")
        print("1 - Create product")
        print("2 - Read products")
        print("3 - Update product")
        print("4 - Delete product")
        print("0 - Exit")

        option = int(input("Choose an option: "))
        if option == 1:
            product = prompt_product()
            create_product(product)

        elif option == 2:
            print("Creating product")
            products = read_products()
            for product in products:
                print(str(product))

        elif option == 3:
            print("Editing product")
            id = int(input("Id:"))
            product = prompt_product()
            update_product(id, product)

        elif option == 4:
            print("Deleting product")
            id = int(input("Id:"))
            delete_product(id)
        
        if option != 0:
            input("Press any key to go back...")
    except:
        input("Error. Press Enter to continue...")
        pass
