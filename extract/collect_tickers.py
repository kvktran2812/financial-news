import requests
import bs4
from typing import List, Sequence, Dict, Tuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


def get_all_tickers(web_driver: str) -> List[str]:
    url = "https://stockanalysis.com/stocks/"

    # Set chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    driver.get(url)
    time.sleep(1)

    elements = driver.find_elements(By.TAG_NAME, 'h1')

    for e in elements:
        print(e.text)

    driver.quit()
    return


get_all_tickers("../web_driver/chromedriver.exe")