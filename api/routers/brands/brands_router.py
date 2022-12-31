#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from fastapi import Depends, HTTPException, APIRouter
from db_engine.database import SessionLocal, engine
from db_engine import brand_crud as crud

#  IMPORTING SCHEMAS
from schemas.store_schemas import Brand_Name
from schemas.base_schema import API_RESPONSE

brands_rounter = APIRouter(
    prefix="/brands",
    tags=["brands"],
)


def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@brands_rounter.get("/get_all_brands")
def get_all_brands(db=Depends(db)):
    """
    Get all brand's
    """
    API_RESPONSE["data"] = crud.get_all_brands(db)
    return API_RESPONSE


@brands_rounter.post("/get_or_create_brand")
def get_or_create_brand(brand_name: Brand_Name, db=Depends(db)):
    """
    Get's a Brand record by name.
    """
    API_RESPONSE["data"] = crud.get_or_create_brand(db, brand_name)
    return API_RESPONSE
