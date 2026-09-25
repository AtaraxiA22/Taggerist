# Taggerist Joint Task List

Last updated: v35.05 (by agent)

**Format:** ID# = `#status.ID` — status: **w** = waiting for user test · 5 = very high · 4 = high · 3 = medium · 2 = low · 1 = very low · 0 = fixed/resolved (user-confirmed). ID is permanent; change status by editing the status digit/letter. Agent re-sorts (w.## first, then 5.## → 1.## descending; 0.## (user-confirmed) at the bottom; newest ID first within a band). Checkbox = "look at this / status changed" signal from user; agent reconciles and re-sorts.

| ☐ | ID# | Item description | Comment |
|:-:|:-:|--------------------------------------------------|--------------------------------------------------|
| ☐ | #w.28 | SearchBox height should match the boxes above | NEW // Implemented v35.05 (larger font + padding) — awaiting user test |
| ☐ | #w.26 | [Reduce] does not remove non-tag text sandwiched between pipe-delimited tags (e.g. 'this is not a tagname' survived) | NEW // v35.02 fix: [Reduce] now checks every pipe-delimited word against ALL taglists and drops anything unknown, keeping only legitimate tags + CI/datestamp/_wm/extension. Verified against the user's example: reduces to |CLR_red|©2026.0718-2103.458_wm.jpg — awaiting user test |
| ☐ | #w.17 | Button cluster: all primary buttons left of the edit box | v35.05 rev4 tweaks per user: CI buttons sized to label + 1 space; Clear/Reduce widths matched to Sort Tags; uniform heights; PROCESS = edit-box height (2 rows); SKIP directly under PROCESS, same width; SearchBox height matches boxes above; TV nav renamed/reordered [External viewer]/[← Previous]/[Next →] vertical, bold, right-justified at TF/TV border — awaiting user test |
| ☐ | #1.16 | Persistent per-list tag colors | On hold per user call |
| ☐ | #0.27 | Long filename in FilenameEditBox should wrap onto the 2nd line | RESOLVED v35.04 — USER TEST OK ("Wrapping worked!") |
| ☐ | #0.25 | Feature: mouseover on a filename in PROC or UNPROC shows a small popup with the full filename+ext, wrapping at the right-hand window margin | FIXED — USER TEST OK v35.01 ("a big help with long-filename files") |
| ☐ | #0.24 | Feature: IF date prefix = '(c)' THEN replace it with '©' | CANCELLED BY USER // He will batch-rename existing files instead; CI symbol handling stays generic for other potential users |
| ☐ | #0.23 | In TF, the PROC and UNPROC directory full paths show in the same line as the [OPEN] buttons, but the directory listings below don't load them — the app seems to 'remember' the paths but doesn't use them | NEW // v34.22 fix: the app stored the chosen directories in memory but never wrote them to the config file on disk, so a restart always fell back to the default paths; it now saves them to disk, and the listings load the remembered directories at startup — USER TEST OK v34.22 |
| ☐ | #0.22 | On startup the window title shows 'v34.21', but clicking a filename in UNPROC changes the top line to 'v34.19' | FIXED // v34.22 fix: the window title was re-written with a hard-coded 'v34.19' inside the program whenever a file was selected; now it always shows the true version. Also explains why no v34.21 buglog appeared: the log file name was also hard-coded to v34.19 — both now use the real version number — USER TEST OK v34.22 |
| ☐ | #0.19 | After search-adding 5-6 tags and [Sort Tags], pressing [Clear] emptied the FilenameEditBox but the tagnames stayed highlighted in the taglist | FIXED // v34.20 root cause: the [Clear] and [Reduce] buttons emptied the edit box but never reset the internal "selected tags" memory, so the taglist kept painting them as selected; both buttons now reset that memory from whatever text remains — USER TEST OK v34.20 |
| ☐ | #0.18 | Unselected TAGLIST_NAME button (first of three) doesn't show list name in FULLWINDOW_FONT_COLOR on FULLWINDOW_BG_COLOR (selected state OK) | FIXED // v34.19 root cause: a comment-stripping helper was eating unquoted color values from the config file, so the app silently fell back to white/black; such values now pass through — awaiting user test |
| ☐ | #0.15 | Bottom row +50% height | Implemented v35.01 (36px row) — kept in v35.02 |
| ☐ | #0.14 | Full path in taglist status line | Implemented v35.01 — kept in v35.02 |
| ☐ | #0.13 | [Sort Tags] button sorts \|tags\| in FilenameEditBox alphabetically | FIXED // Implemented v34.19 (third row, beside [Clear]/[Reduce]); preserves leading text, datestamp, `_wm`, extension — awaiting user test |
| ☐ | #0.12 | Char count numerals in the thermometer bar | RESOLVED v35.04 — USER TEST OK (left-justified numerals, traffic-light colors) |
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
