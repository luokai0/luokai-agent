# 🐉 LUO KAI AGENT — SKILL BATCH 04
# 30 Skills — AI Tools, Health, Education, Real Estate, Geopolitics

from core.router import ask
from core.search import search, search_news
from core.files import write_file
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# 🤖 AI TOOLS & PROMPTING SKILLS 1-6
def prompt_engineer(task, model):
    """Skill 1: Engineer perfect prompts"""
    prompt = f"Engineer the perfect prompt for task: {task} on model: {model}\nInclude: system prompt, user prompt, chain of thought instructions, output format, examples, edge case handling. Make it production grade."
    result = ask(prompt)
    write_file(f"prompt_eng_{timestamp()}.txt", result)
    return result

def ai_agent_designer(purpose):
    """Skill 2: Design AI agent systems"""
    prompt = f"Design a complete AI agent system for: {purpose}\nInclude: agent architecture, tools needed, memory system, reasoning chain, failure modes, evaluation metrics, deployment strategy."
    result = ask(prompt)
    write_file(f"agent_design_{timestamp()}.txt", result)
    return result

def llm_fine_tuner(base_model, use_case, data_description):
    """Skill 3: Plan LLM fine-tuning"""
    prompt = f"Create a fine-tuning plan for {base_model} for use case: {use_case}\nTraining data: {data_description}\nInclude: data preparation, training parameters, evaluation metrics, deployment strategy, cost estimate."
    result = ask(prompt)
    write_file(f"finetune_{timestamp()}.txt", result)
    return result

def ai_product_builder(idea):
    """Skill 4: Build AI products"""
    data = search(f"AI product {idea} market opportunity 2026")
    prompt = f"Build a complete AI product plan for: {idea}\nData:\n{data}\nInclude: core AI features, tech stack, data strategy, monetization, competitive moat, go-to-market, MVP scope."
    result = ask(prompt)
    write_file(f"ai_product_{timestamp()}.txt", result)
    return result

def model_selector(task_requirements):
    """Skill 5: Select best AI model for any task"""
    data = search("best AI models comparison benchmark 2026")
    prompt = f"Select the best AI model for requirements: {task_requirements}\nData:\n{data}\nCompare top models on: accuracy, speed, cost, context window, strengths, weaknesses. Give clear recommendation."
    result = ask(prompt)
    write_file(f"model_select_{timestamp()}.txt", result)
    return result

def ai_monetizer(skills_description):
    """Skill 6: Monetize AI skills"""
    data = search("how to make money with AI skills 2026")
    prompt = f"Create a monetization plan for AI skills: {skills_description}\nData:\n{data}\nInclude: top 10 income streams, platforms, pricing, client acquisition, scaling strategy, income timeline."
    result = ask(prompt)
    write_file(f"ai_monetize_{timestamp()}.txt", result)
    return result

# 💪 HEALTH & PERFORMANCE SKILLS 7-12
def biohacking_protocol(goal, current_state):
    """Skill 7: Design biohacking protocol"""
    data = search(f"biohacking {goal} protocols science backed 2026")
    prompt = f"Design a biohacking protocol for goal: {goal}, current state: {current_state}\nData:\n{data}\nInclude: sleep optimization, nutrition, supplements, exercise, mental performance, tracking metrics, timeline."
    result = ask(prompt)
    write_file(f"biohack_{timestamp()}.txt", result)
    return result

def peak_performance_plan(role, goals):
    """Skill 8: Peak performance system"""
    prompt = f"Build a peak performance system for: {role} with goals: {goals}\nInclude: morning routine, deep work blocks, energy management, recovery protocol, mental training, measurement system."
    result = ask(prompt)
    write_file(f"performance_{timestamp()}.txt", result)
    return result

def nutrition_optimizer(goals, restrictions):
    """Skill 9: Optimize nutrition"""
    data = search(f"optimal nutrition {goals} science 2026")
    prompt = f"Create an optimized nutrition plan for goals: {goals}, restrictions: {restrictions}\nData:\n{data}\nInclude: macros, meal timing, food list, supplements, meal prep strategy, tracking method."
    result = ask(prompt)
    write_file(f"nutrition_{timestamp()}.txt", result)
    return result

def mental_performance(challenges):
    """Skill 10: Mental performance optimization"""
    prompt = f"Create a mental performance optimization plan for challenges: {challenges}\nInclude: focus techniques, stress management, cognitive enhancement, mindset reprogramming, daily practices, measurement."
    result = ask(prompt)
    write_file(f"mental_perf_{timestamp()}.txt", result)
    return result

def longevity_protocol():
    """Skill 11: Longevity and anti-aging"""
    data = search("longevity anti-aging protocols science 2026")
    prompt = f"Create a comprehensive longevity protocol:\nData:\n{data}\nInclude: lifestyle factors, nutrition, exercise, sleep, stress, supplements, medical tests, cutting-edge interventions."
    result = ask(prompt)
    write_file(f"longevity_{timestamp()}.txt", result)
    return result

