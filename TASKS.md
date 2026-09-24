# Taggerist Joint Task List

Last updated: v34.18 test results (by agent)

**Format:** ID# = `#status.ID` — status: **w** = waiting for user test · 5 = very high · 4 = high · 3 = medium · 2 = low · 1 = very low · 0 = fixed/resolved (user-confirmed). ID is permanent; change status by editing the status digit/letter. Agent re-sorts (w.## first, then 5.## → 0.##; newest ID first within a band). Checkbox = "look at this / status changed" signal from user; agent reconciles and re-sorts.

| ☐ | ID# | Item description | Comment |
|:-:|:-:|--------------------------------------------------|--------------------------------------------------|
| ☐ | #4.18 | CI symbol button label still invisible on yellow background (fix from v34.18 did not work) | Reopened from #0.04 after user test; needs diagnosis on TE01 |
| ☐ | #0.09 | [Default Sort All] button | User-tested v34.18 — works |
| ☐ | #0.08 | Cursor defaults to SearchBox after any button | User-tested v34.18 — works |
| ☐ | #0.07 | ENTER accepts first search result | User-tested v34.18 — works |
| ☒ | #0.06 | PROC list not refreshing after PROCESS | Fixed v34.18; USER TEST OK |
| ☒ | #0.05 | [RW] symbol not replacing others / duplicating on repeat | Fixed v34.18; USER TEST OK |
| ☐ | #3.10 | Search case-sensitivity | Code looks case-insensitive; awaiting example tag + search string |
| ☐ | #3.11 | Search entire CSV line ('grn' would find `CLR_grn`) | Trivial |
| ☐ | #3.12 | Char count inside thermometer ('22/255' centered in bar) | Stable, safe |
| ☐ | #2.13 | Dynamic tag sort in FilenameEditBox | Must be button-triggered; live sort would fight the cursor |
| ☐ | #2.14 | Full path in taglist status line | Trivial |
| ☐ | #2.15 | Bottom row +50% height | Trivial |
| ☐ | #1.16 | Persistent per-list tag colors | On hold per user call |
| ☐ | #1.17 | Cosmetic batch: TV nav buttons top-right; FilenameEditBox right-justified; SearchBox beside edit box w/ same-width dropdown; action buttons under thermometer (bold, distinct colors); CI buttons vertical right of edit boxes; strip `[]` from labels; red/green PROC-UNPROC headers, white text | Deferred until crash confirmed dead |
| ☐ | #0.03 | Crash saga history: v34.15 faulthandler traces; v34.16 sorting + v34.15 processEvents were misdiagnoses | Kept for reference |
| ☐ | #0.02 | Date symbol not removed when adding new | Fixed v34.17 |
| ☒ | #0.01 | Search crash `free(): invalid pointer` — PySide6 6.11 stale-wrapper bug in tag-label teardown | Fixed v34.17; **confirmed stable by user** |

**Old ID mapping** (continuity with earlier conversations): B01→10, B02→04, B03→05, B04→06, F01→11, F02→12, F03→13, F04→14, F05→15, F06→07, F07→08, F08→09, C01→16, C02→17, R01→01, R02→02, R03→03
