# Taggerist Joint Task List

Last updated: v34.21 (by agent)

**Format:** ID# = `#status.ID` — status: **w** = waiting for user test · 5 = very high · 4 = high · 3 = medium · 2 = low · 1 = very low · 0 = fixed/resolved (user-confirmed). ID is permanent; change status by editing the status digit/letter. Agent re-sorts (w.## first, then 5.## → 0.##; newest ID first within a band). Checkbox = "look at this / status changed" signal from user; agent reconciles and re-sorts.

| ☐ | ID# | Item description | Comment |
|:-:|:-:|--------------------------------------------------|--------------------------------------------------|
| ☐ | #0.19 | After search-adding 5-6 tags and [Sort Tags], pressing [Clear] emptied the FilenameEditBox but the tagnames stayed highlighted in the taglist | FIXED // v34.20 root cause: the [Clear] and [Reduce] buttons emptied the edit box but never reset the internal "selected tags" memory, so the taglist kept painting them as selected; both buttons now reset that memory from whatever text remains — USER TEST OK v34.20 |
| x | #0.22 | On startup the window title shows 'v34.21', but clicking a filename in UNPROC changes the top line to 'v34.19' | FIXED // v34.22 fix: the window title was re-written with a hard-coded 'v34.19' inside the program whenever a file was selected; now it always shows the true version. Also explains why no v34.21 buglog appeared: the log file name was also hard-coded to v34.19 — both now use the real version number |
| ☐ | #4.12 | Char count ('22/255') centered inside the thermometer bar | Colors are length-driven, not taglist-driven: green under 100 chars, yellow 100–150, red over 150. The count was invisible on the yellow bar because the text fell back to white after switching taglists. // v34.21 fix: the count is now always bold black text on the bar, matching the date-prefix button — could not be tested (see #5.22 title bug report) |
| ☐ | #3.23 | In TF, the PROC and UNPROC directory full paths show in the same line as the [OPEN] buttons, but the directory listings below don't load them — the app seems to 'remember' the paths but doesn't use them | NEW // v34.22 fix: the app stored the chosen directories in memory but never wrote them to the config file on disk, so a restart always fell back to the default paths; it now saves them to disk, and the listings load the remembered directories at startup |
| ☐ | #4.24 | Feature: IF date prefix = '(c)' THEN replace it with '©' | NEW // v34.22: when the config's copyright symbol is '©', clicking a date-prefix button now converts an existing '(c)' prefix to '©' in the filename — awaiting user test |
| ☐ | #2.15 | Bottom row +50% height | Trivial |
| ☐ | #2.14 | Full path in taglist status line | Trivial |
| ☐ | #1.17 | Cosmetic batch: TV nav buttons top-right; FilenameEditBox right-justified; SearchBox beside edit box w/ same-width dropdown; action buttons under thermometer (bold, distinct colors); CI buttons vertical right of edit boxes; strip `[]` from labels; red/green PROC-UNPROC headers, white text | Deferred until crash confirmed dead |
| ☐ | #1.16 | Persistent per-list tag colors | On hold per user call |
| ☐ | #0.18 | Unselected TAGLIST_NAME button (first of three) doesn't show list name in FULLWINDOW_FONT_COLOR on FULLWINDOW_BG_COLOR (selected state OK) | FIXED // v34.19 root cause: a comment-stripping helper was eating unquoted color values from the config file, so the app silently fell back to white/black; such values now pass through — awaiting user test |
| ☐ | #0.13 | [Sort Tags] button sorts \|tags\| in FilenameEditBox alphabetically | FIXED // Implemented v34.19 (third row, beside [Clear]/[Reduce]); preserves leading text, datestamp, `_wm`, extension — awaiting user test |
| ☐ | #0.11 | Search matches aliases anywhere in the CSV line ('grn' finds `CLR_grn`) | FIXED // Implemented v34.19 — awaiting user test |
| ☐ | #0.10 | Search case-sensitivity | FIXED // Code looks case-insensitive; awaiting example tag + search string |
| ☐ | #0.09 | [Default Sort All] button | User-tested v34.18 — works |
| ☐ | #0.08 | Cursor defaults to SearchBox after any button | User-tested v34.18 — works |
| ☐ | #0.07 | ENTER accepts first search result | User-tested v34.18 — works |
| ☐ | #0.06 | PROC list not refreshing after PROCESS | Fixed v34.18; USER TEST OK |
| ☐ | #0.05 | [RW] symbol not replacing others / duplicating on repeat | Fixed v34.18; USER TEST OK |
| ☐ | #0.03 | Crash saga history: v34.15 faulthandler traces; v34.16 sorting + v34.15 processEvents were misdiagnoses | Kept for reference |
| ☐ | #0.02 | Date symbol not removed when adding new | Fixed v34.17 |
| ☐ | #0.01 | Search crash `free(): invalid pointer` — PySide6 6.11 stale-wrapper bug in tag-label teardown | Fixed v34.17; **confirmed stable by user** |

**Old ID mapping** (continuity with earlier conversations): B01→10, B02→04, B03→05, B04→06, F01→11, F02→12, F03→13, F04→14, F05→15, F06→07, F07→08, F08→09, C01→16, C02→17, R01→01, R02→02, R03→03
