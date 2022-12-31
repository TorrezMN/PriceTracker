# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine.database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy_utils import URLType

from sqlalchemy.orm import relationship

#  MODELS
#  ==========================
#  - Store
#  - Category
#  - Product
#  - Brand


class Brand(Base):
    """Maps the brand of each product."""

    __tablename__ = "Brand"
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_name = Column(String(50), unique=True, index=True)
    brand_recorded_date = Column(Date, index=True)


class Store(Base):
    """Maps the name od the store in the  DB."""

    __tablename__ = "Store"
    id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String(50), unique=True, index=True)


class Category(Base):
    """Maps the category name to each store."""

    __tablename__ = "Category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey("Store.id"))
    category_name = Column(String(100), unique=False, index=True)
    category_url = Column(URLType, unique=True)
    category_recorded_date = Column(Date, index=True)


class Product(Base):
    """Maps the product."""

    __tablename__ = "Product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(100), unique=False, index=True)
    product_img = Column(String(200), unique=False, index=True)
    product_brand_id = Column(Integer, ForeignKey("Brand.id"))
    product_price = Column(String(10))
    product_recorded_date = Column(Date, index=True)
