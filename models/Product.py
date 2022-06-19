class Product(object):
    title = ""
    image = ""
    price = 0

    def __init__(self, title, image, price):
        self.title = title
        self.image = image
        self.price = price

def make_product(title, image, price):
    product = Product(title, image, price)
    return product