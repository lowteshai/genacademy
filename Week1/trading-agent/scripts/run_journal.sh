#!/bin/bash
set -euo pipefail

AGENT_DIR="/Users/lowteshai/Documents/Trading-Agent"
cd "$AGENT_DIR"

export $(cat .env | xargs)

echo "=== End of Day Journal: $(date) ===" >> logs/journal.log
bash scripts/notify.sh "📓 *Journal started* — $(date '+%H:%M ET')" || true

CLAUDE_PROMPT="Run the end-of-day journal routine using the local Python scripts in scripts/. Step 1: run 'python3 scripts/research.py positions' for final open positions and 'python3 scripts/research.py' (no args) for total account value and cash. Step 2: read today's journal file (journal/YYYY-MM-DD.md, use today's actual date) to review what was researched and traded. Step 3: append a Reflection section to the journal with: final portfolio value, day's P&L, what worked, what didn't, any stop-losses triggered, and 2-3 symbols to watch tomorrow with reasons. Always write the journal even if no trades were placed."

CLAUDE_EXIT=0
/Users/lowteshai/.local/bin/claude -p "$CLAUDE_PROMPT" \
  --allowedTools "Bash,Read,Write,Edit" \
  --max-turns 15 \
  >> logs/journal.log 2>&1 || CLAUDE_EXIT=$?

if [ $CLAUDE_EXIT -ne 0 ]; then
  echo "=== Retry (60s): $(date) ===" >> logs/journal.log
  sleep 60
  /Users/lowteshai/.local/bin/claude -p "$CLAUDE_PROMPT" \
    --allowedTools "Bash,Read,Write,Edit" \
    --max-turns 15 \
    >> logs/journal.log 2>&1 || true
fi

echo "=== Done: $(date) ===" >> logs/journal.log
bash scripts/notify.sh "✅ *Journal complete* — $(date '+%H:%M ET')" || true
