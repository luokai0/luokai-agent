# 🐉 LUO KAI AGENT — AUTONOMOUS BROWSER
# Does ANYTHING in a browser — search, click, fill forms, sign up, make money

from playwright.sync_api import sync_playwright
from core.router import ask
import json
import time

def browser_agent(goal, headless=True):
    """
    Give Luo Kai a goal — it figures out every step and does it in the browser.
    headless=True means you SEE the browser open on your screen!
    """
    print(f"\n🌐 Browser Agent starting: {goal}")
    
    # First plan the steps
    plan_prompt = f"""You are an autonomous browser agent. Plan exact steps to: {goal}

Return ONLY a JSON array of steps. Each step has:
- "action": one of [goto, click, type, search, scroll, wait, screenshot, extract]
- "value": what to do (URL, text to type, selector description, etc)
- "description": what this step does

Example:
[
  {{"action": "goto", "value": "https://google.com", "description": "Open Google"}},
  {{"action": "type", "value": "make money online 2026", "description": "Search query"}},
  {{"action": "click", "value": "search button", "description": "Submit search"}},
  {{"action": "extract", "value": "all results", "description": "Get results"}}
]

Goal: {goal}
Return ONLY the JSON array, nothing else."""

    steps_raw = ask(plan_prompt)
    
    try:
        if "```" in steps_raw:
            steps_raw = steps_raw.split("```")[1].replace("json","").strip()
        steps = json.loads(steps_raw.strip())
        print(f"📋 Plan: {len(steps)} steps")
        for i, s in enumerate(steps, 1):
            print(f"  {i}. {s.get('description', s.get('action'))}")
    except Exception as e:
        print(f"⚠️ Could not parse plan: {e}")
        steps = [{"action": "goto", "value": "https://google.com", "description": "Open Google"},
                 {"action": "search", "value": goal, "description": "Search for goal"}]

    results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=500)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        page = context.new_page()
        
        print(f"\n🖥️  Browser opened! Executing...")
        
        for i, step in enumerate(steps, 1):
            action = step.get("action", "")
            value = step.get("value", "")
            desc = step.get("description", action)
            
            print(f"\n  Step {i}: {desc}")
            
            try:
                if action == "goto":
                    if not value.startswith("http"):
                        value = "https://" + value
                    page.goto(value, timeout=15000)
                    print(f"    ✅ Opened: {value}")
                    time.sleep(1)

                elif action == "click":
                    # Use AI to find the right element
                    clicked = smart_click(page, value)
                    print(f"    ✅ Clicked: {value}")
                    time.sleep(1)

                elif action == "type":
                    page.keyboard.type(value, delay=50)
                    page.keyboard.press("Enter")
                    print(f"    ✅ Typed: {value}")
                    time.sleep(2)

                elif action == "search":
                    # Find search box and search
                    for selector in ['input[type="search"]', 'input[name="q"]', 'input[type="text"]', 'textarea']:
                        try:
                            page.fill(selector, value)
                            page.keyboard.press("Enter")
                            print(f"    ✅ Searched: {value}")
                            time.sleep(2)
                            break
                        except:
                            continue

                elif action == "fill":
                    # Fill a form field
                    parts = value.split("|")
                    if len(parts) == 2:
                        field, text = parts[0].strip(), parts[1].strip()
                        smart_fill(page, field, text)
                        print(f"    ✅ Filled {field}: {text}")
                    time.sleep(0.5)

                elif action == "scroll":
                    page.evaluate("window.scrollBy(0, 500)")
                    print(f"    ✅ Scrolled down")
                    time.sleep(1)

                elif action == "wait":
                    secs = int(value) if value.isdigit() else 2
                    print(f"    ⏳ Waiting {secs}s...")
                    time.sleep(secs)

                elif action == "extract":
                    content = page.content()
                    text = page.inner_text("body")[:3000]
                    results.append({"step": i, "content": text})
                    print(f"    ✅ Extracted {len(text)} chars")

                elif action == "screenshot":
                    path = f"workspace/screenshot_{int(time.time())}.png"
                    page.screenshot(path=path)
                    print(f"    📸 Screenshot: {path}")

            except Exception as e:
                print(f"    ⚠️ Step failed: {e}")
                continue

        # Get final page content
        try:
            final_content = page.inner_text("body")[:5000]
            final_url = page.url
        except:
            final_content = ""
            final_url = ""
        
        browser.close()
    
    # Summarize what happened
    if results or final_content:
        summary_prompt = f"""Goal was: {goal}
        
Browser visited: {final_url}
Content found: {final_content[:2000]}

Summarize: What was accomplished? What useful info was found? What are the next steps?
Be specific and actionable."""
        summary = ask(summary_prompt)
    else:
        summary = "Browser task completed but no content was extracted."
    
    print(f"\n🐉 Result:\n{summary}")
    
    # Save results
    from core.files import write_file
    from datetime import datetime
    report = f"Goal: {goal}\nURL: {final_url}\n\nSummary:\n{summary}\n\nRaw Content:\n{final_content}"
    write_file(f"browser_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", report)
    
    return summary


def smart_click(page, description):
    """Intelligently click an element by description"""
    # Try common selectors based on description
    desc_lower = description.lower()
    
    selectors = []
    
    if any(w in desc_lower for w in ["search", "find"]):
        selectors = ['button[type="submit"]', 'input[type="submit"]', '[aria-label="Search"]', '.search-button']
    elif any(w in desc_lower for w in ["submit", "send", "go"]):
        selectors = ['button[type="submit"]', 'input[type="submit"]', 'button:has-text("Submit")', 'button:has-text("Send")']
    elif any(w in desc_lower for w in ["next", "continue"]):
        selectors = ['button:has-text("Next")', 'button:has-text("Continue")', 'a:has-text("Next")']
    elif any(w in desc_lower for w in ["sign up", "register", "join"]):
        selectors = ['button:has-text("Sign up")', 'a:has-text("Sign up")', 'button:has-text("Register")', 'a:has-text("Join")']
    elif any(w in desc_lower for w in ["login", "sign in"]):
        selectors = ['button:has-text("Sign in")', 'a:has-text("Sign in")', 'button:has-text("Login")']
    else:
        selectors = [f'button:has-text("{description}")', f'a:has-text("{description}")', f'[aria-label="{description}"]']
    
    for sel in selectors:
        try:
            page.click(sel, timeout=3000)
            return True
        except:
            continue
    
    # Last resort - click by text
    try:
        page.get_by_text(description).first.click(timeout=3000)
        return True
    except:
        pass
    
    return False


def smart_fill(page, field_description, value):
    """Fill a form field intelligently"""
    desc_lower = field_description.lower()
    
    if "email" in desc_lower:
        selectors = ['input[type="email"]', 'input[name="email"]', 'input[placeholder*="email"]']
    elif "password" in desc_lower:
        selectors = ['input[type="password"]', 'input[name="password"]']
    elif "name" in desc_lower:
        selectors = ['input[name="name"]', 'input[placeholder*="name"]', 'input[name="username"]']
    elif "phone" in desc_lower:
        selectors = ['input[type="tel"]', 'input[name="phone"]', 'input[placeholder*="phone"]']
    else:
        selectors = [f'input[placeholder*="{field_description}"]', f'input[name*="{field_description}"]']
    
    for sel in selectors:
        try:
            page.fill(sel, value)
            return True
        except:
            continue
    return False


print("🤖 Autonomous Browser Agent loaded!")
