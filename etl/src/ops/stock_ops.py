#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN


"""Collection of stock ops."""
import csv
import requests
from typing import List
from random import choice
from decouple import config
from dagster import Nothing, get_dagster_logger, op ,get_dagster_logger
from bs4 import BeautifulSoup 
from helper_scripts.helper_scripts import HEADERS

from helper_scripts.helper_scripts import make_soup


#  DB
from db_engine.database import SessionLocal


#  CRUD OPERATIONS
from db_engine import categories_crud,store_crud

#  SCHEMAS
from schemas.store_schemas import Category 


@op
def get_main_content()->str:
    """Gets the main page soup."""
    logger = get_dagster_logger()
    logger.info('GETTING MAIN CONTENT!')
    BASE_URL = config('BASE_URL')
    req = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(str(req.text), "html.parser")
    return(str(soup))

@op
def get_categories(soup:str)->dict:
    """Gets and print all sections and its urls."""
    logger = get_dagster_logger()
    logger.info('GETTING CATEGORIES!')

    s = make_soup(soup) 

    cats = {}

    nav = s.find_all("ul", class_="catnav")

    for i in nav:
        for j in i.find_all('a', href=True):
            cats[j.text]=j['href']
    return(cats)



@op
def update_stock_categories(a:dict):
    logger = get_dagster_logger()
    logger.info('DISPLAYING THE DATA!')
    for i in a.items():
        incert_update_category(i)

    
@op
def incert_update_category(cat):
    logger = get_dagster_logger()
    db = SessionLocal()

    store = store_crud.filter_store_name(db, 'stock')
    category = categories_crud.get_or_create_category(db, Category(
        store_id=store.id,
        category_name=cat[0],
        category_url=cat[1]
    ))

    if (category):
        logger.info('A RECORD WAS UPDATED!')
        logger.info(category)
    else:
        logger.info('A NEW RECORD WAS SAVED!')
    db.close()

