"""
artha-b.sig — scrape.py
Reddit JSON API (no credentials, ~28 req/min).
25 subreddits: Indian wealth/founder + global entrepreneur/income signals.
"""

import requests, sqlite3, hashlib, datetime, time, os

SUBREDDITS = [
    # ── India ────────────────────────────────────────────────
    "Indian_flex",          # 125K  — direct wealth display
    "indianstartups",       # 300K  — founder stories, raises
    "IndiaInvestments",     # 892K  — investment, wealth moves
    "personalfinanceindia", # 427K  — income, savings, milestones
    "IndianStreetBets",     # 200K  — trading wins, wealth signals
    "developersIndia",      # 200K  — dev income, freelance, jobs
    "indiabusiness",        # 100K  — SMB, B2B, local business
    "india",                # 1.7M  — general; flexes surface here too
    "bangalore",            # 250K  — tech hub, salary flex, startups
    # ── Global: Founder / Builder ────────────────────────────
    "Entrepreneur",         # 4.9M  — core founder community
    "EntrepreneurRideAlong",# 300K  — candid revenue updates, MRR
    "sweatystartup",        # 500K  — physical/service biz, real money
    "startups",             # 1.2M  — early stage, traction stories
    "SideProject",          # 300K  — builders sharing what they made
    "IMadeThis",            # 100K  — product launches, first sales
    "advancedentrepreneur", # 50K   — scaling, exits, deep founder takes
    "SaaS",                 # 200K  — MRR, churn, pricing signals
    "ecommerce",            # 300K  — store revenue, product gaps
    "AmazonFBA",            # 200K  — specific business model signals
    # ── Global: Income / Wealth ──────────────────────────────
    "smallbusiness",        # 1.5M  — real SMB operators
    "freelance",            # 500K  — pricing, client wins, income
    "digitalnomad",         # 1.5M  — location-free income signals
    "passive_income",       # 1.5M  — wealth compounding signals
    "financialindependence",# 2.3M  — FIRE, wealth milestones
    "sidehustle",           # 500K  — monetisation experiments
]

SIGNAL_KEYWORDS = [
    # Wealth signals
    "how I made", "how we made", "finally got", "bought a", "got it at",
    "upgraded to", "first car", "crores", "lakh", "AMG", "luxury",
    # Founder / revenue
    "revenue", "MRR", "ARR", "first sale", "paying customers", "customers paying",
    "launched", "bootstrapped", "solo founder", "quit my job", "left my job",
    "started at", "started with", "$100", "$1000", "from zero",
    # Income / side hustle
    "making money", "side income", "passive income", "freelance income",
    "clients", "consulting", "monthly income", "salary", "per month",
    # Pain / gap
    "couldn't find", "no tool for", "wish there was", "anyone else struggling",
    "workaround", "manual process", "hack for", "paying for",
    # Failure / learning
    "failed startup", "shut down", "we failed", "mistake I made",
    "lessons learned", "what I'd do differently",
]

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/signals.db")
HEADERS  = {"User-Agent": "artha-b.sig/0.1 signal-miner (personal use)"}
DELAY    = 2.1  # ~28 req/min

def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            id             TEXT PRIMARY KEY,
            scraped_at     TEXT,
            source         TEXT,
            source_url     TEXT,
            title          TEXT,
            raw_text       TEXT,
            score          INTEGER,
            num_comments   INTEGER,
            signal_type    TEXT DEFAULT NULL,
            summary        TEXT DEFAULT NULL,
            exact_quote    TEXT DEFAULT NULL,
            pain           TEXT DEFAULT NULL,
            why_tools_fail TEXT DEFAULT NULL,
            founder_fit    TEXT DEFAULT NULL,
            reviewed       INTEGER DEFAULT 0,
            notes          TEXT DEFAULT NULL
        )
    """)
    conn.commit()

def post_id(url):
    return __import__('hashlib').sha1(url.encode()).hexdigest()[:16]

def has_keyword(text):
    t = text.lower()
    return any(k.lower() in t for k in SIGNAL_KEYWORDS)

def fetch_sub(sub, limit=100):
    url = f"https://www.reddit.com/r/{sub}/hot.json?limit={limit}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        return r.json()["data"]["children"]
    except Exception as e:
        print(f"  r/{sub} error: {e}"); return []

def scrape():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    inserted = skipped = 0

    for sub in SUBREDDITS:
        for child in fetch_sub(sub):
            p     = child["data"]
            title = p.get("title", "")
            body  = p.get("selftext", "")
            if not has_keyword(f"{title} {body}"):
                skipped += 1; continue
            pid = post_id(p.get("url", title))
            if conn.execute("SELECT 1 FROM signals WHERE id=?", (pid,)).fetchone():
                skipped += 1; continue
            conn.execute(
                "INSERT INTO signals (id,scraped_at,source,source_url,title,raw_text,score,num_comments)"
                " VALUES (?,?,?,?,?,?,?,?)",
                (pid, datetime.datetime.utcnow().isoformat(),
                 f"reddit/r/{sub}",
                 f"https://reddit.com{p.get('permalink','')}",
                 title, body[:3000],
                 p.get("score",0), p.get("num_comments",0))
            )
            inserted += 1
        conn.commit()
        print(f"  r/{sub} ✓")
        time.sleep(DELAY)

    conn.close()
    print(f"\n→ {inserted} inserted, {skipped} skipped")

if __name__ == "__main__":
    scrape()
