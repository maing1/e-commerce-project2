from __init__ import CURSOR, CONN

class Product:
    all = {}

    def __init__(self, name, description, price, stock, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self):
        return (
        f"<Employee {self.id}: {self.name}, {self.description}, {self.price}, {self.stock} >"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) != 0:
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if len(description) != 0:
            self._description = description
        else:
            raise ValueError(
                "description must be a non-empty string"
            )
        
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, int) and len(price) != 0:
            self._price = price
        else:
            raise ValueError(
                "price must be a non-empty integer"
            )
        
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if isinstance(stock, int) and len(stock) < 5:
            self._stock = stock
        else:
            raise ValueError(
                "stock must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY,
            name TEXT ,
            description TEXT,
            price INTEGER ,
            stock INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def add_product(cls, name, description, price, stock):
        sql = """
            INSERT INTO product (name, description, price, stock)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (name, description, price, stock))
        CONN.commit()

    @classmethod
    def display_all_products(cls):
        sql = """
            SELECT * FROM product
        """
        rows = CURSOR.execute(sql).fetchall()

        if rows:
            print("\nAll Products:")
            for row in rows:
                print(f"ID: {row[0]}, Name: {row[1]}, Description: {row[2]}, Price: {row[3]}, Stock: {row[4]}")
        else:
            print("\nNo products found.")

    @classmethod
    def delete_product_by_id(cls, product_id):
        sql = """
            DELETE FROM product
            WHERE id = ?
        """
        CURSOR.execute(sql, (product_id,))
        CONN.commit()
        print(f"Product with ID {product_id} has been deleted.")