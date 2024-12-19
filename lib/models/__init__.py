from lib.db import Base
from .product import Product
from .customer import Customer
from .order import Order

# Add all models to Base.metadata for table creation
def initialize_models():
    Base.metadata.create_all()
