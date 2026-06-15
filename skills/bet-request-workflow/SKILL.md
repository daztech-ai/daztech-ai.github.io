---
name: bet-request-workflow
description: Bet request SOP: engine analysis, expert cross-ref, late mail, SGM builder, drift check, ledger. NRL/World Cup/any sport.
---

# Bet Request Workflow

Complete end-to-end workflow for every bet request. Sport-agnostic — works for NRL, FIFA World Cup, AFL, NBA, any sport supported by the Odds API.

## Pre-Flight: Stake Check (MANDATORY)

Before ANY bet recommendation, ask:
- **How much do you want to stake on this?**

Bankroll, bookmaker, and session target should be gathered naturally over time — don't interrogate up front. The stake amount is the only blocking question.

## Phase 1: Event Discovery

When user requests analysis for a game/match:

```bash
daz-betting-engine pev-events --sport {sport_key} --limit 10
```

Common sport keys: `rugbyleague_nrl`, `soccer_fifa_world_cup`, `aussie_rules_afl`, `basketball_nba`, `soccer_epl`.

Match the user's request to an event_id from the output.

## Phase 2: Engine Analysis

Run the full assistant pipeline:

```bash
ODDS_API_KEY=*** daz-betting-engine assistant game \
  --sport {sport_key} --event-id {event_id}
```

Generates in `bundles/{sport_key}_{event_id}_{timestamp}/`:
- `index.html` — mobile-first betting workflow page
- `agent_feed.json` — machine-readable decision summary
- `bundle_summary.json` — full PEV + SGM analysis
- `ledger.jsonl` — audit trail entry

**Read `agent_feed.json`** for the high-level decision. **Read `bundle_summary.json`** for detailed edge calculations.

## Phase 3: PEV Analysis (Single-Bet Edge)

From `bundle_summary.json` → `pev.recommendations[]`:

- `action`: `check` (place), `verify` (warn), `blocked` (skip)
- `edge`: Positive = value. ≥3% minimum threshold
- `current_odds` / `fair_odds`: Market price vs engine consensus
- `suggested_stake`: ¼ Kelly on $1000 default bankroll
- `warnings`: `verify_liquidity`, `stale_odds`, etc.

**Key rule:** If the user's bookmaker doesn't appear in PEV recommendations, the edge doesn't exist on their platform. Be honest.

## Phase 4: SGM Analysis (Multi-Leg)

From `bundle_summary.json` → `sgm.candidates[]`:

- `action`: `blocked` = no edge, skip
- `minimum_acceptable_sgm_odds`: Minimum combined odds to be +EV
- `estimated_edge_at_leg_product`: Edge at simple multiplication
- `warnings`: `deeply_negative_estimated_edge` = hard pass

For long-shot SGMs (10-leg):
```bash
daz-betting-engine sgm game --sport {sport_key} --event-id {event_id} \
  --bookmaker {bookmaker} --include-long-shot --max-candidates 10
```

### ALWAYS: Generate the HTML card for review

The `assistant game` command always produces `index.html` — a mobile-first betting card. Share this with the user for visual review regardless of engine verdict. The card shows all candidates, odds, and actions.

## Phase 4a: Engine Decision Routing

### Tier 1 — Engine says PLACE ✅
- PEV edge >=5% OR SGM candidates actionable
- Full stake at user's amount
- All markets in play (h2h, spreads, totals, try-scorers)
- Confidence: High 🟢

### Tier 2 — Engine says BLOCKED but expert consensus converges ⚠️
This is the conviction tier. Engine can only see h2h/spreads/totals — it cannot price try-scorer markets or Origin-impacted conditions.

