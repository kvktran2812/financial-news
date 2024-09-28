import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from stockanalysis.stock.constants import BASE_URL, DIVIDEND
from stockanalysis.utils import get_data_from_time_series_table



def compute_dividends_url(stock: str) -> str:
    return f"{BASE_URL}/{stock}/{DIVIDEND}"


def get_dividends(stock: str) -> List[Dict[str, str]]:
    url = compute_dividends_url(stock)
    data = []

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    table = main.find("table")
    data = get_data_from_time_series_table(table)

    return data