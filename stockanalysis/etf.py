import requests
from bs4 import BeautifulSoup
from typing import List
from stockanalysis.utils import get_data_from_time_series_table
from stockanalysis.stock.constants import BASE_URL


ETF_URL = "https://stockanalysis.com/etf"


def get_etfs() -> List[str]:
    url = f"{ETF_URL}"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    data = get_data_from_time_series_table(table)

    return data

def get_etf_new_lauch() -> List[str]:
    url = f"{ETF_URL}/list/new"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    data = get_data_from_time_series_table(table)

    return data


def get_etf_providers() -> List[str]:
    url = f"{ETF_URL}/provider"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    data = get_data_from_time_series_table(table)

    return data