import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    titles = [a.text for a in soup.select('.titleline > a')]
    return titles

def save_titles(titles):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(f"data/{date}.json", "w") as f:
        json.dump(titles, f, indent=2)

if __name__ == "__main__":
    titles = scrape_hackernews()
    print(f"Scraped {len(titles)} titles.")
    save_titles(titles)

# update 3 - refactor: separate save function
# update 9 - docs: explain JSON format
# update 15 - fix: error on empty headline list
