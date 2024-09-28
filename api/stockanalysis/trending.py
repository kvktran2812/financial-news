import requests
from bs4 import BeautifulSoup
from typing import List
from stockanalysis.utils import get_data_from_time_series_table


def get_trending() -> List: 
    url = "https://stockanalysis.com/trending"

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    data = get_data_from_time_series_table(table)

    print(table.prettify())

    return data