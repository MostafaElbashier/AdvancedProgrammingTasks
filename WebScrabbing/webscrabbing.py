import requests
from bs4 import BeautifulSoup
import json


def scrape_local():
    with open("sample_data.html", "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    data = []
    for product in soup.find_all("div", class_="product"):
        data.append(
            {
                "name": product.find("h2", class_="name").get_text(),
                "price": product.find("p", class_="price").get_text(),
                "description": product.find("p", class_="description").get_text(),
            }
        )
    return data


def scrape_web():
    response = requests.get("http://quotes.toscrape.com/", timeout=5)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []
    for quote in soup.find_all("div", class_="quote"):
        data.append(
            {
                "quote": quote.find("span", class_="text").get_text(),
                "author": quote.find("small", class_="author").get_text(),
            }
        )
    return data


if __name__ == "__main__":
    try:
        data = scrape_web()
        print(f"Web: {len(data)} items")
    except:
        data = scrape_local()
        print(f"Local: {len(data)} items")

    with open("scraped_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Saved")
