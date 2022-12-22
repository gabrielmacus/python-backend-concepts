class Product:
    id:int = None
    name:str = None
    description:str = None
    price:float = None

    def __repr__(self) -> str:
        return f"{self.id} - {self.name} - {self.description} - ${str(self.price)}"