#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Torrez, MN

"""Collection of helper ops."""
import csv
from typing import List
import requests
from dagster import Nothing, get_dagster_logger, op
from decouple import config



def check_url_status(url)->bool:
    """Checks if the url exist's."""
    r = requests.head(url)
    return (r.status_code == 200)



