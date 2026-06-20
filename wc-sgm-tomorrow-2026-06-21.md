# World Cup 2026 — SGM Card (Tomorrow's Bets)

> **Alt-market lines are estimated**, not live. The Odds API cache only carries h2h markets. The SGM structures below use typical AU bookmaker pricing for tournament openers. **Verify each leg at the bookie before placing** — if a leg has moved more than 5-10%, recompute the combined odds manually.

**SGM lean matches:** 8  •  Bankroll not set (set BET_BANKROLL_AUD env var to show dollar amounts)

## Netherlands vs Sweden  —  HOME anchor @ 1.68  _(reference only)_

- **Kickoff:** Sun 21 Jun 03:00 AEST
- **Anchor:** home @ 1.68  (best h2h book: betfair_ex_au)
- **By-eye stake:** 0% of bankroll — no recommended bet, structure for reference
- **Why this lean:** WC v3 model says no edge on this SGM slate (best: -15.7%, threshold 5%). The model is calibrated against closing sharp lines; current Sportsbet openers typically overprice the favourite by 5-10% of margin. The line usually tightens into kickoff — re-check with `python -m daz_betting_engine.cli sgm-edges` (or `sgm-fire --min-edge=-5`) closer to kickoff.

### SGM structures

| SGM | Leg 1 | Leg 2 | Leg 3 | Combined | Implied | Anchor alone | SGM premium |
|-----|-------|-------|-------|----------|---------|--------------|-------------|
| Netherlands + Under 2.5 | **Netherlands Win** @ 1.68 | **Under 2.5** @ 1.70 | — | **3.06** | 32.7% | 1.68 | +7.1% |
| Netherlands + BTTS No (clean sheet) | **Netherlands Win** @ 1.68 | **BTTS No** @ 1.80 | — | **3.24** | 30.9% | 1.68 | +7.1% |
| Netherlands + Under 2.5 + BTTS No | **Netherlands Win** @ 1.68 | **Under 2.5** @ 1.70 | **BTTS No** @ 1.80 | **5.91** | 16.9% | 1.68 | +15.0% |
| Netherlands + HT Netherlands / FT Netherlands (wire-to-wire) | **Netherlands Win** @ 1.68 | **HT Home / FT Home** @ 2.30 | — | **4.13** | 24.2% | 1.68 | +6.9% |
| Netherlands + Over 9.5 Corners | **Netherlands Win** @ 1.68 | **Over 9.5 Corners** @ 2.27 | — | **4.19** | 23.9% | 1.68 | +9.9% |
| Netherlands + Under 3.5 Cards | **Netherlands Win** @ 1.68 | **Under 3.5 Cards** @ 2.33 | — | **4.31** | 23.2% | 1.68 | +10.1% |

**SGM premium** = the markup the book charges for combining legs. If the premium is < 30%, the SGM bonus is reasonable. If it's > 60%, the book is gouging and the anchor alone is a better play.

## Germany vs Ivory Coast  —  HOME anchor @ 1.60  _(reference only)_

- **Kickoff:** Sun 21 Jun 06:00 AEST
- **Anchor:** home @ 1.60  (best h2h book: betfair_ex_au)
- **By-eye stake:** 0% of bankroll — no recommended bet, structure for reference
- **Why this lean:** WC v3 model says no edge on this SGM slate (best: -19.2%, threshold 5%). The model is calibrated against closing sharp lines; current Sportsbet openers typically overprice the favourite by 5-10% of margin. The line usually tightens into kickoff — re-check with `python -m daz_betting_engine.cli sgm-edges` (or `sgm-fire --min-edge=-5`) closer to kickoff.

### SGM structures

| SGM | Leg 1 | Leg 2 | Leg 3 | Combined | Implied | Anchor alone | SGM premium |
|-----|-------|-------|-------|----------|---------|--------------|-------------|
| Germany + Under 2.5 | **Germany Win** @ 1.60 | **Under 2.5** @ 1.70 | — | **2.91** | 34.4% | 1.60 | +7.0% |
| Germany + BTTS No (clean sheet) | **Germany Win** @ 1.60 | **BTTS No** @ 1.80 | — | **3.08** | 32.5% | 1.60 | +6.9% |
| Germany + Under 2.5 + BTTS No | **Germany Win** @ 1.60 | **Under 2.5** @ 1.70 | **BTTS No** @ 1.80 | **5.63** | 17.8% | 1.60 | +15.0% |
| Germany + HT Germany / FT Germany (wire-to-wire) | **Germany Win** @ 1.60 | **HT Home / FT Home** @ 2.30 | — | **3.94** | 25.4% | 1.60 | +7.1% |
| Germany + Over 9.5 Corners | **Germany Win** @ 1.60 | **Over 9.5 Corners** @ 2.27 | — | **4.00** | 25.0% | 1.60 | +10.1% |
| Germany + Under 3.5 Cards | **Germany Win** @ 1.60 | **Under 3.5 Cards** @ 2.33 | — | **4.10** | 24.4% | 1.60 | +10.0% |

