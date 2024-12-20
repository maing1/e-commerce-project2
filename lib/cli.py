from helpers import (
    exit_program,
    create_tables,
    create_product,
    list_products,
    add_customer,
    add_product,
    update_stock,
    create_order,
    display_orders,
    delete_order
)

def main():
    create_tables()

    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_product()
        elif choice == "2":
            list_products()
        elif choice == "3":
            add_customer()
        elif choice == "4":
            add_product()
        elif choice == "5":
            update_stock()
        elif choice == "6":
            create_order()
        elif choice == "7":
            display_orders()
        elif choice == "8":
            delete_order()
        else:
            print("Invalid choice. Please try again.")

def menu():
    print("\n--- Main Menu ---")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a new product")
    print("2. List all products")
    print("3. Add a new customer")
    print("4. Add a new product (alternate)")
    print("5. Update Product Stock")
    print("6. Create a new order")
    print("7. Display all orders")
    print("8. Delete an order")

if __name__ == "__main__":
    main()
