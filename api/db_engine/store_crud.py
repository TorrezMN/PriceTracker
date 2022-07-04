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
