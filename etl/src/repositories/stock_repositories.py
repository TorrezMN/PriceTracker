"""Collection of Cereal repositories"""
from dagster import repository

from jobs.stock_jobs import load_stock_categories, get_categorie_products


@repository
def stock_repository():
    """Stock repositorie of jobs and tasks."""
    return [load_stock_categories, get_categorie_products]
