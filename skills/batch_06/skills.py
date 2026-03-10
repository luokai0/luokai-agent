# 🐉 LUO KAI AGENT — SKILL BATCH 06
# 30 Browser-Powered Skills — Web Automation, Research, Monitoring, Domination

from core.router import ask
from core.browser import (
    get_page_content, screenshot, scrape_links,
    scrape_table, google_search_scraper,
    web_researcher, multi_page_scraper,
    monitor_page_changes
)
from core.search import search, search_news
from core.files import write_file
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# 🔍 RESEARCH SKILLS 1-6
def deep_competitor_spy(competitor_url):
    """Skill 1: Spy on any competitor website"""
    content = get_page_content(competitor_url)
    links = scrape_links(competitor_url)
    prompt = f"Analyze this competitor website deeply:\nContent:\n{content[:2000]}\nLinks:\n{links[:1000]}\nReveal: business model, pricing, products, strategy, weaknesses, how to beat them."
    result = ask(prompt)
    write_file(f"competitor_spy_{timestamp()}.txt", result)
    return result

def price_tracker(product_url):
    """Skill 2: Track prices on any website"""
    content = get_page_content(product_url)
    prompt = f"Extract all pricing information from this page:\n{content[:3000]}\nList: all prices, plans, tiers, discounts, hidden fees, best value option."
    result = ask(prompt)
    write_file(f"prices_{timestamp()}.txt", result)
    return result

def job_market_researcher(role, location):
    """Skill 3: Research job market live"""
    results = google_search_scraper(f"{role} jobs {location} salary 2026")
    prompt = f"Analyze the job market for {role} in {location}:\n{results}\nInclude: demand level, salary ranges, required skills, top employers, market trend, negotiation leverage."
    result = ask(prompt)
    write_file(f"jobs_{timestamp()}.txt", result)
    return result

def news_aggregator(topics):
    """Skill 4: Aggregate news from multiple sources"""
    all_news = ""
    for topic in topics.split(","):
        results = google_search_scraper(f"{topic.strip()} news today")
        all_news += f"\n\n## {topic.upper()}\n{results}"
    prompt = f"Synthesize this news into a master briefing:\n{all_news}\nInclude: key events, patterns, opportunities, threats, action items for Luo Kai."
    result = ask(prompt)
    write_file(f"news_brief_{timestamp()}.txt", result)
    return result

def trend_spotter(industry):
    """Skill 5: Spot trends from live web data"""
    google = google_search_scraper(f"{industry} trends emerging 2026")
    research = web_researcher(f"{industry} future trends")
    prompt = f"Spot emerging trends in {industry}:\nGoogle:\n{google}\nResearch:\n{research}\nRank trends by: speed of growth, profit potential, entry barrier, time to act."
    result = ask(prompt)
    write_file(f"trends_{timestamp()}.txt", result)
    return result

def patent_watcher(technology):
    """Skill 6: Watch patent filings"""
    results = google_search_scraper(f"{technology} patent filing 2026 new")
    prompt = f"Analyze patent activity for {technology}:\n{results}\nInclude: who is filing, what innovations, white spaces, investment signals, competitive intelligence."
    result = ask(prompt)
    write_file(f"patents_{timestamp()}.txt", result)
    return result

# 💰 MONEY RESEARCH SKILLS 7-12
def product_researcher(niche):
    """Skill 7: Research winning products live"""
    amazon = google_search_scraper(f"{niche} bestseller Amazon 2026")
    etsy = google_search_scraper(f"{niche} bestseller Etsy 2026")
    prompt = f"Find winning products in {niche}:\nAmazon:\n{amazon}\nEtsy:\n{etsy}\nList top 10 with: demand signals, competition level, profit margin estimate, sourcing angle."
    result = ask(prompt)
    write_file(f"products_{timestamp()}.txt", result)
    return result

def grant_finder(organization_type, country):
    """Skill 8: Find grants and free money"""
    results = google_search_scraper(f"grants funding {organization_type} {country} 2026 apply")
    prompt = f"Find available grants for {organization_type} in {country}:\n{results}\nList each with: amount, eligibility, deadline, application link, success tips."
    result = ask(prompt)
    write_file(f"grants_{timestamp()}.txt", result)
    return result

