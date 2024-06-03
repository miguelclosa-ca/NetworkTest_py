class Product:


    # Define variables of a product

    name = None
    price = None
    category = None

    def __init__(self, price, category, name):
        self.price = price
        self.category = category
        self.name = name


    def get_name(self):
        return self.name

    def set_name(self, newName):
        self.name = newName

    def get_price(self):
        return self.price

    def set_price(self, newPrice):
        self.price = newPrice

    def get_category(self):
        return self.category

    def set_category(self, newCategory):
        self.category = newCategory