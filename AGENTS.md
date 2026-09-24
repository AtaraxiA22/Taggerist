# AGENTS.md — Working Notes for AI Agents on Taggerist

This file is read at the start of every session. It captures project conventions and
working-relationship context that would otherwise be lost when a session expires.
The human partner is AtaraxiA22 ("Jack", per config paths). Keep this file short and
durable; per-session blow-by-blow history goes in `Session_v*.txt` files (NOT `.log` —
`*.log` is gitignored).

## The Project

Taggerist is a PySide6 desktop app for tagging/renaming image files (mostly photos)
with a pipe-delimited tag vocabulary. One self-contained `.py` file per version, in
the repo root: `Taggerist_v34.20.py` is the newest. A version PR should include the
new file (full app), not just a diff.

## Working Relationship & Workflow

- **Session continuity:** Sessions expire without warning. Everything the next agent
  must know must be *committed to the repo*. Reconstruct context from TASKS.md,
  buglogs, git history, PR descriptions, and version-file headers.
- **TASKS.md is the joint task list.** ID# = `#status.ID`: **w** = waiting for user
  test; 5 (very high) → 0 (fixed/resolved, user-confirmed). IDs are permanent; the
  agent re-sorts (w.## first, then 5.## → 0.##, newest first within a band). The
  checkbox column is the user's "look at this / status changed" signal — the agent
  reconciles and re-sorts. User edits TASKS.md directly on main; the agent may commit
  TASKS.md updates straight to main too (established pattern: d63b80c, 62b3f38).
  Version PR branches should NOT include TASKS.md (it conflicts with main).
- **The user tests everything on a real Linux box.** The agent's sandbox has no
  display/PySide6, so GUI fixes are verified by `python3 -m py_compile` plus
  stub-based logic tests only. New fixes land in the w-band awaiting the user's test.
- **Version-file header changelog:** each new `Taggerist_vXX.py` gets a one-line
  `# Taggerist vXX.YY: <task refs> — <what changed>` note directly above the
  `# (c) @... by AtaraxiA under Creative Commons CC BY-SA license` line, with prior
  version notes preserved below it. Verify with a line-based edit, not sed/string
  replace (a naive replace once mangled the header).

## Technical Conventions

- Tags are pipe-delimited: `|TAG1|TAG2|` before the datestamp; extension last.
  Backtick `` ` `` is an alternate delimiter, converted to `|`.
- Filename structure: leading text (optional), tags, datestamp
  (`<CI-symbol><yy>.<mmdd>-<hhmm>.<ss><NN>` e.g. `©26.0920-0644.37`), optional
  `_wm` watermark suffix, extension (default `.jpg`).
- CI (copyright indicator) symbol is `©` in filenames; `(c)` is the fallback when
  config `DISPLAY/CI_SYMBOL` isn't `©`.
- Tag highlight state in the taglist grid is driven by `self.selected_tags` (a set),
  NOT by parsing the FilenameEditBox text. Any code path that changes the edit box
  text must also clear/re-extract `selected_tags` and call `update_tag_highlights()`
  (see #w.19: [Clear]/[Reduce] forgot this).
- Taglist CSVs are private (gitignored). Fallback paths point at
  `/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/`. Config:
  `Taggerist.config.txt`; colors may be bare `#RGB`/`#RRGGBB` — don't let
  `strip_comment()` eat them (see #0.18).
- Known crash history (#0.01): PySide6 6.11 stale-wrapper bug during tag-label
  teardown — fixed v34.17 by pre-allocated chip pool; user confirmed stable.
  Don't reintroduce widget churn in search results.

## Reference Files (read on demand)

- `TASKS.md` — status of every bug/feature
- `Taggerist_v34.17-buglog.txt` and earlier — runtime trace logs
- `Taggerist_vXX_User_Feedback.txt` — the user's test notes per version
- `time stamp format guidance.txt` — datestamp rules
- `map of the top portion of TL©26.0920-0644 .txt`, `Purposed restructuring©26.0919-1217.txt` — UI layout notes

## Delivery

- Version work: branch `vibe/vXX.YY-<slug>-<hash>`, one PR per version, updated in
  place (never delete/reopen). Report the PR URL. PR body uses task IDs and ends
  with `Closes <id>` only if it resolves a tracked GitHub issue (none exist — TASKS.md
  is the tracker).
- TASKS.md updates: commit directly to main (user has approved this pattern).
