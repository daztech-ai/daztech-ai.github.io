// cards.js — Daz Betting Engine bet slip
// Persistent bet slip on the right side of every card. Click any odds to
// add a leg. Slip survives page navigation via sessionStorage. Copy the
// slip to clipboard as a structured bet ticket for pasting into Sportsbet.

(function () {
  "use strict";

  var STORAGE_KEY = "daz_bet_slip_v1";

  /** Load slip from sessionStorage; return [] if missing/corrupt. */
  function loadSlip() {
    try {
      var raw = sessionStorage.getItem(STORAGE_KEY);
      if (!raw) return [];
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) {
      return [];
    }
  }

  function saveSlip(legs) {
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(legs));
    } catch (e) {
      // sessionStorage might be full or disabled; ignore
    }
  }

  function clearSlip() {
    saveSlip([]);
    render();
  }

  function addLeg(leg) {
    var legs = loadSlip();
    // Idempotency: same (event, market, selection) shouldn't be added twice
    var dup = legs.find(function (l) {
      return l.event === leg.event &&
             l.market === leg.market &&
             l.selection === leg.selection;
    });
    if (dup) return;
    legs.push(leg);
    saveSlip(legs);
    render();
  }

  function removeLeg(idx) {
    var legs = loadSlip();
    legs.splice(idx, 1);
    saveSlip(legs);
    render();
  }

  function combinedOdds(legs) {
    if (!legs.length) return 0;
    return legs.reduce(function (acc, l) { return acc * l.odds; }, 1);
  }

  function formatMoney(n) {
    return "$" + n.toFixed(2);
  }

  function buildSlipText(legs, stake) {
    if (!legs.length) return "Empty bet slip";
    var lines = [];
    lines.push("Daz Betting Engine — Bet Ticket");
    lines.push("Stake: " + formatMoney(stake) + " AUD");
    lines.push("Combined odds: " + combinedOdds(legs).toFixed(2));
    lines.push("Potential return: " + formatMoney(stake * combinedOdds(legs)));
    lines.push("---");
    legs.forEach(function (l, i) {
      lines.push("L" + (i + 1) + ": " + l.event);
      lines.push("    " + l.market + ": " + l.selection + " @ " + l.odds.toFixed(2));
    });
    if (legs.length > 1) {
      lines.push("---");
      lines.push("Type: " + (legs.length === 1 ? "Single" : legs.length + "-leg Multi"));
    }
    return lines.join("\n");
  }

  function render() {
    var legs = loadSlip();
    var slipEl = document.getElementById("bet-slip");
    if (!slipEl) return;
    var emptyEl = slipEl.querySelector(".slip-empty");
    var legsEl = slipEl.querySelector(".slip-legs");
    var combinedEl = slipEl.querySelector("#slip-combined");
    var stakeInput = slipEl.querySelector("#slip-stake");
    var returnEl = slipEl.querySelector("#slip-return");
    var copyBtn = slipEl.querySelector("#slip-copy");
    var clearBtn = slipEl.querySelector("#slip-clear");
    var countEl = slipEl.querySelector("#slip-count");

    var stake = parseFloat(stakeInput.value) || 0;
    var comb = combinedOdds(legs);

    if (countEl) countEl.textContent = legs.length;
    if (emptyEl) emptyEl.style.display = legs.length ? "none" : "block";
    if (combinedEl) combinedEl.textContent = legs.length ? comb.toFixed(2) : "—";
    if (returnEl) returnEl.textContent = legs.length ? formatMoney(stake * comb) : "—";

    if (legsEl) {
      legsEl.innerHTML = legs.map(function (l, i) {
        return '<li class="slip-leg">' +
          '<div class="slip-leg-head">' +
            '<span class="slip-leg-event">' + escapeHtml(l.event) + '</span>' +
            '<button class="slip-remove" data-idx="' + i + '" aria-label="Remove">×</button>' +
          '</div>' +
          '<div class="slip-leg-pick">' + escapeHtml(l.market) + ': ' + escapeHtml(l.selection) + '</div>' +
          '<div class="slip-leg-odds">@ ' + l.odds.toFixed(2) + '</div>' +
        '</li>';
      }).join("");
      // Wire remove buttons
      legsEl.querySelectorAll(".slip-remove").forEach(function (btn) {
        btn.addEventListener("click", function () {
          removeLeg(parseInt(btn.getAttribute("data-idx"), 10));
        });
      });
    }

    if (copyBtn) {
      copyBtn.disabled = legs.length === 0;
    }
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  // ── Click handlers on .leg-add and .sgm-add buttons ──
  function attachClickHandlers() {
    // Single-leg picks
    document.querySelectorAll(".leg-add").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        addLeg({
          event: btn.getAttribute("data-event"),
          market: btn.getAttribute("data-market"),
          selection: btn.getAttribute("data-pick"),
          odds: parseFloat(btn.getAttribute("data-odds"))
        });
        // Visual feedback
        btn.classList.add("leg-added");
        setTimeout(function () { btn.classList.remove("leg-added"); }, 600);
      });
    });

    // SGM picks — adds all legs as one ticket
    document.querySelectorAll(".sgm-add").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        try {
          var legs = JSON.parse(btn.getAttribute("data-legs"));
          legs.forEach(function (l) { addLeg(l); });
        } catch (err) {
          // ignore
        }
        btn.classList.add("leg-added");
        setTimeout(function () { btn.classList.remove("leg-added"); }, 600);
      });
    });

    // Top-pick shortcut buttons (actionable picks at top of card)
    document.querySelectorAll(".top-pick-add").forEach(function (btn) {
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        addLeg({
          event: btn.getAttribute("data-event"),
          market: btn.getAttribute("data-market"),
          selection: btn.getAttribute("data-pick"),
          odds: parseFloat(btn.getAttribute("data-odds"))
        });
        btn.classList.add("leg-added");
        setTimeout(function () { btn.classList.remove("leg-added"); }, 600);
      });
    });

    // Stake input change
    var stakeInput = document.getElementById("slip-stake");
    if (stakeInput) {
      stakeInput.addEventListener("input", render);
      stakeInput.addEventListener("change", render);
    }

    // Copy button
    var copyBtn = document.getElementById("slip-copy");
    if (copyBtn) {
      copyBtn.addEventListener("click", function () {
        var legs = loadSlip();
        var stakeInput = document.getElementById("slip-stake");
        var stake = parseFloat(stakeInput.value) || 0;
        var text = buildSlipText(legs, stake);
        // Modern clipboard API
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(function () {
            copyBtn.textContent = "Copied ✓";
            setTimeout(function () { copyBtn.textContent = "Copy Slip"; }, 1500);
          }).catch(function () {
            fallbackCopy(text, copyBtn);
          });
        } else {
          fallbackCopy(text, copyBtn);
        }
      });
    }

    // Clear button
    var clearBtn = document.getElementById("slip-clear");
    if (clearBtn) {
      clearBtn.addEventListener("click", clearSlip);
    }
  }

  function fallbackCopy(text, btn) {
    var ta = document.createElement("textarea");
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      if (btn) {
        btn.textContent = "Copied ✓";
        setTimeout(function () { btn.textContent = "Copy Slip"; }, 1500);
      }
    } catch (e) {
      if (btn) {
        btn.textContent = "Copy failed";
      }
    }
    document.body.removeChild(ta);
  }

  // ── Boot ──
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      attachClickHandlers();
      render();
    });
  } else {
    attachClickHandlers();
    render();
  }
})();
