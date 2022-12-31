#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Torrez, Milton N.

from random import choice
from sqlalchemy import exc
from db_engine import models
from sqlalchemy.orm import Session
from datetime import date


#  IMPORTING SCHEMAS
from schemas.store_schemas import Brand_Name


def get_all_brands(db: Session):
    """Returns all brands registered."""
    return db.query(models.Brand).all()


def get_or_create_brand(db: Session, brand: Brand_Name):
    instance = db.query(models.Brand).filter_by(**brand.dict()).first()
    today = date.today()

    if instance:
        return instance
    else:
        try:
            s = models.Brand(**brand.dict())

            s.brand_recorded_date = date.today()

            db.add(s)
            db.commit()
            db.refresh(s)
            return s
        except exc.IntegrityError as error:
            errorInfo = error.orig
            return errorInfo.pgerror
