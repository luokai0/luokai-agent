# 🐉 LUO KAI AGENT — SKILL BATCH 01
# 30 Money-Making Skills

from core.search import search, search_news
from core.files import write_file
from core.router import ask
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# 💰 MONEY SKILLS 1-5: CONTENT CREATION
def write_blog_post(topic):
    """Skill 1: Write a full SEO blog post"""
    research = search(f"{topic} latest trends 2026")
    prompt = f"Write a full professional SEO blog post about: {topic}\n\nResearch:\n{research}\n\nInclude: title, intro, 5 sections, conclusion. Make it engaging and valuable."
    result = ask(prompt)
    write_file(f"blog_{timestamp()}.md", result)
    return result

def write_social_media_pack(topic):
    """Skill 2: Create 10 social media posts at once"""
    prompt = f"Create 10 different social media posts about: {topic}\nInclude: 3 Twitter/X posts, 3 Instagram captions, 2 LinkedIn posts, 2 Facebook posts. Make each unique and engaging."
    result = ask(prompt)
    write_file(f"social_pack_{timestamp()}.txt", result)
    return result

def write_email_sequence(product, audience):
    """Skill 3: Write a 5-email marketing sequence"""
    prompt = f"Write a 5-email marketing sequence for: {product}\nTarget audience: {audience}\nEmails: Welcome, Value, Story, Offer, Follow-up. Make them persuasive and personal."
    result = ask(prompt)
    write_file(f"email_sequence_{timestamp()}.txt", result)
    return result

def write_youtube_script(topic):
    """Skill 4: Write a full YouTube video script"""
    research = search(f"{topic} tips guide 2026")
    prompt = f"Write a full YouTube video script about: {topic}\nResearch:\n{research}\nInclude: hook, intro, 5 main points, call to action. Make it conversational and engaging."
    result = ask(prompt)
    write_file(f"youtube_script_{timestamp()}.txt", result)
    return result

def write_ad_copy(product, platform):
    """Skill 5: Write ad copy for any platform"""
    prompt = f"Write high-converting ad copy for: {product}\nPlatform: {platform}\nCreate 3 variations: short, medium, long. Include headline, body, call to action."
    result = ask(prompt)
    write_file(f"ad_copy_{timestamp()}.txt", result)
    return result

# 🔍 RESEARCH SKILLS 6-10
def market_research(niche):
    """Skill 6: Full market research report"""
    news = search_news(f"{niche} market trends 2026")
    data = search(f"{niche} market size competitors opportunities")
    prompt = f"Write a detailed market research report for: {niche}\nNews:\n{news}\nData:\n{data}\nInclude: market size, trends, competitors, opportunities, risks."
    result = ask(prompt)
    write_file(f"market_research_{timestamp()}.txt", result)
    return result

def competitor_analysis(business, competitor):
    """Skill 7: Analyze a competitor"""
    data = search(f"{competitor} business model pricing reviews 2026")
    prompt = f"Analyze competitor: {competitor} for business: {business}\nData:\n{data}\nInclude: strengths, weaknesses, pricing, strategy, how to beat them."
    result = ask(prompt)
    write_file(f"competitor_{timestamp()}.txt", result)
    return result

def trend_finder(industry):
    """Skill 8: Find trending opportunities"""
    trends = search(f"{industry} trends opportunities 2026")
    news = search_news(f"{industry} emerging trends")
    prompt = f"Find the top 10 trending opportunities in: {industry}\nTrends:\n{trends}\nNews:\n{news}\nRank by profit potential and ease of entry."
    result = ask(prompt)
    write_file(f"trends_{timestamp()}.txt", result)
    return result

def keyword_research(topic):
    """Skill 9: SEO keyword research"""
    data = search(f"{topic} keywords SEO search volume")
    prompt = f"Do SEO keyword research for: {topic}\nData:\n{data}\nProvide: 20 keywords, search intent, difficulty, content ideas for each."
    result = ask(prompt)
    write_file(f"keywords_{timestamp()}.txt", result)
    return result

def business_idea_generator(skills, budget):
    """Skill 10: Generate business ideas"""
    trends = search("best online business ideas 2026 low investment")
    prompt = f"Generate 10 business ideas for someone with skills: {skills} and budget: {budget}\nTrends:\n{trends}\nFor each: idea, how to start, income potential, first step."
    result = ask(prompt)
    write_file(f"business_ideas_{timestamp()}.txt", result)
    return result

