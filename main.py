import os
from search import search_web
from synthesizer import synthesize_report

def run_beacon(topic: str):
    print("Searching web...")
    results = search_web(topic)
    pages = [r["content"] for r in results]
    
    print("Synthesizing report...")
    report = synthesize_report(topic,pages)
    
    os.makedirs("outputs", exist_ok=True)
    filename = f"outputs/{topic.replace(' ', '_')}_report.md"

    with open(filename, "w") as f:
        f.write(report)
    print(f"Report saved to {filename}!")
        
if __name__ == "__main__":
    topic = input("Enter a topic to research: ")
    run_beacon(topic)