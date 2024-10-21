import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from stockanalysis.stock.constants import BASE_URL, PROFILE, EMPLOYEES
from stockanalysis.utils import *


def compute_profile_url(stock: str) -> str:
    return f"{BASE_URL}/{stock}/{PROFILE}"


def compute_employees_url(stock: str) -> str:
    return f"{BASE_URL}/{stock}/{EMPLOYEES}"


def filter_key_executives(div: BeautifulSoup) -> bool:
    if div.find("h2") is not None:
        if div.find("h2").text.strip() == "Key Executives":
            return True
    return False


def get_key_executive_element(main: BeautifulSoup) -> BeautifulSoup:
    all_div = main.find_all("div")
    filter_div = list(filter(filter_key_executives, all_div))

    if len(filter_div) == 1:
        return filter_div[0]
    else:
        raise Exception("Cannot find key executive element")
    

def get_key_executives(stock: str) -> List[Dict[str, str]]:
    url = compute_profile_url(stock)

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    element = get_key_executive_element(main)
    table = element.find_all("table")[0]

    metadata, data = get_data_from_time_series_table(table)

    return metadata, data


def get_latest_sec_filing(stock: str) -> List[Dict[str, str]]:
    url = compute_profile_url(stock)

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    element = get_key_executive_element(main)
    table = element.find_all("table")[1]

    metadata, data = get_data_from_time_series_table(table)

    return metadata, data


def get_number_of_employees(stock: str) -> List[Dict[str, str]]:
    url = compute_employees_url(stock)

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    table = main.find("table")

    metadata, data = get_data_from_time_series_table(table)

    return metadata, data