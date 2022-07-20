#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN


"""Collection of stock ops."""
import csv
import requests
from typing import List
from random import choice
from decouple import config
from dagster import Nothing, get_dagster_logger, op, get_dagster_logger
from bs4 import BeautifulSoup
from helper_scripts.helper_scripts import HEADERS

from datetime import datetime
from helper_scripts.helper_scripts import make_soup, get_soup


#  DB
from db_engine.database import SessionLocal


#  CRUD OPERATIONS
from db_engine import categories_crud, store_crud
from db_engine import product_crud

#  SCHEMAS
from schemas.store_schemas import Category, Store, Product, Brand


@op
def get_main_content()->str:
    """Gets the main page soup."""
    logger = get_dagster_logger()
    logger.info('GETTING MAIN CONTENT!')
    BASE_URL = config('BASE_URL')
    soup = get_soup(BASE_URL)
    return str(soup)

@op
def get_categories(soup: str)->dict:
    """Gets and print all sections and its urls."""
    logger = get_dagster_logger()
    logger.info('GETTING CATEGORIES!')

    s = make_soup(soup)

    cats = {}

    nav = s.find_all("ul", class_="catnav")

    for i in nav:
        for j in i.find_all('a', href=True):
            cats[j.text] = j['href']
    return cats



@op
def update_stock_categories(a:dict):
    logger = get_dagster_logger()
    logger.info('DISPLAYING THE DATA!')
    for i in a.items():
        incert_update_category(i)

    
@op
def incert_update_category(cat):
    """Incert's new record or updates new record if exist's."""
    logger = get_dagster_logger()
    db = SessionLocal()

    store = store_crud.get_or_create_store(db,Store(store_name='stock'))
    category = categories_crud.get_or_create_category(db, Category(
        store_id=store.id,
        category_name=cat[0],
        category_url=cat[1],
        category_recorded_date = datetime.today().strftime('%Y-%m-%d')
    ))

    if (category):
        logger.info('A RECORD WAS UPDATED!')
        logger.info(category)
    else:
        logger.info('A NEW RECORD WAS SAVED!')
    db.close()

@op
def get_random_stock_category()->dict:
    """Returns a random category to start scrapping."""
    logger = get_dagster_logger()
    logger.info('RUNNING get_random_category op!')

    db = SessionLocal()
    category = categories_crud.get_random_category(db).__dict__
    db.close()

    return(category)

@op
def get_stock_category_soup(cat:dict):
    """Gets the soup for a single category."""
    logger = get_dagster_logger()
    logger.info('=================================================')
    logger.info('GETTING A SINGLE CATEGORY SOUP!')
    logger.info(cat['category_url'])
    logger.info('=================================================')
    soup = get_soup(cat['category_url'])
    return(str(soup))

@op
def get_stock_category_products(soup):
    logger = get_dagster_logger()
    logger.info('=================================================')
    logger.info('GETTING ALL PRODUCTS FOR THIS CATEGORY!')
    logger.info('=================================================')

    s = make_soup(soup) 

    products = s.find_all("div", class_="product-item")

    for i in products:
        process_stock_products(str(i))

@op
def process_stock_products(prod:str):
    db = SessionLocal()
    logger = get_dagster_logger()
    logger.info('=================================================')
    logger.info('LOADING PRODUCT!')
    logger.info('=================================================')
    product = make_soup(prod)


    # IMAGE div.picture>a>img['href']
    # PRICE span.price-label
    # PRODUCT BRAND div.product-brand
    # PRODUCT NAME h2.product-title>a

    image = product.find_all('a', class_='picture-link')[0]['href']
    title = product.find_all('h2', class_='product-title')[0].a.text
    brand = product.find_all('div', class_='product-brand')[0].text.replace('\n', ' ').replace('\r', '')
    price = product.find_all('span', class_='price-label')[0].text

    

    if(isinstance(brand, str)):
        b = Brand(
            brand_name=brand,
            brand_recorded_date = datetime.today().strftime('%Y-%m-%d')
        )
        brand_id = product_crud.get_or_create_brand(
            db,b
            ).id

        new_product = Product(
            product_name = title,
            product_img = image,
            product_brand_id = brand_id,
            product_price = price,
            product_recorded_date = datetime.today().strftime('%Y-%m-%d')
        )

        p = product_crud.create_product(
            db,
            new_product
        )
        logger.info('LOADED A PRODUCT!')



    
