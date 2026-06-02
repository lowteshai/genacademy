#!/bin/bash
set -euo pipefail

AGENT_DIR="/Users/lowteshai/Documents/Trading-Agent"
cd "$AGENT_DIR"

export $(cat .env | xargs)

echo "=== Trading Session: $(date) ===" >> logs/trading.log
bash scripts/notify.sh "📈 *Trading session started* — $(date '+%H:%M ET')" || true

CLAUDE_PROMPT="Run the trading session using the local Python scripts in scripts/. Step 1: run 'python3 scripts/trade.py status' — if market is closed, log it and stop. Step 2: run 'python3 scripts/research.py positions' to get open positions and 'python3 scripts/research.py' (no args) for cash balance. Step 3: read today's journal file (journal/YYYY-MM-DD.md, use today's actual date) for the Research section written earlier. Step 4: read watchlist.json and dynamic_watchlist.json for all symbols. Step 5: for each symbol, apply the decision framework in CLAUDE.md — answer all 5 questions before deciding. Never exceed 5% of portfolio in one position. Always use limit orders within 0.2% of ask. If any position is down 8% from entry, close it first. Step 6: place orders via 'python3 scripts/trade.py order SYMBOL QTY SIDE LIMIT_PRICE'. Step 7: log every decision and its reasoning to the journal under a Trades section."

CLAUDE_EXIT=0
/Users/lowteshai/.local/bin/claude -p "$CLAUDE_PROMPT" \
  --allowedTools "Bash,Read,Write,Edit" \
  --max-turns 20 \
  >> logs/trading.log 2>&1 || CLAUDE_EXIT=$?

if [ $CLAUDE_EXIT -ne 0 ]; then
  echo "=== Retry (60s): $(date) ===" >> logs/trading.log
  sleep 60
  /Users/lowteshai/.local/bin/claude -p "$CLAUDE_PROMPT" \
    --allowedTools "Bash,Read,Write,Edit" \
    --max-turns 20 \
    >> logs/trading.log 2>&1 || true
fi

echo "=== Done: $(date) ===" >> logs/trading.log
bash scripts/notify.sh "✅ *Trading session complete* — $(date '+%H:%M ET')" || true
