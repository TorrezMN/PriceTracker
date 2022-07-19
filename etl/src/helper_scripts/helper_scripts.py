#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from bs4 import BeautifulSoup 
import requests




HEADERS={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



 
def make_soup(s:str)->BeautifulSoup:
    """Creates a BeautifulSoup object."""
    soup = BeautifulSoup(str(s), "html.parser")
    return(soup)




def get_soup(u:str)->BeautifulSoup:
    """Gets and creates the soup from request object."""
    req = requests.get(u, headers=HEADERS)
    soup = BeautifulSoup(str(req.text), "html.parser")
    return(soup)
