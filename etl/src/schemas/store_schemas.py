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

    class Config:
        orm_mode = True

