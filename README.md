# artha-b.sig

Private business signal intelligence. Not open source. Not for portfolio. For finding where to concentrate.

## What it does

Scrapes Reddit for wealth signals, founder stories, business models, pain points, and demand gaps.
Extracts structured fields via LM Studio (local, no API cost).
Generates a weekly digest for manual review.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# fill in .env
```

Reddit API credentials: https://www.reddit.com/prefs/apps → create app → script type.

LM Studio: download, load any 7B+ instruction model, start local server on port 1234.

## Daily workflow

```bash
# runs scrape + extract
bash run.sh

# before Monday review
python3 reports/digest.py
```

Open `reports/digest_YYYY-MM-DD.md`, read 15-20 signals, annotate "Founder fit?" on the interesting ones, mark reviewed.

## The only question that matters

> What is my "solar physics equivalent" — the domain angle nobody else can easily replicate?

Use this to annotate founder_fit on each signal.

## Schema

```
signals.db
├── id           — sha1 of URL
├── scraped_at
├── source       — e.g. reddit/r/Indian_flex
├── source_url
├── title
├── raw_text
├── score        — upvotes
├── num_comments
├── signal_type  — wealth_signal | founder_story | business_model | pain_point | demand_request | workaround | failure_story
├── summary      — LLM: one sentence
├── exact_quote  — LLM: verbatim most signal-rich line
├── pain         — LLM: core problem
├── why_tools_fail
├── founder_fit  — YOUR manual annotation
├── reviewed     — 0/1
└── notes        — YOUR manual notes
```
