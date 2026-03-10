# 🐉 LUO KAI AGENT — BROWSER CONTROL
# Full browser automation — see, click, scrape, control anything

from playwright.sync_api import sync_playwright
from core.files import write_file
from datetime import datetime
import os

SCREENSHOTS_DIR = "workspace/screenshots"
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def get_page_content(url):
    """Read full content of any webpage"""
    print(f"🌐 Reading: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            content = page.inner_text("body")
            title = page.title()
            browser.close()
            result = f"PAGE: {title}\nURL: {url}\n\n{content}"
            write_file(f"page_{timestamp()}.txt", result)
            print(f"✅ Page read: {title}")
            return result
        except Exception as e:
            browser.close()
            print(f"⚠️ Failed to read page: {e}")
            return None

def screenshot(url, filename=None):
    """Take screenshot of any webpage"""
    print(f"📸 Screenshotting: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            if not filename:
                filename = f"{SCREENSHOTS_DIR}/screenshot_{timestamp()}.png"
            page.screenshot(path=filename, full_page=True)
            browser.close()
            print(f"✅ Screenshot saved: {filename}")
            return filename
        except Exception as e:
            browser.close()
            print(f"⚠️ Screenshot failed: {e}")
            return None

def scrape_links(url):
    """Extract all links from a webpage"""
    print(f"🔗 Scraping links: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            links = page.eval_on_selector_all(
                "a[href]",
                "elements => elements.map(el => ({text: el.innerText.trim(), href: el.href}))"
            )
            browser.close()
            result = "\n".join([f"{l['text']} → {l['href']}" for l in links if l['href'].startswith('http')])
            write_file(f"links_{timestamp()}.txt", result)
            print(f"✅ Found {len(links)} links")
            return result
        except Exception as e:
            browser.close()
            print(f"⚠️ Link scrape failed: {e}")
            return None

def scrape_table(url, table_index=0):
    """Extract tables from any webpage"""
    print(f"📊 Scraping table from: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            tables = page.eval_on_selector_all(
                "table",
                """tables => tables.map(table => {
                    const rows = Array.from(table.querySelectorAll('tr'));
                    return rows.map(row => {
                        const cells = Array.from(row.querySelectorAll('td, th'));
                        return cells.map(cell => cell.innerText.trim()).join(' | ');
                    }).join('\\n');
                })"""
            )
            browser.close()
            if tables and table_index < len(tables):
                result = tables[table_index]
                write_file(f"table_{timestamp()}.txt", result)
                print(f"✅ Table extracted")
                return result
            return "No tables found"
        except Exception as e:
            browser.close()
            print(f"⚠️ Table scrape failed: {e}")
            return None

def fill_and_submit_form(url, form_data):
    """Fill and submit any web form"""
    print(f"📝 Filling form at: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            for selector, value in form_data.items():
                try:
                    page.fill(selector, value)
                    print(f"  ✅ Filled: {selector}")
                except:
                    print(f"  ⚠️ Could not fill: {selector}")
            screenshot_path = f"{SCREENSHOTS_DIR}/form_filled_{timestamp()}.png"
            page.screenshot(path=screenshot_path)
            browser.close()
            print(f"✅ Form filled — screenshot saved")
            return screenshot_path
        except Exception as e:
            browser.close()
            print(f"⚠️ Form fill failed: {e}")
            return None

def click_and_extract(url, click_selector, extract_selector):
    """Click something and extract the result"""
    print(f"🖱️ Clicking {click_selector} at: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            page.click(click_selector)
            page.wait_for_load_state("networkidle")
            result = page.inner_text(extract_selector)
            browser.close()
            write_file(f"clicked_{timestamp()}.txt", result)
            print(f"✅ Clicked and extracted content")
            return result
        except Exception as e:
            browser.close()
            print(f"⚠️ Click failed: {e}")
            return None

def google_search_scraper(query, num_results=10):
    """Scrape Google search results directly"""
    print(f"🔍 Google scraping: {query}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(f"https://www.google.com/search?q={query.replace(' ', '+')}", timeout=30000)
            page.wait_for_selector("h3", timeout=10000)
            results = page.eval_on_selector_all(
                "h3",
                "elements => elements.map(el => ({title: el.innerText, url: el.closest('a') ? el.closest('a').href : ''}))"
            )
            browser.close()
            output = "\n".join([f"{i+1}. {r['title']}\n   {r['url']}" for i, r in enumerate(results[:num_results]) if r['title']])
            write_file(f"google_{timestamp()}.txt", output)
            print(f"✅ Google scraped: {len(results)} results")
            return output
        except Exception as e:
            browser.close()
            print(f"⚠️ Google scrape failed: {e}")
            return None

def monitor_page_changes(url, check_selector):
    """Check if something on a page has changed"""
    print(f"👁️ Monitoring: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, wait_until="networkidle", timeout=30000)
            content = page.inner_text(check_selector)
            browser.close()
            result = f"MONITORED: {url}\nSELECTOR: {check_selector}\nCONTENT:\n{content}"
            write_file(f"monitor_{timestamp()}.txt", result)
            print(f"✅ Page monitored")
            return content
        except Exception as e:
            browser.close()
            print(f"⚠️ Monitor failed: {e}")
            return None

def multi_page_scraper(urls, extract_selector="body"):
    """Scrape multiple pages at once"""
    print(f"🕷️ Scraping {len(urls)} pages...")
    results = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for url in urls:
            page = browser.new_page()
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
                content = page.inner_text(extract_selector)
                results[url] = content[:500]
                print(f"  ✅ Scraped: {url[:50]}")
                page.close()
            except Exception as e:
                results[url] = f"Failed: {e}"
                page.close()
        browser.close()
    output = "\n\n".join([f"URL: {url}\n{content}" for url, content in results.items()])
    write_file(f"multi_scrape_{timestamp()}.txt", output)
    return output

def web_researcher(topic):
    """Full web research — search + read top pages + summarize"""
    from core.search import search
    from core.router import ask
    print(f"🔬 Deep web research: {topic}")
    search_results = search(topic, max_results=5)
    import re
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', search_results or "")
    pages_content = ""
    for url in urls[:3]:
        content = get_page_content(url)
        if content:
            pages_content += f"\n\n--- FROM {url} ---\n{content[:1000]}"
    full_prompt = f"Research topic: {topic}\n\nSearch results:\n{search_results}\n\nPage contents:{pages_content}\n\nWrite a comprehensive research report."
    result = ask(full_prompt)
    write_file(f"deep_research_{timestamp()}.txt", result)
    print(f"✅ Deep research complete")
    return result

print("🌐 Browser Control loaded — Luo Kai Agent can now see and control the web!")
