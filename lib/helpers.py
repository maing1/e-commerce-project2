from models.product import Product
from models.customer import Customer
from models.order import Order

def exit_program():
    print("Goodbye!")
    exit()

def create_product():
    name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the stock quantity: "))
    Product.add_product(name, description, price, stock)
    print(f"Product '{name}' created!")

def list_products():
    product = Product.display_all_products()
    for product in product:
        print(f"{product.id}: {product.name} - ${product.price} - Stock: {product.stock}")

def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    address = input("Enter customer address: ")
    Customer.insert_customer(name, email, address)
    print(f"Customer {name} added successfully.")

def add_product():
    name = input("Enter product name: ")
    description = input("Enter product description: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock quantity: "))
    Product.add_product(name, description, price, stock)
    print(f"Product {name} added successfully.")

def create_order():
    customer_id = int(input("Enter customer ID: "))
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))

    # Reuse validation logic here
    # Find customer by ID
    customer = Customer.find_by_id(customer_id)
    if not customer:
        print(f"Customer with ID {customer_id} does not exist.")
        return  # Exit the function if customer doesn't exist

    # Find product by ID
    product = Product.find_by_id(product_id)
    if not product:
        print(f"Product with ID {product_id} does not exist.")
        return  # Exit the function if product doesn't exist

    # Check if quantity is valid
    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return  # Exit the function if quantity is invalid

    # If all validations pass, create the order
    order = Order(None, None, None, None, None)
    order.create_order(customer_id, product_id, quantity)


def display_orders():
    order = Order(None, None, None, None, None)
    order.display_all_orders()

def delete_order():
    order_id = int(input("Enter order ID to delete: "))
    order = Order(None, None, None, None, None)
    order.delete_order_by_id(order_id)


