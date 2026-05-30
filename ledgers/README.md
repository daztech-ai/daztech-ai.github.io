# Bet Ledger System

Daily JSON ledgers tracking every selection published on the Daztech Hub.

## Location
`output/ledgers/` — auto-deployed to `daztech-betting.surge.sh/ledgers/`

## Format
`{date}_{code}_ledger.json` — e.g. `2026-05-29_nrl_ledger.json`

## Schema
```json
{
  "timestamp": "ISO datetime",
  "code": "nrl|racing|nba",
  "selection_details": "Human-readable bet description",
  "model_rating": "STRONG|MODERATE|SPEC or numeric score",
  "edge_pct": 11.2,
  "recommended_stake": 1.0,
  "odds": 1.80,
  "sportsbet_market": "Win|H2H|SGM|Place",
  "status": "pending|won|lost|void",
  "result_payout": null,
  "notes": "Analysis context"
}
```

## Codes
- `nrl` — NRL head-to-head, line, SGM, try scorers
- `racing` — Calibrated win bets, cheatsheet picks
- `nba` — NBA SGM, player props, series bets

## Workflow

### 1. Log bets (when publishing to hub)
```bash
python src/output/jarvis_ledger.py  # or manual JSON
```

### 2. Update results (after games/races finish)
- Match on `selection_details` field
- Set `status` → `won`/`lost`/`void`
- Set `result_payout` → actual return (e.g. 1.80 for $1.80 per $1 staked)
- Timestamp the update

### 3. Calculate daily P&L
```python
total_staked = sum(b['recommended_stake'] for b in bets)
total_returned = sum(b['result_payout'] * b['recommended_stake'] for b in bets if b['status'] == 'won')
roi = (total_returned - total_staked) / total_staked * 100
```

## Active Ledgers
- 2026-05-29: 2 NRL + 8 Racing = 10 selections
