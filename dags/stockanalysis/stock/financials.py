# TODO: Organize and optimize this code
# TODO: Add docstring

import requests
from bs4 import BeautifulSoup
from typing import List
from stockanalysis.utils import get_data_from_financials_table

# define constants
BASE_URL = "https://stockanalysis.com/stocks"
INCOME = "financials"
BALANCE_SHEET = "balance-sheet"
CASH_FLOW = "cash-flow-statement"
RATIOS = "ratios"

# fiscal period type
FM_ANNUAL = "annual"
FM_QUARTERLY = "quarter"
FM_TTM = "ttm"


def get_fiscal_period_params(fiscal_period):
    if fiscal_period == FM_ANNUAL:
        return ""
    elif fiscal_period == FM_QUARTERLY:
        return "quarterly"
    elif fiscal_period == FM_TTM:
        return "trailing"
    else:
        raise ValueError(f"Invalid fiscal period: {fiscal_period}")
    

def get_statement_type(statement_type):
    if statement_type == "income":
        return INCOME
    elif statement_type == "balance":
        return INCOME + "/" + BALANCE_SHEET
    elif statement_type == "cash":
        return INCOME + "/" + CASH_FLOW
    elif statement_type == "ratios":
        return INCOME + "/" + RATIOS
    else:
        raise ValueError(f"Invalid statement type: {statement_type}")


def compute_url(stock, fiscal_period, financial_type):
    fiscal_period = get_fiscal_period_params(fiscal_period)
    statement_type = get_statement_type(financial_type)
    url = f"{BASE_URL}/{stock}/{statement_type}/?p={fiscal_period}"
    return url


def get_income_statement(stock: str, fiscal_period: str = "annual") -> List:
    url = compute_url(stock, fiscal_period, "income")

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    metadata, data = get_data_from_financials_table(table)
    
    return metadata, data


def get_balance_sheet(stock: str, fiscal_period: str = "annual") -> List:
    url = compute_url(stock, fiscal_period, "balance")

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    metadata, data = get_data_from_financials_table(table)
    
    return metadata,data


def get_cash_flow(stock: str, fiscal_period: str = "annual") -> List:
    url = compute_url(stock, fiscal_period, "cash")

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    metadata, data = get_data_from_financials_table(table)

    return metadata, data


def get_ratios(stock: str, fiscal_period: str = "annual") -> List:
    url = compute_url(stock, fiscal_period, "ratios")

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    metadata, data = get_data_from_financials_table(table)

    return metadata, data