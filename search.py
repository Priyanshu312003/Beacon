import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_web(query: str, num_results: int = 5) -> list[str]:
    """
    Search the web for a query.
    Return a list of URLs.
    """
    results = client.search(query, max_results=num_results)
    # print(f"Search results for '{query}':", results)
    
    return [r["url"] for r in results["results"]]
    
if __name__ == "__main__":
    urls = search_web("what is RAG?")
    print(urls)