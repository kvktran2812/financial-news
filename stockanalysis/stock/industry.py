import requests
from bs4 import BeautifulSoup
from typing import List
from stockanalysis.utils import get_data_from_time_series_table
from stockanalysis.stock.constants import BASE_URL


INDUSTRY = "industry"
SECTOR = "sectors"


def get_list_of_tables(main) -> List:
    target_div = main.contents[-1]
    target_div = target_div.contents[-1]
    target_div = target_div.contents[-1]
    all_div = target_div.find_all("div", recursive=False)

    return all_div


def get_industry_sector_overvie():
    data = dict()
    url = f"{BASE_URL}/{INDUSTRY}"

    resonse = requests.get(url)
    html = resonse.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main", {"id": "main"})
    all_div = get_list_of_tables(main)

    for div in all_div:
        h2 = div.find("h2")
        table = div.find("table")

        if h2 is not None and table is not None:
            data[h2.text.strip()] = get_data_from_time_series_table(table)
    
    return data


def get_sectors() -> List:
    data = []
    url = f"{BASE_URL}/{INDUSTRY}/{SECTOR}"

    resonse = requests.get(url)
    html = resonse.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main", {"id": "main"})
    table = main.find("table")

    data = get_data_from_time_series_table(table)

    return data


def get_industries() -> List:
    data = []
    url = f"{BASE_URL}/{INDUSTRY}/all"

    resonse = requests.get(url)
    html = resonse.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main", {"id": "main"})
    table = main.find("table")

    data = get_data_from_time_series_table(table)

    return data