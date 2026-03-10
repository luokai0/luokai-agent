# 🐉 LUO KAI AGENT — SKILL BATCH 03
# 30 Power Skills — Psychology, Automation, eCommerce, Power, Survival

from core.router import ask
from core.search import search, search_news
from core.files import write_file
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# 🧠 PSYCHOLOGY & INFLUENCE SKILLS 1-6
def dark_psychology(situation):
    """Skill 1: Apply dark psychology insights"""
    prompt = f"Analyze this situation using dark psychology principles:\n{situation}\nInclude: manipulation tactics being used, hidden power dynamics, psychological leverage points, how to protect yourself or gain advantage."
    result = ask(prompt)
    write_file(f"dark_psych_{timestamp()}.txt", result)
    return result

def mass_persuasion(message, audience):
    """Skill 2: Mass persuasion strategy"""
    prompt = f"Create a mass persuasion strategy for message: {message}, audience: {audience}\nUse: Cialdini principles, tribal psychology, identity triggers, fear/desire levers, social proof engineering. Make it powerful."
    result = ask(prompt)
    write_file(f"mass_persuasion_{timestamp()}.txt", result)
    return result

def behavior_hacker(target_behavior, person_profile):
    """Skill 3: Change human behavior"""
    prompt = f"Design a behavior change program to make someone: {target_behavior}\nPerson profile: {person_profile}\nUse: BJ Fogg model, habit loops, reward systems, environmental design, social triggers. Step by step plan."
    result = ask(prompt)
    write_file(f"behavior_hack_{timestamp()}.txt", result)
    return result

def reading_people(description):
    """Skill 4: Read people deeply"""
    prompt = f"Deeply analyze this person based on description:\n{description}\nReveal: true motivations, insecurities, desires, how they make decisions, what they respond to, their weak points, how to win them over."
    result = ask(prompt)
    write_file(f"people_read_{timestamp()}.txt", result)
    return result

def cult_of_personality(leader_name, domain):
    """Skill 5: Build a personal brand cult"""
    prompt = f"Build a cult of personality strategy for: {leader_name} in domain: {domain}\nInclude: origin story crafting, belief system, tribe building, enemy creation, rituals, symbols, viral spread tactics."
    result = ask(prompt)
    write_file(f"cult_brand_{timestamp()}.txt", result)
    return result

def social_engineering(goal, target):
    """Skill 6: Social engineering strategy"""
    prompt = f"Design a social engineering approach to achieve: {goal} with target: {target}\nInclude: rapport building, trust establishment, information extraction, influence techniques, execution plan. For educational purposes."
    result = ask(prompt)
    write_file(f"social_eng_{timestamp()}.txt", result)
    return result

# 🤖 AUTOMATION SKILLS 7-12
def workflow_automator(process_description):
    """Skill 7: Automate any business process"""
    prompt = f"Design a complete automation system for: {process_description}\nInclude: tools needed, step by step automation flow, Python code, scheduling, error handling, monitoring, estimated time saved per week."
    result = ask(prompt)
    write_file(f"workflow_{timestamp()}.txt", result)
    return result

def scraper_builder(website, data_needed):
    """Skill 8: Build web scrapers"""
    prompt = f"Write a Python web scraper for: {website} to extract: {data_needed}\nInclude: complete working code using requests/BeautifulSoup, rate limiting, error handling, data saving to CSV, anti-detection measures."
    result = ask(prompt)
    write_file(f"scraper_{timestamp()}.py", result)
    return result

def bot_builder(bot_purpose, platform):
    """Skill 9: Build bots for any platform"""
    prompt = f"Build a {platform} bot for: {bot_purpose}\nInclude: complete Python code, command handling, auto-responses, scheduling, deployment instructions. Make it production ready."
    result = ask(prompt)
    write_file(f"bot_{timestamp()}.py", result)
    return result

def data_pipeline(source, destination, transformation):
    """Skill 10: Build data pipelines"""
    prompt = f"Build a data pipeline from {source} to {destination} with transformation: {transformation}\nInclude: complete Python code, scheduling with cron, error handling, logging, monitoring alerts."
    result = ask(prompt)
    write_file(f"pipeline_{timestamp()}.py", result)
    return result

def ai_workflow(task_description):
    """Skill 11: Build AI-powered workflows"""
    prompt = f"Design an AI-powered workflow for: {task_description}\nInclude: which AI tools to use, how to chain them, Python orchestration code, input/output handling, cost optimization, deployment guide."
    result = ask(prompt)
    write_file(f"ai_workflow_{timestamp()}.txt", result)
    return result

