# TOOLS.md — Nutz Local Notes

## API Keys

- **The Odds API:** `ODDS_API_KEY` (set in environment at `/home/daz/.openclaw/.env`)
- Regions: `au` for Australian bookmakers, `us` for US books
- Base URL: `https://api.the-odds-api.com/v4/`

## BABS

- Library: `/home/daz/babs/`
- Quick start:
  ```python
  async with babs.Client() as client:
      resp = await client.get(url="https://...", schema=...)
  ```
- Auto-escalates: cache → HTTP → browser → stealth → LLM
- curl_cffi transport for bookmaker scraping (chrome120 impersonation)

## Sportsbet Scrape

- Use BABS curl_cffi with chrome120 impersonation
- Extract `window.__PRELOADED_STATE__` from page HTML
- Parse `JSON.parse(...)` → `entities.sportsbook`
- Win price: `(num + den) / den`

## Champion Data (NRL)

- 2025: comp_id `12755`
- 2026: comp_id `12999`
- Fixtures: `GET https://mc.championdata.com/data/{comp_id}/fixture.json`
- Match data: `GET https://mc.championdata.com/data/{comp_id}/{match_id}.json`

## Ledger

- Path: `ledger/betting-journal.md`
- Template: Use the bet recommendation format from SOUL.md
- Post-audit every entry after match result

## SGM Engine Skill

- `~/.openclaw/workspace/skills/nrl-sgm-engine/SKILL.md`

## Group Context

- **Brudda Deez** supergroup: `-1003653936772` (Nutz + Daz)
- **Baccs** supergroup: `-1003843065763` (Nutz only)
- Both groups have Danny and David as decision-makers