**Entry conditions (all must be true):**
- Engine verdict is BLOCKED (no PEV or SGM edge on user's bookmaker)
- 3+ independent expert sources agree on the same direction
- Try-scorers cross-referenced against Zero Tackle confirmed squads

**Rules for Tier 2 bets:**
- **Try-scorer only** — stay away from h2h/spreads/totals (the engine's negative on those)
- **Reduced stake** — 10-15% of bankroll, not full amount
- **Marked CONVICTION** in ledger — tracked separately from engine-backed bets
- **Card still generated** — always show the HTML so Danny/David can review visually

### Tier 3 — Engine BLOCKED + no expert consensus ❌
- PASS. Honest silence. Save the stake for the next game.
- Still generate the card — it shows the blocked verdict for transparency

## Phase 5: Manual SGM Builder (Engine Gap Coverage)

The engine only has h2h/spreads/totals via API. For markets it can't access:

### Try-Scorer Markets
- Pull Stats Insider anytime try probabilities
- Cross-reference with Zero Tackle confirmed 20-man squads ⚠️ MANDATORY
- Check try-scoring streaks (last 5 games)
- Check H2H try-scoring history vs this opponent

### TSS — Try-Scorer Score (out of 100)

Repeatable scoring model used for Tier 2 conviction bets. Computed per player per game.

| Factor | Weight | Source |
|--------|--------|--------|
| Anytime try probability | 30% | Stats Insider 10K sims |
| T/G (tries per game, last 7) | 25% | Champion Data or match logs |
| Try streak (consecutive games) | 10% | Match results |
| H2H tries vs opponent (career) | 15% | Historical data |
| Expert consensus (pick count) | 10% | 4-5 expert sources |
| Position bonus (winger/centre) | 5% | Team sheet |
| Origin/injury context (weakened defence) | 5% | Late mail |

**Scoring rules:**
- Anytime try %: multiply by 100, cap at 80 (e.g. 64% → 64, but 85% → capped 80)
- T/G last 7: T/G ÷ 1.5 × 25, cap at 25 (e.g. 1.0 T/G → 16.7, 2.0 T/G → capped 25)
- Try streak: 2 pts per consecutive try-scoring game, cap at 10
- H2H: (tries vs opponent ÷ games vs opponent) × 15, cap at 15
- Expert consensus: 2 pts per source picking this player, cap at 10
- Position: winger=5, centre=4, fullback=3, half=2, hooker=1, forward=0
- Context: +5 if opposition missing key defenders (Origin/injury), otherwise 0

**Rating tiers:**
- TSS ≥ 70 → 🟢 Strong (primary leg)
- TSS 50–69 → 🟡 Consider (secondary leg)
- TSS < 50 → 🟠 Weak (avoid or long-shot only)

**SGM pricing from TSS:**
For a Tier 2 conviction SGM, estimate fair probability:
- Convert each TSS to implied probability: TSS/100
- Apply +15% correlation bonus for multi-scorer SGMs (scorers are positively correlated)
- Compare against Sportsbet's combined price

### Late Mail / Team Lists
Primary source: Zero Tackle (`zerotackle.com/updated-team-lists-*`)
- Extract confirmed 1-17 and reserves (18-22)
- Note all OUTs with reasons (Origin, injury, suspension, rested)
- Cross-reference every try-scorer pick against confirmed squad ⚠️
- Check freshness: <48h for team lists, <4h before kickoff ideal

### Expert Source Check (NRL)
1. Stats Insider — simulation model, try probabilities
2. Betseeker — ATS trends, under/over analysis
3. Before You Bet — form analysis, total points
4. GoBet — expert picks, SGM suggestions
5. Dimers — ML model predictions

Look for **consensus** — 3+ sources agreeing = higher confidence.

### Round Context
- Origin-affected rounds: check which teams lose/gain players
- Pattern analysis: blowouts? Unders/Overs trend?
- Weather at venue (especially for totals)

## Phase 6: Wiki Cross-Reference

Scan `~/wiki/` for relevant model theory:
- Pythago NRL model (SCWP, WCL, Elo systems)
- Kelly criterion reference
- SGP correlation mathematics

Cross-reference engine findings against wiki principles. Flag contradictions.

## Phase 7: Drift Check (MANDATORY)

```
GAME: {home} v {away} R{round}
  [✅/⚠️/❌] Roster: All players in Zero Tackle confirmed squads
  [✅/⚠️/❌] Team lists: OUTs confirmed, positions verified
  [✅/⚠️/❌] Odds: Live check completed, within expected ranges
  [✅/⚠️/❌] Experts: >=3 sources fetched, consensus verified
  [✅/⚠️/❌] Late mail: <48h freshness
  [✅/⚠️/❌] Round trend: context understood
  RESULT: PASS / FAIL
```

If FAIL on any check → fix before recommending.

## Phase 8: Recommendation Output

```
━━━ Bet Recommendation ━━━
Sport/League: {sport}
Match:       {home} vs {away}
Date:        {kickoff time}
───
Leg 1: {selection} @ {odds}
Leg 2: {selection} @ {odds}
───
Combined Odds:  {x.xx}
Fair Probability: {xx.x%}
Edge:          {±x.x%} {✅/⚠️/❌}
Stake:         {amount} ({x%} of bankroll)
Confidence:    {High 🟢 / Medium 🟡 / Low 🟠}
───
Reasoning: {why}
───
Ledger: {ID}
Status: PENDING
Bookmaker: {platform}
```

## Phase 9: User Confirmation

**Wait for user to:**
1. Build the SGM on their bookmaker's app
2. Confirm exact combined odds
3. Explicitly say "place" or "lock"

**Do NOT write the ledger entry until confirmed.**

## Phase 10: Ledger Entry

Only after confirmed placement. Write to `ledger/betting-journal.md`:

```markdown
### {ID}
**Date:** {YYYY-MM-DD}
**Match:** {Home} vs {Away} R{round}
**Type:** {SGM/H2H/Line} ({N}-leg)
**Stake:** ${xx} ({x%} at ${bankroll} bankroll)
**Odds:** {x.xx}
**Edge:** {±x.x%}
**Confidence:** {Level} {emoji}
**Bookmaker:** {platform}
**Reasoning:** {summary}
**Status:** PENDING
**Result:** ❓
**P&L:** ±$0.00
**Audit Note:**
```

Post-result: update Status to WON/LOST/VOID, calculate P&L, note lessons.

## Edge Thresholds

| Tier | Engine | Expert Consensus | Action | Stake |
|------|--------|-----------------|--------|-------|
| 🟢 Tier 1 | PLACE | Any | Full confidence | 100% of user's stated amount |
| 🟡 Tier 2 | BLOCKED | 3+ sources agree | Conviction bet | 50-75% of user's stated amount |
| 🔴 Tier 3 | BLOCKED | < 3 sources agree | PASS | $0 |

Tier 2 conviction bets:
- Try-scorer only (engine can't price these)
- Ledger marked `CONVICTION`
- Tracked separately to audit conviction vs engine performance
- Always generate HTML card for visual review

## Bankroll Management

- Flat staking 1-5% of bankroll per bet
- Edge-based: ¼ Kelly (half-Kelly max)
- Never exceed user's stated maximum

## Red Lines

- Never recommend below 3% edge (Tier 1)
- Tier 2 conviction bets allowed only when 3+ experts agree AND try-scorer only
- Never bet Tie/Draw in low-scoring sports
- Cross-reference every try-scorer against confirmed squad
- Never skip drift check
- Never write ledger before user confirms
- Engine blocked + no expert consensus → say PASS (Tier 3)
- Honest silence > forced bet
- Always generate the HTML card — even on PASS

## Engine Commands Quick Ref

```bash
# Discovery
daz-betting-engine pev-events --sport {sport} --limit 10

# Full pipeline (PEV + SGM + HTML + ledger)
ODDS_API_KEY=*** daz-betting-engine assistant game --sport {sport} --event-id {id}

# PEV only
ODDS_API_KEY=*** daz-betting-engine game-pev --event-id {id} --sport {sport}

# SGM with long-shot (10-leg)
ODDS_API_KEY=*** daz-betting-engine sgm game --sport {sport} --event-id {id} \
  --bookmaker {bookmaker} --include-long-shot
```

## Data Sources

| Source | What | Access |
|--------|------|--------|
| Odds API | Live odds (h2h, spreads, totals) | `ODDS_API_KEY` env |
| Champion Data | NRL player stats, try data | `mc.championdata.com` |
| Zero Tackle | Team lists, late mail | Web fetch |
| Stats Insider | 10K sim predictions, try probs | Web fetch |
| Betseeker | ATS trends, SGM picks | Web fetch |
| Before You Bet | Form analysis, totals | Web fetch |
| GoBet | Expert picks | Web fetch |
| Dimers | ML predictions | Web fetch |
| ~/wiki/ | Pythago model, strategy | Local filesystem |
