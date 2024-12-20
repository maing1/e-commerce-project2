from models.__init__ import CURSOR, CONN

class Customer:
    all = {}

    def __init__(self, id, name, email, phone):
        self._id = id 
        self._name = name
        self._email = email
        self._phone = phone
    
    def __repr__(self):
        return f"<Customer {self.id}: {self.name}, {self.email}, {self.phone}>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) != 0:
            self.name = name
        else:    
            raise ValueError("Name must be a non-empty string.")
        
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email) != 0:
            self.email = email
        else:    
            raise ValueError("Email must be a non-empty string.")
        
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if isinstance(phone, int) and len(phone) == 10:
            self.phone = phone
        else:    
            raise ValueError("Phone must be a 10-digit integer.")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY,
            name TEXT ,
            email TEXT,
            phone INTEGER
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customer;
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def insert_customer(cls, name, email, phone):
        sql = """
            INSERT INTO customer (name, email, phone)
            VALUES (?, ?, ?)
        """ 

        CURSOR.execute(sql, (name, email, phone))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM customer
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def delete_customer(customer_id):
        customer = Customer.find_by_id(customer_id)
        if customer:
            sql = """
            DELETE FROM customer
            WHERE id = ?
            """
            CURSOR.execute(sql, (customer_id,))
            CONN.commit()
            print(f"Customer with ID {customer_id} has been deleted.")
        else:
            print(f"Customer with ID {customer_id} does not exist.")

    @classmethod
    def instance_from_db(cls, row):
        """Converts a database row into a Customer instance."""
        id, name, email, address = row
        return cls(id, name, email, address)

