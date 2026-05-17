"""
artha-b.sig — digest.py
Generates a priority-sorted HTML report + CSV for daily review.
"""

import sqlite3, os, datetime, csv, html as html_lib

DB_PATH   = os.path.join(os.path.dirname(__file__), "../data/signals.db")
OUT_DIR   = os.path.dirname(__file__)

PRIORITY = {
    "founder_story":   1,
    "wealth_signal":   2,
    "business_model":  3,
    "pain_point":      4,
    "demand_request":  5,
    "workaround":      6,
    "failure_story":   7,
    "other":           8,
}

COLORS = {
    "founder_story":   ("#f0fdf4", "#16a34a", "#dcfce7"),
    "wealth_signal":   ("#fffbeb", "#d97706", "#fef3c7"),
    "business_model":  ("#eff6ff", "#2563eb", "#dbeafe"),
    "pain_point":      ("#fef2f2", "#dc2626", "#fee2e2"),
    "demand_request":  ("#fdf4ff", "#9333ea", "#f3e8ff"),
    "workaround":      ("#fff7ed", "#ea580c", "#ffedd5"),
    "failure_story":   ("#f8fafc", "#64748b", "#f1f5f9"),
    "other":           ("#f8fafc", "#64748b", "#f1f5f9"),
}

LABELS = {
    "founder_story":  "Founder Story",
    "wealth_signal":  "Wealth Signal",
    "business_model": "Business Model",
    "pain_point":     "Pain Point",
    "demand_request": "Demand Request",
    "workaround":     "Workaround",
    "failure_story":  "Failure Story",
    "other":          "Other",
}

def fetch_signals(days=7):
    cutoff = (datetime.datetime.utcnow() - datetime.timedelta(days=days)).isoformat()
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("""
        SELECT id, source, source_url, title, signal_type, summary,
               exact_quote, pain, why_tools_fail, score, num_comments
        FROM signals
        WHERE scraped_at >= ? AND signal_type IS NOT NULL AND reviewed = 0
        ORDER BY score DESC
    """, (cutoff,)).fetchall()
    conn.close()
    return sorted(rows, key=lambda r: (PRIORITY.get(r[4] or "other", 8), -( r[9] or 0)))

