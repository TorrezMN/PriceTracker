"""Collection of Cereal jobs"""
from dagster import ( file_relative_path,get_dagster_logger, job)


from ops.stock_ops import (
    get_main_content, 
    get_categories,
    update_stock_categories,
    get_random_stock_category,
    get_stock_category_soup,
    get_stock_category_products)


@job
def load_stock_categories():
    """Loads in db all the categories of products from Supermercados Stock"""
    logger = get_dagster_logger()
    logger.info("LOADING STOCK CATEGORIES!")

    content = get_main_content()
    update_stock_categories(a=get_categories(content))
            


@job 
def get_categorie_products():
    """Scrapes and saves products from categories."""
    logger = get_dagster_logger()
    logger.info("GETTING PRODUCTS FROM STOCK CATEGORIES!")
    get_stock_category_products(
         get_stock_category_soup(get_random_stock_category())
    )






