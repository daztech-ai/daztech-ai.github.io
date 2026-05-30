// Theme sync — cards default to dark, but respect hub's light mode toggle
(function() {
  const theme = localStorage.getItem('daztech-theme');
  if (theme !== 'light') return; // Default dark — nothing to do

  // Inject light theme overrides
  const style = document.createElement('style');
  style.id = 'daztech-light-theme';
  style.textContent = `
    /* Light theme override */
    body { background: #faf7f2 !important; color: #2d2922 !important; }

    /* Override common surface/container colors */
    [style*="background:#0a0a0f"], [style*="background: #0a0a0f"],
    .container, .card, .pick, .section, .match-card, .meeting,
    .sgm-row, .header-bar, .status-bar, .tip-card, .race-pick,
    div[style*="background:#12121a"], div[style*="background: #12121a"],
    div[style*="background:#111118"], div[style*="background: #111118"],
    div[style*="background:#0d0d14"], div[style*="background: #0d0d14"] {
      background: #ffffff !important;
      color: #2d2922 !important;
      border-color: #e8e4dc !important;
    }

    /* Muted/secondary text */
    [style*="color:#777"], [style*="color: #777"],
    [style*="color:#888"], [style*="color: #888"],
    [style*="color:#999"], [style*="color: #999"] {
      color: #8c8880 !important;
    }

    /* Gold accents — keep warm */
    [style*="color:#ffd700"], [style*="color: #ffd700"] {
      color: #c8960c !important;
    }

    /* Gold borders */
    [style*="border-color:#ffd700"], [style*="border-color: #ffd700"],
    [style*="border: 2px solid #ffd700"] {
      border-color: #c8960c !important;
    }

    /* Links */
    a { color: #c8960c !important; }

    /* Green/live accents */
    [style*="color:#00ff88"], [style*="color: #00ff88"] {
      color: #16a34a !important;
    }
  `;
  document.head.appendChild(style);

  // Listen for theme changes from other tabs
  window.addEventListener('storage', function(e) {
    if (e.key === 'daztech-theme') {
      location.reload();
    }
  });
})();
