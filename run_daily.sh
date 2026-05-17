#!/bin/bash
# artha-b.sig — daily automated pipeline
# scrape → extract (LM Studio) → commit → push to GitHub

DIR="$(cd "$(dirname "$0")" && pwd)"
LOG="$DIR/data/run.log"
DATE=$(date '+%Y-%m-%d %H:%M')

log() { echo "[$DATE] $1" | tee -a "$LOG"; }

cd "$DIR"

# Load .env
[ -f "$DIR/.env" ] && export $(grep -v '^#' "$DIR/.env" | xargs)

log "=== artha-b.sig daily run ==="

# 1. Scrape
log "Scraping Reddit..."
python3 digest/scrape.py >> "$LOG" 2>&1 && log "Scrape done." || log "Scrape error."

# 2. Extract — skip gracefully if LM Studio not running
log "Checking LM Studio..."
if curl -s --max-time 3 "${LM_STUDIO_BASE:-http://localhost:1234}/v1/models" > /dev/null 2>&1; then
    log "LM Studio online — extracting..."
    python3 extract/extract.py >> "$LOG" 2>&1 && log "Extraction done." || log "Extraction error."
else
    log "LM Studio offline — raw signals saved, extraction queued for next run."
fi

# 3. Generate digest report
python3 reports/digest.py >> "$LOG" 2>&1

# 4. Count new signals for commit message
NEW=$(python3 -c "
import sqlite3, datetime
c = sqlite3.connect('data/signals.db')
today = datetime.date.today().isoformat()
n = c.execute('SELECT COUNT(*) FROM signals WHERE scraped_at >= ?', (today,)).fetchone()[0]
print(n)
c.close()
" 2>/dev/null || echo "?")

# 5. Commit + push
git add data/signals.db reports/ data/run.log 2>/dev/null || true
git diff --cached --quiet 2>/dev/null || git commit -m "daily: $(date '+%Y-%m-%d') — ${NEW} new signals" >> "$LOG" 2>&1
git push origin main >> "$LOG" 2>&1 && log "Pushed to GitHub." || log "Push failed — check credentials."

log "=== done ==="
