"""
artha-b.sig — digest.py
Generates a GitHub-rendered markdown digest + CSV.
Collapsible cards, priority sorted, emoji type badges.
"""

import sqlite3, os, datetime, csv

DB_PATH  = os.path.join(os.path.dirname(__file__), "../data/signals.db")
OUT_DIR  = os.path.dirname(__file__)

PRIORITY = {
    "founder_story":  1,
    "wealth_signal":  2,
    "business_model": 3,
    "pain_point":     4,
    "demand_request": 5,
    "workaround":     6,
    "failure_story":  7,
    "other":          8,
}

EMOJI = {
    "founder_story":  "🏆",
    "wealth_signal":  "💰",
    "business_model": "💼",
    "pain_point":     "🔥",
    "demand_request": "📣",
    "workaround":     "🔧",
    "failure_story":  "💀",
    "other":          "📌",
}

LABEL = {
    "founder_story":  "Founder Story",
    "wealth_signal":  "Wealth Signal",
    "business_model": "Business Model",
    "pain_point":     "Pain Point",
    "demand_request": "Demand Request",
    "workaround":     "Workaround",
    "failure_story":  "Failure Story",
    "other":          "Other",
}

def fetch(days=7):
    cutoff = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).isoformat()
    conn   = sqlite3.connect(DB_PATH)
    rows   = conn.execute("""
        SELECT id, source, source_url, title, signal_type,
               summary, exact_quote, pain, why_tools_fail, score, num_comments
        FROM signals
        WHERE scraped_at >= ? AND signal_type IS NOT NULL AND reviewed = 0
        ORDER BY score DESC
    """, (cutoff,)).fetchall()
    conn.close()
    return sorted(rows, key=lambda r: (PRIORITY.get(r[4] or "other", 8), -(r[9] or 0)))

def generate():
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    rows     = fetch()

    if not rows:
        print("No extracted signals this week."); return

    # ── CSV ───────────────────────────────────────────────────────────────────
    csv_path = os.path.join(OUT_DIR, f"digest_{date_str}.csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["priority","type","title","summary","exact_quote",
                    "pain","why_tools_fail","score","comments","source","url"])
        for r in rows:
            _, src, url, title, stype, summary, quote, pain, why, score, comments = r
            w.writerow([PRIORITY.get(stype or "other", 8), stype, title,
                        summary, quote, pain, why, score, comments, src, url])

    # ── Markdown ──────────────────────────────────────────────────────────────
    md_path = os.path.join(OUT_DIR, f"digest_{date_str}.md")

    # count by type
    counts = {}
    for r in rows:
        t = r[4] or "other"
        counts[t] = counts.get(t, 0) + 1

    # summary bar
    summary_pills = "  ".join(
        f"{EMOJI.get(t,'📌')} **{LABEL.get(t,t)}** `{counts[t]}`"
        for t in sorted(counts, key=lambda x: PRIORITY.get(x, 8))
    )

    lines = [
        f"# artha-b.sig &nbsp;·&nbsp; {date_str}",
        f"",
        f"> **{len(rows)} signals** &nbsp;·&nbsp; priority sorted → upvotes &nbsp;·&nbsp; expand each card &nbsp;·&nbsp; annotate `Founder fit?`",
        f"",
        f"---",
        f"",
        f"{summary_pills}",
        f"",
        f"---",
        f"",
    ]

    prev_type = None
    for r in rows:
        _, src, url, title, stype, summary, quote, pain, why, score, comments = r
        stype = stype or "other"
        em    = EMOJI.get(stype, "📌")
        lbl   = LABEL.get(stype, stype)

        # Section header on type change
        if stype != prev_type:
            prev_type = stype
            n = counts.get(stype, 0)
            lines += [f"## {em} {lbl} &nbsp; `{n}`", ""]

        # Collapsible card
        score_bar = "▓" * min(int((score or 0) / 100), 10)
        summary_short = (summary or "")[:120]

        lines.append(f"<details>")
        lines.append(f"<summary>")
        lines.append(f"<strong><a href=\"{url}\">{title}</a></strong>")
        lines.append(f"<br><sub>{src} &nbsp;·&nbsp; ↑{score} {score_bar} &nbsp;·&nbsp; {comments} 💬 &nbsp;·&nbsp; {summary_short}</sub>")
        lines.append(f"</summary>")
        lines.append(f"")
        if quote:
            lines.append(f"> *\"{quote}\"*")
            lines.append(f"")
        if pain:
            lines.append(f"**🔍 Pain:** {pain}")
            lines.append(f"")
        if why:
            lines.append(f"**⚡ Why tools fail:** {why}")
            lines.append(f"")
        lines.append(f"**🧠 Founder fit?** &nbsp; ___")
        lines.append(f"")
        lines.append(f"</details>")
        lines.append(f"")

    lines += [
        "---",
        f"",
        f"*Generated {date_str} · [CSV](./{os.path.basename(csv_path)})*",
    ]

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"Markdown → {md_path}")
    print(f"CSV      → {csv_path}")
    print(f"{len(rows)} signals ready.")

if __name__ == "__main__":
    generate()