def scholarship_hunter(profile):
    """Skill 9: Hunt scholarships"""
    results = google_search_scraper(f"scholarships {profile} 2026 apply")
    prompt = f"Find scholarships for profile: {profile}:\n{results}\nList each with: amount, requirements, deadline, application tips, success rate."
    result = ask(prompt)
    write_file(f"scholarships_{timestamp()}.txt", result)
    return result

def crowdfunding_researcher(project_type):
    """Skill 10: Research crowdfunding opportunities"""
    kickstarter = google_search_scraper(f"{project_type} Kickstarter success stories 2026")
    indiegogo = google_search_scraper(f"{project_type} Indiegogo funded 2026")
    prompt = f"Research crowdfunding for {project_type}:\nKickstarter:\n{kickstarter}\nIndiegogo:\n{indiegogo}\nInclude: success patterns, optimal funding goals, reward tiers, marketing tactics, realistic projections."
    result = ask(prompt)
    write_file(f"crowdfunding_{timestamp()}.txt", result)
    return result

def freelance_rate_researcher(skill, market):
    """Skill 11: Research real freelance rates"""
    upwork = google_search_scraper(f"{skill} freelance rate Upwork {market} 2026")
    fiverr = google_search_scraper(f"{skill} Fiverr pricing 2026")
    prompt = f"Research real freelance rates for {skill} in {market}:\nUpwork:\n{upwork}\nFiverr:\n{fiverr}\nInclude: beginner/mid/expert rates, positioning strategy, how to charge premium."
    result = ask(prompt)
    write_file(f"rates_{timestamp()}.txt", result)
    return result

def investment_opportunity_scanner(sector):
    """Skill 12: Scan for live investment opportunities"""
    news = google_search_scraper(f"{sector} investment opportunity undervalued 2026")
    research = web_researcher(f"{sector} investment thesis 2026")
    prompt = f"Scan investment opportunities in {sector}:\nNews:\n{news}\nResearch:\n{research}\nFind: undervalued assets, timing signals, entry points, risk/reward, position sizing."
    result = ask(prompt)
    write_file(f"invest_scan_{timestamp()}.txt", result)
    return result

# 🤖 AUTOMATION SKILLS 13-18
def social_media_monitor(brand, competitors):
    """Skill 13: Monitor social media mentions"""
    brand_results = google_search_scraper(f"{brand} social media mentions reviews 2026")
    comp_results = google_search_scraper(f"{competitors} social media sentiment 2026")
    prompt = f"Monitor social media for brand: {brand} vs {competitors}:\nBrand:\n{brand_results}\nCompetitors:\n{comp_results}\nInclude: sentiment analysis, trending topics, reputation risks, opportunities."
    result = ask(prompt)
    write_file(f"social_monitor_{timestamp()}.txt", result)
    return result

def content_aggregator(topic, sources_count):
    """Skill 14: Aggregate content from web"""
    queries = [
        f"{topic} latest news",
        f"{topic} expert opinion",
        f"{topic} case studies",
        f"{topic} statistics data"
    ]
    all_content = ""
    for q in queries[:int(sources_count)]:
        results = google_search_scraper(q, num_results=3)
        all_content += f"\n\n## {q.upper()}\n{results}"
    prompt = f"Aggregate and synthesize content about {topic}:\n{all_content}\nCreate: comprehensive overview, key insights, actionable takeaways, content ideas."
    result = ask(prompt)
    write_file(f"aggregated_{timestamp()}.txt", result)
    return result

def website_analyzer(url):
    """Skill 15: Full website analysis"""
    content = get_page_content(url)
    links = scrape_links(url)
    screenshot(url)
    prompt = f"Analyze this website completely:\nContent:\n{content[:2000]}\nLinks:\n{links[:500]}\nInclude: purpose, target audience, business model, UX quality, SEO signals, improvement opportunities, monetization potential."
    result = ask(prompt)
    write_file(f"site_analysis_{timestamp()}.txt", result)
    return result

def api_discovery(company):
    """Skill 16: Discover available APIs"""
    results = google_search_scraper(f"{company} API documentation developer 2026")
    prompt = f"Discover and analyze APIs for {company}:\n{results}\nInclude: available APIs, use cases, pricing, rate limits, best opportunities to build with, integration ideas."
    result = ask(prompt)
    write_file(f"apis_{timestamp()}.txt", result)
    return result