# 💼 FREELANCE SKILLS 11-15
def write_proposal(service, client_needs):
    """Skill 11: Write a winning freelance proposal"""
    prompt = f"Write a winning freelance proposal for service: {service}\nClient needs: {client_needs}\nInclude: hook, understanding of problem, solution, timeline, price suggestion, CTA."
    result = ask(prompt)
    write_file(f"proposal_{timestamp()}.txt", result)
    return result

def write_fiverr_gig(service):
    """Skill 12: Write a Fiverr gig description"""
    prompt = f"Write an optimized Fiverr gig for: {service}\nInclude: title, description, 3 packages (basic/standard/premium), FAQ, tags. Make it convert."
    result = ask(prompt)
    write_file(f"fiverr_gig_{timestamp()}.txt", result)
    return result

def cold_email(prospect_business, your_service):
    """Skill 13: Write cold outreach emails"""
    prompt = f"Write 3 cold email variations to: {prospect_business}\nOffering: {your_service}\nMake them short, personal, value-focused. Include subject lines."
    result = ask(prompt)
    write_file(f"cold_email_{timestamp()}.txt", result)
    return result

def pricing_strategy(service, market):
    """Skill 14: Create a pricing strategy"""
    data = search(f"{service} freelance rates pricing {market} 2026")
    prompt = f"Create a pricing strategy for: {service} in market: {market}\nData:\n{data}\nInclude: market rates, your positioning, 3 package tiers, upsell opportunities."
    result = ask(prompt)
    write_file(f"pricing_{timestamp()}.txt", result)
    return result

def portfolio_builder(skills, niche):
    """Skill 15: Plan a portfolio"""
    prompt = f"Create a portfolio building plan for skills: {skills} in niche: {niche}\nInclude: 5 portfolio project ideas, how to present each, platforms to list on, how to get first clients."
    result = ask(prompt)
    write_file(f"portfolio_plan_{timestamp()}.txt", result)
    return result

# 📈 MONEY MAKING SKILLS 16-20
def affiliate_research(niche):
    """Skill 16: Find best affiliate programs"""
    data = search(f"best affiliate programs {niche} high commission 2026")
    prompt = f"Find the best affiliate programs for niche: {niche}\nData:\n{data}\nList top 10 with: commission rate, cookie duration, payment method, how to promote."
    result = ask(prompt)
    write_file(f"affiliate_{timestamp()}.txt", result)
    return result

def dropshipping_product_finder(niche):
    """Skill 17: Find winning dropshipping products"""
    trends = search(f"trending dropshipping products {niche} 2026")
    prompt = f"Find 10 winning dropshipping products in: {niche}\nTrends:\n{trends}\nFor each: product, supplier, selling price, profit margin, target audience."
    result = ask(prompt)
    write_file(f"dropshipping_{timestamp()}.txt", result)
    return result

def digital_product_ideas(expertise):
    """Skill 18: Generate digital product ideas"""
    trends = search(f"best selling digital products {expertise} 2026")
    prompt = f"Generate 10 digital product ideas based on expertise: {expertise}\nTrends:\n{trends}\nFor each: product type, target audience, price point, platform to sell on."
    result = ask(prompt)
    write_file(f"digital_products_{timestamp()}.txt", result)
    return result

def passive_income_plan(budget, skills):
    """Skill 19: Create a passive income plan"""
    data = search("best passive income streams 2026 realistic")
    prompt = f"Create a 90-day passive income plan for budget: {budget} and skills: {skills}\nData:\n{data}\nInclude: streams to build, week by week actions, realistic income projections."
    result = ask(prompt)
    write_file(f"passive_income_{timestamp()}.txt", result)
    return result

def side_hustle_guide(time_available, skills):
    """Skill 20: Build a side hustle guide"""
    data = search(f"best side hustles {skills} {time_available} hours per week 2026")
    prompt = f"Create a complete side hustle guide for someone with {time_available} hours/week and skills: {skills}\nData:\n{data}\nInclude: top 5 options, how to start each, income timeline."
    result = ask(prompt)
    write_file(f"side_hustle_{timestamp()}.txt", result)
    return result

# 🧠 AI SKILLS 21-25
def ai_prompt_pack(use_case):
    """Skill 21: Generate a pack of AI prompts to sell"""
    prompt = f"Create a pack of 20 professional AI prompts for: {use_case}\nMake them detailed, reusable, and valuable. Format them ready to sell on PromptBase."
    result = ask(prompt)
    write_file(f"prompt_pack_{timestamp()}.txt", result)
    return result