**SGM premium** = the markup the book charges for combining legs. If the premium is < 30%, the SGM bonus is reasonable. If it's > 60%, the book is gouging and the anchor alone is a better play.

## Ecuador vs Curaçao  —  HOME anchor @ 1.21  _(reference only)_

- **Kickoff:** Sun 21 Jun 10:00 AEST
- **Anchor:** home @ 1.21  (best h2h book: betfair_ex_au)
- **By-eye stake:** 0% of bankroll — no recommended bet, structure for reference
- **Why this lean:** WC v3 model says no edge on this SGM slate (best: -42.9%, threshold 5%). The model is calibrated against closing sharp lines; current Sportsbet openers typically overprice the favourite by 5-10% of margin. The line usually tightens into kickoff — re-check with `python -m daz_betting_engine.cli sgm-edges` (or `sgm-fire --min-edge=-5`) closer to kickoff.

### SGM structures

| SGM | Leg 1 | Leg 2 | Leg 3 | Combined | Implied | Anchor alone | SGM premium |
|-----|-------|-------|-------|----------|---------|--------------|-------------|
| Ecuador + Under 2.5 | **Ecuador Win** @ 1.21 | **Under 2.5** @ 1.55 | — | **2.01** | 49.8% | 1.21 | +7.2% |
| Ecuador + BTTS No (clean sheet) | **Ecuador Win** @ 1.21 | **BTTS No** @ 1.60 | — | **2.07** | 48.3% | 1.21 | +6.9% |
| Ecuador + Under 2.5 + BTTS No | **Ecuador Win** @ 1.21 | **Under 2.5** @ 1.55 | **BTTS No** @ 1.60 | **3.45** | 29.0% | 1.21 | +15.0% |
| Ecuador + HT Ecuador / FT Ecuador (wire-to-wire) | **Ecuador Win** @ 1.21 | **HT Home / FT Home** @ 1.80 | — | **2.33** | 42.9% | 1.21 | +7.0% |
| Ecuador + Over 9.5 Corners | **Ecuador Win** @ 1.21 | **Over 9.5 Corners** @ 2.91 | — | **3.87** | 25.8% | 1.21 | +9.9% |
| Ecuador + Under 3.5 Cards | **Ecuador Win** @ 1.21 | **Under 3.5 Cards** @ 2.76 | — | **3.67** | 27.3% | 1.21 | +9.9% |

**SGM premium** = the markup the book charges for combining legs. If the premium is < 30%, the SGM bonus is reasonable. If it's > 60%, the book is gouging and the anchor alone is a better play.

## Tunisia vs Japan  —  AWAY anchor @ 1.72  _(reference only)_

- **Kickoff:** Sun 21 Jun 14:00 AEST
- **Anchor:** away @ 1.72  (best h2h book: betfair_ex_au)
- **By-eye stake:** 0% of bankroll — no recommended bet, structure for reference
- **Why this lean:** WC v3 model says no edge on this SGM slate (best: -56.8%, threshold 5%). The model is calibrated against closing sharp lines; current Sportsbet openers typically overprice the favourite by 5-10% of margin. The line usually tightens into kickoff — re-check with `python -m daz_betting_engine.cli sgm-edges` (or `sgm-fire --min-edge=-5`) closer to kickoff.

### SGM structures

| SGM | Leg 1 | Leg 2 | Leg 3 | Combined | Implied | Anchor alone | SGM premium |
|-----|-------|-------|-------|----------|---------|--------------|-------------|
| Japan + Under 2.5 | **Japan Win** @ 1.72 | **Under 2.5** @ 1.70 | — | **3.13** | 31.9% | 1.72 | +7.0% |
| Japan + Over 9.5 Corners | **Japan Win** @ 1.72 | **Over 9.5 Corners** @ 2.27 | — | **4.29** | 23.3% | 1.72 | +9.9% |

**SGM premium** = the markup the book charges for combining legs. If the premium is < 30%, the SGM bonus is reasonable. If it's > 60%, the book is gouging and the anchor alone is a better play.

