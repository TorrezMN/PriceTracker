#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from db_engine import models
from sqlalchemy.orm import Session
#  IMPORTING SCHEMAS
from schemas.store_schemas import Store


def save_store(db: Session, data: Store):
    store = models.Store(**data.dict())
    db.add(store)
    db.commit()
    db.refresh(store)
    return (store)

def filter_store_name(db: Session, store_name: str):
    return db.query(models.Store).filter(
        models.Store.store_name.contains(store_name)).first()

def get_all_stores(db: Session):
    return db.query(models.Store).all()


def get_or_create_store(db: Session, store:Store):
    instance = db.query(models.Store).filter_by(**store.dict()).first()
    if instance:
        return instance
    else:
        s = models.Store(**store.dict())
        db.add(s)
        db.commit()
        db.refresh(s)
        return (s)
