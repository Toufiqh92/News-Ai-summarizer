import requests
from bs4 import BeautifulSoup
import time
import random

def get_nytimes_headlines():
    """Get headlines from NY Times"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get('https://www.nytimes.com', headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        headlines = []
        # Look for headline elements
        for headline in soup.find_all(['h1', 'h2', 'h3'], class_=lambda x: x and 'headline' in x.lower()):
            if headline.text.strip():
                headlines.append(headline.text.strip())
        
        # If no headlines found, try alternative selectors
        if not headlines:
            for headline in soup.find_all(['h1', 'h2', 'h3'])[:10]:
                if headline.text.strip() and len(headline.text.strip()) > 20:
                    headlines.append(headline.text.strip())
        
        return headlines[:5]  # Return top 5 headlines
    except Exception as e:
        print(f"Error scraping NY Times: {e}")
        return []

def get_nypost_headlines():
    """Get headlines from NY Post"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get('https://nypost.com', headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        headlines = []
        # Look for headline elements
        for headline in soup.find_all(['h1', 'h2', 'h3'])[:15]:
            if headline.text.strip() and len(headline.text.strip()) > 15:
                headlines.append(headline.text.strip())
        
        return headlines[:5]
    except Exception as e:
        print(f"Error scraping NY Post: {e}")
        return []

def get_amny_headlines():
    """Get headlines from AM New York"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get('https://www.amny.com', headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        headlines = []
        for headline in soup.find_all(['h1', 'h2', 'h3'])[:10]:
            if headline.text.strip() and len(headline.text.strip()) > 20:
                headlines.append(headline.text.strip())
        
        return headlines[:5]
    except Exception as e:
        print(f"Error scraping AM New York: {e}")
        return []

def scrape_all_news():
    """Scrape headlines from all news sources"""
    print("Starting news scraping...")
    
    all_headlines = []
    
    # Scrape each source
    all_headlines.extend(get_nytimes_headlines())
    time.sleep(random.uniform(1, 3))  # Be nice to servers
    
    all_headlines.extend(get_nypost_headlines())
    time.sleep(random.uniform(1, 3))
    
    all_headlines.extend(get_amny_headlines())
    
    # Remove duplicates and clean up
    unique_headlines = list(set(all_headlines))
    clean_headlines = [h.strip() for h in unique_headlines if h.strip() and len(h.strip()) > 10]
    
    print(f"Scraped {len(clean_headlines)} headlines")
    return clean_headlines[:15]  # Return top 15 unique headlines

if __name__ == "__main__":
    headlines = scrape_all_news()
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline}")
