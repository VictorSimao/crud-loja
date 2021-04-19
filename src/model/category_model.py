"""
This class convert an object to Category type.
"""


class Category:

    def __init__(self, name, description, id=None):
        self.name = name
        self.description = description
        self.id = id
<<<<<<< HEAD:src/models/category_model.py
=======

    def __str__(self):
        return f"{self.id} - {self.name} - {self.description}"
>>>>>>> main:src/model/category_model.py
