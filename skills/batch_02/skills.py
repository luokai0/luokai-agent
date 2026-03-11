from core.router import ask
from core.search import search, search_news
from core.files import write_file
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def crypto_analysis(coin):
    data = search(f"{coin} price analysis prediction 2026")
    result = ask(f"Deep crypto analysis of {coin}:\n{data}\nInclude: trend, sentiment, buy/sell signals, risk, outlook.")
    write_file(f"crypto_{timestamp()}.txt", result)
    return result

def stock_research(ticker):
    data = search(f"{ticker} stock analysis 2026")
    result = ask(f"Research stock {ticker}:\n{data}\nInclude: fundamentals, technicals, risks, opportunity.")
    write_file(f"stock_{timestamp()}.txt", result)
    return result

def investment_strategy(capital, risk_level, goals):
    data = search(f"best investment strategy {risk_level} risk 2026")
    result = ask(f"Build investment strategy:\nCapital:{capital}\nRisk:{risk_level}\nGoals:{goals}\nData:\n{data}")
    write_file(f"investment_{timestamp()}.txt", result)
    return result

def forex_analysis(pair):
    data = search(f"{pair} forex analysis 2026")
    result = ask(f"Analyze forex {pair}:\n{data}\nInclude: trend, key levels, entry/exit, risk/reward.")
    write_file(f"forex_{timestamp()}.txt", result)
    return result

def defi_opportunities():
    data = search("best DeFi yield farming 2026")
    result = ask(f"Find best DeFi opportunities:\n{data}\nTop 10 with APY, risk, how to enter.")
    write_file(f"defi_{timestamp()}.txt", result)
    return result

def financial_plan(income, expenses, goals):
    result = ask(f"Complete financial plan:\nIncome:{income}\nExpenses:{expenses}\nGoals:{goals}\nInclude: budget, savings, investments, milestones.")
    write_file(f"financial_{timestamp()}.txt", result)
    return result

def scientific_research(topic):
    data = search(f"{topic} latest research 2026")
    result = ask(f"Deep scientific research on {topic}:\n{data}\nInclude: findings, studies, applications.")
    write_file(f"science_{timestamp()}.txt", result)
    return result

def legal_research(topic, jurisdiction):
    data = search(f"{topic} law {jurisdiction} 2026")
    result = ask(f"Legal research: {topic} in {jurisdiction}:\n{data}\nNot legal advice.")
    write_file(f"legal_{timestamp()}.txt", result)
    return result

def patent_research(invention):
    data = search(f"{invention} patents landscape")
    result = ask(f"Patent landscape for {invention}:\n{data}\nInclude: existing patents, white spaces, strategy.")
    write_file(f"patent_{timestamp()}.txt", result)
    return result

def academic_paper_summary(topic):
    data = search(f"{topic} academic research 2026")
    result = ask(f"Summarize academic research on {topic}:\n{data}\nKey findings, consensus, takeaways.")
    write_file(f"academic_{timestamp()}.txt", result)
    return result

def industry_report(industry):
    data = search(f"{industry} industry report 2026")
    result = ask(f"Industry report for {industry}:\n{data}\nMarket size, players, trends, opportunities.")
    write_file(f"industry_{timestamp()}.txt", result)
    return result

def due_diligence(company):
    data = search(f"{company} financials reviews 2026")
    result = ask(f"Due diligence on {company}:\n{data}\nFinancial health, reputation, risks, verdict.")
    write_file(f"due_diligence_{timestamp()}.txt", result)
    return result

def code_generator(description, language):
    result = ask(f"Write production {language} code for: {description}\nInclude error handling, comments.")
    write_file(f"code_{timestamp()}.txt", result)
    return result

def code_reviewer(code):
    result = ask(f"Review this code as senior engineer:\n{code}\nBugs, security, performance, improved version.")
    write_file(f"review_{timestamp()}.txt", result)
    return result

def api_builder(service_description):
    result = ask(f"Design REST API for: {service_description}\nEndpoints, schemas, auth, Python implementation.")
    write_file(f"api_{timestamp()}.txt", result)
    return result

def database_designer(app_description):
    result = ask(f"Design database for: {app_description}\nTables, relationships, SQL, optimization.")
    write_file(f"db_{timestamp()}.txt", result)
    return result

def bug_fixer(code, error):
    result = ask(f"Fix bug:\nCode:\n{code}\nError:\n{error}\nRoot cause, fix, prevention.")
    write_file(f"bugfix_{timestamp()}.txt", result)
    return result

