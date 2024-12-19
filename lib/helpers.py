from models.product import Product
from models.customer import Customer
from models.order import Order

def create_product():
    name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the stock quantity: "))
    Product.create(name, description, price, stock)
    print(f"Product '{name}' created!")

def list_products():
    products = Product.get_all()
    for product in products:
        print(f"{product.id}: {product.name} - ${product.price} - Stock: {product.stock}")
