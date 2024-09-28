import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from stockanalysis.stock.constants import BASE_URL, STATISTICS, MARKET_CAP, REVENUE
from stockanalysis.utils import *


def compute_statistics_url(stock: str) -> str:
    url = f"{BASE_URL}/{stock}/{STATISTICS}"
    return url


def get_total_evaluation(stock: str) -> Dict[str, str]:
    data = {}
    url = compute_statistics_url(stock)
    print(url)

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    possible_div = main.find_all("div")
    targeted_div = filter(lambda div: div.find("table") is not None, possible_div)

    for div in targeted_div:
        h2 = div.find("h2")
        attribute = h2.text.strip()

        if attribute not in data:
            table = div.find("table")
            data[attribute] = get_data_from_listed_table(table)
    
    return data


def filter_market_cap(div):
    h2 = div.find("h2")
    if h2 is None:
        return False
    elif h2.text.strip() != "Market Cap History":
        return False
    elif div.find("table") is None:
        return False
    else: 
        return True
    

def filter_revenue(div):
    h2 = div.find("h2")
    if h2 is None:
        return False
    elif h2.text.strip() != "Revenue History":
        return False
    elif div.find("table") is None:
        return False
    else: 
        return True


def get_market_cap_history(stock: str) -> List:
    url = BASE_URL + "/" + stock + "/" + MARKET_CAP
    data = []

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    possible_div = main.find_all("div")
    tareted_div = list(filter(filter_market_cap, possible_div))
    target_div = tareted_div[0]

    table = target_div.find("table")
    data = get_data_from_time_series_table(table)

    return data


def get_revenue_history(stock: str) -> List:
    url = BASE_URL + "/" + stock + "/" + REVENUE
    data = []

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    possible_div = main.find_all("div")
    tareted_div = list(filter(filter_revenue, possible_div))
    target_div = tareted_div[0]

    table = target_div.find("table")
    data = get_data_from_time_series_table(table)

    return data