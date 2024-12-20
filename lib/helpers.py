from models.product import Product
from models.customer import Customer
from models.order import Order

def exit_program():
    print("Goodbye!")
    exit()

def create_tables():
    """Create tables for Product, Customer, and Order models."""
    print("Creating tables...")
    Product.create_table()
    Customer.create_table()
    Order.create_table()
    print("All tables created successfully!")

def create_product():
    name = input("Enter the product name: ")
    description = input("Enter the product description: ")
    price = float(input("Enter the product price: "))
    stock = int(input("Enter the stock quantity: "))
    Product.add_product(name, description, price, stock)
    print(f"Product '{name}' created!")

def list_products():
    """Display all products."""
    print("\nListing all products:")
    products = Product.display_all_products()
    if not products:
        print("No products available.")
        return

    for product in products:
        print(f"ID: {product[0]}, Name: {product[1]}, Description: {product[2]}, Price: ${product[3]}, Stock: {product[4]}")

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

def update_stock():
    """Update the stock of a product."""
    product_id = int(input("Enter the product ID: "))
    new_stock = int(input("Enter the new stock quantity: "))

    # Find the product by ID
    product = Product.find_by_id(product_id)
    if not product:
        print(f"Product with ID {product_id} does not exist.")
        return

    # Update the stock
    Product.update_stock(product_id, new_stock)
    print(f"Stock for '{product.name}' has been updated to {new_stock}.")


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
    Order.create_order(customer_id, product_id, quantity)


def display_orders():
    Order.display_all_orders()

def delete_order():
    order_id = int(input("Enter order ID to delete: "))
    Order.delete_order_by_id(order_id)


