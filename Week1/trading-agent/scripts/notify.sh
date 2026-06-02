#!/bin/bash
# Usage: notify.sh "your message"
MESSAGE="$1"
curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage" \
  -d chat_id="${TELEGRAM_CHAT_ID}" \
  -d text="${MESSAGE}" \
  -d parse_mode="Markdown" \
  > /dev/null
