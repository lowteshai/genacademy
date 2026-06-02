#!/bin/bash
set -euo pipefail

AGENT_DIR="/Users/lowteshai/Documents/Trading-Agent"
cd "$AGENT_DIR"

export $(cat .env | xargs)

echo "=== Morning Research: $(date) ===" >> logs/research.log
bash scripts/notify.sh "🔍 *Research started* — $(date '+%H:%M ET')" || true

# Generate dynamic watchlist from screener before the agent runs
python3 scripts/screener.py >> logs/research.log 2>&1

CLAUDE_PROMPT="Run the morning research routine using the local Python scripts in scripts/. Step 1: run 'python3 scripts/trade.py status' to check market status. If market is closed, write a brief journal entry and stop. Step 2: read watchlist.json for core symbols and dynamic_watchlist.json for today's screener picks. Step 3: for each symbol in both lists, run 'python3 scripts/research.py bars SYMBOL' and 'python3 scripts/research.py news SYMBOL' — do NOT use web search. Step 4: compute the 20-day and 50-day moving averages from the bars data. Step 5: save all findings to journal/YYYY-MM-DD.md (use today's actual date) under a Research section — core symbols first, then dynamic picks with a note on why they appeared in the screener."

CLAUDE_EXIT=0
/Users/lowteshai/.local/bin/claude -p "$CLAUDE_PROMPT" \
  --allowedTools "Bash,Read,Write,Edit" \
  --max-turns 20 \
  >> logs/research.log 2>&1 || CLAUDE_EXIT=$?

if [ $CLAUDE_EXIT -ne 0 ]; then
  echo "=== Retry (60s): $(date) ===" >> logs/research.log
  sleep 60
  /Users/lowteshai/.local/bin/claude -p "$CLAUDE_PROMPT" \
    --allowedTools "Bash,Read,Write,Edit" \
    --max-turns 20 \
    >> logs/research.log 2>&1 || true
fi

echo "=== Done: $(date) ===" >> logs/research.log
bash scripts/notify.sh "✅ *Research complete* — $(date '+%H:%M ET')" || true
