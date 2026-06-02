# Autonomous Trading Agent

An AI-driven paper trading agent built on Claude Code that runs a daily research → trade → journal cycle against the Alpaca paper trading API.

## How It Works

The agent runs three automated routines every market day:

| Time (ET) | Script | What it does |
|-----------|--------|--------------|
| 9:45 AM | `run_research.sh` | Pulls price bars and news for every watchlist symbol, computes 20/50-day MAs, writes findings to the day's journal |
| 10:00 AM | `run_trading.sh` | Reads the morning research, applies the decision framework, places limit orders, logs all reasoning |
| 4:15 PM | `run_journal.sh` | Fetches final positions and P&L, appends a Reflection section to the journal |

Each shell script invokes `claude -p` (Claude Code CLI in non-interactive mode) with a structured prompt and a restricted tool set (`Bash`, `Read`, `Write`, `Edit`). Claude handles all reasoning; the Python scripts handle all API I/O.

## Project Structure

```
.
├── CLAUDE.md                  # Agent instructions: rules, decision framework, output format
├── watchlist.json             # Core symbols the agent always researches
├── dynamic_watchlist.json     # Today's screener picks (regenerated each morning)
├── .env.example               # Required environment variables (copy to .env and fill in)
├── .claude/
│   └── routines.json          # Scheduled routine definitions (Claude Code harness)
├── scripts/
│   ├── screener.py            # Generates dynamic_watchlist.json from Alpaca screener API
│   ├── research.py            # Fetches bars, news, positions, account data
│   ├── trade.py               # Places/cancels orders, checks market status
│   ├── run_research.sh        # Morning research driver
│   ├── run_trading.sh         # Trading session driver
│   ├── run_journal.sh         # End-of-day journal driver
│   └── notify.sh              # Sends Telegram notifications on routine start/end
└── journal/
    ├── 2026-05-12.md          # Daily journal entries written by the agent
    ├── 2026-05-13.md
    ├── 2026-05-14.md
    ├── 2026-05-15.md
    ├── 2026-05-18.md
    ├── 2026-05-20.md
    ├── 2026-05-21.md
    └── 2026-05-22.md
```

## Trading Rules (enforced via CLAUDE.md)

- Never invest more than 5% of total portfolio value in a single position
- Never place a market order — always use limit orders within 0.2% of ask
- Close any position that drops 8% from entry, no exceptions
- Always write a journal entry, even on no-trade days
- Never place trades when market status is "closed"

## Decision Framework

Before each trade the agent answers five questions:
1. What is the current cash balance?
2. What positions are already open?
3. What does recent news say about this ticker?
4. What do the 20-day and 50-day moving averages show?
5. What is the downside risk if this trade goes wrong?

## Setup

1. Clone the repo
2. Copy `.env.example` to `.env` and fill in your Alpaca paper trading credentials
3. Install dependencies: `pip install requests`
4. Install Claude Code CLI: `npm install -g @anthropic/claude-code`
5. Register the routines with the Claude Code harness or run the shell scripts manually

## Stack

- **Agent runtime:** [Claude Code](https://claude.ai/code) (`claude -p` non-interactive mode)
- **Brokerage API:** [Alpaca Markets](https://alpaca.markets) (paper trading)
- **Notifications:** Telegram Bot API
- **Language:** Python 3 (API scripts) + Bash (orchestration)
