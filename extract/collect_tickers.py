from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from typing import List, Sequence, Dict, Tuple
import time
import math


def get_number_of_tickers(html: str) -> int:
    n = 0

    h2 = html.find("h2")
    text = h2.text.split(' ')
    n = int(text[0])

    return n


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


def get_all_tickers(t_per_page=500) -> List[List[str]]:
    url = "https://stockanalysis.com/stocks/"
    data = None
    
    # setup chrome
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    # setup elements
    driver.get(url)
    elements = wait.until(EC.presence_of_element_located((By.ID, 'main')))
    next_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/nav/button[2]')

    # fetch data
    html = elements.get_attribute("innerHTML")
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("table", {"id": "main-table"})
    data = get_table_body_data(table)
    n = get_number_of_tickers(soup)
    n = n // t_per_page
    

    for i in range(n):
        next_button.click()
        time.sleep(0.5)
        elements = wait.until(EC.presence_of_element_located((By.ID, 'main')))
        html = elements.get_attribute("innerHTML")
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find("table", {"id": "main-table"})
        t_data = get_table_body_data(table)
        data.extend(t_data)

    driver.quit()
    
    return data


def get_ticker_detail() -> Dict[str, str]:
    return


get_all_tickers()