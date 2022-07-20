#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN


from datetime import date
from typing import Optional

from pydantic import BaseModel


class Store(BaseModel):
    store_name : str 

    class Config:
        orm_mode = True

class Category(BaseModel):
    store_id : int
    category_name : str
    category_url : str
    category_recorded_date : date

    class Config:
        orm_mode = True


class Product(BaseModel):
    product_name : str
    product_img : str
    product_brand_id : int
    product_price : str
    product_recorded_date : date
    
    class Config:
        orm_mode = True


class Brand(BaseModel):
    brand_name : str
    brand_recorded_date : date


    class Config:
        orm_mode = True
