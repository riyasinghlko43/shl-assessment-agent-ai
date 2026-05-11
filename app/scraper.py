import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"


def scrape_catalog():

    print("Fetching SHL catalog...")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(BASE_URL, headers=headers)

    print("Status Code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    assessments = []

    # find all product cards
    links = soup.find_all("a", href=True)

    for link in links:

        href = link["href"]

        text = link.get_text(strip=True)

        if "/products/" in href:

            if len(text) > 2:

                if not href.startswith("http"):
                    href = "https://www.shl.com" + href

                assessments.append({
                    "name": text,
                    "url": href
                })

    # remove duplicates
    unique = []
    seen = set()

    for item in assessments:

        if item["url"] not in seen:

            unique.append(item)

            seen.add(item["url"])

    with open("app/catalog.json", "w", encoding="utf-8") as f:

        json.dump(unique, f, indent=4)

    print(f"Saved {len(unique)} assessments")


if __name__ == "__main__":

    scrape_catalog()