def saas_builder(idea):
    """Skill 12: Plan and build a SaaS"""
    data = search(f"{idea} SaaS competitors pricing market 2026")
    prompt = f"Create a complete SaaS build plan for: {idea}\nData:\n{data}\nInclude: tech stack, MVP features, database design, API design, pricing model, go-to-market, monetization timeline."
    result = ask(prompt)
    write_file(f"saas_plan_{timestamp()}.txt", result)
    return result

# 🛒 ECOMMERCE SKILLS 13-18
def product_hunter(niche):
    """Skill 13: Hunt winning products"""
    data = search(f"winning ecommerce products {niche} high margin 2026")
    prompt = f"Hunt the top 10 winning products in: {niche}\nData:\n{data}\nFor each: product name, supplier source, cost price, sell price, profit margin, target audience, marketing angle, competition level."
    result = ask(prompt)
    write_file(f"product_hunt_{timestamp()}.txt", result)
    return result

def amazon_optimizer(product):
    """Skill 14: Optimize Amazon listings"""
    data = search(f"{product} Amazon listing optimization keywords 2026")
    prompt = f"Optimize Amazon listing for: {product}\nData:\n{data}\nInclude: title formula, bullet points, description, backend keywords, A+ content ideas, review strategy, PPC campaign structure."
    result = ask(prompt)
    write_file(f"amazon_{timestamp()}.txt", result)
    return result

def shopify_store_plan(niche):
    """Skill 15: Plan a Shopify store"""
    data = search(f"Shopify {niche} store success strategies 2026")
    prompt = f"Create a complete Shopify store plan for niche: {niche}\nData:\n{data}\nInclude: store name, product selection, supplier list, theme recommendation, app stack, marketing plan, first 90 days roadmap."
    result = ask(prompt)
    write_file(f"shopify_{timestamp()}.txt", result)
    return result

def print_on_demand(niche):
    """Skill 16: Print on demand business"""
    data = search(f"print on demand {niche} bestselling designs 2026")
    prompt = f"Build a print-on-demand business plan for: {niche}\nData:\n{data}\nInclude: platform selection, design ideas, pricing strategy, marketing on Pinterest/Etsy/TikTok, scaling roadmap."
    result = ask(prompt)
    write_file(f"pod_{timestamp()}.txt", result)
    return result

def etsy_dominator(product_type):
    """Skill 17: Dominate Etsy"""
    data = search(f"{product_type} Etsy bestsellers keywords 2026")
    prompt = f"Create Etsy domination strategy for: {product_type}\nData:\n{data}\nInclude: shop setup, listing optimization, pricing psychology, review building, Etsy SEO, social traffic, scaling to $10k/month."
    result = ask(prompt)
    write_file(f"etsy_{timestamp()}.txt", result)
    return result

def supply_chain_finder(product):
    """Skill 18: Find best suppliers"""
    data = search(f"{product} suppliers manufacturers wholesale Alibaba 2026")
    prompt = f"Find the best suppliers for: {product}\nData:\n{data}\nInclude: top 5 suppliers, pricing comparison, MOQ, quality checks, negotiation script, red flags to avoid, shipping options."
    result = ask(prompt)
    write_file(f"suppliers_{timestamp()}.txt", result)
    return result

# 👑 POWER & STRATEGY SKILLS 19-24
def power_moves(situation, goal):
    """Skill 19: Calculate power moves"""
    prompt = f"Calculate the most powerful moves in this situation:\nSituation: {situation}\nGoal: {goal}\nApply: 48 Laws of Power, Sun Tzu, Machiavelli, Chess thinking. Give top 5 power moves ranked by effectiveness."
    result = ask(prompt)
    write_file(f"power_moves_{timestamp()}.txt", result)
    return result

def war_room(challenge, resources, enemies):
    """Skill 20: War room strategy session"""
    prompt = f"Run a war room strategy session:\nChallenge: {challenge}\nResources: {resources}\nOpponents: {enemies}\nApply military strategy, competitive intelligence, asymmetric warfare tactics. Build winning battle plan."
    result = ask(prompt)
    write_file(f"war_room_{timestamp()}.txt", result)
    return result

def empire_builder(vision, current_position):
    """Skill 21: Build an empire"""
    prompt = f"Create an empire building roadmap:\nVision: {vision}\nCurrent position: {current_position}\nInclude: territory expansion strategy, alliance building, revenue streams, team building, moat creation, legacy planning."
    result = ask(prompt)
    write_file(f"empire_{timestamp()}.txt", result)
    return result

def intelligence_report(target, purpose):
    """Skill 22: Gather intelligence"""
    data = search(f"{target} latest news analysis background")
    prompt = f"Compile an intelligence report on: {target} for purpose: {purpose}\nData:\n{data}\nInclude: background, current activities, strengths, weaknesses, connections, vulnerabilities, strategic assessment."
    result = ask(prompt)
    write_file(f"intel_{timestamp()}.txt", result)
    return result

