class Category:
    def __init__(self, name, description, id=None):
        self.name = name
        self.description = description
        self.id = id
        
    def list_category(self):
        categories = self.category_dao.read_all()
        for cat in categories:
            data = f"{cat.id} - {cat.name} - {cat.description}"
            print(data)

    def register_category(self):
        category_name = input("Escreva o nome da categoria:")
        category_description = input("Escreva a descrição da categoria:")
        category = Category(category_name, category_description)
        self.category_id = self.category_dao.create(category)