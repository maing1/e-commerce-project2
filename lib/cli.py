import sys
from database.setup import create_tables
from models.customer import Customer
from models.product import Product
from models.order import Order

def show_menu():
    print("\nE-commerce CLI")
    print("1. Add a customer")
    print("2. Add a product")
    print("3. Create an order")
    print("4. Display all orders")
    print("5. Delete an order")
    print("6. Exit")

def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    address = input("Enter customer address: ")
    Customer.add_customer(name, email, address)
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
    order = Order(None, None, None, None, None)
    order.create_order(customer_id, product_id, quantity)

def display_orders():
    order = Order(None, None, None, None, None)
    order.display_all_orders()

def delete_order():
    order_id = int(input("Enter order ID to delete: "))
    order = Order(None, None, None, None, None)
    order.delete_order_by_id(order_id)

def main():
    # Initialize the database tables if they don't exist
    order = Order(None, None, None, None, None)
    order.create_table()

    # Main loop
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            add_product()
        elif choice == "3":
            create_order()
        elif choice == "4":
            display_orders()
        elif choice == "5":
            delete_order()
        elif choice == "6":
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