def stress_destroyer(stress_sources):
    """Skill 12: Eliminate stress completely"""
    prompt = f"Create a complete stress elimination system for: {stress_sources}\nInclude: root cause analysis, immediate relief techniques, long-term solutions, lifestyle redesign, mental reprogramming, support systems."
    result = ask(prompt)
    write_file(f"stress_{timestamp()}.txt", result)
    return result

# 📚 EDUCATION & LEARNING SKILLS 13-18
def speed_learner(subject, timeframe):
    """Skill 13: Learn anything fast"""
    data = search(f"how to learn {subject} fast accelerated learning 2026")
    prompt = f"Create an accelerated learning plan for: {subject} in timeframe: {timeframe}\nData:\n{data}\nInclude: learning path, resources, spaced repetition schedule, projects, milestones, mastery test."
    result = ask(prompt)
    write_file(f"learn_{timestamp()}.txt", result)
    return result

def course_creator(topic, audience):
    """Skill 14: Create online courses"""
    prompt = f"Create a complete online course for topic: {topic}, audience: {audience}\nInclude: course outline, module breakdown, lesson scripts, exercises, quizzes, pricing strategy, platform selection, marketing plan."
    result = ask(prompt)
    write_file(f"course_{timestamp()}.txt", result)
    return result

def book_writer(title, topic, audience):
    """Skill 15: Write a complete book outline"""
    data = search(f"{topic} book bestsellers key ideas 2026")
    prompt = f"Create a complete book plan for: {title}\nTopic: {topic}, Audience: {audience}\nData:\n{data}\nInclude: hook, chapter outline, key arguments, stories to include, research needed, publishing strategy."
    result = ask(prompt)
    write_file(f"book_{timestamp()}.txt", result)
    return result

def knowledge_synthesizer(topics):
    """Skill 16: Synthesize knowledge across domains"""
    prompt = f"Synthesize knowledge across these domains: {topics}\nFind: hidden connections, cross-domain insights, unified principles, novel combinations, breakthrough ideas that emerge from synthesis."
    result = ask(prompt)
    write_file(f"synthesis_{timestamp()}.txt", result)
    return result

def expert_interviewer(expert_domain, goals):
    """Skill 17: Extract knowledge from experts"""
    prompt = f"Design an expert knowledge extraction system for domain: {expert_domain}, goals: {goals}\nInclude: 20 deep questions, follow-up frameworks, knowledge capture system, insight organization method."
    result = ask(prompt)
    write_file(f"interview_{timestamp()}.txt", result)
    return result

def skill_stacker(current_skills, target_goal):
    """Skill 18: Stack skills for maximum value"""
    data = search(f"rare skill combinations high value career 2026")
    prompt = f"Design a skill stacking strategy with current skills: {current_skills} to achieve: {target_goal}\nData:\n{data}\nInclude: skills to add, learning order, combination value, unique positioning, monetization."
    result = ask(prompt)
    write_file(f"skill_stack_{timestamp()}.txt", result)
    return result

# 🏠 REAL ESTATE SKILLS 19-24
def property_analyzer(location, budget):
    """Skill 19: Analyze real estate opportunities"""
    data = search(f"real estate investment {location} market analysis 2026")
    prompt = f"Analyze real estate opportunities in {location} with budget: {budget}\nData:\n{data}\nInclude: market conditions, best neighborhoods, ROI projections, rental yield, appreciation potential, risks."
    result = ask(prompt)
    write_file(f"realestate_{timestamp()}.txt", result)
    return result

def rental_income_calculator(property_details):
    """Skill 20: Calculate rental income potential"""
    prompt = f"Calculate rental income potential for: {property_details}\nInclude: gross rental yield, net yield after expenses, cash flow projection, occupancy assumptions, 5 year income projection, break even analysis."
    result = ask(prompt)
    write_file(f"rental_{timestamp()}.txt", result)
    return result

def house_flipper(market, budget):
    """Skill 21: House flipping strategy"""
    data = search(f"house flipping {market} profit margins strategy 2026")
    prompt = f"Create a house flipping strategy for market: {market}, budget: {budget}\nData:\n{data}\nInclude: property criteria, renovation budget, timeline, contractor management, selling strategy, profit projection."
    result = ask(prompt)
    write_file(f"flip_{timestamp()}.txt", result)
    return result

def airbnb_optimizer(location, property_type):
    """Skill 22: Maximize Airbnb income"""
    data = search(f"Airbnb {location} optimization income strategy 2026")
    prompt = f"Maximize Airbnb income for {property_type} in {location}\nData:\n{data}\nInclude: pricing strategy, listing optimization, guest experience, review building, occupancy tactics, income projection."
    result = ask(prompt)
    write_file(f"airbnb_{timestamp()}.txt", result)
    return result

def real_estate_negotiator(deal_details):
    """Skill 23: Negotiate real estate deals"""
    prompt = f"Create negotiation strategy for real estate deal: {deal_details}\nInclude: opening offer strategy, contingencies to use, seller psychology, inspection leverage, financing leverage, closing tactics, walk-away point."
    result = ask(prompt)
    write_file(f"re_negotiate_{timestamp()}.txt", result)
    return result

