from core.router import ask
from core.search import search
from core.files import write_file
from datetime import datetime

def ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def stock_screener(criteria):
    data = search(f"stocks {criteria} 2026")
    result = ask(f"Screen stocks: {criteria}. Data:{data}. Top 10 with ticker, reason, entry, target, stop loss.")
    write_file(f"stocks_{ts()}.txt", result)
    return result

def crypto_trading_strategy(coin, timeframe):
    data = search(f"{coin} price analysis 2026")
    result = ask(f"Trading strategy for {coin} on {timeframe}. Data:{data}. Trend, levels, entry/exit, risk management.")
    write_file(f"crypto_{ts()}.txt", result)
    return result

def build_saas_mvp(idea, stack):
    result = ask(f"Build MVP for SaaS: {idea} using {stack}. Architecture, database, API endpoints, core features, deployment.")
    write_file(f"saas_{ts()}.txt", result)
    return result

def telegram_bot_builder(purpose):
    result = ask(f"Build Telegram bot for: {purpose}. Complete Python code using python-telegram-bot, commands, deployment.")
    write_file(f"tgbot_{ts()}.py", result)
    return result

def competitor_intelligence(company):
    data = search(f"{company} revenue strategy weakness 2026")
    result = ask(f"Deep competitor intelligence on {company}. Data:{data}. Business model, weaknesses, opportunities.")
    write_file(f"intel_{ts()}.txt", result)
    return result

def keyword_researcher(niche, intent):
    data = search(f"{niche} keywords {intent} 2026")
    result = ask(f"Keyword research for {niche}, intent: {intent}. Data:{data}. 50 keywords with volume, competition, angle.")
    write_file(f"keywords_{ts()}.txt", result)
    return result

def sales_call_script(product, objections):
    result = ask(f"Complete sales call script for {product}. Objections: {objections}. Opening, pitch, handlers, closing.")
    write_file(f"sales_call_{ts()}.txt", result)
    return result

def workout_plan_builder(goals, equipment, days):
    result = ask(f"Workout plan for {goals}, equipment: {equipment}, {days} days/week. Exercises, sets, reps, progression.")
    write_file(f"workout_{ts()}.txt", result)
    return result

def tax_strategy(income_type, country):
    data = search(f"tax optimization {income_type} {country} 2026")
    result = ask(f"Tax optimization for {income_type} in {country}. Data:{data}. Legal strategies. Consult a professional.")
    write_file(f"tax_{ts()}.txt", result)
    return result

def trend_spotter(industry):
    data = search(f"{industry} emerging trends 2026 2027")
    result = ask(f"Emerging trends in {industry}. Data:{data}. Top 10 with timing, opportunity size, how to capitalize.")
    write_file(f"trends_{ts()}.txt", result)
    return result

SKILLS = {
    "stock_screener": stock_screener,
    "crypto_trading_strategy": crypto_trading_strategy,
    "build_saas_mvp": build_saas_mvp,
    "telegram_bot_builder": telegram_bot_builder,
    "competitor_intelligence": competitor_intelligence,
    "keyword_researcher": keyword_researcher,
    "sales_call_script": sales_call_script,
    "workout_plan_builder": workout_plan_builder,
    "tax_strategy": tax_strategy,
    "trend_spotter": trend_spotter,
}
print(f"✅ Batch 08 loaded — {len(SKILLS)} skills ready!")
