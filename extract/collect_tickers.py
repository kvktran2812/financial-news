import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import List, Sequence, Dict, Tuple


def get_all_tickers() -> List[str]:
    url = "https://stockanalysis.com/stocks/"

    # Set chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.ID, 'main')))

    for e in elements:
        print(e.text)

    driver.quit()
    return


def get_table_head_data(table: str) -> List[str]:
    thead_data = []
    thead = table.find('thead')
    ths = thead.find_all("th")

    for th in ths:
        thead_data.append(th.text.strip())

    return thead_data


def get_table_body_data(table, n: int = -1) -> List[List[str]]:
    tbody_data = []
    tbody = table.find("tbody")
    trs = tbody.find_all('tr')

    for tr in trs:
        td = tr.find_all('td')
        td = [t.text.strip() for t in td]
        tbody_data.append(td)
    return tbody_data


def get_ticker_detail() -> Dict[str, str]:
    return


get_all_tickers()