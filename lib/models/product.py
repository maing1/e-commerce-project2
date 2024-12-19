from sqlalchemy import Column, Integer, String, Float
from lib.db import Base

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)

    @classmethod
    def create(cls, name, description, price, stock):
        product = cls(name=name, description=description, price=price, stock=stock)
        db.session.add(product)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()

    @classmethod
    def get_by_id(cls, product_id):
        return db.session.query(cls).filter_by(id=product_id).first()

    @classmethod
    def delete(cls, product_id):
        product = cls.get_by_id(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