def lead_generator(niche, location):
    """Skill 17: Generate business leads"""
    results = google_search_scraper(f"{niche} businesses {location} contact")
    prompt = f"Generate leads for {niche} in {location}:\n{results}\nExtract: business names, contact signals, decision makers, pain points, outreach angles, priority ranking."
    result = ask(prompt)
    write_file(f"leads_{timestamp()}.txt", result)
    return result

def review_analyzer(product_or_business):
    """Skill 18: Analyze reviews for insights"""
    reviews = google_search_scraper(f"{product_or_business} reviews complaints praise 2026")
    prompt = f"Analyze reviews for {product_or_business}:\n{reviews}\nExtract: common complaints, praised features, emotional triggers, improvement opportunities, competitor weaknesses, marketing angles."
    result = ask(prompt)
    write_file(f"reviews_{timestamp()}.txt", result)
    return result

# 📊 INTELLIGENCE SKILLS 19-24
def dark_web_monitor(keywords):
    """Skill 19: Monitor surface web for dark signals"""
    results = google_search_scraper(f"{keywords} leaked exposed breach warning 2026")
    prompt = f"Monitor for dark signals related to: {keywords}:\n{results}\nIdentify: risks, threats, exposed information, early warning signs, protective actions needed."
    result = ask(prompt)
    write_file(f"dark_signals_{timestamp()}.txt", result)
    return result

def regulatory_tracker(industry, jurisdiction):
    """Skill 20: Track regulatory changes"""
    results = google_search_scraper(f"{industry} regulation law change {jurisdiction} 2026")
    prompt = f"Track regulatory changes for {industry} in {jurisdiction}:\n{results}\nInclude: new regulations, pending changes, compliance requirements, business impact, opportunities created."
    result = ask(prompt)
    write_file(f"regulatory_{timestamp()}.txt", result)
    return result

def influencer_researcher(niche):
    """Skill 21: Research influencers"""
    results = google_search_scraper(f"top influencers {niche} 2026 audience size")
    prompt = f"Research influencers in {niche}:\n{results}\nList top 20 with: platform, audience size, engagement rate, content style, collaboration rates, contact approach."
    result = ask(prompt)
    write_file(f"influencers_{timestamp()}.txt", result)
    return result

def viral_content_analyzer(niche):
    """Skill 22: Analyze what goes viral"""
    results = google_search_scraper(f"{niche} viral content most shared 2026")
    prompt = f"Analyze viral content patterns in {niche}:\n{results}\nExtract: viral triggers, emotional hooks, format patterns, timing factors, replication formula for Luo Kai."
    result = ask(prompt)
    write_file(f"viral_{timestamp()}.txt", result)
    return result

def salary_negotiator(role, location, experience):
    """Skill 23: Research salary for negotiation"""
    results = google_search_scraper(f"{role} salary {location} {experience} years 2026")
    prompt = f"Research salary data for {role} in {location} with {experience} experience:\n{results}\nInclude: salary ranges, negotiation tactics, total comp breakdown, competing offers strategy, exact scripts to use."
    result = ask(prompt)
    write_file(f"salary_{timestamp()}.txt", result)
    return result

def technology_radar(domain):
    """Skill 24: Technology radar scan"""
    emerging = google_search_scraper(f"{domain} emerging technology 2026 2027")
    dying = google_search_scraper(f"{domain} dying technology replaced 2026")
    prompt = f"Create technology radar for {domain}:\nEmerging:\n{emerging}\nDying:\n{dying}\nCategorize: adopt now, trial, assess, hold, avoid. Investment and career implications."
    result = ask(prompt)
    write_file(f"tech_radar_{timestamp()}.txt", result)
    return result

# 🐉 ULTIMATE BROWSER SKILLS 25-30
def market_intelligence_report(market):
    """Skill 25: Full market intelligence"""
    news = google_search_scraper(f"{market} market news 2026")
    players = google_search_scraper(f"{market} top companies market share")
    trends = web_researcher(f"{market} market analysis future")
    prompt = f"Create full market intelligence report for {market}:\nNews:\n{news}\nPlayers:\n{players}\nAnalysis:\n{trends}\nInclude: market size, growth rate, key players, disruptions, entry points, profit zones."
    result = ask(prompt)
    write_file(f"market_intel_{timestamp()}.txt", result)
    return result

