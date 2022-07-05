#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

from bs4 import BeautifulSoup 




HEADERS={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}



 
def make_soup(s:str)->BeautifulSoup:
    print("MAKING A SOUP!")
    soup = BeautifulSoup(str(s), "html.parser")
    return(soup)
