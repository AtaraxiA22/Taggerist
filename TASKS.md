# Taggerist Joint Task List

Last updated: v34.18 (by agent) — edit freely, commit after changes.

## 🐛 Bugs — OPEN

| Item | Reported in | Status / Notes |
|---|---|---|
| Case-insensitive search may miss some tags | v34.16 feedback | Code looks case-insensitive already; awaiting example tag + search string |

## ✅ Fixed — awaiting your confirmation (tick ✅ after testing)

- [x] **CI symbol buttons invisible on yellow** — fixed in v34.18 (contrast-aware text; chips too)
- [ ] **[RW] symbol not replacing others / duplicating on repeat** — fixed in v34.18 (symbols now read from config, not hard-coded)
- [ ] **PROC list not refreshing after PROCESS** — fixed in v34.18 (refresh always runs; processed file scrolled to center)

## ✨ Features — REQUESTED (not yet built)

- [ ] **Search entire CSV line** — 'grn' would find `CLR_grn` (aliases too). Trivial.
- [ ] **Char count inside thermometer** — '22/255' centered in the bar. Stable, safe.
- [ ] **Dynamic tag sort in FilenameEditBox** — feasible, but must be button-triggered (live sorting would fight the cursor).
- [ ] **Full path in taglist status line** — trivial.
- [ ] **Bottom row +50% height** — trivial.
- [ ] **ENTER accepts first search result** — ✅ DONE in v34.18
- [ ] **Cursor defaults to SearchBox after any button** — ✅ DONE in v34.18
- [ ] **[Default Sort All] button** — ✅ DONE in v34.18 (right-justified above UNPROCESSED)

## 🔥 Back burner

- [ ] **Persistent per-list tag colors** (feature #6) — on hold per your call
- [ ] **Cosmetic batch** (deferred until crash confirmed dead): TV nav buttons top-right; FilenameEditBox right-justified; SearchBox beside edit box w/ same-width dropdown; action buttons under thermometer, bold labels, distinct colors; CI buttons vertical right of edit boxes; strip `[]` from all button labels; red/green PROC & UNPROC header backgrounds w/ white text

## 📜 Resolved (history)

- [x] Search crash `free(): invalid pointer` — root-caused (PySide6 6.11 stale-wrapper bug in tag-label teardown), fixed v34.17, **confirmed stable** by user
- [x] Date symbol not removed when adding new — fixed v34.17
- [x] Crash during PROCESS / search — misdiagnosed twice (v34.16 sorting, v34.15 processEvents); real cause found via faulthandler traces
