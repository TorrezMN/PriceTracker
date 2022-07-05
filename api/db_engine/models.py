
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine.database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy_utils import URLType

from sqlalchemy.orm import relationship

#  MODELS
#  ==========================
#  - Store
#  - Category





class Store(Base):
    __tablename__ = 'Store'
    id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String(50), unique=True, index=True)





class Category(Base):
    __tablename__ = 'Category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    store_id = Column(Integer, ForeignKey('Store.id'))
    category_name = Column(String(100), unique=False, index=True)
    category_url = Column(URLType)


