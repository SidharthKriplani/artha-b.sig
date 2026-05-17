<div align="center">

# artha-b.sig

**Private business signal intelligence.**

*Not open source. Not for portfolio. For finding where to concentrate.*

---

![Status](https://img.shields.io/badge/status-live-16a34a?style=flat-square)
![Runs](https://img.shields.io/badge/runs-daily%20%40%2008%3A00-3b82f6?style=flat-square)
![Sources](https://img.shields.io/badge/sources-9%20subreddits-f59e0b?style=flat-square)
![Private](https://img.shields.io/badge/repo-private-374151?style=flat-square)

</div>

---

> The system mines. The LLM extracts. You decide.

Every morning at 08:00 AM: 9 subreddits scraped → signals extracted via local LM Studio → digest pushed to this repo for review.

---

## How it works

```
Reddit JSON API (no credentials)
        ↓
  keyword filter
        ↓
   SQLite (local)
        ↓
  LM Studio extract
        ↓
  digest_YYYY-MM-DD.md
        ↓
   pushed to GitHub  ← you review here
        ↓
  annotate founder_fit
```

---

## Review your signals

**Latest digest:** [`reports/`](./reports/)

Open the most recent `digest_YYYY-MM-DD.md`. Read 15–20 signals. For each interesting one, answer:

> *What is my "solar physics equivalent" here — the domain angle nobody else can reach yet?*

Annotate the `Founder fit?` field in the digest. That annotation is the whole point.

---

## Subreddits tracked

`r/Indian_flex` · `r/indianstartups` · `r/IndiaInvestments` · `r/developersIndia` · `r/indiabusiness` · `r/Entrepreneur` · `r/sweatystartup` · `r/SideProject` · `r/smallbusiness`

---

## Signal types captured

| Type | What it means |
|---|---|
| `wealth_signal` | Someone flexing real money — ICP with purchasing power |
| `founder_story` | How they built it, got traction, distributed |
| `business_model` | What people are actually paying for |
| `pain_point` | Unmet need with real frustration |
| `demand_request` | Explicit "I wish X existed" |
| `workaround` | Manual hack = gap waiting to be filled |
| `failure_story` | What didn't work and why |

---

## Setup (one time)

```bash
pip3 install -r requirements.txt
cp .env.example .env
# set LM_STUDIO_BASE and LM_STUDIO_MODEL in .env
bash setup_schedule.sh   # installs 08:00 AM daily job
```

LM Studio: load any 7B+ instruction model, start server on port 1234.

---

## Run manually

```bash
bash run_daily.sh
```

---

## What stays local (not on GitHub)

- `data/signals.db` — raw signal database
- `.env` — LM Studio config

Everything else including digests is pushed here for review.

---

## Schema

```
signals.db
├── signal_type    — wealth_signal | founder_story | business_model | ...
├── summary        — LLM: one sentence
├── exact_quote    — LLM: verbatim most signal-rich line
├── pain           — LLM: core problem
├── why_tools_fail — LLM: why existing tools fall short
├── founder_fit    — YOUR annotation
├── reviewed       — 0 / 1
└── notes          — YOUR notes
```
