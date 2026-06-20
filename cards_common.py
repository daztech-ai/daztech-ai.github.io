"""Shared rendering helpers for all Daz Betting Engine cards.

Every card (wc_model_edge, wc_tomorrow, sgm_tomorrow, nrl_tomorrow,
wc_player_props, my_offers, rebirth_summary) renders through this shell
so the visual system stays consistent.

The shell returns a full HTML document that links to `cards.css` (served
from daztech-pages, copied into the engine at cards/cards.css for tests).
Adding a new card = writing a thin module that computes the body HTML and
calls ``render_shell(...)``.

See ``docs/card-design-system-2026-06-20.md`` for the spec.
"""
from __future__ import annotations

import html as _html
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

# Path to the shared CSS — sibling of this file, shipped with the engine
# for tests, mirrored to ~/.openclaw/workspace-baccs/cards.css for prod.
_CSS_PATH = Path(__file__).parent / "cards.css"

# Where the live CSS lives for the rendered cards (Cloudflare worker).
PROD_CSS_HREF = "cards.css"


def _css_link(href: str = PROD_CSS_HREF) -> str:
    """Return the <link> tag for the shared design system CSS."""
    return f'<link rel="stylesheet" href="{_html.escape(href)}" />'


def _esc(s: object) -> str:
    """HTML-escape a value (text content or attribute).

    We escape angle brackets, ampersands, and double quotes
    (which can break out of attributes), but leave single quotes
    alone so contractions like Danny's and Tomorrow's render
    naturally. This matches what most static-site generators do.
    """
    return _html.escape(str(s), quote=False)


# ---- Edge-to-tier classification -----------------------------------------


def tier_for_edge(edge_pct: float) -> str:
    """Map an edge percentage to a tier label.

    Thresholds match the design system spec (Atlas research, 2026-06-19):
      edge >= 10%     -> "lock"
      edge >=  5%     -> "back"
      edge >=  0%     -> "watch"
      edge >= -3%     -> "watch"   (small negative still shown for transparency)
      edge <  -3%     -> "fade"
    """
    if edge_pct >= 10.0:
        return "lock"
    if edge_pct >= 5.0:
        return "back"
    if edge_pct >= -3.0:
        return "watch"
    return "fade"


def edge_class(tier: str) -> str:
    """CSS class for the edge number, by tier."""
    return {
        "lock": "edge-strong",
        "back": "edge-mid",
        "watch": "edge-weak",
        "fade": "edge-fade",
    }.get(tier, "edge-weak")


def pill_class(tier: str) -> str:
    """CSS class for the tier pill."""
    return {
        "lock": "pill pill-lock",
        "back": "pill pill-back",
        "watch": "pill pill-watch",
        "fade": "pill pill-fade",
        "boost": "pill pill-boost",
    }.get(tier, "pill pill-watch")


# ---- Track record / hero stat blocks -------------------------------------


@dataclass
class TrackStat:
    """One cell in the 4-up track record strip."""
    label: str
    value: str
    tone: str = ""  # "" (default accent), "good", "warn", "bad"


def render_track_record(stats: Sequence[TrackStat]) -> str:
    """Render a 4-up metrics strip (ROI / hit rate / Brier / sample)."""
    if not stats:
        return ""
    cells = []
    for s in stats:
        cls = f"value {_html.escape(s.tone)}" if s.tone else "value"
        cells.append(
            f'<div class="metric"><span class="{cls}">{_esc(s.value)}</span>'
            f'<span class="label">{_esc(s.label)}</span></div>'
        )
    return f'<div class="track-record">{"".join(cells)}</div>'


def render_hero_strip(stats: Sequence[tuple[str, str, str]]) -> str:
    """Render inline hero stats (label, value, tone).

    Each tuple is (label, value, tone_class) where tone_class is one of
    "good", "warn", "bad", or "".
    """
    if not stats:
        return ""
    cells = []
    for label, value, tone in stats:
        cls = f"val {_html.escape(tone)}" if tone else "val"
        cells.append(
            f'<div class="hero-stat"><span class="lbl">{_esc(label)}</span>'
            f'<span class="{cls}">{_esc(value)}</span></div>'
        )
    return f'<div class="hero-stats">{"".join(cells)}</div>'


# ---- Pick / offer card primitives ----------------------------------------


@dataclass
class PickRow:
    """A single pick/fixture card row.

    Used by the WC model edge, SGM, and NRL cards. The renderer fills in
    the tier pill, edge number, and book/stake footer from these fields.
    """
    match: str               # "Tunisia vs Japan"
    kickoff: str             # "Sun 21 Jun 14:00 AEST"
    outcome: str             # "Tunisia (Home Win)" or "Over 2.5"
    edge_pct: float          # 0.148 -> +14.8%
    odds: float | None = None
    bookmaker: str = "sportsbet"
    stake_pct: float = 0.0
    bankroll_aud: float = 1000.0
    market_prob: float | None = None
    model_prob: float | None = None
    cta_url: str = ""        # deep link to the bookie (optional)

    def tier(self) -> str:
        return tier_for_edge(self.edge_pct)

    def stake_aud(self) -> float:
        return round(self.stake_pct * self.bankroll_aud, 2)

    def stake_str(self) -> str:
        if self.stake_pct <= 0:
            return "\u2014 no bet \u2014"
        aud = self.stake_aud()
        pct = f"{self.stake_pct:.0%}"
        return f"{pct} (${aud:,.0f})"

    def edge_str(self) -> str:
        return f"{self.edge_pct:+.1f}%"

    def model_str(self) -> str:
        if self.model_prob is None:
            return ""
        return f"{self.model_prob:.0%}"

    def odds_str(self) -> str:
        if self.odds is None:
            return ""
        return f"{self.odds:.2f}"