def leverage_finder(situation):
    """Skill 23: Find hidden leverage"""
    prompt = f"Find all hidden leverage points in this situation:\n{situation}\nIdentify: information leverage, relationship leverage, financial leverage, timing leverage, positional leverage. Rank by power and show how to use each."
    result = ask(prompt)
    write_file(f"leverage_{timestamp()}.txt", result)
    return result

def crisis_manager(crisis):
    """Skill 24: Manage any crisis"""
    prompt = f"Manage this crisis with maximum effectiveness:\n{crisis}\nProvide: immediate actions (first 24hrs), damage control strategy, communication plan, recovery roadmap, how to emerge stronger, lessons to extract."
    result = ask(prompt)
    write_file(f"crisis_{timestamp()}.txt", result)
    return result

# 🌍 GLOBAL & SURVIVAL SKILLS 25-30
def arbitrage_finder(market1, market2):
    """Skill 25: Find arbitrage opportunities"""
    data = search(f"arbitrage opportunities {market1} {market2} 2026")
    prompt = f"Find arbitrage opportunities between {market1} and {market2}:\nData:\n{data}\nInclude: specific opportunities, price gaps, execution strategy, risk management, profit potential, scaling approach."
    result = ask(prompt)
    write_file(f"arbitrage_{timestamp()}.txt", result)
    return result

def offshore_strategy(goal):
    """Skill 26: Offshore and international strategy"""
    data = search(f"offshore strategy {goal} legal tax optimization 2026")
    prompt = f"Create an offshore strategy for: {goal}\nData:\n{data}\nInclude: best jurisdictions, legal structures, tax optimization, banking options, compliance requirements. Note: consult professionals for implementation."
    result = ask(prompt)
    write_file(f"offshore_{timestamp()}.txt", result)
    return result

def network_builder(industry, goal):
    """Skill 27: Build a powerful network"""
    prompt = f"Build a powerful network in {industry} to achieve: {goal}\nInclude: target people to connect with, platforms to use, value-first approach, conversation starters, follow-up system, relationship maintenance, leverage strategy."
    result = ask(prompt)
    write_file(f"network_{timestamp()}.txt", result)
    return result

def media_dominator(message, target_audience):
    """Skill 28: Dominate media narrative"""
    prompt = f"Create a media domination strategy for message: {message}, audience: {target_audience}\nInclude: platform strategy, content calendar, PR tactics, influencer outreach, viral triggers, narrative control, crisis PR plan."
    result = ask(prompt)
    write_file(f"media_{timestamp()}.txt", result)
    return result

def wealth_protector(assets, threats):
    """Skill 29: Protect wealth"""
    data = search(f"wealth protection strategies asset protection legal 2026")
    prompt = f"Create a wealth protection strategy for assets: {assets}, threats: {threats}\nData:\n{data}\nInclude: legal structures, diversification, insurance, digital security, privacy measures, succession planning."
    result = ask(prompt)
    write_file(f"wealth_protect_{timestamp()}.txt", result)
    return result

def legacy_planner(vision, resources):
    """Skill 30: Plan a lasting legacy"""
    prompt = f"Create a legacy plan for vision: {vision} with resources: {resources}\nInclude: impact areas, foundation/organization structure, wealth transfer strategy, brand immortalization, how to be remembered 100 years from now."
    result = ask(prompt)
    write_file(f"legacy_{timestamp()}.txt", result)
    return result

SKILLS = {
    "dark_psychology": dark_psychology,
    "mass_persuasion": mass_persuasion,
    "behavior_hacker": behavior_hacker,
    "reading_people": reading_people,
    "cult_of_personality": cult_of_personality,
    "social_engineering": social_engineering,
    "workflow_automator": workflow_automator,
    "scraper_builder": scraper_builder,
    "bot_builder": bot_builder,
    "data_pipeline": data_pipeline,
    "ai_workflow": ai_workflow,
    "saas_builder": saas_builder,
    "product_hunter": product_hunter,
    "amazon_optimizer": amazon_optimizer,
    "shopify_store_plan": shopify_store_plan,
    "print_on_demand": print_on_demand,
    "etsy_dominator": etsy_dominator,
    "supply_chain_finder": supply_chain_finder,
    "power_moves": power_moves,
    "war_room": war_room,
    "empire_builder": empire_builder,
    "intelligence_report": intelligence_report,
    "leverage_finder": leverage_finder,
    "crisis_manager": crisis_manager,
    "arbitrage_finder": arbitrage_finder,
    "offshore_strategy": offshore_strategy,
    "network_builder": network_builder,
    "media_dominator": media_dominator,
    "wealth_protector": wealth_protector,
    "legacy_planner": legacy_planner,
}

print(f"✅ Batch 03 loaded — {len(SKILLS)} power skills ready!")