def ai_tool_review(tool_name):
    """Skill 22: Write an AI tool review"""
    data = search(f"{tool_name} AI tool review features pricing 2026")
    prompt = f"Write a detailed review of AI tool: {tool_name}\nData:\n{data}\nInclude: features, pricing, pros, cons, best use cases, verdict. Make it SEO optimized."
    result = ask(prompt)
    write_file(f"tool_review_{timestamp()}.txt", result)
    return result

def automation_ideas(business_type):
    """Skill 23: Find automation opportunities"""
    prompt = f"Find 10 automation opportunities for: {business_type}\nFor each: what to automate, tool to use, time saved, money saved, how to implement."
    result = ask(prompt)
    write_file(f"automation_{timestamp()}.txt", result)
    return result

def chatgpt_business_plan(idea):
    """Skill 24: Build an AI-powered business plan"""
    research = search(f"{idea} business model market size competition")
    prompt = f"Create a complete AI-powered business plan for: {idea}\nResearch:\n{research}\nInclude: executive summary, market analysis, revenue model, marketing plan, 90-day roadmap."
    result = ask(prompt)
    write_file(f"business_plan_{timestamp()}.txt", result)
    return result

def niche_site_plan(niche):
    """Skill 25: Plan a niche website"""
    keywords = search(f"{niche} blog keywords topics monetization")
    prompt = f"Create a complete niche website plan for: {niche}\nKeywords:\n{keywords}\nInclude: domain name ideas, content plan, monetization strategy, traffic plan, 6-month roadmap."
    result = ask(prompt)
    write_file(f"niche_site_{timestamp()}.txt", result)
    return result

# 🛠️ UTILITY SKILLS 26-30
def summarize_anything(text):
    """Skill 26: Summarize any text"""
    prompt = f"Summarize this in clear bullet points, keep all key information:\n\n{text}"
    return ask(prompt)

def translate_content(text, target_language):
    """Skill 27: Translate content"""
    prompt = f"Translate this to {target_language}, keep the tone and meaning:\n\n{text}"
    result = ask(prompt)
    write_file(f"translated_{timestamp()}.txt", result)
    return result

def rewrite_content(text, style):
    """Skill 28: Rewrite content in any style"""
    prompt = f"Rewrite this content in style: {style}\nKeep the meaning, improve quality:\n\n{text}"
    result = ask(prompt)
    write_file(f"rewritten_{timestamp()}.txt", result)
    return result

def faq_generator(topic, audience):
    """Skill 29: Generate FAQs"""
    data = search(f"{topic} frequently asked questions {audience}")
    prompt = f"Generate 15 FAQs about: {topic} for audience: {audience}\nData:\n{data}\nMake answers detailed, helpful, and SEO optimized."
    result = ask(prompt)
    write_file(f"faq_{timestamp()}.txt", result)
    return result

def product_description(product, platform):
    """Skill 30: Write product descriptions"""
    prompt = f"Write 3 product descriptions for: {product} on platform: {platform}\nMake them: compelling, SEO optimized, conversion focused. Include bullet points and benefits."
    result = ask(prompt)
    write_file(f"product_desc_{timestamp()}.txt", result)
    return result

# Skill registry
SKILLS = {
    "write_blog_post": write_blog_post,
    "write_social_media_pack": write_social_media_pack,
    "write_email_sequence": write_email_sequence,
    "write_youtube_script": write_youtube_script,
    "write_ad_copy": write_ad_copy,
    "market_research": market_research,
    "competitor_analysis": competitor_analysis,
    "trend_finder": trend_finder,
    "keyword_research": keyword_research,
    "business_idea_generator": business_idea_generator,
    "write_proposal": write_proposal,
    "write_fiverr_gig": write_fiverr_gig,
    "cold_email": cold_email,
    "pricing_strategy": pricing_strategy,
    "portfolio_builder": portfolio_builder,
    "affiliate_research": affiliate_research,
    "dropshipping_product_finder": dropshipping_product_finder,
    "digital_product_ideas": digital_product_ideas,
    "passive_income_plan": passive_income_plan,
    "side_hustle_guide": side_hustle_guide,
    "ai_prompt_pack": ai_prompt_pack,
    "ai_tool_review": ai_tool_review,
    "automation_ideas": automation_ideas,
    "chatgpt_business_plan": chatgpt_business_plan,
    "niche_site_plan": niche_site_plan,
    "summarize_anything": summarize_anything,
    "translate_content": translate_content,
    "rewrite_content": rewrite_content,
    "faq_generator": faq_generator,
    "product_description": product_description,
}

print(f"✅ Batch 01 loaded — {len(SKILLS)} skills ready!")
