from helpers import (
    create_product,
    list_products,
    create_customer,
    list_customers,
    create_order,
    list_orders,
    exit_program
)

def main():
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
            create_customer()
        elif choice == "4":
            list_customers()
        elif choice == "5":
            create_order()
        elif choice == "6":
            list_orders()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a Product")
    print("2. List Products")
    print("3. Create a Customer")
    print("4. List Customers")
    print("5. Create an Order")
    print("6. List Orders")

if __name__ == "__main__":
    main()
