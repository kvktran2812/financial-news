import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from constants import BASE_URL, DIVIDEND


def compute_dividends_url(stock: str) -> str:
    return f"{BASE_URL}/{stock}/{DIVIDEND}"


def get_dividends(stock: str) -> List[Dict[str, str]]:
    url = compute_dividends_url(stock)
    data = []

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    main = soup.find("main")
    table = main.find("table")
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")
    for row in rows:
        td = row.find_all("td")
        t_data = []
        for i in td:
            t_data.append(i.text.strip())
        data.append(t_data)

    return data


data = get_dividends("aapl")
for d in data:
    print(d)