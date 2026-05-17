"""
artha-b.sig — extract.py
Runs LM Studio (OpenAI-compatible) extraction on unprocessed signals.
Fills: signal_type, summary, exact_quote, pain, why_tools_fail
"""

import sqlite3, os, json
from openai import OpenAI

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/signals.db")
LM_STUDIO_BASE = os.environ.get("LM_STUDIO_BASE", "http://localhost:1234/v1")
MODEL = os.environ.get("LM_STUDIO_MODEL", "local-model")

PROMPT = """You are analyzing a Reddit post to extract a structured signal.

Post title: {title}
Post text: {text}
Source: {source}

Extract ONLY what is explicitly stated. Do not invent.

Return a JSON object with these exact keys:
{{
  "signal_type": one of: "wealth_signal" | "founder_story" | "business_model" | "pain_point" | "demand_request" | "workaround" | "failure_story" | "other",
  "summary": "one sentence, what happened or what the person is saying",
  "exact_quote": "the single most signal-rich sentence from the post, verbatim",
  "pain": "the core problem or need in one sentence, or null if not a pain signal",
  "why_tools_fail": "why existing tools/solutions don't solve this, or null if not applicable"
}}

Return only valid JSON. No explanation."""

def extract_all():
    client = OpenAI(base_url=LM_STUDIO_BASE, api_key="lm-studio")
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT id, title, raw_text, source FROM signals WHERE signal_type IS NULL LIMIT 50"
    ).fetchall()

    print(f"Processing {len(rows)} signals...")

    for sid, title, text, source in rows:
        try:
            prompt = PROMPT.format(
                title=title, text=(text or "")[:1500], source=source
            )
            resp = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=400,
            )
            raw = resp.choices[0].message.content.strip()
            # strip markdown fences if present
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"): raw = raw[4:]
            data = json.loads(raw)
            conn.execute("""
                UPDATE signals SET
                    signal_type=?, summary=?, exact_quote=?, pain=?, why_tools_fail=?
                WHERE id=?
            """, (
                data.get("signal_type"), data.get("summary"),
                data.get("exact_quote"), data.get("pain"),
                data.get("why_tools_fail"), sid
            ))
            conn.commit()
            print(f"  ✓ {sid[:8]}… [{data.get('signal_type')}]")
        except Exception as e:
            print(f"  ✗ {sid[:8]}… ERROR: {e}")

    conn.close()
    print("Done.")

if __name__ == "__main__":
    extract_all()
