#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import store_crud as crud

#  IMPORTING SCHEMAS
from schemas.store_schemas import Store
from schemas.base_schema import API_RESPONSE

store_router = APIRouter(
    prefix="/store",
    tags=["store"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@store_router.get("/get_all_stores")
def get_all_stores(db=Depends(db)):
    """
    Get all store's
    """

    data = crud.get_all_stores(db)
    API_RESPONSE["size"] = len(data)
    API_RESPONSE["data"] = data

    return API_RESPONSE


@store_router.post("/save_store")
def save_dose(store: Store, db=Depends(db)):
    """
    Save a store.
    """

    API_RESPONSE["data"] = crud.save_store(db, store)
    return API_RESPONSE


@store_router.get("/get_store/{store_name}")
def get_store(store_name: str, db=Depends(db)):
    """
    Get's a store record by name.
    """

    API_RESPONSE["data"] = crud.filter_store_name(db, store_name)
    return API_RESPONSE
