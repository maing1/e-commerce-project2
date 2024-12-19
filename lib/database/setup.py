from connection import CURSOR, CONN

def create_tables():
    # Create a customer table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY,
            name TEXT ,
            email TEXT,
            phone INTEGER
        )
    """)

    # Create the order table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS 'order' (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER ,
            product_id INTEGER ,
            quantity INTEGER ,
            total_price INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customer(id),
            FOREIGN KEY (product_id) REFERENCES product(id)
        )
    """)

    # Create the product table
    CURSOR.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY,
            name TEXT ,
            description TEXT,
            price INTEGER ,
            stock INTEGER
        )
    """)

    CONN.commit()
