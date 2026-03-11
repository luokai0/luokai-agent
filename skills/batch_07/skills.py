from core.router import ask
from core.search import search
from core.files import write_file
from datetime import datetime

def ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def write_viral_thread(topic):
    data = search(f"{topic} interesting facts 2026")
    result = ask(f"Write a viral 10-tweet thread about {topic}. Data:{data}. Number each tweet under 280 chars.")
    write_file(f"thread_{ts()}.txt", result)
    return result

def youtube_video_script(topic):
    result = ask(f"Write a complete 10 minute YouTube video script about {topic}. Include hook, intro, sections, CTA.")
    write_file(f"yt_script_{ts()}.txt", result)
    return result

def sales_page_writer(product, price, audience):
    result = ask(f"Write a complete sales page for {product} at ${price} for {audience}. Include headline, benefits, CTA, FAQ.")
    write_file(f"sales_page_{ts()}.txt", result)
    return result

def email_sequence_writer(product, audience):
    result = ask(f"Write a 7-email welcome sequence for {product} targeting {audience}. Full subject lines and body for each.")
    write_file(f"email_seq_{ts()}.txt", result)
    return result

def business_model_designer(idea, market):
    result = ask(f"Design complete business model for {idea} targeting {market}. Revenue streams, costs, value proposition.")
    write_file(f"biz_model_{ts()}.txt", result)
    return result

def dropshipping_strategy(niche):
    data = search(f"dropshipping {niche} suppliers 2026")
    result = ask(f"Complete dropshipping strategy for {niche}. Data:{data}. Suppliers, products, ads, scaling.")
    write_file(f"dropship_{ts()}.txt", result)
    return result

def ai_service_business(skill_level):
    result = ask(f"Build AI services business for {skill_level} skill level. Services, pricing, clients, tools, income potential.")
    write_file(f"ai_business_{ts()}.txt", result)
    return result

def tiktok_content_plan(niche):
    result = ask(f"Create 30-day TikTok content plan for {niche}. Daily video ideas, hooks, posting times, growth tactics.")
    write_file(f"tiktok_{ts()}.txt", result)
    return result

def linkedin_profile_optimizer(name, profession):
    result = ask(f"Optimize LinkedIn profile for {name}, {profession}. Headline, about section, skills, connection strategy.")
    write_file(f"linkedin_{ts()}.txt", result)
    return result

def course_creator(topic, audience, price):
    result = ask(f"Create online course: {topic} for {audience} at ${price}. Full outline, lessons, sales strategy.")
    write_file(f"course_{ts()}.txt", result)
    return result

SKILLS = {
    "write_viral_thread": write_viral_thread,
    "youtube_video_script": youtube_video_script,
    "sales_page_writer": sales_page_writer,
    "email_sequence_writer": email_sequence_writer,
    "business_model_designer": business_model_designer,
    "dropshipping_strategy": dropshipping_strategy,
    "ai_service_business": ai_service_business,
    "tiktok_content_plan": tiktok_content_plan,
    "linkedin_profile_optimizer": linkedin_profile_optimizer,
    "course_creator": course_creator,
}
print(f"✅ Batch 07 loaded — {len(SKILLS)} skills ready!")