def generate():
    date_str  = datetime.datetime.now().strftime("%Y-%m-%d")
    rows      = fetch_signals()

    if not rows:
        print("No new extracted signals this week.")
        return

    # ── CSV ───────────────────────────────────────────────────────────────────
    csv_path = os.path.join(OUT_DIR, f"digest_{date_str}.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["priority","signal_type","title","summary","exact_quote",
                    "pain","why_tools_fail","score","comments","source","url"])
        for r in rows:
            sid, source, url, title, stype, summary, quote, pain, why, score, comments = r
            w.writerow([PRIORITY.get(stype or "other", 8), stype, title, summary,
                        quote, pain, why, score, comments, source, url])

    # ── HTML ──────────────────────────────────────────────────────────────────
    html_path = os.path.join(OUT_DIR, f"digest_{date_str}.html")

    def e(s): return html_lib.escape(str(s or ""))

    cards = ""
    prev_type = None
    for r in rows:
        sid, source, url, title, stype, summary, quote, pain, why, score, comments = r
        stype = stype or "other"
        bg, accent, tag_bg = COLORS.get(stype, COLORS["other"])
        label = LABELS.get(stype, stype)

        if stype != prev_type:
            prev_type = stype
            cards += f"""
            <div class="section-header" style="border-left:4px solid {accent}">
                <span style="color:{accent}">● {label}</span>
            </div>"""

        pain_block = f'<div class="field"><span class="field-label">Pain</span><span class="field-val">{e(pain)}</span></div>' if pain else ""
        why_block  = f'<div class="field"><span class="field-label">Why tools fail</span><span class="field-val">{e(why)}</span></div>' if why else ""
        quote_block = f'<blockquote>{e(quote)}</blockquote>' if quote else ""

        cards += f"""
        <div class="card" style="border-left:3px solid {accent};background:{bg}">
            <div class="card-top">
                <span class="tag" style="background:{tag_bg};color:{accent}">{label}</span>
                <span class="meta">{e(source)} &nbsp;·&nbsp; ↑{score} &nbsp;·&nbsp; {comments} comments</span>
            </div>
            <a class="card-title" href="{e(url)}" target="_blank">{e(title)}</a>
            <p class="summary">{e(summary)}</p>
            {quote_block}
            {pain_block}
            {why_block}
            <div class="founder-fit">
                <span class="field-label">Founder fit?</span>
                <span class="fit-hint">— annotate here —</span>
            </div>
        </div>"""

    counts = {}
    for r in rows:
        t = r[4] or "other"
        counts[t] = counts.get(t, 0) + 1

    pills = "".join(
        f'<span class="pill" style="background:{COLORS[t][2]};color:{COLORS[t][1]}">'
        f'{LABELS.get(t,t)} {counts[t]}</span>'
        for t in sorted(counts, key=lambda x: PRIORITY.get(x, 8))
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>artha-b.sig — {date_str}</title>
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  body {{ font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
          background:#0f172a; color:#e2e8f0; padding:2rem 1rem; }}
  .wrap {{ max-width:780px; margin:0 auto; }}
  h1 {{ font-size:1.4rem; font-weight:700; color:#f8fafc; letter-spacing:-.3px; }}
  .sub {{ color:#64748b; font-size:.85rem; margin-top:.25rem; }}
  .pills {{ display:flex; flex-wrap:wrap; gap:.4rem; margin:1.2rem 0 2rem; }}
  .pill {{ padding:.25rem .65rem; border-radius:999px; font-size:.75rem; font-weight:600; }}
  .section-header {{ padding:.5rem .75rem; margin:1.5rem 0 .5rem;
                     border-radius:6px; font-weight:700; font-size:.8rem;
                     letter-spacing:.5px; text-transform:uppercase; background:#1e293b; }}
  .card {{ border-radius:10px; padding:1.1rem 1.2rem; margin-bottom:.85rem; }}
  .card-top {{ display:flex; align-items:center; gap:.6rem; margin-bottom:.5rem; }}
  .tag {{ padding:.2rem .55rem; border-radius:999px; font-size:.7rem; font-weight:700; }}
  .meta {{ font-size:.75rem; color:#64748b; margin-left:auto; }}
  .card-title {{ display:block; font-weight:600; font-size:.95rem; color:#1e293b;
                 text-decoration:none; margin-bottom:.4rem; line-height:1.35; }}
  .card-title:hover {{ text-decoration:underline; }}
  .summary {{ font-size:.85rem; color:#334155; line-height:1.5; margin-bottom:.5rem; }}
  blockquote {{ border-left:3px solid #cbd5e1; padding:.35rem .75rem;
                font-size:.82rem; color:#475569; margin:.5rem 0; font-style:italic; }}
  .field {{ display:flex; gap:.5rem; font-size:.8rem; margin:.3rem 0; flex-wrap:wrap; }}
  .field-label {{ font-weight:700; color:#64748b; white-space:nowrap; min-width:90px; }}
  .field-val {{ color:#334155; flex:1; }}
  .founder-fit {{ margin-top:.7rem; padding-top:.6rem; border-top:1px solid #e2e8f0;
                  display:flex; gap:.5rem; font-size:.8rem; align-items:center; }}
  .fit-hint {{ color:#94a3b8; font-style:italic; }}
</style>
</head>
<body>
<div class="wrap">
  <h1>artha-b.sig &nbsp;·&nbsp; {date_str}</h1>
  <p class="sub">{len(rows)} signals · sorted by priority then upvotes · annotate founder fit before marking reviewed</p>
  <div class="pills">{pills}</div>
  {cards}
</div>
</body>
</html>"""

    with open(html_path, "w") as f:
        f.write(html)

    print(f"HTML  → {html_path}")
    print(f"CSV   → {csv_path}")
    print(f"{len(rows)} signals. Open the HTML in your browser.")

if __name__ == "__main__":
    generate()
