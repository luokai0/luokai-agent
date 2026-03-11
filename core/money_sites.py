from core.web_signup import signup_to_site

MONEY_SITES = [
    {"name": "gumroad", "url": "https://app.gumroad.com/signup", "type": "digital products", "pays": "90%+ per sale"},
    {"name": "redbubble", "url": "https://www.redbubble.com/signup", "type": "print on demand", "pays": "10-30% per sale"},
    {"name": "teepublic", "url": "https://www.teepublic.com/signup", "type": "print on demand", "pays": "$2-$6 per sale"},
    {"name": "digistore24", "url": "https://www.digistore24.com/signup", "type": "affiliate", "pays": "30-75% commission"},
    {"name": "warriorplus", "url": "https://warriorplus.com/user/register", "type": "affiliate", "pays": "50-100% commission"},
    {"name": "jvzoo", "url": "https://www.jvzoo.com/register", "type": "affiliate", "pays": "25-100% commission"},
    {"name": "shareasale", "url": "https://www.shareasale.com/newregister.cfm", "type": "affiliate", "pays": "varies"},
    {"name": "prizerebel", "url": "https://www.prizerebel.com/register.php", "type": "surveys", "pays": "$0.50-$5/survey"},
    {"name": "timebucks", "url": "https://timebucks.com/register", "type": "surveys+tasks", "pays": "$0.50-$3/survey"},
    {"name": "swagbucks", "url": "https://www.swagbucks.com/register", "type": "surveys", "pays": "$1-$5/survey"},
]

def print_money_sites():
    print("\n💰 LUO KAI MONEY SITES")
    print("=" * 50)
    for i, s in enumerate(MONEY_SITES, 1):
        print(f"  {i}. {s['name']:<20} {s['pays']:<25} [{s['type']}]")
    print(f"\n✅ Total: {len(MONEY_SITES)} sites ready!")

def signup_all(limit=3):
    print(f"\n🚀 Signing up to {limit} sites...")
    results = []
    for site in MONEY_SITES[:limit]:
        print(f"\n{'='*40}")
        try:
            signup_to_site(site['url'], site['name'])
            results.append(f"✅ {site['name']} — {site['pays']}")
        except Exception as e:
            results.append(f"⚠️ {site['name']} — {e}")
    print(f"\n💰 RESULTS:")
    for r in results:
        print(f"  {r}")

print("💰 Money Sites loaded!")
