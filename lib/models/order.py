from models.__init__ import CURSOR, CONN
from models.customer import Customer
from models.product import Product

class Order:

    all = {}

    def __init__(self, id, customer_id, product_id, quantity, total_price):
        self.id = id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS 'order' (
            id INTEGER PRIMARY KEY,
            customer_id INTEGER ,
            product_id INTEGER ,
            quantity INTEGER ,
            total_price INTEGER,
            FOREIGN KEY (customer_id) REFERENCES customer(id),
            FOREIGN KEY (product_id) REFERENCES product(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS order;
        """
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def create_order(self, customer_id, product_id, quantity):
        # Validate customer and product existence
        customer = Customer.find_by_id(customer_id)
        product = Product.find_by_id(product_id)

        if not customer:
            print(f"Customer with ID {customer_id} does not exist.")
            return

        if not product:
            print(f"Product with ID {product_id} does not exist.")
            return

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > product.stock:
            print(f"Not enough stock for product {product.name}. Available stock: {product.stock}")
            return

        # Calculate total price
        total_price = product.price * quantity

        # Insert order into database
        sql = """
            INSERT INTO order (customer_id, product_id, quantity, total_price)
            VALUES (?, ?, ?, ?)
        """
  
        CURSOR.execute(sql, (customer_id, product_id, quantity, total_price))
        
        # Update product stock
        product.update_stock(product.id, product.stock - quantity)

        CONN.commit()
        print(f"Order created: Customer {customer.name} -> Product {product.name} (x{quantity}) - Total: ${total_price:.2f}")

    @classmethod
    def display_all_orders(self):
        sql = """
            SELECT o.id, c.name AS customer_name, p.name AS product_name, o.quantity, o.total_price
            FROM orders o
            JOIN customer c ON o.customer_id = c.id
            JOIN product p ON o.product_id = p.id
        """

        rows = CURSOR.execute(sql).fetchall()

        if rows:
            print("\nAll Orders:")
            for row in rows:
                print(f"Order ID: {row[0]}, Customer: {row[1]}, Product: {row[2]}, Quantity: {row[3]}, Total Price: ${row[4]:.2f}")
        else:
            print("\nNo orders found.")

    @classmethod
    def delete_order_by_id(self, order_id):
        sql = """
            DELETE FROM orders
            WHERE id = ?
        """

        # Find the order to restock the product
        order = self.find_by_id(order_id)
        if not order:
            print(f"Order with ID {order_id} does not exist.")
            return

        product = Product.find_by_id(order.product_id)
        if product:
            # Restock the product
            product.update_stock(product.id, product.stock + order.quantity)

        CURSOR.execute(sql, (order_id,))
        CONN.commit()
        print(f"Order with ID {order_id} has been deleted.")

    @classmethod
    def find_by_id(cls, order_id):
        sql = """
            SELECT * FROM orders
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (order_id,)).fetchone()

        if row:
            return Order(row[0], row[1], row[2], row[3], row[4])
        return None