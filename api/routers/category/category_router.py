#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import categories_crud  as crud

#  IMPORTING SCHEMAS
from schemas.store_schemas import Category
from schemas.base_schema import API_RESPONSE

category_router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()



@category_router.get('/get_all_categories')
def get_all_categories(db=Depends(db)):
    """
    Get all categorie's
    """

    API_RESPONSE['data'] = crud.get_all_categories(db)

    return(API_RESPONSE)

@category_router.post('/save_new_category')
def save_new_category(cat:Category, db=Depends(db)):
    """
    Save's a new category.
    """

    API_RESPONSE['data'] = crud.save_category(db, cat)

    return(API_RESPONSE)

@category_router.post('/get_or_create_category')
def get_or_create_category(cat:Category, db=Depends(db)):
    """
    Save's a new category.
    """

    API_RESPONSE['data'] = crud.get_or_create_category(db, cat)

    return(API_RESPONSE)

