import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def synthesize_report(topic: str, scraped_texts: list[str]) -> str:
    """
    Given a topic and list of scraped page texts,
    return a structured markdown report.
    """
    
    prompt = f"""
    You are a research assistant.
    Topic: {topic}

    Web page texts:
    {chr(10).join(scraped_texts)}

    Write a structured markdown report on the topic based on the texts above.
    Include: Summary, Key Findings, and Conclusion.
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    texts = [
        "RAG stands for Retrieval Augmented Generation. It combines search with LLMs.",
        "RAG pipelines fetch relevant documents and pass them to the LLM as context."
    ]
    print(synthesize_report("What is RAG?", texts))