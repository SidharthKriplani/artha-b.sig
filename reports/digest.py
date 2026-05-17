"""
artha-b.sig — digest.py
Generates weekly markdown digest of strongest signals for manual review.
Run this before your Monday review session.
"""

import sqlite3, os, datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/signals.db")
REPORTS_DIR = os.path.dirname(__file__)

PRIORITY_TYPES = ["founder_story", "wealth_signal", "business_model", "pain_point", "demand_request"]

def generate():
    conn = sqlite3.connect(DB_PATH)

    # Last 7 days, extracted, not yet reviewed, sorted by score
    week_ago = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).isoformat()
    rows = conn.execute("""
        SELECT id, source, source_url, title, signal_type, summary,
               exact_quote, pain, why_tools_fail, score, num_comments, notes
        FROM signals
        WHERE scraped_at >= ?
          AND signal_type IS NOT NULL
          AND reviewed = 0
        ORDER BY
            CASE signal_type
                WHEN 'founder_story'  THEN 1
                WHEN 'wealth_signal'  THEN 2
                WHEN 'business_model' THEN 3
                WHEN 'pain_point'     THEN 4
                WHEN 'demand_request' THEN 5
                ELSE 6
            END,
            score DESC
        LIMIT 30
    """, (week_ago,)).fetchall()
    conn.close()

    if not rows:
        print("No new signals this week.")
        return

    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    out_path = os.path.join(REPORTS_DIR, f"digest_{date_str}.md")

    lines = [
        f"# artha-b.sig — Weekly Digest ({date_str})",
        f"> {len(rows)} signals · review, annotate notes, mark reviewed\n",
        "---\n",
    ]

    current_type = None
    for sid, source, url, title, stype, summary, quote, pain, why_fail, score, comments, notes in rows:
        if stype != current_type:
            current_type = stype
            label = stype.replace("_", " ").upper()
            lines.append(f"\n## {label}\n")

        lines.append(f"### [{title}]({url})")
        lines.append(f"*{source} · ↑{score} · {comments} comments*\n")
        if summary:   lines.append(f"**Summary:** {summary}\n")
        if quote:     lines.append(f"> {quote}\n")
        if pain:      lines.append(f"**Pain:** {pain}\n")
        if why_fail:  lines.append(f"**Why tools fail:** {why_fail}\n")
        lines.append(f"**Founder fit?** _(annotate here)_\n")
        lines.append(f"**ID:** `{sid}` — mark reviewed: `UPDATE signals SET reviewed=1 WHERE id='{sid}';`\n")
        lines.append("---\n")

    with open(out_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Digest written: {out_path}")
    print(f"{len(rows)} signals. Spend 20 minutes. Mark the 2-3 that matter.")

if __name__ == "__main__":
    generate()
