from ddgs import DDGS
import time

def search(query, max_results=5):
    """Search the web using DuckDuckGo — unlimited & free"""
    print(f"🔍 Searching: {query}")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            if results:
                formatted = []
                for i, r in enumerate(results, 1):
                    formatted.append(f"{i}. {r['title']}\n   {r['href']}\n   {r['body']}")
                output = "\n\n".join(formatted)
                print(f"✅ Found {len(results)} results")
                return output
            return "No results found"
    except Exception as e:
        print(f"⚠️ Search failed: {e}")
        return None

def search_news(query, max_results=5):
    """Search latest news"""
    print(f"📰 Searching news: {query}")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.news(query, max_results=max_results))
            if results:
                formatted = []
                for i, r in enumerate(results, 1):
                    formatted.append(f"{i}. {r['title']}\n   {r['url']}\n   {r['body']}")
                output = "\n\n".join(formatted)
                print(f"✅ Found {len(results)} news results")
                return output
            return "No news found"
    except Exception as e:
        print(f"⚠️ News search failed: {e}")
        return None