def property_portfolio(goals, capital):
    """Skill 24: Build property portfolio"""
    data = search(f"property portfolio building strategy {capital} 2026")
    prompt = f"Build a property portfolio plan for goals: {goals}, capital: {capital}\nData:\n{data}\nInclude: portfolio strategy, property types, financing structure, growth roadmap, risk management, exit strategies."
    result = ask(prompt)
    write_file(f"portfolio_{timestamp()}.txt", result)
    return result

# 🌍 GEOPOLITICS & MACRO SKILLS 25-30
def geopolitical_analysis(region, situation):
    """Skill 25: Geopolitical analysis"""
    data = search(f"{region} geopolitical situation analysis 2026")
    news = search_news(f"{region} geopolitics")
    prompt = f"Analyze geopolitical situation in {region}: {situation}\nData:\n{data}\nNews:\n{news}\nInclude: power dynamics, economic implications, investment impact, risks, opportunities, 12 month outlook."
    result = ask(prompt)
    write_file(f"geopolitics_{timestamp()}.txt", result)
    return result

def macro_economist(economy, indicators):
    """Skill 26: Macro economic analysis"""
    data = search(f"{economy} economy macro indicators outlook 2026")
    prompt = f"Analyze macro economy of {economy} using indicators: {indicators}\nData:\n{data}\nInclude: GDP outlook, inflation, employment, monetary policy, fiscal policy, currency outlook, investment implications."
    result = ask(prompt)
    write_file(f"macro_{timestamp()}.txt", result)
    return result

def sanctions_analyzer(country, sector):
    """Skill 27: Analyze sanctions impact"""
    data = search(f"{country} sanctions {sector} impact 2026")
    prompt = f"Analyze sanctions impact on {country} in sector {sector}:\nData:\n{data}\nInclude: current sanctions, business impact, workarounds, compliance requirements, opportunity gaps created."
    result = ask(prompt)
    write_file(f"sanctions_{timestamp()}.txt", result)
    return result

def emerging_market_finder():
    """Skill 28: Find emerging market opportunities"""
    data = search("emerging markets investment opportunities growth 2026")
    news = search_news("emerging markets opportunities")
    prompt = f"Find the top emerging market opportunities right now:\nData:\n{data}\nNews:\n{news}\nList top 10 countries/sectors with: growth drivers, entry strategies, risks, profit potential."
    result = ask(prompt)
    write_file(f"emerging_{timestamp()}.txt", result)
    return result

def currency_strategist(base_currency, goals):
    """Skill 29: Currency strategy"""
    data = search(f"{base_currency} currency strategy forex outlook 2026")
    prompt = f"Create currency strategy for base: {base_currency}, goals: {goals}\nData:\n{data}\nInclude: currency outlook, hedging strategies, best currencies to hold, timing, tools to use."
    result = ask(prompt)
    write_file(f"currency_{timestamp()}.txt", result)
    return result

def black_swan_preparedness(portfolio, lifestyle):
    """Skill 30: Prepare for black swan events"""
    prompt = f"Create black swan preparedness plan for portfolio: {portfolio}, lifestyle: {lifestyle}\nInclude: tail risks to prepare for, hedging strategies, physical preparations, geographic diversification, digital security, anti-fragility tactics."
    result = ask(prompt)
    write_file(f"blackswan_{timestamp()}.txt", result)
    return result

SKILLS = {
    "prompt_engineer": prompt_engineer,
    "ai_agent_designer": ai_agent_designer,
    "llm_fine_tuner": llm_fine_tuner,
    "ai_product_builder": ai_product_builder,
    "model_selector": model_selector,
    "ai_monetizer": ai_monetizer,
    "biohacking_protocol": biohacking_protocol,
    "peak_performance_plan": peak_performance_plan,
    "nutrition_optimizer": nutrition_optimizer,
    "mental_performance": mental_performance,
    "longevity_protocol": longevity_protocol,
    "stress_destroyer": stress_destroyer,
    "speed_learner": speed_learner,
    "course_creator": course_creator,
    "book_writer": book_writer,
    "knowledge_synthesizer": knowledge_synthesizer,
    "expert_interviewer": expert_interviewer,
    "skill_stacker": skill_stacker,
    "property_analyzer": property_analyzer,
    "rental_income_calculator": rental_income_calculator,
    "house_flipper": house_flipper,
    "airbnb_optimizer": airbnb_optimizer,
    "real_estate_negotiator": real_estate_negotiator,
    "property_portfolio": property_portfolio,
    "geopolitical_analysis": geopolitical_analysis,
    "macro_economist": macro_economist,
    "sanctions_analyzer": sanctions_analyzer,
    "emerging_market_finder": emerging_market_finder,
    "currency_strategist": currency_strategist,
    "black_swan_preparedness": black_swan_preparedness,
}

print(f"✅ Batch 04 loaded — {len(SKILLS)} skills ready!")
