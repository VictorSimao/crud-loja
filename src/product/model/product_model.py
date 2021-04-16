class Product:
    
    def __init__(self, name, description, price, categories, id=None):
        #TODO: make the categories attribute optional
        
        self.name = name
        self.description = description
        self.price = price
        self.categories = categories
        self.id = id
