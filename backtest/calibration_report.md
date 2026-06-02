# 30-Day Calibration Backtest — Daztech Betting Engine

**Generated:** 2026-06-02 08:38:15 UTC
**Ledger files processed:** 7

## Headline

- **Total bets:** 104 (21 settled, 83 pending)
- **Hit rate:** 38.1% (8 won / 13 lost)
- **Staked:** $24.25
- **Returned:** $44.28
- **P&L:** $+20.03
- **ROI:** +82.6%

## Edge Thresholds (reference)

- Racing: 8.0%
- Liquid sports: 5.0%

## By Sport

| Sport      | Bets | Settled | Won | Lost | Staked $ | Returned $ | P&L $ | ROI %   | Hit % | Avg Edge | Avg CLV |
|------------|------|---------|-----|------|----------|------------|-------|---------|-------|----------|---------|
| nba        | 13   | 13      | 6   | 7    | 16.25    | 26.28      | 10.03 | +61.7%  | 46.1% | 6.8%     | —       |
| nrl        | 63   | 0       | 0   | 0    | 0.00     | 0.00       | 0.00  | —       | —     | 0.4%     | —       |
| racing     | 18   | 8       | 2   | 6    | 8.00     | 18.00      | 10.00 | +125.0% | 25.0% | 11.4%    | +0.00%  |
| greyhounds | 10   | 0       | 0   | 0    | 0.00     | 0.00       | 0.00  | —       | —     | 18.5%    | —       |

## By Discipline (racing family)

| Discipline   | Bets | Settled | Won | Lost | Staked $ | P&L $ | ROI %   | Hit % |
|--------------|------|---------|-----|------|----------|-------|---------|-------|
| thoroughbred | 8    | 8       | 2   | 6    | 8.00     | 10.00 | +125.0% | 25.0% |
| greyhounds   | 10   | 0       | 0   | 0    | 0.00     | 0.00  | —       | —     |
| harness      | 10   | 0       | 0   | 0    | 0.00     | 0.00  | —       | —     |

## By Model Rating

| Rating   | Bets | Settled | Won | Lost | Staked $ | P&L $ | ROI %    | Hit %  |
|----------|------|---------|-----|------|----------|-------|----------|--------|
| STRONG   | 19   | 6       | 3   | 3    | 9.50     | 5.16  | +54.3%   | 50.0%  |
| MODERATE | 77   | 7       | 3   | 4    | 6.75     | 4.87  | +72.2%   | 42.9%  |
| 59.3     | 1    | 1       | 0   | 1    | 1.00     | -1.00 | -100.0%  | 0.0%   |
| 57.3     | 1    | 1       | 1   | 0    | 1.00     | 11.00 | +1100.0% | 100.0% |
| 50.5     | 1    | 1       | 1   | 0    | 1.00     | 5.00  | +500.0%  | 100.0% |
| 49.5     | 1    | 1       | 0   | 1    | 1.00     | -1.00 | -100.0%  | 0.0%   |
| 48.4     | 1    | 1       | 0   | 1    | 1.00     | -1.00 | -100.0%  | 0.0%   |
| 48.1     | 1    | 1       | 0   | 1    | 1.00     | -1.00 | -100.0%  | 0.0%   |
| 47.4     | 1    | 1       | 0   | 1    | 1.00     | -1.00 | -100.0%  | 0.0%   |
| 45.8     | 1    | 1       | 0   | 1    | 1.00     | -1.00 | -100.0%  | 0.0%   |

## By Edge Bucket

| Edge % | Bets | Settled | Won | Lost | Staked $ | P&L $ | ROI %   | Hit % |
|--------|------|---------|-----|------|----------|-------|---------|-------|
| 10-15% | 11   | 10      | 3   | 7    | 12.50    | 12.34 | +98.7%  | 30.0% |
| 5-10%  | 4    | 4       | 2   | 2    | 5.25     | 1.19  | +22.7%  | 50.0% |
| 0-5%   | 62   | 2       | 0   | 2    | 2.50     | -2.50 | -100.0% | 0.0%  |
| 15-20% | 10   | 0       | 0   | 0    | 0.00     | 0.00  | —       | —     |
| 20%+   | 1    | 0       | 0   | 0    | 0.00     | 0.00  | —       | —     |

## By Confidence Tier (top-10, mid 10-20, low 20+, unranked)

| Tier      | Bets | Settled | Won | Lost | Staked $ | P&L $ | ROI %   | Hit % |
|-----------|------|---------|-----|------|----------|-------|---------|-------|
| unranked  | 16   | 5       | 3   | 2    | 4.00     | 9.00  | +225.0% | 60.0% |
| top_10    | 37   | 16      | 5   | 11   | 20.25    | 11.03 | +54.5%  | 31.2% |
| mid_10_20 | 10   | 0       | 0   | 0    | 0.00     | 0.00  | —       | —     |
| low_20+   | 41   | 0       | 0   | 0    | 0.00     | 0.00  | —       | —     |

## CLV (Closing Line Value)

- **Bets with closing_odds set:** 0
- **No bets have `closing_odds` set in the window** — CLV analysis uncomputable from current data.
- Closing-odds capture is recommended in a follow-up card (out of scope here per scope doc).

## Source Files

- `2026-05-28_nba_ledger.json`
- `2026-05-29_nrl_ledger.json`
- `2026-05-29_racing_ledger.json`
- `2026-05-31_nba_ledger.json`
- `2026-05-31_nrl_ledger.json`
- `2026-06-01_daily.json`
- `2026-06-02_daily.json`

## Skipped Files (consolidated/duplicate)

- `all_ledgers.json` — would double-count primary ledger data

## Notes

- Stake and payout are taken at face value from the ledger (paper bets use `recommended_stake` as notional).
- Code normalisation maps `nrl_paper` → `nrl`, `racing_paper` → `racing`, `football_paper` → `football`.
- Edge bucket assignment uses the recorded `edge_pct` field; nulls are excluded from bucket tables.
- Confidence tier assigned per (date, code) by `edge_pct` desc — top 10 = rank 1-10 etc.
- This is a measurement artefact, not a model change. Re-runs are idempotent.
