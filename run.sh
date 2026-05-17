#!/bin/bash
# artha-b.sig — daily runner
# Set env vars first: REDDIT_CLIENT_ID, REDDIT_SECRET
# LM Studio must be running on localhost:1234

set -e
cd "$(dirname "$0")"

echo "=== artha-b.sig — $(date) ==="
echo ""
echo "1. Scraping Reddit..."
python3 digest/scrape.py

echo ""
echo "2. Extracting signals (LM Studio)..."
python3 extract/extract.py

echo ""
echo "Done. Run 'python3 reports/digest.py' before your weekly review."
