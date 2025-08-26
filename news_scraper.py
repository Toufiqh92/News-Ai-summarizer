import requests
from bs4 import BeautifulSoup
import time, random

def get_nytimes_headlines():
    try:
        response = requests.get("https://www.nytimes.com", headers={"User-Agent": "Mozilla/5.0"}, timeout=10) # NY Times
        soup = BeautifulSoup(response.content, "html.parser")  # Parse HTML
        headlines = [] # Store headlines
        for tag in soup.find_all(["h1", "h2", "h3"])[:15]: # Look for headline tags
            text = tag.get_text(strip=True) # Get text
            link = tag.find("a") # Find link
            if text and link and link.get("href"): # Ensure valid headline and link
                url = link["href"]
                if url.startswith("/"): # Relative URL
                    url = "https://www.nytimes.com" + url
                headlines.append({"title": text, "url": url}) #

        return headlines[:5]
    except Exception as e:
        print(f"Error scraping NY Times: {e}") # error handling
        return []
def get_nypost_headlines(): # Get headlines from NY Post
    try:
        response = requests.get("https://nypost.com", headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        headlines = []
        for tag in soup.find_all(["h1", "h2", "h3"])[:15]:
            text = tag.get_text(strip=True)
            link = tag.find("a")
            if text and len(text) > 15 and link and link.get("href"):
                url = link["href"]
                if url.startswith("/"):
                    url = "https://nypost.com" + url
                headlines.append({"title": text, "url": url})

        return headlines[:5]
    except Exception as e:
        print(f"Error scraping NY Post: {e}")
        return []
def get_amny_headlines():
    try:
        response = requests.get("https://www.amny.com", headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")

        headlines = []
        for tag in soup.find_all(["h1", "h2", "h3"])[:15]:
            text = tag.get_text(strip=True)
            link = tag.find("a")
            if text and len(text) > 20 and link and link.get("href"):
                url = link["href"]
                if url.startswith("/"):
                    url = "https://www.amny.com" + url
                headlines.append({"title": text, "url": url})
        return headlines[:5]
    except Exception as e:
        print(f"Error scraping AM New York: {e}")
        return []

def scrape_all_news():
    """Scrape all news sources and combine unique headlines"""
    print("Starting news scraping...")
    all_headlines = []

    # Scrape each source
    all_headlines.extend(get_nytimes_headlines())
    time.sleep(random.uniform(1, 3))

    all_headlines.extend(get_nypost_headlines())
    time.sleep(random.uniform(1, 3))

    all_headlines.extend(get_amny_headlines())

    # Deduplicate by title
    seen = set()
    unique_headlines = []
    for h in all_headlines:
        if h["title"] not in seen:
            seen.add(h["title"])
            unique_headlines.append(h)

    print(f"Scraped {len(unique_headlines)} headlines")
    return unique_headlines[:15]

if __name__ == "__main__":
    headlines = scrape_all_news()
    for i, item in enumerate(headlines, 1):
        print(f"{i}. {item['title']} ({item['url']})")
