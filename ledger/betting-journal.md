# 🥜 Nutz Betting Journal

> Master ledger. Every recommended bet logged before kickoff, reconciled after.
> Performance doesn't lie — the ledger proves it.

### AUS-TUR-ARB-20260614
**Date:** 2026-06-14
**Match:** Australia vs Türkiye — World Cup Group D
**Type:** Promo Arbitrage (Betr Early Payout + Betfair Lay)
**Stake:** $50 Betr Back + $42.60 Betfair Lay = $92.60 deployed
**Odds:** Betr $5.00 (Back) / Betfair $5.70 (Lay)
**Edge:** Promo middle — Australia scores first + doesn't win = both sides cash
**Confidence:** High 🟢 (promo arb)
**Bookmaker:** Betr + Betfair
**Reasoning:** Betr promo pays Australia as winner if they score first. Betfair lay at $5.70 covers if they don't win. 4-scenario matrix: max win +$240.47 (Aus scores 1st, doesn't win), max loss -$9.53 (Aus never scores 1st, doesn't win), near-breakeven on other 2.
**Status:** PENDING
**Result:** ❓
**P&L:** ±$0.00
**Audit Note:** Betr promo cap $200 winnings. Lay price drifted from $5.80 → $5.70 before placement. Liability $200.22.

### NYK-SAS-SGM-20260614
**Date:** 2026-06-14
**Match:** Knicks @ Spurs — NBA Finals Game 5
**Type:** SGM (3-leg player props)
**Stake:** $50 ($50 bet return multi)
**Odds:** 6.75
**Bookmaker:** Sportsbet
**Edge:** +32.3% (estimated fair ~19.6%, implied 14.8%)
**Confidence:** Medium 🟡
**Promo:** Bet Return — ANY legs fail = $50 Bonus Bet back
**Reasoning:**
- KAT O16.5: Foul trouble killed G4 (13pts in limited mins). Model bounce-back 18.7+, better line than initial 17.5 float
- Castle O15.5: 14/18 home games cleared 14.5, avg 17.6 at Frost Bank
- Wemby O28.5: Elim game, extra day rest, projections to 29. The alien delivers
- Positive correlation: all three hitting = high-scoring game flow
- Bet Return insurance makes this near-freeroll

**Status:** PENDING
**Result:** ❓
**P&L:** ±$0.00
**Bet ID:** 0/3841547/0000034/D
**Audit Note:** Manual SGM build — NBA not supported by engine SGM. Expert sources: Covers (SGP template), OddsShark prop trends. Lines adjusted from initial model — KAT better (16.5 vs 17.5), Castle/Wemby slightly tougher (15.5/28.5 vs 14.5/27.5). Bet Return promo reduces effective risk to ~$0 EV.

## Bankroll Tracker

| Date | Bankroll | Change | Notes |
|------|----------|--------|-------|
| — | — | — | Start tracking from first session |

## Betting Records

### 2026-06-13

### EEL-CAN-SGM-20260613
**Date:** 2026-06-13
**Match:** Eels vs Raiders R15
**Type:** SGM (2-leg)
**Stake:** $20
**Odds:** 3.65
**Edge:** +31.5%
**Confidence:** High 🟢
**Reasoning:** Eels +2.5 + Under 48.5. Full 8-factor engine (3-season weighted, Moses-adjusted) gives Eels 69.2% WP, total ~34.1. Under edge +32.6%. Raiders + Under SGM is engine-negative (-5.0%). Engine overrules 5/6 experts who missed Moses impact and overvalued Raiders roster.
**Status:** PENDING
**Result:** ❓
**P&L:** ±$0.00
**Audit Note:**

### NYK-SAS-SGM-20260613
**Date:** 2026-06-13
**Match:** Knicks @ Spurs NBA Finals G5
**Type:** SGM (3-leg)
**Stake:** $50 (Sportsbet bonus bet back insured)
**Odds:** ~6.82
**Edge:** Positive (insurance-adjusted)
**Confidence:** Medium-High 🟡
**Reasoning:** Knicks +5.5 (3-0 ATS road closeouts) + Under 216.5 (SportsLine 213 proj, 3-1 in series) + KAT O16.5 (Covers projects 18.7, 19.5 avg in SA). Insurance = bonus bet back if loses.
**Status:** PENDING
**Result:** ❓
**P&L:** ±$0.00
**Audit Note:**

---

## Performance Summary

| Metric | Value | Target |
|--------|-------|--------|
| Win Rate | — | >55% |
| ROI | — | >5% |
| Avg Edge | — | >5% |
| CLV | — | >0 (positive) |
| Bets Tracked | 0 | — |
| Kelly Efficiency | — | 0.5-1.0 |

---

## Legend

- **Status:** PENDING / WON / LOST / VOID
- **Confidence:** High 🟢 / Medium 🟡 / Low 🟠
- **Edge threshold:** <3% = pass, 3-5% = consider, >5% = value
- **Staking:** Kelly (full), ½ Kelly (conservative), flat (% of bankroll)
