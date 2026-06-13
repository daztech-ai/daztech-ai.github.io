#!/usr/bin/env bash
set -euo pipefail

# deploy.sh — Push new cards to GitHub + trigger Cloudflare Pages deploy
# Run from daztech-pages repo root after generating cards.
#
# Usage:  ./deploy.sh "commit message"
#         ./deploy.sh  (auto-generates timestamp message)

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO_DIR"

# Deploy hook — triggers Cloudflare Pages to pull and deploy
DEPLOY_HOOK="https://api.cloudflare.com/client/v4/workers/builds/deploy_hooks/11253939-f632-4da8-b9dc-9c5a50f97a40"

# Commit message
if [[ $# -ge 1 ]]; then
  MSG="$1"
else
  MSG="Card deploy $(date '+%Y-%m-%d %H:%M:%S %Z')"
fi

# Stage all changes
git add -A

# Check if anything changed
if git diff --cached --quiet; then
  echo "✓ No changes to deploy."
  exit 0
fi

# Commit
git commit -m "$MSG"
echo "→ Committed: $MSG"

# Push to GitHub — Cloudflare Pages auto-deploys from this
git push origin
echo "→ Pushed to GitHub."

# Also trigger deploy hook directly (redundant with auto-deploy, but ensures
# fast CDN refresh and works even if GitHub webhooks are delayed)
echo "→ Triggering Cloudflare deploy hook..."
HTTP_CODE=$(curl -sS -o /dev/null -w "%{http_code}" -X POST "$DEPLOY_HOOK" 2>&1 || echo "failed")
if [[ "$HTTP_CODE" == "200" || "$HTTP_CODE" == "201" ]]; then
  echo "✓ Cloudflare deploy triggered (HTTP $HTTP_CODE)"
else
  echo "⚠ Deploy hook returned HTTP $HTTP_CODE — auto-deploy from git push should still work"
fi
