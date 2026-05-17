"""
artha-b.sig — Agency Ops Pain Brief Prospector
Finds high-relevance Reddit users discussing agency/B2B ops pain.
Output: ranked CSV for manual review. Does NOT automate contact.

Usage:
    python3 tools/prospect.py
    python3 tools/prospect.py --subreddits indianstartups SideProject
    python3 tools/prospect.py --top 20
"""

import argparse
import csv
import time
from collections import Counter
from datetime import datetime
from pathlib import Path

import requests

# ── Config ────────────────────────────────────────────────────────────────────

HEADERS = {
    "User-Agent": "agency-ops-brief/0.1 prospect-finder (private research, non-commercial)"
}

DEFAULT_SUBREDDITS = [
    "indianstartups",
    "india_indiehackers",
    "SideProject",
    "indiehackers",
    "developersIndia",
    "freelance",
    "Entrepreneur",
    "digital_marketing",
    "webdev",
    "agency",
    "startups",
]

SEARCH_QUERIES = [
    "scope creep agency tool",
    "unpaid invoice freelancer India",
    "client follow up automation",
    "agency reporting tool India",
    "building tool for agencies",
    "SaaS freelancers India",
    "client management agency India",
    "quoting tool freelancer",
    "client ops automation agency",
    "agency workflow problem",
]

# 3 pts each — person is actively building
BUILDER_SIGNALS = [
    "i built", "i'm building", "i am building", "we built", "we're building",
    "building a tool", "building a saas", "working on a",
    "just launched", "i made", "my product", "my tool", "my startup",
    "side project", "indie hacker", "bootstrapped", "solofounder",
    "i'm a developer", "i'm a founder", "automation consultant",
]

# 2 pts each — person is actively seeking a solution
DEMAND_SIGNALS = [
    "does anyone know a tool", "is there a tool", "any tool for",
    "looking for a tool", "i'd pay for", "would pay", "wish there was",
    "nothing exists", "i've been looking", "no good solution",
    "any recommendations", "what do you use for", "how do you handle",
    "we've been trying to solve", "spent hours looking",
]

# 1 pt each — domain relevant
DOMAIN_SIGNALS = [
    "scope creep", "unpaid invoice", "client follow up", "chasing payment",
    "client ghosted", "client went quiet", "reporting for clients",
    "quoting clients", "pricing agencies", "retainer", "freelance crm",
    "agency crm", "project handoff", "client onboarding",
    "scope change", "change request", "invoice dispute",
    "client approval", "client communication", "agency workflow",
]

# ── Scoring ───────────────────────────────────────────────────────────────────

def score_text(text: str) -> tuple:
    t = text.lower()
    matches = []
    score = 0
    for phrase in BUILDER_SIGNALS:
        if phrase in t:
            matches.append(f"[builder] {phrase}")
            score += 3
    for phrase in DEMAND_SIGNALS:
        if phrase in t:
            matches.append(f"[demand] {phrase}")
            score += 2
    for phrase in DOMAIN_SIGNALS:
        if phrase in t:
            matches.append(f"[domain] {phrase}")
            score += 1
    return score, matches


def guess_approach(signal_score: int, signal_matches: list, entry_type: str) -> str:
    has_builder = any("[builder]" in m for m in signal_matches)
    has_demand  = any("[demand]" in m for m in signal_matches)
    if has_builder and signal_score >= 6:
        return "dm_or_linkedin"
    elif has_demand:
        return "public_reply"
    else:
        return "review"

# ── Reddit ────────────────────────────────────────────────────────────────────

def search_subreddit(subreddit: str, query: str, limit: int = 8) -> list:
    url = (
        f"https://www.reddit.com/r/{subreddit}/search.json"
        f"?q={requests.utils.quote(query)}&limit={limit}&sort=relevance&t=year&restrict_sr=1"
    )
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        return r.json().get("data", {}).get("children", [])
    except Exception as e:
        print(f"    [!] r/{subreddit} '{query[:30]}': {e}")
        return []


def get_comments(permalink: str, limit: int = 40) -> list:
    url = f"https://www.reddit.com{permalink}.json?limit={limit}&sort=top"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        data = r.json()
        if not isinstance(data, list) or len(data) < 2:
            return []
        return [c["data"] for c in data[1]["data"]["children"] if c.get("kind") == "t1"]
    except Exception as e:
        print(f"    [!] Comments: {e}")
        return []

