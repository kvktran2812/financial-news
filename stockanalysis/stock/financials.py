# TODO: Organize and optimize this code
# TODO: Add docstring

import requests
from bs4 import BeautifulSoup
from typing import List

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


def get_income_statement(stock: str, fiscal_period: str = "annual") -> List:
    url = compute_url(stock, fiscal_period, "income")
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


def get_balance_sheet(stock: str, fiscal_period: str = "annual") -> List:
    url = compute_url(stock, fiscal_period, "balance")
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


def get_cash_flow(stock: str, fiscal_period: str = "annual") -> List:
    url = compute_url(stock, fiscal_period, "cash")
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


def get_ratios(stock: str, fiscal_period: str = "annual") -> List:
    url = compute_url(stock, fiscal_period, "ratios")
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