## Spain vs Saudi Arabia  —  HOME anchor @ 1.12  _(reference only)_

- **Kickoff:** Mon 22 Jun 02:00 AEST
- **Anchor:** home @ 1.12  (best h2h book: betfair_ex_au)
- **By-eye stake:** 0% of bankroll — no recommended bet, structure for reference
- **Why this lean:** WC v3 model says no edge on this SGM slate (best: -43.6%, threshold 5%). The model is calibrated against closing sharp lines; current Sportsbet openers typically overprice the favourite by 5-10% of margin. The line usually tightens into kickoff — re-check with `python -m daz_betting_engine.cli sgm-edges` (or `sgm-fire --min-edge=-5`) closer to kickoff.

### SGM structures

| SGM | Leg 1 | Leg 2 | Leg 3 | Combined | Implied | Anchor alone | SGM premium |
|-----|-------|-------|-------|----------|---------|--------------|-------------|
| Spain + Under 2.5 | **Spain Win** @ 1.12 | **Under 2.5** @ 1.55 | — | **1.86** | 53.8% | 1.12 | +7.1% |
| Spain + BTTS No (clean sheet) | **Spain Win** @ 1.12 | **BTTS No** @ 1.60 | — | **1.92** | 52.1% | 1.12 | +7.1% |
| Spain + Under 2.5 + BTTS No | **Spain Win** @ 1.12 | **Under 2.5** @ 1.55 | **BTTS No** @ 1.60 | **3.19** | 31.4% | 1.12 | +14.8% |
| Spain + HT Spain / FT Spain (wire-to-wire) | **Spain Win** @ 1.12 | **HT Home / FT Home** @ 1.80 | — | **2.16** | 46.3% | 1.12 | +7.1% |
| Spain + Over 9.5 Corners | **Spain Win** @ 1.12 | **Over 9.5 Corners** @ 2.91 | — | **3.59** | 27.9% | 1.12 | +10.2% |
| Spain + Under 3.5 Cards | **Spain Win** @ 1.12 | **Under 3.5 Cards** @ 2.76 | — | **3.40** | 29.4% | 1.12 | +10.0% |

**SGM premium** = the markup the book charges for combining legs. If the premium is < 30%, the SGM bonus is reasonable. If it's > 60%, the book is gouging and the anchor alone is a better play.

## Belgium vs Iran  —  HOME anchor @ 1.42  _(reference only)_

- **Kickoff:** Mon 22 Jun 05:00 AEST
- **Anchor:** home @ 1.42  (best h2h book: betfair_ex_au)
- **By-eye stake:** 0% of bankroll — no recommended bet, structure for reference
- **Why this lean:** WC v3 model says no edge on this SGM slate (best: -28.4%, threshold 5%). The model is calibrated against closing sharp lines; current Sportsbet openers typically overprice the favourite by 5-10% of margin. The line usually tightens into kickoff — re-check with `python -m daz_betting_engine.cli sgm-edges` (or `sgm-fire --min-edge=-5`) closer to kickoff.

### SGM structures

| SGM | Leg 1 | Leg 2 | Leg 3 | Combined | Implied | Anchor alone | SGM premium |
|-----|-------|-------|-------|----------|---------|--------------|-------------|
| Belgium + Under 2.5 | **Belgium Win** @ 1.42 | **Under 2.5** @ 1.70 | — | **2.58** | 38.8% | 1.42 | +6.9% |
| Belgium + BTTS No (clean sheet) | **Belgium Win** @ 1.42 | **BTTS No** @ 1.80 | — | **2.73** | 36.6% | 1.42 | +6.8% |
| Belgium + Under 2.5 + BTTS No | **Belgium Win** @ 1.42 | **Under 2.5** @ 1.70 | **BTTS No** @ 1.80 | **5.00** | 20.0% | 1.42 | +15.1% |
| Belgium + HT Belgium / FT Belgium (wire-to-wire) | **Belgium Win** @ 1.42 | **HT Home / FT Home** @ 2.30 | — | **3.49** | 28.6% | 1.42 | +6.9% |
| Belgium + Over 9.5 Corners | **Belgium Win** @ 1.42 | **Over 9.5 Corners** @ 2.27 | — | **3.55** | 28.2% | 1.42 | +10.1% |
| Belgium + Under 3.5 Cards | **Belgium Win** @ 1.42 | **Under 3.5 Cards** @ 2.33 | — | **3.64** | 27.5% | 1.42 | +10.0% |

