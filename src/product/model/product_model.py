class Product:
    def __init__(
        self,
        name:str, 
        description:str, 
        price :float, 
        categories: int=None, 
        id: int=None
        ):

        self.name = name
        self.description = description
        self.price = price
        self.categories = categories
        self.id = id