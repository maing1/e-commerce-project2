from __init__ import CURSOR, CONN
from customer import Customer

class Order:
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)

    customer = relationship('Customer', backref='orders')

    @classmethod
    def create(cls, customer_id):
        order = cls(customer_id=customer_id)
        db.session.add(order)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()

    @classmethod
    def get_by_id(cls, order_id):
        return db.session.query(cls).filter_by(id=order_id).first()