def render_pick_card(p: PickRow) -> str:
    """Render one pick/fixture card using the unified design system.

    Returns a full <article class="pick-card" data-tier="...">...</article>
    block ready to drop inside the shell body.
    """
    tier = p.tier()
    pill = pill_class(tier)
    edge_cls = edge_class(tier)
    book = _esc(p.bookmaker) if p.bookmaker else ""
    model_html = (
        f'<span class="t-sm muted">Model <strong class="accent">{p.model_str()}</strong></span>'
        if p.model_prob is not None else ""
    )
    odds_html = (
        f'<span class="t-sm muted">Odds <strong class="mono">{p.odds_str()}</strong></span>'
        if p.odds is not None else ""
    )
    cta_html = (
        f'<a class="cta" href="{_esc(p.cta_url)}" target="_blank" rel="noopener">Place bet \u2192</a>'
        if p.cta_url else ""
    )
    return f"""
<article class="pick-card" data-tier="{tier}">
  <div class="pick-head">
    <div>
      <div class="t-xs muted">{_esc(p.kickoff)}</div>
      <div class="t-lg" style="margin-top:.15rem">{_esc(p.match)}</div>
      <div class="t-sm muted" style="margin-top:.15rem">{_esc(p.outcome)}</div>
    </div>
    <div class="tier-edge {edge_cls}">{p.edge_str()}</div>
  </div>
  <div class="pick-foot">
    <span class="{pill}">{tier.title()} \u00b7 {p.edge_str()}</span>
    {f'<span class="book">{book}</span>' if book else ''}
    {model_html}
    {odds_html}
    <span class="stake accent" style="margin-left:auto">{_esc(p.stake_str())}</span>
    {cta_html}
  </div>
</article>""".strip()


# ---- Top-level shell -----------------------------------------------------


@dataclass
class ShellConfig:
    """Configuration for the document shell."""
    title: str                              # <title> and <h1> base
    subtitle: str = ""                      # small line under h1
    body_html: str = ""                     # the card content
    track_record: Sequence[TrackStat] = field(default_factory=list)
    hero_stats: Sequence[tuple[str, str, str]] = field(default_factory=list)
    banner: str = ""                        # optional top-of-body banner
    badges: Sequence[tuple[str, str]] = field(default_factory=list)
    footer: str = ""                        # custom footer HTML (else default)
    css_href: str = PROD_CSS_HREF
    meta_description: str = ""


def render_shell(cfg: ShellConfig) -> str:
    """Render a full HTML document using the unified design system.

    Layout (top to bottom):
      - header.strip: subtitle (small) + h1 (title) + badges
      - optional hero stats (inline row)
      - optional track record (4-up metrics)
      - optional banner
      - body_html (the cards / tables / picks)
      - default or custom footer
    """
    badges_html = "".join(
        f'<span class="badge {cls}">{_esc(text)}</span>'
        for text, cls in cfg.badges
    )
    hero_html = render_hero_strip(cfg.hero_stats) if cfg.hero_stats else ""
    tr_html = render_track_record(cfg.track_record) if cfg.track_record else ""
    banner_html = (
        f'<div class="banner">{cfg.banner}</div>' if cfg.banner else ""
    )
    subtitle_html = (
        f'<div class="t-xs muted" style="margin-bottom:.25rem">{_esc(cfg.subtitle)}</div>'
        if cfg.subtitle else ""
    )
    footer_html = cfg.footer if cfg.footer else (
        '<footer><p>Generated by <code>daz_betting_engine.cards</code>. '
        'Place bets at your own risk. Odds move; verify lines at the bookie.</p></footer>'
    )
    meta_html = (
        f'<meta name="description" content="{_esc(cfg.meta_description)}" />'
        if cfg.meta_description else ""
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  {_esc_str(cfg.title)}
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  {meta_html}
  {_css_link(cfg.css_href)}
</head>
<body>
<main class="container">
  <header class="strip">
    <div>
      {subtitle_html}
      <h1 class="t-xl">{_esc(cfg.title)}</h1>
    </div>
    {badges_html}
  </header>
  {hero_html}
  {tr_html}
  {banner_html}
  {cfg.body_html}
  {footer_html}
</main>
</body>
</html>
"""


def _esc_str(s: str) -> str:
    """Build a <title> tag from a string (escaped)."""
    return f"<title>{_esc(s)}</title>"


# ---- Convenience: build a list of PickRow + render -----------------------


def render_pick_list(
    picks: Sequence[PickRow],
    *,
    container: bool = True,
) -> str:
    """Render a list of PickRow cards.

    If ``container`` is True, wraps in a <div> (default). Otherwise just
    concatenates the card blocks.
    """
    body = "\n".join(render_pick_card(p) for p in picks)
    if not body:
        return '<div class="empty"><h2>No picks today</h2><p>Model found no edge above threshold.</p></div>'
    if container:
        return f'<div class="pick-list">\n{body}\n</div>'
    return body
