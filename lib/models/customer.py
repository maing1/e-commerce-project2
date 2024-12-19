from __init__ import CURSOR, CONN

class Customer:
    all = {}

    def __init__(self, id, name, email, phone):
        self.id = id 
        self.name = name
        self.email = email
        self.phone = phone
    
    def __repr__(self):
        return f"<Customer {self.id}: {self.name}, {self.email}, {self.phone}>"
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) == 0:
            self.name = name
        else:    
            raise ValueError("Name must be a non-empty string.")
        
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email) == 0:
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
    def insert_customer(self):
        sql = """
            INSERT INTO customer (name, email, phone)
            VALUES (?, ?, ?)
    """ 

        CURSOR.execute(sql, (self.name, self.email, self.phone))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

def delete_customer(customer_id):
        sql = """
        DELETE FROM customer 
        WHERE id = ?
        """
    
        CURSOR.execute(sql, (customer_id,))
        CONN.commit()

