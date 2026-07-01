import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get("https://labs.limitlesstcg.com/0070/standings")
doc = BeautifulSoup(response.text, "lxml")

items = doc.select("tr.day2, tr.day1, tr.topcut")

rows = []

for item in items:
    cells = item.select("td")
    if len(cells) < 7:
        continue

    row = {
        "rank":       cells[0].get_text(strip=True),
        "player":     item.select_one("td:nth-child(2) a").get_text(strip=True),
        "country":    item.select_one("img[title]")["title"] if item.select_one("img[title]") else "",
        "points":     cells[3].get_text(strip=True),
        "record":     cells[4].get_text(strip=True),
        "owr":        cells[5].get_text(strip=True),
        "oowp":       cells[6].get_text(strip=True),
        "deck":       item.select_one(".pokemon")["alt"] if item.select_one(".pokemon") else "",
        "player_url": "https://play.limitlesstcg.net" + item.select_one("td:nth-child(2) a")["href"],
    }
    rows.append(row)

pd.options.display.max_colwidth = 500

df = pd.json_normalize(rows)
df.head()
print(df)

df.to_csv("standings.csv", index=False, encoding="utf-8-sig")