def opportunity_scanner(keywords):
    """Skill 26: Scan for opportunities everywhere"""
    results = []
    for kw in keywords.split(","):
        r = google_search_scraper(f"{kw.strip()} opportunity 2026")
        results.append(f"## {kw.upper()}\n{r}")
    all_results = "\n\n".join(results)
    prompt = f"Scan all these results for hidden opportunities:\n{all_results}\nRank top 10 opportunities by: profit potential, speed to revenue, resource requirement, competition level."
    result = ask(prompt)
    write_file(f"opportunities_{timestamp()}.txt", result)
    return result

def web_arbitrage_finder(product_category):
    """Skill 27: Find web arbitrage opportunities"""
    buy_low = google_search_scraper(f"{product_category} wholesale cheap price")
    sell_high = google_search_scraper(f"{product_category} retail price Amazon eBay")
    prompt = f"Find arbitrage opportunities for {product_category}:\nBuy low:\n{buy_low}\nSell high:\n{sell_high}\nCalculate: profit margins, volume potential, sourcing strategy, risk factors."
    result = ask(prompt)
    write_file(f"web_arb_{timestamp()}.txt", result)
    return result

def crisis_detector(company_or_brand):
    """Skill 28: Detect brewing crises early"""
    signals = google_search_scraper(f"{company_or_brand} problems issues complaints 2026")
    news = google_search_scraper(f"{company_or_brand} negative news warning")
    prompt = f"Detect crisis signals for {company_or_brand}:\nSignals:\n{signals}\nNews:\n{news}\nAssess: crisis probability, severity, timeline, short opportunity, protective actions."
    result = ask(prompt)
    write_file(f"crisis_detect_{timestamp()}.txt", result)
    return result

def power_network_mapper(industry):
    """Skill 29: Map power networks"""
    results = google_search_scraper(f"{industry} most powerful influential people connections 2026")
    prompt = f"Map the power network in {industry}:\n{results}\nIdentify: key nodes, power brokers, hidden influencers, relationship clusters, how to infiltrate, who to connect with first."
    result = ask(prompt)
    write_file(f"power_map_{timestamp()}.txt", result)
    return result

def ultimate_web_agent(mission):
    """Skill 30: Full autonomous web mission"""
    print(f"🐉 Executing web mission: {mission}")
    search_results = google_search_scraper(mission)
    research = web_researcher(mission)
    news = google_search_scraper(f"{mission} latest news 2026")
    prompt = f"Execute this mission using all web data:\nMISSION: {mission}\nSearch:\n{search_results}\nResearch:\n{research}\nNews:\n{news}\nDeliver: complete mission report with findings, analysis, recommendations, and action plan for Luo Kai."
    result = ask(prompt)
    write_file(f"mission_{timestamp()}.txt", result)
    print(f"✅ Mission complete")
    return result

SKILLS = {
    "deep_competitor_spy": deep_competitor_spy,
    "price_tracker": price_tracker,
    "job_market_researcher": job_market_researcher,
    "news_aggregator": news_aggregator,
    "trend_spotter": trend_spotter,
    "patent_watcher": patent_watcher,
    "product_researcher": product_researcher,
    "grant_finder": grant_finder,
    "scholarship_hunter": scholarship_hunter,
    "crowdfunding_researcher": crowdfunding_researcher,
    "freelance_rate_researcher": freelance_rate_researcher,
    "investment_opportunity_scanner": investment_opportunity_scanner,
    "social_media_monitor": social_media_monitor,
    "content_aggregator": content_aggregator,
    "website_analyzer": website_analyzer,
    "api_discovery": api_discovery,
    "lead_generator": lead_generator,
    "review_analyzer": review_analyzer,
    "dark_web_monitor": dark_web_monitor,
    "regulatory_tracker": regulatory_tracker,
    "influencer_researcher": influencer_researcher,
    "viral_content_analyzer": viral_content_analyzer,
    "salary_negotiator": salary_negotiator,
    "technology_radar": technology_radar,
    "market_intelligence_report": market_intelligence_report,
    "opportunity_scanner": opportunity_scanner,
    "web_arbitrage_finder": web_arbitrage_finder,
    "crisis_detector": crisis_detector,
    "power_network_mapper": power_network_mapper,
    "ultimate_web_agent": ultimate_web_agent,
}

print(f"✅ Batch 06 loaded — {len(SKILLS)} browser skills ready!")
