# WC Model Edge Picks — Sat 20 Jun 2026

**13 confident picks today**, **13 total across the slate** (0 with ≥1 unknown team). Expected ROI **+13.8%** (LOTO-CV backtest).

**Total recommended stake:** 13 × 1% = **13%** of bankroll ($130 of $1000 AUD)

> **Model:** WC v3 international Poisson + isotonic calibrator (LOTO-CV on 2014/2018/2022). Edge ≥ 5% to fire a pick. Stake is **1% of bankroll per pick** (forward-test conservative size — see scripts/forward_test_wc.py).

## Confident picks (both teams known to model)

These are the actionable picks. The calibrated model has specific attack/defence parameters for both teams.

| Match | Kickoff (AEST) | Pick | Model Prob | Best Odds | Edge | Stake | Status |
|-------|----------------|------|------------|-----------|------|-------|--------|
| Tunisia vs Japan | Sun 21 Jun 14:00 AEST | H | 28.3% | 7.40 | +14.8% | 1% ($10) | pending |
| Spain vs Saudi Arabia | Mon 22 Jun 02:00 AEST | A | 21.1% | 29.00 | +17.7% | 1% ($10) | pending |
| Belgium vs Iran | Mon 22 Jun 05:00 AEST | A | 21.1% | 8.20 | +8.9% | 1% ($10) | pending |
| England vs Ghana | Wed 24 Jun 06:00 AEST | A | 21.1% | 16.00 | +14.9% | 1% ($10) | pending |
| Panama vs Croatia | Wed 24 Jun 09:00 AEST | D | 29.4% | 4.20 | +5.6% | 1% ($10) | pending |
| Bosnia & Herzegovina vs Qatar | Thu 25 Jun 05:00 AEST | A | 21.2% | 7.40 | +7.7% | 1% ($10) | pending |
| Switzerland vs Canada | Thu 25 Jun 05:00 AEST | A | 48.7% | 3.35 | +18.8% | 1% ($10) | pending |
| Japan vs Sweden | Fri 26 Jun 09:00 AEST | A | 53.4% | 3.40 | +24.0% | 1% ($10) | pending |
| Tunisia vs Netherlands | Fri 26 Jun 09:00 AEST | D | 29.4% | 5.90 | +12.4% | 1% ($10) | pending |
| Uruguay vs Spain | Sat 27 Jun 10:00 AEST | H | 28.3% | 6.25 | +12.3% | 1% ($10) | pending |
| Egypt vs Iran | Sat 27 Jun 13:00 AEST | A | 46.4% | 3.92 | +20.8% | 1% ($10) | pending |
| Panama vs England | Sun 28 Jun 07:00 AEST | D | 29.4% | 7.20 | +15.5% | 1% ($10) | pending |
| Colombia vs Portugal | Sun 28 Jun 09:30 AEST | H | 58.7% | 3.70 | +31.7% | 1% ($10) | pending |

### Per-bucket breakdown

| Bucket | Edge range | Confident picks | Backtest ROI (LOTO) |
|--------|------------|----------------:|--------------------:|
| low | 5–10% | 3 | +15.21% |
| medium | 10–15% | 4 | +16.26% |
| high | 15–20% | 3 | +10.84% |
| very_high | 20%+ | 3 | +11.94% |

---

**Notes for Daz:**
- Card is read-only. No bets are placed automatically.
- Confident picks are sorted by kickoff time (earliest first).
- Stake column shows the ledger's recommended % of bankroll and the dollar amount (on a $1000 bankroll). Adjust the dollar amount to your actual bankroll.
- 'Best odds' is the best decimal price across all bookmakers in the local odds cache — Betfair AU is the typical sharp book in our cache. Compare to your bookie apps before placing.
- The 'Pick' column is the outcome the model has the largest edge on (Home / Draw / Away). The other two outcomes are also scored but the card shows the best one.
- Re-run anytime with `python -m daz_betting_engine.cards.wc_model_edge --date YYYY-MM-DD`.