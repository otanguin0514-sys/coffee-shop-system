from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Text, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), default="customer")
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    reviews = relationship("Review", back_populates="user")
    orders = relationship("Order", back_populates="user")


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), default="Bean & Bloom Coffee House")
    address = Column(String(255))
    city = Column(String(100))
    phone = Column(String(20))
    opening_hours = Column(String(100))
    average_rating = Column(Float, default=0.0)
    total_reviews = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    reviews = relationship("Review", back_populates="shop")


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text)

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Numeric(10, 2), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    image_url = Column(String(255), default="")
    stock_quantity = Column(Integer, default=0)
    available = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    reviews = relationship("Review", back_populates="product")
    inventory = relationship("Inventory", back_populates="product", uselist=False)


class Inventory(Base):
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), unique=True, nullable=False)
    stock_level = Column(Integer, nullable=False)
    reorder_level = Column(Integer, default=5)
    unit = Column(String(50), default="cups")
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    product = relationship("Product", back_populates="inventory")


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    shop_id = Column(Integer, ForeignKey("shop.id"), default=1)
    order_number = Column(String(50), unique=True)
    order_total = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), default="pending")
    payment_method = Column(String(50), default="card")
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, default=1)
    price = Column(Numeric(10, 2), nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product", back_populates="order_items")


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    shop_id = Column(Integer, ForeignKey("shop.id"), default=1)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=True)
    rating = Column(Integer, nullable=False)
    title = Column(String(255), default="")
    comment = Column(Text)
    is_verified_purchase = Column(Boolean, default=False)
    approved = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="reviews")
    shop = relationship("Shop", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")


class Loyalty(Base):
    __tablename__ = "loyalty"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), unique=True, nullable=False)
    points = Column(Integer, default=0)
    tier = Column(String(50), default="bronze")
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
