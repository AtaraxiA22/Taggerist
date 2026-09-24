# Taggerist Joint Task List

Last updated: v34.18 (by agent) — edit freely, commit after changes.
Item IDs (B/F/C/R + number) are permanent quick references: never renumbered, never reused, even after an item closes.

## 🐛 Bugs — OPEN

| ID | Item | Reported in | Status / Notes |
|---|---|---|---|
| B01 | Search case-sensitivity | v34.16 feedback | Code looks case-insensitive already; awaiting example tag + search string |

## ✅ Fixed — awaiting your confirmation (tick ✅ after testing)

- [ ] **B02 — CI symbol buttons invisible on yellow** — fixed in v34.18 (contrast-aware text; chips too)
- [ ] **B03 — [RW] symbol not replacing others / duplicating on repeat** — fixed in v34.18 (symbols now read from config, not hard-coded)
- [ ] **B04 — PROC list not refreshing after PROCESS** — fixed in v34.18 (refresh always runs; processed file scrolled to center)

## ✨ Features — REQUESTED (not yet built)

- [ ] **F01 — Search entire CSV line** — 'grn' would find `CLR_grn` (aliases too). Trivial.
- [ ] **F02 — Char count inside thermometer** — '22/255' centered in the bar. Stable, safe.
- [ ] **F03 — Dynamic tag sort in FilenameEditBox** — feasible, but must be button-triggered (live sorting would fight the cursor).
- [ ] **F04 — Full path in taglist status line** — trivial.
- [ ] **F05 — Bottom row +50% height** — trivial.
- [x] **F06 — ENTER accepts first search result** — ✅ DONE in v34.18
- [x] **F07 — Cursor defaults to SearchBox after any button** — ✅ DONE in v34.18
- [x] **F08 — [Default Sort All] button** — ✅ DONE in v34.18 (right-justified above UNPROCESSED)

## 🔥 Back burner

- [ ] **C01 — Persistent per-list tag colors** (feature #6) — on hold per your call
- [ ] **C02 — Cosmetic batch** (deferred until crash confirmed dead): TV nav buttons top-right; FilenameEditBox right-justified; SearchBox beside edit box w/ same-width dropdown; action buttons under thermometer, bold labels, distinct colors; CI buttons vertical right of edit boxes; strip `[]` from all button labels; red/green PROC & UNPROC header backgrounds w/ white text

## 📜 Resolved (history)

- [x] **R01 — Search crash `free(): invalid pointer`** — root-caused (PySide6 6.11 stale-wrapper bug in tag-label teardown), fixed v34.17, **confirmed stable** by user
- [x] **R02 — Date symbol not removed when adding new** — fixed v34.17
- [x] **R03 — Crash during PROCESS / search** — misdiagnosed twice (v34.16 sorting, v34.15 processEvents); real cause found via faulthandler traces
