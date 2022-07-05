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


#  def get_random_url():
    #  urls = get_categories()
    #  url_links = list(urls.items())
    #  print(f'TAMAÑO LISTA URLS : {len(url_links)}')
    #  return(choice(url_links))

#  FUNCTIONS
#  def process_categroy(cat_cont):
    #  """Process category of products."""
    #  print(type(cat_cont))
    #  products = cat_cont.find_all("div", {"class": "item-box"})
    #  print(len(products))
    #  for i in products:
        #  prod_title = i.find_all('h2', {'class':'product-title'})[0].a.text
        #  prod_price = i.find_all('span', {'class', 'productPrice'})[0].text
        #  prod_picture = i.find_all('a', {'class','picture-link'})[0].img['src']
        #  print(prod_title)
        #  print(prod_price)
        #  print(prod_picture)
        #  print('='*20)
#
    #  has_next = cat_cont.find_all('div', {'class':'product-pager'})[0].find_all('a').pop()
    #  print('#'*20)
    #  print(has_next)
    #  print(has_next['href'])


@op
def get_main_content()->str:
    """Gets the main page soup."""
    logger = get_dagster_logger()
    logger.info('GETTING MAIN CONTENT!')
    BASE_URL = config('BASE_URL')
    req = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(str(req.text), "html.parser")
    return(str(soup))

#  def get_category_content(url):
    #  """Gets the category page content."""
    #  print(f'Getting page: {url}')
    #  req = requests.get(url, headers=HEADERS)
    #  soup = BeautifulSoup(req.text, 'lxml')
    #  return(soup)


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
#
@op
def display_results(a):
    logger = get_dagster_logger()
    logger.info('DISPLAYING THE DATA!')
    logger.info(a)
