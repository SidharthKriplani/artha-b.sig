"""
artha-b.sig — scrape.py
Collects raw signals from Reddit into SQLite.
Targets: wealth signals, founder stories, business models, pain+demand.
"""

import praw, sqlite3, hashlib, datetime, os

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
]

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/signals.db")

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

def scrape():
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_SECRET"],
        user_agent=os.environ.get("REDDIT_USER_AGENT", "artha-b.sig/0.1"),
    )
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    inserted = skipped = 0

    for sub_name in SUBREDDITS:
        try:
            for post in reddit.subreddit(sub_name).hot(limit=100):
                text = f"{post.title} {post.selftext}"
                if not has_keyword(text):
                    skipped += 1; continue
                pid = post_id(post.url)
                if conn.execute("SELECT 1 FROM signals WHERE id=?", (pid,)).fetchone():
                    skipped += 1; continue
                conn.execute(
                    "INSERT INTO signals (id,scraped_at,source,source_url,title,raw_text,score,num_comments) VALUES (?,?,?,?,?,?,?,?)",
                    (pid, datetime.datetime.utcnow().isoformat(), f"reddit/r/{sub_name}",
                     f"https://reddit.com{post.permalink}", post.title, post.selftext[:3000],
                     post.score, post.num_comments)
                )
                inserted += 1
            conn.commit()
            print(f"  r/{sub_name} ✓")
        except Exception as e:
            print(f"  r/{sub_name} ERROR: {e}")

    conn.close()
    print(f"\n→ {inserted} inserted, {skipped} skipped")

if __name__ == "__main__":
    scrape()
