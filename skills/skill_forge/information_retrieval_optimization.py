from core.router import ask
from core.files import write_file
from core.search import search, search_news
from datetime import datetime
import os

def optimize_database_retrieval(query):
    thought = ask(f"Optimizing database retrieval for query: {query}")
    result = search(query)
    write_file(f"database_retrieval_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt", result)
    return thought

def optimize_document_retrieval(document, query):
    thought = ask(f"Optimizing document retrieval for query: {query} in document: {document}")
    result = search(query, document)
    write_file(f"document_retrieval_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt", result)
    return thought

def optimize_internet_retrieval(query):
    thought = ask(f"Optimizing internet retrieval for query: {query}")
    result = search_news(query)
    write_file(f"internet_retrieval_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt", result)
    return thought

def optimize_information_retrieval(query, source):
    thought = ask(f"Optimizing information retrieval for query: {query} from source: {source}")
    if source == "database":
        result = optimize_database_retrieval(query)
    elif source == "document":
        result = optimize_document_retrieval("example_document", query)
    elif source == "internet":
        result = optimize_internet_retrieval(query)
    write_file(f"information_retrieval_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt", result)
    return thought

SKILLS = {
    "Information Retrieval Optimization": optimize_information_retrieval,
    "Database Retrieval Optimization": optimize_database_retrieval,
    "Document Retrieval Optimization": optimize_document_retrieval,
    "Internet Retrieval Optimization": optimize_internet_retrieval
}

print(f"Loaded {len(SKILLS)} skills")