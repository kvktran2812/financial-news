from bs4 import BeautifulSoup
from typing import List, Dict


def get_data_from_listed_table(table) -> Dict[str, str]:
    data = {}
    rows = table.find_all("tr")

    for row in rows:
        td = row.find_all("td")
        attribute = td[0].text.strip()
        value = td[1].text.strip()

        data[attribute] = value

    return data


def get_data_from_time_series_table(table):
    # compute meta data
    metadata = []
    thead = table.find("thead")
    rows = thead.find_all("tr")
    for row in rows:
        th = row.find_all("th")
        attributes = [t.text.strip() for t in th]
        metadata.append(attributes)

    # compute data
    data = []
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")

    for row in rows:
        td = row.find_all("td")
        values = [t.text.strip() for t in td]
        data.append(values)

    return metadata, data


def get_data_from_multi_period_comparison_table(table):
    return





def print_dict(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")


def print_list(list):
    for item in list:
        print(item)