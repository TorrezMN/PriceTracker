#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from random import choice
from bs4 import BeautifulSoup
import requests
from decouple import config


def check_url_status(url):
    """Checks if the url exist's."""
    r = requests.head(url)
    return r.status_code == 200


def get_random_url():
    urls = get_categories()
    url_links = list(urls.items())
    print(f"TAMAÑO LISTA URLS : {len(url_links)}")
    return choice(url_links)


#  FUNCTIONS
def process_categroy(cat_cont):
    """Process category of products."""
    print(type(cat_cont))
    products = cat_cont.find_all("div", {"class": "item-box"})
    print(len(products))
    for i in products:
        prod_title = i.find_all("h2", {"class": "product-title"})[0].a.text
        prod_price = i.find_all("span", {"class", "productPrice"})[0].text
        prod_picture = i.find_all("a", {"class", "picture-link"})[0].img["src"]
        print(prod_title)
        print(prod_price)
        print(prod_picture)
        print("=" * 20)

    has_next = (
        cat_cont.find_all("div", {"class": "product-pager"})[0].find_all("a").pop()
    )
    print("#" * 20)
    print(has_next)
    print(has_next["href"])


def get_main_content():
    """Gets the main page soup."""
    req = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(req.text, "lxml")
    return soup


def get_category_content(url):
    """Gets the category page content."""
    print(f"Getting page: {url}")
    req = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(req.text, "lxml")
    return soup


def get_categories():
    """Gets and print all sections and its urls."""
    s = get_main_content()
    nav = s.find_all("ul", class_="catnav")
    for i in nav:
        for j in i.find_all("a", href=True):
            cats[j.text] = j["href"]
    return cats


if __name__ == "__main__":
    print("Getting random url!")
    item = get_random_url()
    print(f"Getting category content {item}")
    cat_soup = get_category_content(item[1])
    print("Process category.!")
    process_categroy(cat_soup)
