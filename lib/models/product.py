from models.__init__ import CURSOR, CONN

class Product:
    all = {}

    def __init__(self, name, description, price, stock, id=None):
        self._id = id
        self._name = name
        self._description = description
        self._price = price
        self._stock = stock
        
    def __repr__(self):
        return (
        f"<Employee {self.id}: {self.name}, {self.description}, {self.price}, {self.stock} >"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
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
        if isinstance(price, int) and price > 0:
            self._price = price
        else:
            raise ValueError(
                "price must be a positive integer"
            )
        
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if isinstance(stock, int) and stock >= 0 :
            self._stock = stock
        else:
            raise ValueError(
                "Stock must be a non-negative integer"
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
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS product;
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

    # @classmethod
    # def display_all_products(cls):
    #     """Fetch all products and return them as a list of Product instances."""
    #     sql = """
    #         SELECT * FROM product
    #     """
    #     rows = CURSOR.execute(sql).fetchall()

    #     if not rows:
    #         return []  # Return an empty list if no products found

    #     # Construct Product instances from rows
    #     products = [cls(row[1], row[2], float(row[3]), int(row[4]), id=row[0]) for row in rows]
    #     return products

    @classmethod
    def display_all_products(cls):
        sql = "SELECT * FROM product"
        return CURSOR.execute(sql).fetchall()

    @classmethod
    def delete_product_by_id(self, product_id):
        sql = """
            DELETE FROM product
            WHERE id = ?
        """
        CURSOR.execute(sql, (product_id,))
        CONN.commit()
        print(f"Product with ID {product_id} has been deleted.")

    @classmethod
    def update_stock(self, product_id, new_stock):
        if isinstance(new_stock, int) and new_stock >= 0:
            sql = """
                UPDATE product
                SET stock = ?
                WHERE id = ?
            """
            CURSOR.execute(sql, (new_stock, product_id))
            CONN.commit()
            print(f"Stock updated for product ID {product_id}. New stock: {new_stock}")
        else:
            raise ValueError("New stock must be a non-negative integer")
        
    @classmethod
    def find_by_id(cls, id):
        sql = """
        SELECT * FROM product WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def instance_from_db(cls, row):
        id, name, description, price, stock = row
        return cls(id, name, description, price, stock)

    # @classmethod
    # def instance_from_db(cls, row):
    #     """Converts a database row into a Product instance."""
    #     id, name, description, price, stock = row
    #     return cls(id, name, description, price, stock)
    