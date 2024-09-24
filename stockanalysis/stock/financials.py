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
BASE_URL = "https://stockanalysis.com/stocks/"
FM_ANNUAL = 1
FM_QUARTERLY = 2
FM_TTM = 3


def get_income_statement(stock: str, fiscal_period: str = "annually") -> List:
    
    
    return 


def get_balance_sheet(stock: str, fiscal_period: str = "annually") -> List:
    
    
    return


def get_cash_flow(stock: str, fiscal_period: str = "annually") -> List:
    
    
    return


def get_ratios(stock: str, interval: str = "annually") -> List:
    
    
    return