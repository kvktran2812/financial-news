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

# import modules
from stockanalysis.utils import *

def get_number_of_stocks(html: str) -> int:
    """
    Get the number of stocks from the html

    Args:
        html (str): The input html, looks for the h2 tag and retrieve data from there

    Returns:
        int: The number of stocks
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


def get_all_stocks(stock_per_page=500, early_stop=False) -> List[List[str]]:
    """
    Get all stocks from stockanalysis website

    Args:
        t_per_page (int, optional): The number of stocks per page. Defaults to 500.

    Returns:
        List[List[str]]: a list of all stocks
    """
    # setup url and data variable
    url = "https://stockanalysis.com/stocks/"
    data = None
    metadata = []

    # setup chrome 
    chrome_options = Options()
    chrome_options.add_argument("--headless")
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
    # data = get_table_body_data(table)
    metadata, data = get_data_from_time_series_table(table)
    n = get_number_of_stocks(soup)
    n = n // stock_per_page

    # early stop
    if early_stop:
        return metadata, data

    # go to next page and keep fetching data until reach last stock
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
    return metadata, data


def get_stock_overview(stock: str) -> Dict[str, str]:
    """
    Get stock overview data from stockanalysis

    Args:
        stock (str): name of the stock

    Raises:
        ConnectionError: if the somehow the status code is not 200, meaning the request is not successful

    Returns:
        Dict[str, str]: a dictionary of overview data
    """
    data = dict()
    url = "https://stockanalysis.com/stocks/" + stock

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main", {"id": "main"})
    tables = main.find_all("table")
    
    for table in tables:
        t_data = get_data_from_listed_table(table)
        data.update(t_data)
    
    return data


def get_stock_news_press_release(stock: str) -> List[Dict[str, str]]:
    """
    Get stock news and press release from stockanalysis

    Args:
        stock (str): name of the stock

    Returns:
        List[Dict[str, str]]: a list of news and press release information
    """
    data = list()
    url = "https://stockanalysis.com/stocks/" + stock

    # setup chrome
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    # send request to website     
    driver.get(url)
    elements = wait.until(EC.presence_of_element_located((By.ID, 'main')))
    button = driver.find_element(By.XPATH, '//*[@id="main"]/div[3]/div[2]/div/div[1]/div/ul/li[3]/button')
    button.click()
    time.sleep(0.5)
    elements = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div[3]/div[2]/div/div[2]')))
    
    # fetch data and retrive useful information
    html = elements.get_attribute("innerHTML")
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find("body")
    news = body.find_all("div", recursive=False)

    for single_news in news:
        title = single_news.find("h3").text
        link = single_news.find("a").get("href")
        summary = single_news.find("p").text
        time_upload = single_news.find("div", {"class": "mt-1 text-sm text-faded sm:order-1 sm:mt-0"}).get("title")
        data.append({
            "title": title,
            "link": link,
            "summary": summary,
            "time_upload": time_upload
        })

    driver.quit()
        
    return data