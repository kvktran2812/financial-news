import time
import math
import requests
from bs4 import BeautifulSoup
from typing import List, Sequence, Dict, Tuple

# Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# define constants
BASE_URL = "https://stockanalysis.com/stocks"
INCOME = "financials"
BALANCE_SHEET = "balance-sheet"
CASH_FLOW = "cash-flow-statement"
RATIOS = "ratios"

# fiscal period type
FM_ANNUAL = 1
FM_QUARTERLY = 2
FM_TTM = 3


def get_fiscal_period_params(fiscal_period):
    if fiscal_period == FM_ANNUAL:
        return ""
    elif fiscal_period == FM_QUARTERLY:
        return "quarterly"
    elif fiscal_period == FM_TTM:
        return "trailing"
    else:
        raise ValueError(f"Invalid fiscal period: {fiscal_period}")
    

def compute_url(stock, fiscal_period, financial_type):
    pass
    

def get_number_of_columns(rows):
    first_row = rows[0]
    headers = first_row.find_all("th")
    columns = list(filter(lambda h: h["id"] != "header-title" and h["id"] != "header-cell", headers))
    return len(columns)


def get_data_from_thead(rows, data, n):
    first_row = rows[0]
    headers = first_row.find_all("th")
    columns = list(filter(lambda h: h["id"] != "header-title" and h["id"] != "header-cell", headers))

    fiscal_period = headers[0].text.strip()

    for i in range(n):
        data[i][fiscal_period] = columns[i].text.strip()
        data[i]["Period Ending"] = columns[i]["id"]
    return 


def get_data_from_tbody(rows, data, n):
    for row in rows:
        t_data = row.find_all("td")
        attribute = t_data[0].text.strip()

        for i in range(n):
            data[i][attribute] = t_data[i+1].text.strip()


def get_income_statement(stock: str, fiscal_period: str = FM_ANNUAL) -> List:
    FP = get_fiscal_period_params(fiscal_period)
    url = f"{BASE_URL}/{stock}/{INCOME}/?p={FP}"
    print(url)


    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    thead = table.find("thead")
    tbody = table.find("tbody")
    head_rows = thead.find_all("tr")
    body_rows = tbody.find_all("tr")
    
    # Data initialization
    n = get_number_of_columns(head_rows)
    data = [{} for _ in range(n)]

    get_data_from_thead(head_rows, data, n)
    get_data_from_tbody(body_rows, data, n)
    
    return data


def get_balance_sheet(stock: str, fiscal_period: str = "annually") -> List:
    
    
    return


def get_cash_flow(stock: str, fiscal_period: str = "annually") -> List:
    
    
    return


def get_ratios(stock: str, interval: str = "annually") -> List:
    
    
    return



if __name__ == "__main__":
    print(get_income_statement("aapl"))