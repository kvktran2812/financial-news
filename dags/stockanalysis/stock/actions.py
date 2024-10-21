import requests
from bs4 import BeautifulSoup
from typing import List
from stockanalysis.utils import get_data_from_time_series_table
from stockanalysis.stock.constants import BASE_URL

# constants
LISTED = "listed"
DELISTED = "delisted"
SPLITS = "splits"
CHANGES = "changes"
SPINOFFS = "spinoffs"
BANKCRUPTCIES = "bankruptcies"
ACQUISITIONS = "acquisitions"

ALL_ACTIONS = [LISTED, DELISTED, SPLITS, CHANGES, SPINOFFS, BANKCRUPTCIES, ACQUISITIONS]


def get_corporate_actions() -> List:
    data = []
    url = "https://stockanalysis.com/actions/"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    main = soup.find("main", {"id": "main"})
    table = main.find("table")
    metadate, data = get_data_from_time_series_table(table)

    return metadate, data


def check_action_type(action_type: str) -> bool:
    return action_type in ALL_ACTIONS


def check_year(year: int) -> bool:
    return year >= 1998 or -1


def compute_action_url(action_type: str, year: int = -1) -> str:
    if not check_action_type(action_type):
        raise ValueError(f"{action_type} is not a valid action type")
    if not check_year(year):
        raise ValueError(f"{year} is not a valid year")
    
    if year == -1:
        return f"https://stockanalysis.com/actions/{action_type}"
    
    return f"https://stockanalysis.com/actions/{action_type}/{year}"


def get_actions_by_type(action_type: str, year: int = -1) -> List:
    url = compute_action_url(action_type, year)
    data = []
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    main = soup.find("main", {"id": "main"})
    table = main.find("table")
    metadate, data = get_data_from_time_series_table(table)

    return metadate, data