import httpx
from bs4 import BeautifulSoup

def scrape_page(url: str) -> str:
    """
    Fetch a URL and return clean text content.
    """
    
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = soup.find_all("p")
    return " ".join([p.get_text() for p in paragraphs])

if __name__ == "__main__":
    print(scrape_page("https://memgraph.com/blog/previsant-ai-agents-graphrag-data-lineage-memgraph"))