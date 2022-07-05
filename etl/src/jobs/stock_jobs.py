"""Collection of Cereal jobs"""
from dagster import ( file_relative_path,get_dagster_logger, job)


from ops.stock_ops import (
    get_main_content, 
    get_categories,
    display_results)


@job
def get_stock_content():
    logger = get_dagster_logger()
    logger.info("GETTING MAIN CONTENT!")

    content = get_main_content()

    display_results(a=get_categories(content))
            






