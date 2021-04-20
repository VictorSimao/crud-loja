
class Category:
    def __init__(self, name, description, id=None):
        self.name = name
        self.description = description
        self.id = id

    def __str__(self):
        return f"{self.id} - {self.name} - {self.description}"
