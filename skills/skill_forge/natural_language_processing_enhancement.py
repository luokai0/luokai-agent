from core.router import ask
from core.files import write_file
from core.search import search, search_news
from datetime import datetime
import os

def enhance_nlp_context(context):
    response = ask(f"Enhance NLP context: {context}")
    write_file("nlp_context.txt", response)
    return response

def generate_nlp_response(query):
    response = ask(f"Generate NLP response: {query}")
    write_file("nlp_response.txt", response)
    return response

def analyze_nlp_sentiment(text):
    response = ask(f"Analyze NLP sentiment: {text}")
    write_file("nlp_sentiment.txt", response)
    return response

def search_nlp_related_topics(topic):
    response = ask(f"Search NLP related topics: {topic}")
    write_file("nlp_related_topics.txt", response)
    return response

def search_nlp_news(query):
    response = search_news(query)
    write_file("nlp_news.txt", response)
    return response

SKILLS = {
    "enhance_nlp_context": enhance_nlp_context,
    "generate_nlp_response": generate_nlp_response,
    "analyze_nlp_sentiment": analyze_nlp_sentiment,
    "search_nlp_related_topics": search_nlp_related_topics,
    "search_nlp_news": search_nlp_news
}

print(f"Loaded {len(SKILLS)} skills")