from sqlalchemy import Column, Integer, String, DECIMAL, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_name = Column(String(255))  # Adjusted the String length
    email = Column(String(255))  # Adjusted the String length
    phone_number = Column(String(20))  # Adjusted the String length

    sales = relationship('Sale', back_populates='customer')

class Product(Base):
    __tablename__ = 'products'
    
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String(255))  # Adjusted the String length
    description = Column(String(500))  # Adjusted the String length
    price = Column(DECIMAL(10, 2))  # Adjusted the DECIMAL precision and scale
    
    sales = relationship('Sale', back_populates='product')
    inventory = relationship('Inventory', uselist=False, back_populates='product')
    inventory_alerts = relationship("InventoryAlert", back_populates="product")
    order_details = relationship('OrderDetail', back_populates='product')

class Sale(Base):
    __tablename__ = 'sales'
    
    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.customer_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    order_date = Column(Date)
    quantity_sold = Column(Integer)
    unit_price = Column(DECIMAL(10, 2))  # Adjusted the DECIMAL precision and scale
    
    customer = relationship('Customer', back_populates='sales')
    product = relationship('Product', back_populates='sales')
    order_details = relationship('OrderDetail', back_populates='sale')

class Inventory(Base):
    __tablename__ = 'inventory'
    
    product_id = Column(Integer, ForeignKey('products.product_id'), primary_key=True)
    quantity_in_stock = Column(Integer)
    
    product = relationship('Product', back_populates='inventory')

class InventoryAlert(Base):
    __tablename__ = 'inventory_alerts'
    
    alert_id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    alert_date = Column(Date)
    threshold_quantity = Column(Integer)
    current_quantity = Column(Integer)
    
    product = relationship('Product', back_populates='inventory_alerts')

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True)
    username = Column(String(255))  # Adjusted the String length
    password_hash = Column(String(255))  # Adjusted the String length
    role = Column(String(50))  # Adjusted the String length

class OrderDetail(Base):
    __tablename__ = 'order_details'
    
    order_detail_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('sales.order_id'))
    product_id = Column(Integer, ForeignKey('products.product_id'))
    quantity = Column(Integer)
    subtotal = Column(DECIMAL(10, 2))  # Adjusted the DECIMAL precision and scale
    
    sale = relationship('Sale', back_populates='order_details')
    product = relationship('Product', back_populates='order_details')
