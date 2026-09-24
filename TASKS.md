# Taggerist Joint Task List

Last updated: v34.18 (by agent) — edit freely, commit after changes.

**Format: `#priority.ID`**
- Priority: 0 = fixed/resolved · 1 = very low · 2 = low · 3 = medium · 4 = high · 5 = very high
- ID: permanent two-digit number, never renumbered or reused. Sort: 5.## at top → 0.## at bottom; within a priority band, newest (highest ID) first.
- To change status, edit the priority digit and re-sort the list (agent maintains sort order).
- Inside priority 0: `- [ ]` = fixed, awaiting user test · `- [x]` = confirmed by user.

## Task List

- [ ] **#3.10** — Search case-sensitivity (v34.16 report) — code looks case-insensitive; awaiting example tag + search string
- [ ] **#3.11** — Search entire CSV line — 'grn' would find `CLR_grn` (aliases too). Trivial.
- [ ] **#3.12** — Char count inside thermometer — '22/255' centered in the bar. Stable, safe.
- [ ] **#2.13** — Dynamic tag sort in FilenameEditBox — feasible; must be button-triggered (live sorting would fight the cursor)
- [ ] **#2.14** — Full path in taglist status line — trivial
- [ ] **#2.15** — Bottom row +50% height — trivial
- [ ] **#1.16** — Persistent per-list tag colors (old feature #6) — on hold per user call
- [ ] **#1.17** — Cosmetic batch (deferred until crash confirmed dead): TV nav buttons top-right; FilenameEditBox right-justified; SearchBox beside edit box w/ same-width dropdown; action buttons under thermometer, bold labels, distinct colors; CI buttons vertical right of edit boxes; strip `[]` from all button labels; red/green PROC & UNPROC header backgrounds w/ white text
- [ ] **#0.09** — [Default Sort All] button — done in v34.18 (right-justified above UNPROCESSED)
- [ ] **#0.08** — Cursor defaults to SearchBox after any button — done in v34.18
- [ ] **#0.07** — ENTER accepts first search result — done in v34.18
- [ ] **#0.06** — PROC list not refreshing after PROCESS — fixed v34.18 (refresh always runs; processed file scrolled to center)
- [ ] **#0.05** — [RW] symbol not replacing others / duplicating on repeat — fixed v34.18 (symbols read from config, not hard-coded)
- [ ] **#0.04** — CI symbol buttons invisible on yellow — fixed v34.18 (contrast-aware text; chips too)
- [ ] **#0.02** — Date symbol not removed when adding new — fixed v34.17
- [x] **#0.01** — Search crash `free(): invalid pointer` — root-caused (PySide6 6.11 stale-wrapper bug in tag-label teardown), fixed v34.17, **confirmed stable**
- [ ] **#0.03** — Crash saga history (v34.15 faulthandler traces; v34.16 sorting and v34.15 processEvents were misdiagnoses) — kept for reference

**Old ID mapping** (for continuity in past conversations): B01→10, B02→04, B03→05, B04→06, F01→11, F02→12, F03→13, F04→14, F05→15, F06→07, F07→08, F08→09, C01→16, C02→17, R01→01, R02→02, R03→03