def automation_script(task_description):
    result = ask(f"Write Python automation for: {task_description}\nComplete code, scheduling, error handling.")
    write_file(f"automation_{timestamp()}.py", result)
    return result

def seo_audit(website):
    data = search(f"{website} SEO analysis")
    result = ask(f"SEO audit for {website}:\n{data}\nTechnical issues, keywords, backlinks, action plan.")
    write_file(f"seo_{timestamp()}.txt", result)
    return result

def content_strategy(niche, audience):
    result = ask(f"Content strategy for {niche}, audience {audience}\nPillars, calendar, formats, monetization.")
    write_file(f"content_{timestamp()}.txt", result)
    return result

def viral_hook_generator(topic):
    result = ask(f"20 viral hooks for {topic}\nTwitter, YouTube, Instagram, LinkedIn. Make irresistible.")
    write_file(f"hooks_{timestamp()}.txt", result)
    return result

def brand_builder(business_name, niche):
    result = ask(f"Brand identity for {business_name} in {niche}\nStory, values, voice, tagline, positioning.")
    write_file(f"brand_{timestamp()}.txt", result)
    return result

def funnel_builder(product, audience):
    result = ask(f"Sales funnel for {product}, audience {audience}\nAwareness, interest, decision, action stages.")
    write_file(f"funnel_{timestamp()}.txt", result)
    return result

def growth_hacking(startup, stage):
    data = search(f"growth hacking {stage} startup 2026")
    result = ask(f"Growth hacking for {startup} at {stage}:\n{data}\nQuick wins, viral loops, 90 day plan.")
    write_file(f"growth_{timestamp()}.txt", result)
    return result

def strategic_thinking(problem):
    result = ask(f"Strategic analysis of: {problem}\nFirst principles, second order thinking, game theory, optimal strategy.")
    write_file(f"strategy_{timestamp()}.txt", result)
    return result

def future_forecasting(topic):
    data = search(f"{topic} future trends 2026 2030")
    result = ask(f"Forecast future of {topic}:\n{data}\n1/3/5/10 year predictions, opportunities.")
    write_file(f"forecast_{timestamp()}.txt", result)
    return result

def negotiation_playbook(deal, parties):
    result = ask(f"Negotiation playbook for {deal} between {parties}\nBATNA, concessions, tactics, closing.")
    write_file(f"negotiation_{timestamp()}.txt", result)
    return result

def decision_framework(decision, options):
    result = ask(f"Decision framework for: {decision}\nOptions: {options}\nMatrix, risk, expected value, recommendation.")
    write_file(f"decision_{timestamp()}.txt", result)
    return result

def mental_models(problem):
    result = ask(f"Apply mental models to: {problem}\nOccam's Razor, Pareto, compounding, network effects. Actionable insights.")
    write_file(f"mental_{timestamp()}.txt", result)
    return result

def master_plan(goal, timeframe, resources):
    data = search(f"how to achieve {goal} 2026")
    result = ask(f"Master plan for {goal}:\nTimeframe:{timeframe}\nResources:{resources}\nMilestones, actions, obstacles, metrics.")
    write_file(f"masterplan_{timestamp()}.txt", result)
    return result

SKILLS = {
    "crypto_analysis": crypto_analysis,
    "stock_research": stock_research,
    "investment_strategy": investment_strategy,
    "forex_analysis": forex_analysis,
    "defi_opportunities": defi_opportunities,
    "financial_plan": financial_plan,
    "scientific_research": scientific_research,
    "legal_research": legal_research,
    "patent_research": patent_research,
    "academic_paper_summary": academic_paper_summary,
    "industry_report": industry_report,
    "due_diligence": due_diligence,
    "code_generator": code_generator,
    "code_reviewer": code_reviewer,
    "api_builder": api_builder,
    "database_designer": database_designer,
    "bug_fixer": bug_fixer,
    "automation_script": automation_script,
    "seo_audit": seo_audit,
    "content_strategy": content_strategy,
    "viral_hook_generator": viral_hook_generator,
    "brand_builder": brand_builder,
    "funnel_builder": funnel_builder,
    "growth_hacking": growth_hacking,
    "strategic_thinking": strategic_thinking,
    "future_forecasting": future_forecasting,
    "negotiation_playbook": negotiation_playbook,
    "decision_framework": decision_framework,
    "mental_models": mental_models,
    "master_plan": master_plan,
}

print(f"✅ Batch 02 loaded — {len(SKILLS)} skills ready!")