# ── Main ──────────────────────────────────────────────────────────────────────

def run(subreddits: list, top: int = 30):
    OUTPUT_DIR = Path(__file__).parent.parent / "data"
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    outfile = OUTPUT_DIR / f"prospects_{datetime.utcnow().strftime('%Y%m%d_%H%M')}.csv"

    candidates: dict = {}  # username → best-scoring entry

    for subreddit in subreddits:
        print(f"\nScanning r/{subreddit}...")
        for query in SEARCH_QUERIES:
            posts = search_subreddit(subreddit, query)
            for item in posts:
                p           = item.get("data", {})
                author      = p.get("author", "")
                title       = p.get("title", "")
                body        = p.get("selftext", "")
                permalink   = p.get("permalink", "")
                post_score  = p.get("score", 0)
                n_comments  = p.get("num_comments", 0)
                thread_url  = f"https://reddit.com{permalink}"

                if author in ("", "[deleted]", "AutoModerator"):
                    continue

                # Score post author
                sig, matches = score_text(f"{title} {body}")
                if sig > 0:
                    if author not in candidates or candidates[author]["signal_score"] < sig:
                        candidates[author] = {
                            "username":         author,
                            "profile_url":      f"https://reddit.com/u/{author}",
                            "source_thread":    thread_url,
                            "entry_type":       "post",
                            "subreddit":        subreddit,
                            "snippet":          title[:220],
                            "comment_score":    post_score,
                            "signal_score":     sig,
                            "signal_matches":   " | ".join(matches[:5]),
                            "why_they_care":    "",
                            "contact_approach": guess_approach(sig, matches, "post"),
                            "notes":            "",
                            "date":             datetime.utcnow().strftime("%Y-%m-%d"),
                        }

                # Score commenters in this thread
                if n_comments > 0:
                    time.sleep(1.5)
                    for c in get_comments(permalink):
                        c_author = c.get("author", "")
                        c_body   = c.get("body", "")
                        c_score  = c.get("score", 0)
                        if c_author in ("", "[deleted]", "AutoModerator"):
                            continue
                        c_sig, c_matches = score_text(c_body)
                        if c_sig > 0:
                            if c_author not in candidates or candidates[c_author]["signal_score"] < c_sig:
                                candidates[c_author] = {
                                    "username":         c_author,
                                    "profile_url":      f"https://reddit.com/u/{c_author}",
                                    "source_thread":    thread_url,
                                    "entry_type":       "comment",
                                    "subreddit":        subreddit,
                                    "snippet":          c_body[:220],
                                    "comment_score":    c_score,
                                    "signal_score":     c_sig,
                                    "signal_matches":   " | ".join(c_matches[:5]),
                                    "why_they_care":    "",
                                    "contact_approach": guess_approach(c_sig, c_matches, "comment"),
                                    "notes":            "",
                                    "date":             datetime.utcnow().strftime("%Y-%m-%d"),
                                }

            time.sleep(2)

    # Rank and export
    ranked = sorted(candidates.values(), key=lambda x: x["signal_score"], reverse=True)[:top]

    fields = [
        "username", "profile_url", "source_thread", "entry_type", "subreddit",
        "snippet", "comment_score", "signal_score", "signal_matches",
        "why_they_care", "contact_approach", "notes", "date",
    ]
    with open(outfile, "w", newline="", encoding="utf-8") as f:
        csv.DictWriter(f, fieldnames=fields).writeheader()
        csv.DictWriter(f, fieldnames=fields).writerows(ranked)

    print(f"\n{'='*55}")
    print(f"  {len(ranked)} candidates → {outfile.name}")
    print(f"  Open in Sheets. Fill 'why_they_care', override 'contact_approach'.")
    approach_counts = Counter(r["contact_approach"] for r in ranked)
    for approach, count in approach_counts.most_common():
        print(f"    {approach}: {count}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--subreddits", nargs="+", default=DEFAULT_SUBREDDITS)
    parser.add_argument("--top", type=int, default=30)
    args = parser.parse_args()
    run(subreddits=args.subreddits, top=args.top)
