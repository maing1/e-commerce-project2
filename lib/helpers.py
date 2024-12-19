from models.product import Product
from models.customer import Customer
from models.order import Order

# def create_product():
#     name = input("Enter the product name: ")
#     description = input("Enter the product description: ")
#     price = float(input("Enter the product price: "))
#     stock = int(input("Enter the stock quantity: "))
#     Product.create(name, description, price, stock)
#     print(f"Product '{name}' created!")

# def list_products():
#     products = Product.get_all()
#     for product in products:
#         print(f"{product.id}: {product.name} - ${product.price} - Stock: {product.stock}")


def get_input(prompt, input_type=str, valid_values=None):
    """
    A helper function to get input from the user and validate it.
    
    :param prompt: The prompt to display to the user
    :param input_type: The type to which the input should be converted (default is str)
    :param valid_values: A list of valid values (optional, defaults to None)
    :return: The valid input value
    """
    while True:
        user_input = input(prompt)
        try:
            # Convert the input to the required type
            user_input = input_type(user_input)
            
            # If valid_values is provided, check if the input is in the list
            if valid_values and user_input not in valid_values:
                print(f"Invalid value. Please choose from {valid_values}.")
                continue
            
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__} value.")

def display_error(message):
    """
    A helper function to display error messages.

    :param message: The error message to display
    """
    print(f"Error: {message}")

def display_success(message):
    """
    A helper function to display success messages.

    :param message: The success message to display
    """
    print(f"Success: {message}")

def display_data(data, headers=None):
    """
    A helper function to display data in a formatted table-like structure.

    :param data: The data to display (list of tuples or dictionaries)
    :param headers: A list of headers (optional)
    """
    if headers:
        print(" | ".join(headers))
        print("-" * (len(headers) * 10))
    
    for row in data:
        if isinstance(row, tuple):
            print(" | ".join(str(cell) for cell in row))
        elif isinstance(row, dict):
            print(" | ".join(f"{key}: {value}" for key, value in row.items()))
        else:
            print(row)

def prompt_continue():
    """
    A helper function to ask the user if they want to continue.
    """
    continue_choice = get_input("Do you want to continue? (y/n): ", input_type=str, valid_values=["y", "n"])
    return continue_choice.lower() == "y"

def confirm_deletion(entity_name):
    """
    A helper function to confirm if the user wants to delete an entity.
    
    :param entity_name: The name of the entity to delete (e.g., "product", "order")
    :return: True if the user confirms, False otherwise
    """
    confirmation = get_input(f"Are you sure you want to delete this {entity_name}? (y/n): ", input_type=str, valid_values=["y", "n"])
    return confirmation.lower() == "y"

