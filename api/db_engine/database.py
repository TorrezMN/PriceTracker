#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://username:password@db:5433/price_tracker"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
