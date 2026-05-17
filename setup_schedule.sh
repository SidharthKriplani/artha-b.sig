#!/bin/bash
# One-time setup: installs the daily launchd job on macOS

PLIST_SRC="$(cd "$(dirname "$0")" && pwd)/com.sidharthkriplani.artha-b.sig.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/com.sidharthkriplani.artha-b.sig.plist"

cp "$PLIST_SRC" "$PLIST_DEST"
launchctl load "$PLIST_DEST"
echo "Scheduled: artha-b.sig will run every day at 08:00 AM"
echo "To check status: launchctl list | grep artha"
echo "To unload:       launchctl unload $PLIST_DEST"
echo "To run now:      bash $(cd "$(dirname "$0")" && pwd)/run_daily.sh"
