import httpx
from bs4 import BeautifulSoup

def scrape_page(url: str) -> str:
    """
    Fetch a URL and return clean text content.
    """
    try:
        response = httpx.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join([p.get_text() for p in paragraphs])
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""
    
if __name__ == "__main__":
    print(scrape_page("https://memgraph.com/blog/previsant-ai-agents-graphrag-data-lineage-memgraph"))