"""
artha-b.sig — scrape.py
Reddit JSON API (no credentials, 30 req/min).
"""

import requests, sqlite3, hashlib, datetime, time, os

SUBREDDITS = [
    "Indian_flex", "indianstartups", "IndiaInvestments",
    "developersIndia", "indiabusiness", "Entrepreneur",
    "sweatystartup", "SideProject", "smallbusiness",
]

SIGNAL_KEYWORDS = [
    "how I made", "how we made", "started at", "quit my job",
    "making money", "side income", "passive income", "revenue",
    "customers paying", "first sale", "launched", "bootstrapped",
    "built with AI", "solo founder", "failed startup", "shut down",
    "couldn't find a tool", "no tool for this", "paying for",
    "wish there was", "anyone else struggling", "workaround",
    "hack for", "manual process", "AMG", "bought a", "got it at",
    "crores", "lakh", "salary", "freelance", "clients",
]

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/signals.db")
HEADERS = {"User-Agent": "artha-b.sig/0.1 signal-miner (personal use)"}
DELAY = 2.1  # ~28 req/min, stays under 30

def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            id           TEXT PRIMARY KEY,
            scraped_at   TEXT,
            source       TEXT,
            source_url   TEXT,
            title        TEXT,
            raw_text     TEXT,
            score        INTEGER,
            num_comments INTEGER,
            signal_type  TEXT DEFAULT NULL,
            summary      TEXT DEFAULT NULL,
            exact_quote  TEXT DEFAULT NULL,
            pain         TEXT DEFAULT NULL,
            why_tools_fail TEXT DEFAULT NULL,
            founder_fit  TEXT DEFAULT NULL,
            reviewed     INTEGER DEFAULT 0,
            notes        TEXT DEFAULT NULL
        )
    """)
    conn.commit()

def post_id(url):
    return hashlib.sha1(url.encode()).hexdigest()[:16]

def has_keyword(text):
    t = text.lower()
    return any(kw.lower() in t for kw in SIGNAL_KEYWORDS)

def fetch_subreddit(sub, sort="hot", limit=100):
    url = f"https://www.reddit.com/r/{sub}/{sort}.json?limit={limit}"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        return r.json()["data"]["children"]
    except Exception as e:
        print(f"  r/{sub} fetch error: {e}")
        return []

def scrape():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    inserted = skipped = 0

    for sub in SUBREDDITS:
        posts = fetch_subreddit(sub)
        for child in posts:
            p = child["data"]
            title = p.get("title", "")
            body  = p.get("selftext", "")
            text  = f"{title} {body}"

            if not has_keyword(text):
                skipped += 1
                continue

            pid = post_id(p.get("url", title))
            if conn.execute("SELECT 1 FROM signals WHERE id=?", (pid,)).fetchone():
                skipped += 1
                continue

            conn.execute(
                """INSERT INTO signals
                   (id,scraped_at,source,source_url,title,raw_text,score,num_comments)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (pid,
                 datetime.datetime.utcnow().isoformat(),
                 f"reddit/r/{sub}",
                 f"https://reddit.com{p.get('permalink','')}",
                 title,
                 body[:3000],
                 p.get("score", 0),
                 p.get("num_comments", 0))
            )
            inserted += 1

        conn.commit()
        print(f"  r/{sub} ✓")
        time.sleep(DELAY)

    conn.close()
    print(f"\n→ {inserted} inserted, {skipped} skipped")

if __name__ == "__main__":
    scrape()
