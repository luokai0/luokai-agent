# 🐉 LUO KAI MONEY ENGINE — REAL MONEY MAKER
from core.router import ask
from core.search import search
from core.email_sender import send_email
from core.files import write_file
from datetime import datetime

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def find_affiliate_programs(niche):
    """Find real affiliate programs in any niche"""
    print(f"🔍 Finding affiliate programs for: {niche}")
    data = search(f"best affiliate programs {niche} 2026 high commission")
    result = ask(f"""Find the best affiliate programs for {niche}.
Research: {data}

For each program give:
- Program name
- Commission rate
- Cookie duration  
- Signup URL
- How to get approved
- Average earning potential

Find at least 10 programs. Focus on HIGH paying ones ($50+ per sale).
Be specific with real program names and real URLs.""")
    
    filename = f"affiliates_{niche}_{timestamp()}.txt"
    write_file(filename, result)
    print(f"💾 Saved: workspace/{filename}")
    return result

def write_seo_article(keyword, word_count=1500):
    """Write a full SEO-optimized article"""
    print(f"✍️ Writing SEO article: {keyword}")
    data = search(f"{keyword} 2026")
    
    result = ask(f"""Write a complete {word_count} word SEO article about: {keyword}

Research data: {data}

Requirements:
- Catchy H1 title
- Meta description (150 chars)
- Introduction with hook
- 5-7 H2 sections with real content
- Include statistics and facts
- Natural keyword usage
- Call to action at end
- Ready to publish on a blog

Make it genuinely useful and high quality.""")
    
    filename = f"article_{keyword[:30].replace(' ','_')}_{timestamp()}.txt"
    write_file(filename, result)
    print(f"💾 Saved: workspace/{filename}")
    return result

def write_cold_email(service, target_industry, your_offer):
    """Write a cold email that actually gets responses"""
    result = ask(f"""Write 3 variations of a cold email:
Service offering: {service}
Target industry: {target_industry}  
Value proposition: {your_offer}

Each email should:
- Subject line that gets opened (not salesy)
- 3-4 sentences max
- One clear call to action
- Feel personal not automated
- Focus on THEIR pain point not your features

Label them: Version A (direct), Version B (curiosity), Version C (social proof)""")
    
    filename = f"cold_email_{timestamp()}.txt"
    write_file(filename, result)
    print(f"💾 Saved: workspace/{filename}")
    return result

def find_freelance_jobs(skill):
    """Find real freelance job opportunities right now"""
    print(f"🔍 Finding freelance jobs for: {skill}")
    data = search(f"{skill} freelance jobs remote 2026 site:reddit.com OR site:news.ycombinator.com OR site:linkedin.com")
    data2 = search(f"hire {skill} freelancer 2026")
    
    result = ask(f"""Find real freelance opportunities for: {skill}

Data: {data}
More data: {data2}

List:
1. Where to find clients (specific platforms, communities, subreddits)
2. What to charge (rates by experience level)
3. How to get first client fast (exact steps)
4. What portfolio pieces to create
5. Top 5 job boards with direct links
6. Cold outreach strategy that works

Be specific and actionable. No fluff.""")
    
    filename = f"freelance_{skill}_{timestamp()}.txt"
    write_file(filename, result)
    print(f"💾 Saved: workspace/{filename}")
    return result

def create_digital_product(topic, product_type="ebook"):
    """Create a sellable digital product"""
    print(f"📦 Creating {product_type}: {topic}")
    
    result = ask(f"""Create a complete {product_type} about: {topic}

Requirements:
- Title that sells
- Table of contents (10+ chapters)
- Full content for each chapter (detailed)
- Real actionable advice
- Make it worth $27-$97
- Include bonuses section
- Add testimonial templates

This should be a complete, publishable product.""")
    
    filename = f"product_{topic[:30].replace(' ','_')}_{timestamp()}.txt"
    write_file(filename, result)
    print(f"💾 Saved: workspace/{filename}")
    return result

def niche_research(niche):
    """Deep research on a money-making niche"""
    print(f"📊 Researching niche: {niche}")
    data = search(f"{niche} market size revenue 2026")
    data2 = search(f"{niche} affiliate programs products to sell")
    data3 = search(f"{niche} blog income report 2026")
    
    result = ask(f"""Deep niche analysis for: {niche}

Data: {data}
Affiliate data: {data2}  
Income data: {data3}

Provide:
1. Market size and growth rate
2. Target audience profile
3. Top 10 products/services to promote
4. Best affiliate programs (with commission rates)
5. Content ideas that rank and convert
6. Monetization strategy (multiple income streams)
7. Realistic income timeline (month 1, 3, 6, 12)
8. Competition analysis
9. Exact action plan to start today

Be brutally honest about difficulty and realistic earnings.""")
    
    filename = f"niche_{niche}_{timestamp()}.txt"
    write_file(filename, result)
    print(f"💾 Saved: workspace/{filename}")
    return result

def send_outreach_campaign(service, targets):
    """Send real cold emails to potential clients"""
    print(f"📧 Starting outreach campaign for: {service}")
    
    emails_sent = 0
    for target in targets:
        email_content = ask(f"""Write a personalized cold email:
Service: {service}
Target: {target}
Keep it under 100 words. Subject line + body only.""")
        
        lines = email_content.strip().split('\n')
        subject = lines[0].replace('Subject:', '').replace('Subject Line:', '').strip()
        body = '\n'.join(lines[1:]).strip()
        
        result = send_email(target if '@' in target else 'creationslous@gmail.com', subject, body)
        if result:
            emails_sent += 1
            print(f"  ✅ Email sent to {target}")
    
    print(f"\n📧 Campaign complete: {emails_sent}/{len(targets)} emails sent!")
    return emails_sent

def daily_money_report():
    """Generate daily money-making action plan"""
    print("💰 Generating daily money report...")
    data = search("best money making opportunities online today 2026")
    
    result = ask(f"""Generate today's money-making action plan.
Date: {datetime.now().strftime('%Y-%m-%d')}
Market data: {data}

Include:
1. TOP opportunity right now (most urgent)
2. 3 tasks to do TODAY that make money
3. One content piece to create
4. One outreach to do
5. One skill to learn this week
6. Expected earnings if executed perfectly

Be specific. No motivational fluff. Just actions and numbers.""")
    
    filename = f"daily_report_{timestamp()}.txt"
    write_file(filename, result)
    send_email('creationslous@gmail.com', f'💰 Daily Money Report {datetime.now().strftime("%Y-%m-%d")}', result)
    print(f"💾 Saved and emailed!")
    return result

print("💰 Money Engine loaded — Real money maker ready!")
