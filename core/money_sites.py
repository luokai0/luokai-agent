# 🐉 LUO KAI AGENT — MONEY SITES AUTO SIGNUP
# Sites with simple signup — no reCAPTCHA or easy to bypass

MONEY_SITES = [
    # FREELANCE / TASKS
    {"name": "picoworkers", "url": "https://picoworkers.com/register", "type": "microtasks", "pays": "$0.01-$5 per task"},
    {"name": "rapidworkers", "url": "https://rapidworkers.com/register", "type": "microtasks", "pays": "$0.01-$3 per task"},
    {"name": "microworkers", "url": "https://microworkers.com/register", "type": "microtasks", "pays": "$0.01-$5 per task"},
    {"name": "clickworker", "url": "https://workplace.clickworker.com/en/register", "type": "data tasks", "pays": "$9-$25/hr"},
    {"name": "appen", "url": "https://connect.appen.com/qrp/public/register", "type": "AI training data", "pays": "$13-$18/hr"},
    
    # WRITING / CONTENT
    {"name": "textbroker", "url": "https://www.textbroker.com/author-registration", "type": "writing", "pays": "$0.007-$0.05/word"},
    {"name": "iwriter", "url": "https://www.iwriter.com/register", "type": "writing", "pays": "$1.50-$15 per article"},
    {"name": "writerbay", "url": "https://www.writerbay.com/apply", "type": "writing", "pays": "$7-$15/page"},
    
    # SURVEY / REWARDS  
    {"name": "swagbucks", "url": "https://www.swagbucks.com/register", "type": "surveys", "pays": "$1-$5/survey"},
    {"name": "timebucks", "url": "https://timebucks.com/register", "type": "surveys+tasks", "pays": "$0.50-$3/survey"},
    {"name": "inboxdollars", "url": "https://www.inboxdollars.com/signup", "type": "surveys", "pays": "$0.50-$5/survey"},
    {"name": "prizerebel", "url": "https://www.prizerebel.com/register.php", "type": "surveys", "pays": "$0.50-$5/survey"},
    
    # AFFILIATE
    {"name": "digistore24", "url": "https://www.digistore24.com/signup", "type": "affiliate", "pays": "30-75% commission"},
    {"name": "jvzoo", "url": "https://www.jvzoo.com/register", "type": "affiliate", "pays": "25-100% commission"},
    {"name": "warriorplus", "url": "https://warriorplus.com/user/register", "type": "affiliate", "pays": "50-100% commission"},
    {"name": "shareasale", "url": "https://www.shareasale.com/newregister.cfm", "type": "affiliate", "pays": "varies"},
    
    # CRYPTO / PASSIVE
    {"name": "cointiply", "url": "https://cointiply.com/register", "type": "crypto faucet", "pays": "small crypto daily"},
    {"name": "freebitco", "url": "https://freebitco.in/register", "type": "crypto faucet", "pays": "small BTC daily"},
    
    # SELLING
    {"name": "redbubble", "url": "https://www.redbubble.com/signup", "type": "print on demand", "pays": "10-30% per sale"},
    {"name": "teepublic", "url": "https://www.teepublic.com/signup", "type": "print on demand", "pays": "$2-$6 per sale"},
    {"name": "gumroad", "url": "https://app.gumroad.com/signup", "type": "digital products", "pays": "90%+ per sale"},
]

def print_money_sites():
    print("\n💰 LUO KAI MONEY SITES — AUTO SIGNUP LIST")
    print("=" * 60)
    types = {}
    for site in MONEY_SITES:
        t = site['type']
        if t not in types:
            types[t] = []
        types[t].append(site)
    
    for type_name, sites in types.items():
        print(f"\n📂 {type_name.upper()}")
        for s in sites:
            print(f"  • {s['name']:<20} {s['pays']}")
    
    print(f"\n✅ Total: {len(MONEY_SITES)} sites ready for auto-signup!")

def signup_all(limit=5):
    """Auto signup to multiple money sites"""
    from core.web_signup import signup_to_site
    print(f"\n🚀 Auto-signing up to {limit} sites...")
    results = []
    for site in MONEY_SITES[:limit]:
        print(f"\n{'='*40}")
        try:
            profile = signup_to_site(site['url'], site['name'])
            results.append({"site": site['name'], "status": "✅ done", "pays": site['pays']})
        except Exception as e:
            results.append({"site": site['name'], "status": f"⚠️ {e}", "pays": site['pays']})
    
    print(f"\n\n💰 SIGNUP RESULTS:")
    for r in results:
        print(f"  {r['status']} {r['site']} — {r['pays']}")
    return results

print("💰 Money Sites loaded!")
