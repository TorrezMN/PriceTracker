#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine import models
from sqlalchemy.orm import Session

#  IMPORTING SCHEMAS
from schemas.store_schemas import Brand, Product


def filter_brand_name(db: Session, brand: str):
    return (
        db.query(models.Brand).filter(models.Brand.brand_name.contains(brand)).first()
    )


def get_all_brands(db: Session):
    return db.query(models.Brand).all()


def get_all_products(db: Session):
    return db.query(models.Product).all()


def get_or_create_brand(db: Session, brand: Brand):
    instance = db.query(models.Brand).filter_by(**brand.dict()).first()
    if instance:
        return instance
    else:
        b = models.Brand(**brand.dict())
        db.add(b)
        db.commit()
        db.refresh(b)
        return b


def create_product(db: Session, prod: Product):
    p = models.Product(**prod.dict())
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
