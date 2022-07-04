
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine.database import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

#  MODELS
#  ==========================
#  - Store


class Store(Base):
    __tablename__ = 'Store'
    id = Column(Integer, primary_key=True, autoincrement=True)
    store_name = Column(String(50), unique=True, index=True)


