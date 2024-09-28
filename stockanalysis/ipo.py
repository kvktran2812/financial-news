import requests
from bs4 import BeautifulSoup
from typing import List
from stockanalysis.utils import get_data_from_time_series_table
from stockanalysis.stock.constants import BASE_URL

IPO_URL = "https://stockanalysis.com/ipos"


def check_year(year: int) -> bool:
    return year >= 2010 or -1


def compute_ipos_url(year: int = -1) -> str:
    if not check_year(year):
        raise ValueError(f"{year} is not a valid year")

    if year == -1:
        return f"{IPO_URL}"

    return f"{IPO_URL}/{year}"


def get_ipos(year: int = -1) -> List:
    url = compute_ipos_url(year)
    data = []

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main", {"id": "main"})
    table = main.find("table")
    metadate, data = get_data_from_time_series_table(table)

    return metadate, data


def get_next_week_ipos() -> List:
    url = f"{IPO_URL}/calendar"
    data = []

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    metadate, data = get_data_from_time_series_table(table)

    return metadate, data 


def get_ipos_filings() -> List:
    url = f"{IPO_URL}/filings"
    data = []

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    metadate, data = get_data_from_time_series_table(table)

    return metadate, data 


def get_ipos_withdrawn() -> List:
    url = f"{IPO_URL}/withdrawn"
    data = []

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    metadate, data = get_data_from_time_series_table(table)

    return metadate, data 


def get_ipo_news() -> List:
    return