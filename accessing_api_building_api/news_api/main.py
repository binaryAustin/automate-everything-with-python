import os
from dotenv import load_dotenv
import requests

load_dotenv(".env")

news_api_key = os.getenv("NEWS_API_KEY")


def get_news(topic: str, from_date: str, to_date: str, lang="en"):
    url = f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sortBy=relevancy&language={lang}&pageSize=10&apiKey={news_api_key}"
    res = requests.get(url, timeout=10.0)
    content = res.json()
    articles = content["articles"]
    results = [
        {"title": article["title"], "description": article["description"]}
        for article in articles
    ]
    return results
