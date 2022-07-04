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


#  @store_router.get('/get_all_dose')
#  def get_all_dose(db=Depends(db)):
    #  """
    #  Get All Dose
    #  ---
#
    #  Returns a list of ``all`` dose registered in the sistem.
#
    #  """
#
    #  data = crud.get_all_dose(db)
    #  size = len(data)
    #  API_RESPONSE['size'] = size
    #  API_RESPONSE['data'] = data
    #  return (API_RESPONSE)
#

@store_router.post('/save_store')
def save_dose(store: Store, db=Depends(db)):
    API_RESPONSE['data'] = crud.save_store(db, store)
    return (API_RESPONSE)


#  @store_router.post('/get_or_create_dose')
#  def get_or_create_new_dose(d: Dose_Name, db=Depends(db)):
    #  """
    #  Get or Create - Dose
    #  ---
#
    #  Allows users to ``get or create`` a new dose in the db.
#
    #  """
    #  API_RESPONSE['data'] = crud.get_or_create_new_dose(db, d)
    #  return (API_RESPONSE)
