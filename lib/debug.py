import sqlite3

# Connect to the database
CONN = sqlite3.connect('customer.db')
CURSOR = CONN.cursor()

def display_customers():
    """Display all customers in the database."""
    print("\n--- Customers ---")
    try:
        rows = CURSOR.execute("SELECT * FROM customer").fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Phone: {row[3]}")
    except sqlite3.Error as e:
        print(f"Error fetching customers: {e}")

def display_products():
    """Display all products in the database."""
    print("\n--- Products ---")
    try:
        rows = CURSOR.execute("SELECT * FROM product").fetchall()
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}, Price: ${row[3]}, Stock: {row[4]}")
    except sqlite3.Error as e:
        print(f"Error fetching products: {e}")

def display_orders():
    """Display all orders in the database."""
    print("\n--- Orders ---")
    try:
        rows = CURSOR.execute(
            """
            SELECT o.id, c.name AS customer_name, p.name AS product_name, o.quantity, o.total_price
            FROM 'order' o
            JOIN customer c ON o.customer_id = c.id
            JOIN product p ON o.product_id = p.id
            """
        ).fetchall()
        for row in rows:
            print(f"Order ID: {row[0]}, Customer: {row[1]}, Product: {row[2]}, Quantity: {row[3]}, Total Price: ${row[4]:.2f}")
    except sqlite3.Error as e:
        print(f"Error fetching orders: {e}")

def test_create_customer():
    """Test adding a new customer."""
    try:
        CURSOR.execute(
            "INSERT INTO customer (name, email, phone) VALUES (?, ?, ?)",
            ("Test User", "testuser@example.com", "5555555555"),
        )
        CONN.commit()
        print("\nTest customer created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating test customer: {e}")

def test_create_product():
    """Test adding a new product."""
    try:
        CURSOR.execute(
            "INSERT INTO product (name, description, price, stock) VALUES (?, ?, ?, ?)",
            ("Test Product", "This is a test product.", 99, 10),
        )
        CONN.commit()
        print("\nTest product created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating test product: {e}")

def test_create_order():
    """Test creating an order."""
    try:
        CURSOR.execute(
            "INSERT INTO 'order' (customer_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)",
            (1, 1, 1, 99),
        )
        CONN.commit()
        print("\nTest order created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating test order: {e}")

def clear_test_data():
    """Clear test data from the database."""
    try:
        CURSOR.execute("DELETE FROM customer WHERE name = 'Test User'")
        CURSOR.execute("DELETE FROM product WHERE name = 'Test Product'")
        CURSOR.execute("DELETE FROM 'order' WHERE customer_id = 1 AND product_id = 1")
        CONN.commit()
        print("\nTest data cleared.")
    except sqlite3.Error as e:
        print(f"Error clearing test data: {e}")

def main():
    print("Debugging Skincare Database")
    display_customers()
    display_products()
    display_orders()
    
    print("\nRunning tests...")
    test_create_customer()
    test_create_product()
    test_create_order()
    
    print("\nUpdated data after tests:")
    display_customers()
    display_products()
    display_orders()

    print("\nClearing test data...")
    clear_test_data()

if __name__ == "__main__":
    main()
