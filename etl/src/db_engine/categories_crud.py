#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from sqlalchemy import exc
from db_engine import models
from sqlalchemy.orm import Session

#  IMPORTING SCHEMAS
from schemas.store_schemas import Category



def get_all_categories(db: Session):
    """Returns a list of all categories."""
    return db.query(models.Category).all()

def save_category(db: Session, data: Category):
    """Saves a new category."""
    category = models.Category(**data.dict())
    db.add(category)
    db.commit()
    db.refresh(category)
    return (category)


def get_or_create_category(db: Session, cat:Category):
    instance = db.query(models.Category).filter_by(**cat.dict()).first()

    if instance:
        return instance
    else:
        try:
            s = models.Category(**cat.dict())
            db.add(s)
            db.commit()
            db.refresh(s)
            return (s)
        except exc.IntegrityError as error:
            errorInfo = error.orig
            return(errorInfo.pgerror)