**SGM premium** = the markup the book charges for combining legs. If the premium is < 30%, the SGM bonus is reasonable. If it's > 60%, the book is gouging and the anchor alone is a better play.

## Uruguay vs Cape Verde  —  HOME anchor @ 1.45  _(reference only)_

- **Kickoff:** Mon 22 Jun 08:00 AEST
- **Anchor:** home @ 1.45  (best h2h book: betfair_ex_au)
- **By-eye stake:** 0% of bankroll — no recommended bet, structure for reference
- **Why this lean:** WC v3 model says no edge on this SGM slate (best: -32.4%, threshold 5%). The model is calibrated against closing sharp lines; current Sportsbet openers typically overprice the favourite by 5-10% of margin. The line usually tightens into kickoff — re-check with `python -m daz_betting_engine.cli sgm-edges` (or `sgm-fire --min-edge=-5`) closer to kickoff.

### SGM structures

| SGM | Leg 1 | Leg 2 | Leg 3 | Combined | Implied | Anchor alone | SGM premium |
|-----|-------|-------|-------|----------|---------|--------------|-------------|
| Uruguay + Under 2.5 | **Uruguay Win** @ 1.45 | **Under 2.5** @ 1.70 | — | **2.64** | 37.9% | 1.45 | +7.1% |
| Uruguay + BTTS No (clean sheet) | **Uruguay Win** @ 1.45 | **BTTS No** @ 1.60 | — | **2.48** | 40.3% | 1.45 | +6.9% |
| Uruguay + Under 2.5 + BTTS No | **Uruguay Win** @ 1.45 | **Under 2.5** @ 1.70 | **BTTS No** @ 1.60 | **4.54** | 22.0% | 1.45 | +15.1% |
| Uruguay + HT Uruguay / FT Uruguay (wire-to-wire) | **Uruguay Win** @ 1.45 | **HT Home / FT Home** @ 2.30 | — | **3.57** | 28.0% | 1.45 | +7.0% |
| Uruguay + Over 9.5 Corners | **Uruguay Win** @ 1.45 | **Over 9.5 Corners** @ 2.27 | — | **3.62** | 27.6% | 1.45 | +10.0% |
| Uruguay + Under 3.5 Cards | **Uruguay Win** @ 1.45 | **Under 3.5 Cards** @ 2.33 | — | **3.72** | 26.9% | 1.45 | +10.1% |

**SGM premium** = the markup the book charges for combining legs. If the premium is < 30%, the SGM bonus is reasonable. If it's > 60%, the book is gouging and the anchor alone is a better play.

## New Zealand vs Egypt  —  AWAY anchor @ 1.80  _(reference only)_

- **Kickoff:** Mon 22 Jun 11:00 AEST
- **Anchor:** away @ 1.80  (best h2h book: betfair_ex_au)
- **By-eye stake:** 0% of bankroll — no recommended bet, structure for reference
- **Why this lean:** WC v3 model says no edge on this SGM slate (best: -54.7%, threshold 5%). The model is calibrated against closing sharp lines; current Sportsbet openers typically overprice the favourite by 5-10% of margin. The line usually tightens into kickoff — re-check with `python -m daz_betting_engine.cli sgm-edges` (or `sgm-fire --min-edge=-5`) closer to kickoff.

### SGM structures

| SGM | Leg 1 | Leg 2 | Leg 3 | Combined | Implied | Anchor alone | SGM premium |
|-----|-------|-------|-------|----------|---------|--------------|-------------|
| Egypt + Under 2.5 | **Egypt Win** @ 1.80 | **Under 2.5** @ 1.85 | — | **3.56** | 28.1% | 1.80 | +6.9% |
| Egypt + Over 9.5 Corners | **Egypt Win** @ 1.80 | **Over 9.5 Corners** @ 1.80 | — | **3.56** | 28.1% | 1.80 | +9.9% |

**SGM premium** = the markup the book charges for combining legs. If the premium is < 30%, the SGM bonus is reasonable. If it's > 60%, the book is gouging and the anchor alone is a better play.

---

**How to use this card:**
1. For each lean, pick the SGM structure with the lowest SGM premium that's still meaningful.
2. Pull the live h2h, totals, and BTTS lines from your bookie app for the match.
3. If the live combined odds are within 5% of the estimate, the structure is liveable.
4. If a leg has moved > 10%, recompute by hand using the new live odds.
5. If the bookie is offering a 'Bonus Back if 1 leg fails' promo (Neds / Sportsbet typical), the SGM premium is effectively refunded on a 1-leg fail. **That's the play.**
