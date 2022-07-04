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
