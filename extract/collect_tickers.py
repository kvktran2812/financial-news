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
    """
    Get the number of tickers from the html

    Args:
        html (str): The input html, looks for the h2 tag and retrieve data from there

    Returns:
        int: The number of tickers
    """
    n = 0

    h2 = html.find("h2")
    text = h2.text.split(" ")
    n = int(text[0])

    return n


def get_table_head_data(table: str) -> List[str]:
    """
    Get the head data from the table tag, useful for csv header

    Args:
        table (str): table tag from html

    Returns:
        List[str]: a list of head information
    """
    thead_data = []
    thead = table.find("thead")
    ths = thead.find_all("th")

    for th in ths:
        thead_data.append(th.text.strip())

    return thead_data


def get_table_body_data(table) -> List[List[str]]:
    """
    Get the body data from the table tag

    Args:
        table (_type_): table tag from html

    Returns:
        List[List[str]]: a list of body information
    """
    tbody_data = []
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")

    for tr in trs:
        td = tr.find_all("td")
        td = [t.text.strip() for t in td]
        tbody_data.append(td)
    return tbody_data


def get_all_tickers(t_per_page=500) -> List[List[str]]:
    """
    Get all tickers from stockanalysis website

    Args:
        t_per_page (int, optional): The number of tickers per page. Defaults to 500.

    Returns:
        List[List[str]]: a list of all tickers
    """
    # setup url and data variable
    url = "https://stockanalysis.com/stocks/"
    data = None

    # setup chrome
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    # setup elements
    driver.get(url)
    elements = wait.until(EC.presence_of_element_located((By.ID, "main")))
    next_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/nav/button[2]')

    # fetch data
    html = elements.get_attribute("innerHTML")
    soup = BeautifulSoup(html, "lxml")
    table = soup.find("table", {"id": "main-table"})
    data = get_table_body_data(table)
    n = get_number_of_tickers(soup)
    n = n // t_per_page

    # go to next page and keep fetching data until reach last ticker
    for i in range(n):
        next_button.click()
        time.sleep(0.5)
        elements = wait.until(EC.presence_of_element_located((By.ID, "main")))
        html = elements.get_attribute("innerHTML")
        soup = BeautifulSoup(html, "lxml")
        table = soup.find("table", {"id": "main-table"})
        t_data = get_table_body_data(table)
        data.extend(t_data)

    # close driver
    driver.quit()

    # return data
    return data


def get_ticker_detail() -> Dict[str, str]:
    return


if __name__ == "__main__":
    data = get_all_tickers()
    for member in data:
        print(member)
    print(len(data))