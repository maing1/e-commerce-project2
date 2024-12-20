#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.customer import Customer
from models.order import Order

def seed_customers():
    """Seed some customers into the database"""
    customers = [
        ('Emily Johnson', 'emilyj@example.com', '5551234567'),
        ('Michael Brown', 'mbrown@example.com', '5559876543'),
        ('Sophia Davis', 'sophiad@example.com', '5557654321')
    ]

    for customer in customers:
        CURSOR.execute("INSERT INTO customer (name, email, phone) VALUES (?, ?, ?)", customer)
    
    CONN.commit()
    print("Customers seeded!")

def seed_products():
    """Seed some skincare products into the database"""
    products = [
        ('Gentle Cleanser', 'A mild cleanser suitable for all skin types', 20, 150),
        ('Hydrating Moisturizer', 'A lightweight, hydrating face moisturizer', 30, 100),
        ('Vitamin C Serum', 'Brightens skin and reduces dark spots', 40, 80),
        ('Sunscreen SPF 50', 'Broad-spectrum sun protection', 25, 120),
        ('Exfoliating Scrub', 'Removes dead skin cells for a radiant glow', 15, 50)
    ]

    for product in products:
        CURSOR.execute("INSERT INTO product (name, description, price, stock) VALUES (?, ?, ?, ?)", product)
    
    CONN.commit()
    print("Products seeded!")

def seed_orders():
    """Seed some orders into the database"""
    orders = [
        (1, 2, 1, 30),  # Emily Johnson orders 1 Hydrating Moisturizer
        (2, 3, 2, 80),  # Michael Brown orders 2 Vitamin C Serums
        (3, 4, 1, 25),  # Sophia Davis orders 1 Sunscreen SPF 50
    ]
    
    for order in orders:
        CURSOR.execute("INSERT INTO 'order' (customer_id, product_id, quantity, total_price) VALUES (?, ?, ?, ?)", order)

    CONN.commit()
    print("Orders seeded!")

def main():
    """Seed the database with initial data"""
    seed_customers()
    seed_products()
    seed_orders()
    print("Database seeded successfully for the skincare website!")

if __name__ == "__main__":
    main()
