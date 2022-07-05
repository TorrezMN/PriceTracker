"""Collection of Cereal repositories"""
from dagster import repository

from jobs.stock_jobs import get_stock_content


@repository
def stock_repository():
    """Stock repositorie of jobs and tasks."""
    return [get_stock_content]
