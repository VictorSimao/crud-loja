
class ProductCategory:
    def __init__(self, product_id, category_id):
        self.product_id = product_id
        self.category_id = category_id

    def __str__(self):
        return f"{self.product_id} - {self.category_id}"
