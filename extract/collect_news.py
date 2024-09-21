import bs4
import requests
from pymongo import MongoClient


def get_daily_news():
    url = "https://ca.finance.yahoo.com/topic/news/"
    response = requests.get(url)

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    new_list = soup.find_all("li", class_="js-stream-content Pos(r)")
    data = []

    for li in new_list:
        h3 = li.find("h3")
        a = h3.find("a")
        link = a.get("href")
        para = get_article_text(link)

        data.append(
            {
                "title": a.text,
                "link": a.get("href"),
                "content": para,
            }
        )
    return data


def get_article_text(url):
    if url[0] == "/":
        url = "https://ca.finance.yahoo.com" + url
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", class_="caas-body")
    paragraphs = content.find_all("p")

    data = []

    for p in paragraphs:
        data.append(p.text)
    return data


if __name__ == "__main__":
    data = get_daily_news()

    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["mycollection"]

    collection.insert_many(data)
