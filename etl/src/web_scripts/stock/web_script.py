#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from random import choice
from bs4 import BeautifulSoup
import requests


#  BASE CONFIGS
BASE_URL = 'https://www.stock.com.py/default.aspx'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


cats = {}



def check_url_status(url):
    """Checks if the url exist's."""
    r = requests.head(url)
    return (r.status_code == 200)

def get_content():
    """Gets the main page soup."""
    req = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(req.text, 'lxml')
    return(soup)

def get_categories():
    """Gets and print all sections and its urls."""
    s = get_content()
    nav = s.find_all("ul", class_="catnav")

    for i in nav:
        for j in i.find_all('a', href=True):
            cats[j.text]=j['href']








if __name__ == '__main__':
    get_categories()
    for i in cats.items():
        print(check_url_status(i[1]))
        break

