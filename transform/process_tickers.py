import pandas as pd
import csv
from typing import List, Sequence, Dict, Tuple


def process_tickers():
    new_lines = []
    with open("tickers.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("(", "")
            line = line.replace(")", "")
            new_lines.append(line)
            # print(line)

    with open("tickers.txt", "w") as f:
        for line in new_lines:
            # print(line)
            f.write(line)


def get_tickers_info(ticker: Sequence[str]) -> Tuple[str]:
    symbol = ticker[-1]
    company = ""

    for i in range(len(ticker) - 1):
        company += ticker[i] + " "
    company = company.strip()

    return symbol, company


def save_tickers_to_csv():
    with open("tickers.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            symbol, company = get_tickers_info(line.split())
            # print(symbol, company)

    with open("tickers.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["symbol", "company"])
        for line in lines:
            symbol, company = get_tickers_info(line.split())
            writer.writerow([symbol, company])


if __name__ == "__main__":
    process_tickers()
    save_tickers_to_csv()

    df = pd.read_csv("tickers.csv")
    print(df)