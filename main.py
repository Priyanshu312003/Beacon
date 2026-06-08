from search import search_web
from scraper import scrape_page
from synthesizer import synthesize_report

def run_beacon(topic: str):
    print("Searching web...")
    urls = search_web(topic)
    
    print("Scraping pages...")
    pages = [scrape_page(url) for url in urls]
    
    print("Synthesizing report...")
    report = synthesize_report(topic,pages)
    
    with open(f"{topic.replace(' ', '_')}_report.md","w") as f:
        f.write(report)
    print(f"Report saved!")
        
if __name__ == "__main__":
    topic = input("Enter a topic to research: ")
    run_beacon(topic)