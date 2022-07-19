
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import store_crud as store_crud
from db_engine import product_crud as prod_crud

#  IMPORTING SCHEMAS
from schemas.store_schemas import Store, Brand
from schemas.base_schema import API_RESPONSE

products_router = APIRouter(
    prefix="/products",
    tags=["products"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@products_router.get('/get_all_brands')
def get_all_brands(db=Depends(db)):
    """
    Get all brand's
    """
    data = prod_crud.get_all_brands(db)
    API_RESPONSE['size'] = len(data)
    API_RESPONSE['data'] = data

    return(API_RESPONSE)


@products_router.post('/new_brand')
def create_new_brand(brand:Brand , db=Depends(db)):
    data = prod_crud.get_or_create_brand(db, brand) 
    API_RESPONSE['data'] = data
    return(API_RESPONSE)
