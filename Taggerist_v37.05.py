# Taggerist v37.05

# Personal Configurations (fallback defaults; overridden by Taggerist.config.txt)
TAGLIST_1 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[NC].csv,©,white,red'
TAGLIST_2 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[Xpix].csv,@,white,yellow'
TAGLIST_3 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[RW].csv,!!,white,green'

TAGLIST_ID_1 = '©'
TAGLIST_ID_2 = '@'
TAGLIST_ID_3 = '!!'

DELIMITERS = ['|', '`']

HELP_FILE_PATH = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/README.md'
# P.D. Reviewed @26.0909-0700.00
# Taggerist v35.07: #26-analysis — buglog diagnostics proved the tag pool healthy (788 tags); Reduce is working as designed; user's test words simply aren't in any taglist. #w.30 new — ENTER now triggers PROCESS (when focus is in the Search box or edit box). #w.31 new — [PROCESS] auto-sorts the tagline before saving (config line PROCESS_AUTO_SORT, True/False, default True). #w.29 new — after any TL or TV button press (incl. Previous/Next/External viewer and CI buttons), focus returns to the Search box. #w.17 rev6: (c) TV labels right-justified; (e) TV buttons shifted down one more line; NEW.1 taglist buttons placed vertically between the CI and Tagline columns, aligned per row; NEW.2 vertical border lines between CI/Taglist/Tagline columns + horizontal border over the edit box extended left to the TF/TV border; NEW.6 border added around [Default Sort All]; NEW.7 'The TAGGERIST / by AtaraxiA and Vibe' title block added at top of TF, right-justified, with separator line under it.
# Taggerist v35.06: #w.26 rev — [Reduce] known-tag check now also draws on the active list's own tag set and writes every drop/keep decision to the buglog (drop reasons readable in Taggerist_v35.06-buglog.txt); #w.17 rev5 per user: CI buttons narrowed to 3-char width, bracket-free, bold, no padding; Reduce/Sort Tagline widths re-matched to Clear; vertical alignment fixed (uniform 30px row heights across CI and action buttons); TV nav buttons right-justified labels, thicker white borders, shifted down to align with CI rows, styled same as cluster buttons (white on black, white border); Clear/Reduce/Sort Tagline restyled to default window colors with white borders; label [Sort Tags] renamed [Sort Tagline]; thermometer count now shows 'NN/255 chars.'
# Taggerist v35.05: #w.28 — SearchBox height now matches the boxes above. #w.17 rev4 tweaks per user map: CI buttons sized to their label with one space padding; CLEAR/REDUCE widths matched to SORT TAGS; uniform cluster button heights; PROCESS same height as the FilenameEditBox; SKIP directly under PROCESS, same width; TV nav buttons reordered/renamed [External viewer] [Previous] [Next], vertically stacked at the TF/TV border aligned with the CI rows, heights matching the CI buttons, bold larger labels
# Taggerist v35.04: #w.27 — long filenames in the FilenameEditBox now wrap onto the second line instead of scrolling sideways
# Taggerist v35.03: #w.17 rev3 — per revised user map, [PROCESS] is now two rows tall (was three)
# Taggerist v35.02: #w.17 rev2 — all primary buttons clustered left of the edit box per user map: taglist/CI rows + CLEAR→PROCESS column, PROCESS button 3 rows tall, edit box and pathname stretch to right margin, thermometer right-aligned above search; #w.12 rev — bar numerals left-justified (centered text sat on the unfilled black part when the count is low), colors now green→yellow→red traffic-light order; #w.26 — [Reduce] now validates every pipe-delimited segment against all taglists and drops unknown words (keeps CI/datestamp/_wm/extension); [Sort Tags] stays in the left cluster on row 4 beside SKIP
# Taggerist v35.01: #w.25 — mouseover on a PROC/UNPROC filename shows a small wrapping popup with the full filename+ext. #w.12 — thermometer numerals are now larger bold black (taller bar) for visibility. #w.17 — cosmetic batch: TV nav buttons moved top-right; CI buttons vertical stack; Clear/Reduce/Sort Tags row under the thermometer with bold distinct colors; Search box beside the edit-box column; brackets stripped from all button labels; PROC header red / UNPROC header green. #w.15 — bottom row 50% taller. #w.14 — full taglist path shown in the status line. NOTE: #4.24 cancelled by user — he will batch-rename existing files instead; CI symbol handling stays generic
# Taggerist v34.22: #5.22 fix — the window title and the debug-log file name were hard-coded to v34.19; both now use the true version number. #3.23 fix — the PROC/UNPROC directory choices are now actually written to the config file on disk (previously kept only in memory), so the app remembers them between sessions. #4.24 — when the config copyright symbol is ©, clicking a date-prefix button now converts an existing (c) prefix to © in the filename
# Taggerist v34.21: #4.12 fix — the char count inside the thermometer bar is now always bold black text in all four places that style the bar; previously the text color was only set on one of them, so after switching taglists the count fell back to white and vanished on the yellow (100+ chars) warning bar
# Taggerist v34.20: #w.19 fix — [Clear] and [Reduce] now reset selected_tags and re-extract them from the kept text (datestamp, _wm, extension) before repainting the taglist; previously tag names stayed highlighted after the FilenameEditBox was emptied
# Taggerist v34.19: #4.18 fix — unselected taglist buttons now use FULLWINDOW_FONT_COLOR on FULLWINDOW_BG_COLOR (was hard-coded #000); unquoted hex colors in Taggerist.config.txt were being swallowed as comments — bare #RGB/#RRGGBB values now pass through unchanged; #3.12 — char count '22/255' now shown centered inside the thermometer bar (side label removed); #3.11 — search now matches aliases from every taglist CSV line (typing 'grn' finds CLR_grn); #2.13 — NEW [Sort Tags] button (third row, beside [Clear]/[Reduce]) sorts the |tags| in FilenameEditBox alphabetically, preserving leading text, datestamp, _wm, and extension
# Taggerist v35.08: #w.32 fix — tag-alias conversion now matches whole pipe-delimited words only; previously aliases like 'forest' or 'PTY_' were replaced wherever they appeared inside a word, doubling prefixes in the FilenameEditBox (LOC_LOC_forest, PTY_fernshat, wha%_100%ver). #w.29 rev — focus now returns to the Search box also after a TF file click, [SKIP], the taglist buttons, and [Edit tags]/[Refresh]/[Help].
# Taggerist v36.01: #w.33 — taglist buttons removed; replaced by font-size and columns spin-controls (live repaint, values saved to config). One-screen taglist: short display names (root after first underscore; col2 of the CSV overrides, e.g. '50.00' for %_50%), bold non-clickable section headers (___ rows, title from col2), all three lists load together with sort/grouping still by full tag, and the grid scrolls horizontally. FilenameEditBox/PROCESS/Sort/Clear/Reduce keep full-tag equivalence: old prefixed filenames still load, highlight and reduce correctly; new tags insert as short names (a short name matches its full tag when unique; ambiguity falls back to the full tag). [Edit tags] renamed [Edit Tags].
# Taggerist v36.02: #w.35 fix — the Cols spin-control now truly controls the column count (root cause: the grid silently derived columns from screen height, so the value drifted between repaints); rows per column = tags ÷ columns, vertical scrollbar returns only if needed. #w.37 new — main taglist (and search results) sort case-insensitively, so e.g. LOC_House and LOC_house now sit together. Subdirectory listing in PROC/UNPROC considered and dropped per user ('not a big deal'; the empty-list report was a false alarm — images were in a subfolder).
# Taggerist v36.03: #w.39 fix — [Refresh Tags] (and [Edit Tags] round-trips) no longer wipe the FilenameEditBox; previously the refresh re-loaded the file's ORIGINAL name from disk, discarding unsaved tags typed in the box; now the box text is kept and only the highlights are re-derived. #w.40 — taglist columns always fill the TL area down to the bottom margin: with few columns the vertical spacing stretches so the list no longer ends mid-screen. #w.41 — ' Font'/' Cols' labels padded with a leading space so they no longer hug the border line.
# Taggerist v37.03: v37.02 feedback — [Brackets] box 24 chars (Search aligns with [SKIP]/[PROCESS]); [Reduce]/Alt+R, [Clear], [Skip] now also clear the Search and Brackets boxes; NEW Alt+Delete clears both boxes any time; NEW: on [PROCESS], unknown words in the filename prompt a checkbox dialog to append selected names to the current taglist (then reload, so Search finds them immediately); fix: selected-tag highlight is always black-on-pale-yellow (was white-on-yellow after Reduce); legend + README.md updated (Alt+Del).
# Taggerist v37.02: v37.01 feedback — keystroke legend reworded ('Alt+T Sort Filename', 'Alt+1/© · Alt+2/@ · Alt+3/!!') and enlarged 10→12pt; taglist status says '3 lists' (variable, pluralized) instead of '3 taglists loaded'; CI button group width now hugs the widest symbol (no wasted space; FilenameEditBox expands into the freed room); [Brackets] box default width 25 chars (config BRACKETS_BOX_WIDTH); bottom row: Search box expands, [Edit Tags]/[Refresh Tags] flush to the far right edge.
# Taggerist v37.01: v36.10 crash fix — the program failed to start ('TaggeristList' object has no attribute 'brackets_edit'): the Brackets box's key handler and focus-color filter were being attached before the box was created; creation order corrected (box first, then hookups). Also renames the file to the v37.01 version line.
# Taggerist v36.10: #0.48 rev2 — CI button on a camera-dated file no longer appends a second (system) datestamp: after prefixing the camera date with the CI, the append-system-date step is skipped. #w.55 NEW — [Brackets] text box left of the Search box (40 chars, width set by config BRACKETS_BOX_WIDTH): ENTER wraps the typed text in [square brackets], prefixes it to the FilenameEditBox, clears itself, focus returns to Search. #w.56 NEW — ←/→ move the 'hot' highlight across search result tags (default: 1st); ← from the 1st tag moves focus to the Brackets box; → from the Brackets box moves to the 1st tag; ENTER adds the hot tag (or the bracketed string) to the filename and refocuses Search. #w.57 NEW — '[' and ']' render blue in the FilenameEditBox; an unmatched bracket blinks. #w.58 NEW — the focused box gets a colored thick border: Brackets box BLUE, Search box ORANGE, FilenameEditBox YELLOW. #w.59 NEW — bottom row restyled: total tag count flush left; [Edit Tags]/[Refresh Tags] move up beside the Search box; a center-justified keystroke legend sits between the count and [?] (narrower, right-justified).
# Taggerist v36.09: #0.48 rev — CI buttons now also prefix camera-style dates (e.g. '2024-09-20 00-52-28-081') with the chosen symbol when no Taggerist datestamp exists. #w.52 NEW — Alt+D (and a [Fix Date] button next to the Font/Cols controls) converts a recognized camera-style date into the Taggerist datestamp shape yy.mmdd-HHMM.ssnn — optional, one explicit action, nothing automatic. #w.53 fix — [bracketed] data now survives Reduce even when glued to other text in the same pipe segment (e.g. '[gym workout]Veronica'); the bracketed part is kept and logged to TagCandidates.txt, the rest still reduces. #w.54 NEW — ESC puts the cursor in the Search box; Ctrl+ENTER puts it in the Filename edit box.
# Taggerist v36.08: #w.51 — CI symbol for taglist 3 changed from '=' to '!!' per user (his config already carries '!!'; no space between the bangs). The change itself is pure config — no code needed — BUT '=' is now kept as a built-in legacy symbol so old files already named with '=' still load, highlight and convert (pressing any CI button replaces an old '=' prefix with the new symbol). Fallback defaults updated to '!!'.
# Taggerist v36.07: #w.48 fix — Reduce no longer deletes camera-style dates (e.g. '2024-09-20 00-52-28-081') and their CI symbol; Reduce now recognizes any year-led date-like segment and keeps it, so Alt+R only drops genuine junk words. #w.49 fix — when the tag rows would run past the bottom of the taglist frame, the list now wraps into extra columns (horizontal scroll) instead of requiring vertical scrolling. #w.50 NEW — non-tag words enclosed in [square brackets] survive [Reduce] and [PROCESS], and each is appended to TagCandidates.txt in the config directory (created if missing) for later taglist review.
# Taggerist v36.06: #w.44 fix — the gap between tagnames was still a full line high because the v36.03 'fill to the bottom margin' rule re-stretched the spacing after the halving; the stretch is now removed so the configured gap (0.5 line) is exactly what you get. #w.45 fix — style flags were only read from column 2 of the CSV; when column 2 is present it overrides column 1, so flags written in the tag name (CHR_i^James) were ignored; flags are now read from BOTH columns, stripped from the tag identity at load (so CHR_b^Thalia no longer leaks into filenames), and inherited by the tag's aliases. #w.46 fix — Alt+C did nothing on the user's desktop (window manager reserves it); Alt+L is added as a second Clear key. #w.47 new — spinner up/down arrows enlarged (wider buttons, bigger arrows). #0.41 rev — ' Font'/' Cols' labels get one more space of padding. Startup buglog banner no longer says v35.08.
# Taggerist v36.05: #w.44 fix — the empty vertical gap between tagnames is halved (default TAGLIST_VERTICAL_SPACING now 0.5 of a line; a value already in the config still wins). #w.45 NEW — per-tag style flags in the taglist CSV: a '^' marker switches that tag's style in the taglist — b^=bold, i^=italic, fd^=default font, fc^=Ubuntu Condensed, fl^=Ubuntu Light, fm^=Ubuntu Mono (e.g. PTY_fd^hat shows 'hat' in the default font; the flag itself is never shown or saved into filenames). #w.46 NEW — shortcut keys: Alt+P=PROCESS, Alt+S=SKIP, Alt+R=Reduce, Alt+C=Clear, Alt+T=Sort Tagline, Alt+1/Alt+2/Alt+3=the three CI buttons.
# Taggerist v36.04: #w.42 fix — the CI date-prefix buttons [@]/[©] injected fragments of button-color HTML into the filename; root cause: the edit box colored each CI symbol one at a time, and the new '=' symbol then matched the '=' characters inside the color markup of already-processed symbols, shredding it; the box now wraps all symbols in a single pass so inserted markup is never re-scanned. #w.43 — every '(c)' in a filename is now automatically converted to '©' on load and on save, per user request (the ci_symbol config line is no longer needed for this).
# Taggerist v37.04: v37.03 feedback — Alt+Delete is now actually wired (the v37.03 changelog claimed it but no shortcut existed; legend + README updated); unknown-tag prompt now catches bracketed words glued to a datestamp (root cause: a pipe segment containing a date was skipped whole, so e.g. [xjunk©26.0930-1257]©datestamp never prompted — datestamps/camera dates/_wm/CI are now stripped per segment before the unknown check); [?] button background yellow; navigation rework: Alt+←/→ move between FilenameEditBox/BracketsBox/SearchBox, plain ←/→ in the Search box still walk the hot tag, ↑/↓ move up/down between boxes; taglist rows per column now fill to the bottom margin dynamically (recomputed from font size + viewport instead of tags÷columns); PROC list scrolls to the newly processed file after refresh (scroll deferred until sorting/layout completes).
# Taggerist v37.05: v37.04 feedback — NEW keystroke popup (toggle: [?] button or Alt+K; contents from an editable Taggerist_Keystrokes.txt in the config directory; draggable, position remembered; replaces the bottom-row legend and the legend-rework items; README trimmed); #w.55 fix: re-processing a PROC file whose name is unchanged is a no-op instead of a "same file" error; #w.56 fix: Down arrow from Filename/Brackets moves focus down the box stack (Up already worked); #w.62 change: unknown words appended to the CSV keep their brackets/pipes ([EastBradyBend], |foggy|); Sort Tagline now reports "no recognized tags to sort" instead of silently doing nothing; manually typed brackets in the FilenameEditBox color blue (re-render on every text change); NEW: text selected in the FilenameEditBox copies to the Search box, ESC clears both; #0.52 add: two-digit-year camera dates (19-10-13-15-05-41) treated as 20+yy when the year digits are 10-30.
# (c) @26.0830-2150.00 by AtaraxiA under Creative Commons CC BY-SA license

import re
import html
import sys
import os
import csv
import shutil
import random
import subprocess
import configparser
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QWidget,
                               QLabel, QLineEdit, QTextEdit, QPushButton, QFileDialog, QScrollArea,
                               QGridLayout, QRadioButton, QButtonGroup, QMessageBox,
                               QSplitter, QSizePolicy, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QProgressBar, QLayout,
                               QSpinBox, QCheckBox, QDialogButtonBox)
from PySide6.QtCore import Qt, QSize, QTimer, QPoint, QRect, Signal, QEvent
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor, QShortcut, QKeySequence, QFontMetrics, QPainter, QGuiApplication, QScreen, QTextCursor
from PIL import Image
import faulthandler
faulthandler.enable()

# ========== DEFAULT CONFIG ==========
DEFAULTS = {
    'TAGLIST_COLUMNS': '8',
    'TAGLIST_ROWS': '0',
    'TAGLIST_COLUMN_WIDTH': '160',
    'TAGLIST_FONT_SIZE': '12',
    'TAGLIST_SPACING': '0',
    'TAGLIST_VERTICAL_SPACING': '1',  # blank lines between tagnames (1 = one full line)
    'TAGLIST_FONT_COLOR': '#fff',
    'TAGLIST_BG_COLOR': '#000',
    'FULLWINDOW_FONT_COLOR': '#fff',
    'FULLWINDOW_BG_COLOR': '#000',
    'START_DISPLAY': '2',
    'START_MAXIMIZED': 'True',
    'CI_SYMBOL': '(c)',  # '(c)' = keep as typed; '©' = auto-convert (c) to ©
    'PROCESS_AUTO_SORT': 'True',
    'TAGLIST_DIR': os.path.expanduser("~/Pictures/TAGLISTS/"),
    'PROC_DIR': '/home/jack/Pictures/TAGGERIST/test3',
    'UNPROC_DIR': '/home/jack/Pictures/TAGGERIST/Test2',
    'CONFIGS_DIR': '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs',
    'TAGLIST_NAME_1': TAGLIST_1,
    'TAGLIST_NAME_2': TAGLIST_2,
    'TAGLIST_NAME_3': TAGLIST_3,
    'TAGLIST_ID_1': TAGLIST_ID_1,
    'TAGLIST_ID_2': TAGLIST_ID_2,
    'TAGLIST_ID_3': TAGLIST_ID_3,
    'HELP_FILE_PATH': HELP_FILE_PATH,
}

# ========== CONFIG LOADER ==========
CONFIG_SECTIONS = {
    'DIRECTORIES': [
        ('TAGLIST_NAME_1', 'Taglist 1: path,identifying-symbol,font-color,background-color'),
        ('TAGLIST_NAME_2', 'Taglist 2: path,identifying-symbol,font-color,background-color'),
        ('TAGLIST_NAME_3', 'Taglist 3: path,identifying-symbol,font-color,background-color'),
        ('PROC_DIR', 'Directory where PROCESS copies files'),
        ('UNPROC_DIR', 'Directory of files waiting to be processed'),
        ('CONFIGS_DIR', 'Directory holding this config and the .csv taglists'),
        ('HELP_FILE_PATH', 'Path of the help file shown by [?]'),
        ('TAGLIST_ID_1', 'Date identifier for taglist 1 (used only if not given in TAGLIST_NAME_1)'),
        ('TAGLIST_ID_2', 'Date identifier for taglist 2 (used only if not given in TAGLIST_NAME_2)'),
        ('TAGLIST_ID_3', 'Date identifier for taglist 3 (used only if not given in TAGLIST_NAME_3)'),
    ],
    'DISPLAY': [
        ('TAGLIST_COLUMNS', 'Max columns of tagnames (list wraps to a new column at screen bottom)'),
        ('TAGLIST_ROWS', 'Max rows per column; 0 = fit to screen height'),
        ('TAGLIST_COLUMN_WIDTH', 'Pixel width of each tagname column'),
        ('TAGLIST_FONT_SIZE', 'Font size of tagnames in TL'),
        ('TAGLIST_VERTICAL_SPACING', 'Blank lines between tagnames (1 = one full line; 0.5 = half a line; 0 = no gap)'),
        ('START_DISPLAY', 'Display number to open on'),
        ('START_MAXIMIZED', 'True or False'),
        ('CI_SYMBOL', "Date-prefix symbol: '(c)' = keep (c) as typed; '©' = auto-convert (c) to ©"),
        ('PROCESS_AUTO_SORT', 'True = [PROCESS] sorts the tagline before saving; False = saves as shown'),
    ],
    'COLORS': [
        ('TAGLIST_FONT_COLOR', 'Tagname font color'),
        ('TAGLIST_BG_COLOR', 'Taglist background color'),
        ('FULLWINDOW_FONT_COLOR', 'Window font color'),
        ('FULLWINDOW_BG_COLOR', 'Window background color'),
    ],
}


def write_default_config(config_path):
    lines = [
        '# Taggerist configuration',
        '# Lines and values are reread at every start. Delete this file to regenerate it.',
        '',
    ]
    for section, entries in CONFIG_SECTIONS.items():
        lines.append(f'[{section}]')
        for key, comment in entries:
            value = DEFAULTS[key]
            if isinstance(value, str) and ('#' in value or ';' in value):
                value = f"'{value}'"
            lines.append(f'{key} = {value}   ; {comment}')
        lines.append('')
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    except Exception as e:
        print(f"Error writing config: {e}")


def load_config(config_path):
    config = configparser.ConfigParser()
    config.read_dict({'DEFAULT': DEFAULTS})
    if not os.path.exists(config_path):
        write_default_config(config_path)
    if os.path.exists(config_path):
        try:
            config.read(config_path)
        except Exception as e:
            print(f"Error loading config: {e}")
    if not config.has_section('DIRECTORIES'):
        config.add_section('DIRECTORIES')
    return config

# ========== HELPER FUNCTION TO STRIP COMMENTS ==========
def strip_comment(value):
    if isinstance(value, str):
        v = value.strip()
        if re.fullmatch(r'#[0-9a-fA-F]{3,8}', v):
            return v
        quote = None
        cut = -1
        for i, ch in enumerate(v):
            if quote:
                if ch == quote:
                    quote = None
                continue
            if ch in ("'", '"'):
                quote = ch
            elif ch == ';' or ch == '#':
                cut = i
                break
        result = v if cut == -1 else v[:cut]
        result = result.strip()
        if len(result) >= 2 and result[0] == result[-1] and result[0] in ("'", '"'):
            result = result[1:-1]
        return result
    return value

def to_int(value, fallback):
    try:
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return fallback

def to_float(value, fallback):
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return fallback

# ========== MAIN WINDOW ==========
class TaggeristMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        try:
            import PySide6
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("--- Taggerist v37.05 startup ---\n")
                f.write("PySide6 version: " + str(getattr(PySide6, '__version__', 'unknown')) + "\n")
                f.write("Python version: " + sys.version.replace("\n", " ") + "\n")
                f.write("Qt version: " + str(getattr(PySide6.QtCore, '__version__', 'unknown')) + "\n")
        except Exception:
            pass
        configs_dir = os.path.expanduser(strip_comment(DEFAULTS['CONFIGS_DIR']))
        os.makedirs(configs_dir, exist_ok=True)
        self.config_path = os.path.join(configs_dir, "Taggerist.config.txt")
        self.config = load_config(self.config_path)
        self.current_file = None
        self.setup_ui()
        self.load_taglist_and_conversions()
        self.load_settings()
        QTimer.singleShot(100, self.move_to_display_2)

    def move_to_display_2(self):
        screens = QGuiApplication.screens()
        for screen in screens:
            if screen.size().width() == 2560 and screen.size().height() == 1440:
                self.move(screen.geometry().topLeft())
                self.showMaximized()
                return
        self.move(1600, 0)
        self.showMaximized()

    def get_config(self, section, key):
        try:
            value = self.config.get(section, key, fallback=DEFAULTS.get(key))
            return strip_comment(value)
        except:
            return DEFAULTS.get(key)

    def _config_file_only(self):
        file_cfg = configparser.ConfigParser()
        try:
            file_cfg.read(self.config_path)
        except Exception:
            pass
        return file_cfg

    def get_taglist_spec(self, number):
        file_cfg = self._config_file_only()
        for key in (f'TAGLIST_NAME_{number}', f'TAGLIST_{number}'):
            if file_cfg.has_option('DIRECTORIES', key):
                return strip_comment(file_cfg.get('DIRECTORIES', key))
        return strip_comment(self.config.get('DIRECTORIES', f'TAGLIST_NAME_{number}', fallback=DEFAULTS.get(f'TAGLIST_NAME_{number}', '')))

    def get_taglist_id(self, number):
        parts = [p.strip() for p in self.get_taglist_spec(number).split(',')]
        if len(parts) >= 4 and parts[1]:
            return parts[1]
        file_cfg = self._config_file_only()
        for key in (f'TAGLIST_ID_{number}', f'COLLECTION_ID_{number}'):
            if file_cfg.has_option('DIRECTORIES', key):
                value = strip_comment(file_cfg.get('DIRECTORIES', key))
                if value:
                    return value
        return strip_comment(self.config.get('DIRECTORIES', f'TAGLIST_ID_{number}', fallback=DEFAULTS.get(f'TAGLIST_ID_{number}', '')))

    def get_taglist_colors(self, number):
        parts = [p.strip() for p in self.get_taglist_spec(number).split(',')]
        if len(parts) >= 4:
            fg = parts[2] if len(parts) > 2 else 'white'
            bg = parts[3] if len(parts) > 3 else 'black'
        else:
            fg = parts[1] if len(parts) > 1 else 'white'
            bg = parts[2] if len(parts) > 2 else 'black'
        return fg, bg

    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.setCentralWidget(main_widget)
        self.tv = TaggeristViewer(self)
        main_layout.addWidget(self.tv, stretch=25)
        self.tl = TaggeristList(self)
        main_layout.addWidget(self.tl, stretch=55)
        self.tf = TaggeristFiles(self)
        main_layout.addWidget(self.tf, stretch=20)
        for frame in (self.tv, self.tl, self.tf):
            frame.setObjectName(frame.__class__.__name__)
            frame.setStyleSheet(f"#{frame.__class__.__name__} {{ border: 1px solid #FFFFCC; }}")
        self.apply_border_colors('#FFFFCC')
        start_maximized = self.get_config('DISPLAY', 'START_MAXIMIZED').lower() == 'true'
        if start_maximized:
            self.showMaximized()
        else:
            self.setGeometry(100, 100, 2560, 1440)
        self.setWindowFlags(
            Qt.Window | Qt.CustomizeWindowHint |
            Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint |
            Qt.WindowCloseButtonHint
        )

    def apply_border_colors(self, color):
        self.setStyleSheet(f"""
            background-color: #000;
            color: #fff;
            QFrame {{ background-color: #000; border: 1px solid {color}; }}
            QLabel {{ color: #fff; background-color: #000; }}
            QLineEdit {{ background-color: #000; color: #fff; border: 1px solid {color}; }}
            QPushButton {{ background-color: #000; color: #fff; border: 1px solid {color}; }}
            QTableWidget {{ background-color: #000; color: #fff; gridline-color: #000; }}
            QScrollArea {{ background-color: #000; border: 1px solid {color}; }}
            QRadioButton {{ color: #fff; background-color: #000; }}
            QHeaderView::section {{ background-color: #000; color: #fff; border: 1px solid {color}; }}
            QSplitter::handle {{ background-color: #000; }}
            QProgressBar {{ background-color: #000; border: 1px solid {color}; color: #000; font-weight: bold; font-size: 13px; }}
        """)
        for name in ('tv', 'tl', 'tf'):
            frame = getattr(self, name, None)
            if frame is not None:
                frame.setStyleSheet(f"#{frame.__class__.__name__} {{ border: 1px solid {color}; }}")
        tv = getattr(self, 'tv', None)
        if tv is not None and hasattr(tv, 'image_label'):
            tv.image_label.setStyleSheet(f"background-color: #000; border: 1px solid {color};")

    def load_taglist_and_conversions(self):
        self.tl.load_taglist_and_conversions()

    def refresh_taglist(self):
        try:
            self.tl.filename_edit.textChanged.disconnect()
        except:
            pass
        try:
            self.load_taglist_and_conversions()
            self.tl.populate_taglist()
            kept_text = self.tl.filename_edit.text()
            self.tl.selected_tags.clear()
            self.tl.extract_tags_from_filename(kept_text)
            self.tl.update_tag_highlights()
        finally:
            self.tl.filename_edit.textChanged.connect(self.tl.update_tag_highlights)
            self.tl.filename_edit.textChanged.connect(self.tl.update_length_monitor)
        if hasattr(self.tl, 'search_edit') and self.tl.search_edit:
            self.tl.search_edit.setFocus()

    def load_settings(self):
        proc_dir = os.path.expanduser(self.get_config('DIRECTORIES', 'PROC_DIR'))
        unproc_dir = os.path.expanduser(self.get_config('DIRECTORIES', 'UNPROC_DIR'))
        self.tf.proc_dir = proc_dir
        self.tf.unproc_dir = unproc_dir
        self.tf.proc_path_label.setText(proc_dir)
        self.tf.unproc_path_label.setText(unproc_dir)
        self.tf.refresh_lists()

    def save_settings(self):
        if not os.path.exists(os.path.dirname(self.config_path)):
            os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        if not self.config.has_section('DIRECTORIES'):
            self.config.add_section('DIRECTORIES')
        self.config.set('DIRECTORIES', 'PROC_DIR', self.tf.proc_dir)
        self.config.set('DIRECTORIES', 'UNPROC_DIR', self.tf.unproc_dir)
        updated = {'proc_dir': self.tf.proc_dir, 'unproc_dir': self.tf.unproc_dir}
        try:
            lines = []
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    lines = f.read().split('\n')
            except Exception:
                lines = []
            found = set()
            in_directories = False
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith('[') and stripped.endswith(']'):
                    in_directories = stripped.lower() == '[directories]'
                    continue
                if in_directories and '=' in line:
                    head, tail = line.split('=', 1)
                    key = head.strip().lower()
                    if key in updated:
                        comment = ''
                        if ';' in tail:
                            comment = '   ' + tail[tail.index(';'):].rstrip()
                        lines[i] = f"{head}= {updated[key]}{comment}"
                        found.add(key)
            missing = [k for k in updated if k not in found]
            if missing:
                if not any(l.strip().lower() == '[directories]' for l in lines):
                    lines.append('[DIRECTORIES]')
                idx = next((i for i, l in enumerate(lines) if l.strip().lower() == '[directories]'), len(lines) - 1)
                for k in missing:
                    lines.insert(idx + 1, f"{k} = {updated[k]}")
            with open(self.config_path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
        except Exception as e:
            print(f"Error saving config: {e}")

    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)

    def update_window_title(self):
        if self.current_file:
            self.setWindowTitle(f"Taggerist v37.05 - {os.path.basename(self.current_file)}")
        else:
            self.setWindowTitle("Taggerist v37.05")

# ========== TV (Taggerist-Viewer) ==========
class TaggeristViewer(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.current_file = None
        self.current_dir = None
        self.file_list = []
        self.current_index = -1
        self._pixmap = None
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(5, 5, 5, 5)
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("background-color: #000; border: 1px solid #FFFFCC;")
        self.image_label.setFixedWidth(600)
        self.image_label.setFixedHeight(800)
        self.image_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.image_label, stretch=1, alignment=Qt.AlignCenter)
        self.image_info_label = QLabel()
        self.image_info_label.setAlignment(Qt.AlignCenter)
        self.image_info_label.setStyleSheet("color: #fff;")
        layout.addWidget(self.image_info_label)
        nav_layout = QVBoxLayout()
        nav_layout.addStretch(0)
        top_spacer = QWidget()
        top_spacer.setFixedHeight(2 * self.image_info_label.sizeHint().height())
        nav_layout.addWidget(top_spacer)
        self.external_btn = QPushButton("External viewer")
        self.external_btn.clicked.connect(self.open_external_viewer)
        self.prev_btn = QPushButton("← Previous")
        self.prev_btn.clicked.connect(self.prev_file)
        self.next_btn = QPushButton("Next →")
        self.next_btn.clicked.connect(self.next_file)
        for btn in (self.external_btn, self.prev_btn, self.next_btn):
            btn.setFont(QFont("Ubuntu", 11, QFont.Bold))
            btn.setStyleSheet("color: #fff; background-color: #000; border: 2px solid #fff; font-weight: bold; padding: 4px 8px; text-align: right; QPushButton { text-align: right; }")
            btn.setLayoutDirection(Qt.RightToLeft)
            btn.setMinimumHeight(30)
            nav_layout.addWidget(btn)
        nav_layout.addStretch(1)
        layout.insertLayout(0, nav_layout)
        self.next_btn.setEnabled(False)
        self.prev_btn.setEnabled(False)
        QShortcut(QKeySequence(Qt.Key_Left), self, activated=self.prev_file)
        QShortcut(QKeySequence(Qt.Key_Right), self, activated=self.next_file)

    def load_file(self, filepath):
        if not os.path.exists(filepath):
            self.image_label.setText("File not found")
            return
        self.current_file = filepath
        self.current_dir = os.path.dirname(filepath)
        self.parent.current_file = filepath
        self.load_image(filepath)
        self.parent.update_window_title()
        self.parent.tl.load_image(filepath)
        self.parent.tl.update_pathname(filepath)
        self.parent.tf.highlight_current_file(filepath)
        self.file_list = [f for f in os.listdir(self.current_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        self.file_list.sort()
        if os.path.basename(filepath) in self.file_list:
            self.current_index = self.file_list.index(os.path.basename(filepath))
        else:
            self.current_index = -1
        self.next_btn.setEnabled(self.current_index < len(self.file_list) - 1)
        self.prev_btn.setEnabled(self.current_index > 0)

    def load_image(self, filepath):
        try:
            img = Image.open(filepath)
            if img.mode in ("P", "PA"):
                img = img.convert("RGBA" if "transparency" in img.info or img.mode == "PA" else "RGB")
            elif img.mode == "LA":
                img = img.convert("RGBA")
            width, height = img.size
            file_size = os.path.getsize(filepath) / 1024
            mod_date = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%Y-%m-%d %H:%M:%S")
            self.image_info_label.setText(f"{width}x{height} | {file_size:.1f} KB | Modified: {mod_date}")
            img.thumbnail((600, 800))
            temp_thumb_path = "temp_thumb.png"
            img.save(temp_thumb_path)
            pixmap = QPixmap(temp_thumb_path)
            self._pixmap = pixmap
            self.image_label.setPixmap(pixmap)
            if os.path.exists(temp_thumb_path):
                os.remove(temp_thumb_path)
        except Exception as e:
            self.image_label.setText(f"Error loading image: {e}")

    def _return_focus_to_search(self):
        tl = getattr(self.parent, 'tl', None)
        if tl is not None and getattr(tl, 'search_edit', None):
            tl.search_edit.setFocus()

    def prev_file(self):
        if self.current_index > 0:
            prev_file = os.path.join(self.current_dir, self.file_list[self.current_index - 1])
            self.load_file(prev_file)
        self._return_focus_to_search()

    def next_file(self):
        if self.current_index < len(self.file_list) - 1:
            next_file = os.path.join(self.current_dir, self.file_list[self.current_index + 1])
            self.load_file(next_file)
        self._return_focus_to_search()

    def open_external_viewer(self):
        if self.current_file:
            command = ["xdg-open", self.current_file]
            try:
                subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                QMessageBox.warning(self, "Error", "Could not open external viewer.")
        self._return_focus_to_search()

# ========== FilenameEditBox (rich text: color-coded date prefixes) ==========
class FilenameEdit(QTextEdit):
    process_requested = Signal()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.process_requested.emit()
            return
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Down and self.parent() is not None and getattr(self.parent(), 'brackets_edit', None):
            self.parent().brackets_edit.setFocus()
            return
        if event.key() in (Qt.Key_BracketLeft, Qt.Key_BracketRight):
            cursor = self.textCursor()
            plain = self.toPlainText()
            self.setText(plain)
            cursor.movePosition(QTextCursor.End)
            self.setTextCursor(cursor)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ci_colors = {}
        self.convert_ci = False
        self.setFixedHeight(84)
        self.setLineWrapMode(QTextEdit.WidgetWidth)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTabChangesFocus(True)
        self.setAlignment(Qt.AlignRight)

    def text(self):
        return self.toPlainText()

    def setText(self, plain):
        plain = plain or ''
        plain = plain.replace('(c)', '©')
        rendered = self._render_brackets(html.escape(plain), plain)
        if self.ci_colors:
            def _color(m):
                s = html.unescape(m.group(1))
                fg, bg = self.ci_colors.get(s, ('#fff', '#000'))
                return f'<span style="color:{fg}; background-color:{bg};">{m.group(1)}</span>'
            syms = sorted(self.ci_colors, key=len, reverse=True)
            pattern = '(' + '|'.join(re.escape(html.escape(s)) for s in syms) + ')'
            rendered = re.sub(pattern, _color, rendered)
        self.blockSignals(True)
        self.setHtml(rendered)
        self.blockSignals(False)
        self.textChanged.emit()

    def _unmatched_bracket(self, plain):
        opens = [i for i, ch in enumerate(plain) if ch == '[']
        closes = [i for i, ch in enumerate(plain) if ch == ']']
        if len(opens) == len(closes):
            for o, c in zip(sorted(opens), sorted(closes)):
                if c < o:
                    return o, c
            return None
        idx = (opens if len(opens) > len(closes) else closes)
        return (sorted(idx)[0], None) if len(opens) > len(closes) else (None, sorted(idx)[0])

    def _render_brackets(self, rendered, plain):
        mismatch = self._unmatched_bracket(plain)
        bad_open, bad_close = (mismatch if mismatch else (None, None))
        ci_syms = sorted(self.ci_colors, key=len, reverse=True) if self.ci_colors else []
        ci_pat = re.compile('(' + '|'.join(re.escape(s) for s in ci_syms) + ')') if ci_syms else None
        out = []
        i = 0
        n = len(plain)
        while i < n:
            ch = plain[i]
            if ch in '[]':
                color = '#FFFF00' if ((ch == '[' and i == bad_open) or (ch == ']' and i == bad_close)) else '#2020c0'
                out.append(f'<span style="color:{color};">{html.escape(ch)}</span>')
                i += 1
                continue
            if ci_pat:
                m = ci_pat.match(plain, i)
                if m:
                    seg = m.group(1)
                    fg, bg = self.ci_colors.get(seg, ('#fff', '#000'))
                    out.append(f'<span style="color:{fg}; background-color:{bg};">{html.escape(seg)}</span>')
                    i = m.end()
                    continue
            out.append(html.escape(ch))
            i += 1
        return ''.join(out)

    def clear(self):
        self.setText('')


# ========== TL (Taggerist-List) ==========
class ClickableTagLabel(QLabel):
    clicked = Signal(str)

    def __init__(self, tag, parent=None):
        super().__init__(tag, parent)
        self.tag = tag

    def mousePressEvent(self, event):
        self.clicked.emit(self.tag)
        if event is not None:
            super().mousePressEvent(event)
class TaggeristList(QFrame):
    def _ci_alt(self):
        syms = []
        for n in (1, 2, 3):
            cid = self.parent.get_taglist_id(n)
            if cid and cid not in syms:
                syms.append(cid)
        if '(c)' not in syms:
            syms.append('(c)')
        if '=' not in syms:
            syms.append('=')
        return '|'.join(re.escape(s) for s in sorted(syms, key=len, reverse=True))

    def update_date_prefix(self, symbol):
        current_filename = self.filename_edit.text()
        if not current_filename:
            return
        if symbol == '\u00a9' and '(c)' in current_filename:
            current_filename = current_filename.replace('(c)', '\u00a9')
            self.filename_edit.setText(current_filename)
        ci_alt = self._ci_alt()
        # Replace any existing CI(s) before the datestamp with the selected symbol
        new_filename, n_sub = re.subn(r'(?:' + ci_alt + r')+(?=\d{2,4}\.\d{4}-\d{4}\.)', symbol, current_filename)
        # If a datestamp exists but has no CI in front of it, insert the CI before the datestamp
        if n_sub == 0:
            m = re.search(r'\d{2,4}\.\d{4}-\d{4}\.', new_filename)
            if m:
                new_filename = new_filename[:m.start()] + symbol + new_filename[m.start():]
        # If no Taggerist datestamp present, try prefixing a recognized camera-style date with the CI symbol
        prefixed_camera_date = False
        if not re.search(r'\d{2,4}\.\d{4}-\d{4}\.\d+', new_filename):
            m_cam = re.search(r'(?P<pre>[^\d|]*)?(?P<ds>(?:19|20)\d{2}[-._ ]\d{1,2}[-._ ]\d{1,2}[-._ ]?\d{0,2}[-._ ]?\d{0,2}[-._ ]?\d{0,2}(?:[-._ ]?\d{2,3})?)', new_filename)
            if m_cam and m_cam.group('ds'):
                new_filename = new_filename[:m_cam.start('ds')] + symbol + m_cam.group('ds') + new_filename[m_cam.end('ds'):]
                prefixed_camera_date = True
        # If still no datestamp present, strip any stray CI symbol, then append current system date/timestamp with the new CI
        if not prefixed_camera_date and not re.search(r'\d{2,4}\.\d{4}-\d{4}\.\d+', new_filename):
            now = datetime.now()
            stamp = now.strftime("%y.%m%d-%H%M.%S") + f"{now.microsecond // 10000:02d}"
            base, ext = self._split_extension(new_filename)
            base = re.sub(r'(?:' + ci_alt + r')+(?=_wm$|$)', '', base)
            new_filename = f"{base}{symbol}{stamp}{ext}"
        # Ensure _wm is at the end (before the extension)
        if '_wm' in new_filename:
            root, ext = self._split_extension(new_filename)
            root = root.replace('_wm', '')
            new_filename = f"{root}_wm{ext}"
        self.filename_edit.setText(new_filename)
        self.update_tag_highlights()
        self.update_length_monitor()
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    STYLE_FLAG_CODES = {'b^': 'bold', 'i^': 'italic', 'fd^': 'default', 'fc^': 'condensed', 'fl^': 'light', 'fm^': 'mono'}

    def _parse_style_flags(self, shown):
        codes = []
        for code in ('fc^', 'fl^', 'fm^', 'fd^', 'b^', 'i^'):
            while code in shown:
                shown = shown.replace(code, '', 1)
                style = self.STYLE_FLAG_CODES[code]
                if style not in codes:
                    codes.append(style)
        return shown, codes

    def _styled_font(self, base_size, codes):
        weight = QFont.Bold if 'bold' in codes else QFont.Normal
        italic = True if 'italic' in codes else False
        family = 'Ubuntu'
        if 'condensed' in codes:
            family = 'Ubuntu Condensed'
        elif 'light' in codes:
            family = 'Ubuntu Light'
        elif 'mono' in codes:
            family = 'Ubuntu Mono'
        elif 'default' in codes:
            family = 'Ubuntu'
        return QFont(family, base_size, weight), italic

    def _display_name(self, full_tag, col2):
        if col2:
            return self._parse_style_flags(col2)[0]
        return full_tag.split('_', 1)[1] if '_' in full_tag else full_tag

    def _header_title(self, full_tag, col2):
        if col2:
            return col2
        rest = full_tag.split('_', 1)[1] if '_' in full_tag else full_tag
        cleaned = rest.replace('_', ' ').strip()
        cleaned = cleaned.lstrip('- ').strip()
        return cleaned or full_tag

    def load_taglist_and_conversions(self):
        self.all_tags = []
        self.conversion_table = {}
        self.display_names = {}
        self.tag_styles = {}
        self.header_tags = set()
        self.header_titles = {}
        self.list_tags = {n: set() for n in (1, 2, 3)}
        try:
            self.active_taglist_path = self.parent.get_taglist_spec(1).split(',')[0].strip()
        except Exception:
            self.active_taglist_path = None
        for n in (1, 2, 3):
            try:
                spec = self.parent.get_taglist_spec(n)
                conv_path = spec.split(',')[0].strip()
            except Exception:
                continue
            if not conv_path or not os.path.exists(conv_path):
                with open('Taggerist_v37.05-buglog.txt', 'a') as dbg:
                    dbg.write(f"load_taglist (list {n}): file missing or no path set: {conv_path}\n")
                continue
            try:
                with open(conv_path, mode='r') as conv_csv:
                    for row in csv.reader(conv_csv):
                        if not row:
                            continue
                        raw_tag = row[0].strip()
                        if not raw_tag or raw_tag.startswith('#'):
                            continue
                        full_tag, tag_codes = self._parse_style_flags(raw_tag)
                        col2 = row[1].strip() if len(row) > 1 else ''
                        self.list_tags[n].add(full_tag)
                        if full_tag not in self.display_names:
                            self.all_tags.append(full_tag)
                            disp, codes = self._parse_style_flags(self._display_name(full_tag, col2))
                            codes = list(dict.fromkeys(tag_codes + codes))
                            self.display_names[full_tag] = disp
                            if '___' in full_tag:
                                self.header_tags.add(full_tag)
                                self.header_titles[full_tag] = self._parse_style_flags(self._header_title(full_tag, col2))[0]
                        if tag_codes or (col2 and self._parse_style_flags(col2)[1]):
                            disp, codes = self._parse_style_flags(self._display_name(full_tag, col2))
                            merged = list(dict.fromkeys(self.tag_styles.get(full_tag, []) + tag_codes + codes))
                            if merged:
                                self.tag_styles[full_tag] = merged
                        if len(row) > 2:
                            for old_tag in row[2:]:
                                old_tag = old_tag.strip()
                                if old_tag:
                                    self.conversion_table[old_tag.lower()] = full_tag
                                    alias_disp, alias_codes = self._parse_style_flags(old_tag)
                                    if alias_codes:
                                        merged = list(dict.fromkeys(self.tag_styles.get(full_tag, []) + alias_codes))
                                        self.tag_styles[full_tag] = merged
                                    if alias_disp != old_tag:
                                        self.conversion_table[alias_disp.lower()] = full_tag
            except Exception as e:
                with open('Taggerist_v37.05-buglog.txt', 'a') as dbg:
                    dbg.write(f"load_taglist (list {n}) ERROR: {e}\n")
        self.all_tags = sorted(set(self.all_tags))
        self._build_reverse_maps()
        with open('Taggerist_v37.05-buglog.txt', 'a') as dbg:
            dbg.write(f"load_taglist: {len(self.all_tags)} tags ({len(self.header_tags)} headers), {len(self.display_names)} display names, {len(self.conversion_table)} conversions\n")
        self.populate_taglist()

    def _build_reverse_maps(self):
        self._full_set = set(self.all_tags)
        full_lower = {}
        full_lower_counts = {}
        for t in self.all_tags:
            key = t.lower()
            full_lower_counts[key] = full_lower_counts.get(key, 0) + 1
            full_lower[key] = t
        self._full_lower = full_lower
        self._full_lower_counts = full_lower_counts
        disp_exact = {}
        disp_lower = {}
        for full, disp in self.display_names.items():
            if full in self.header_tags:
                continue
            disp_exact.setdefault(disp, set()).add(full)
            disp_lower.setdefault(disp.lower(), set()).add(full)
        self.display_to_full = {d: (next(iter(s)) if len(s) == 1 else None) for d, s in disp_exact.items()}
        self.display_to_full_ci = {d: (next(iter(s)) if len(s) == 1 else None) for d, s in disp_lower.items()}

    def _resolve_tag(self, segment):
        if not segment:
            return None
        if segment in self._full_set:
            return segment
        exact = self.display_to_full.get(segment)
        if exact:
            return exact
        low = segment.lower()
        if self._full_lower_counts.get(low) == 1:
            return self._full_lower.get(low)
        ci = self.display_to_full_ci.get(low)
        if ci:
            return ci
        conv = self.conversion_table.get(low)
        return conv or None

    @staticmethod
    def _contrast_text(bg):
        try:
            c = QColor(bg)
            lum = 0.299 * c.red() + 0.587 * c.green() + 0.114 * c.blue()
            return '#000' if lum > 127 else '#fff'
        except Exception:
            return '#fff'

    def apply_border_colors(self, color):
        self.active_border_color = color
        self.filename_edit.setStyleSheet(f"background-color: #000; color: #fff; border: 1px solid {color};")
        self.length_bar.setStyleSheet(f"QProgressBar {{ background-color: #000; border: 1px solid {color}; color: #000; font-weight: bold; font-size: 13px; }} QProgressBar::chunk {{ background-color: #00cc00; }}")
        self.parent.apply_border_colors(color)


    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.selected_tags = set()
        self.all_tags = []
        self.current_mode = None
        self.conversion_table = {}
        self.list_tags = {n: set() for n in (1, 2, 3)}
        self.display_names = {}
        self.tag_styles = {}
        self.header_tags = set()
        self.header_titles = {}
        self.display_to_full = {}
        self.display_to_full_ci = {}
        self._full_set = set()
        self._full_lower = {}
        self._full_lower_counts = {}
        self.active_border_color = '#FFFFCC'
        self.taglist_columns = to_int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_COLUMNS')), 8)
        self.taglist_rows = to_int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_ROWS')), 0)
        self.taglist_column_width = to_int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_COLUMN_WIDTH')), 160)
        self.taglist_font_size = to_int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_FONT_SIZE')), 12)
        self.taglist_vertical_spacing = to_float(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_VERTICAL_SPACING')), 0.5)
        self.taglist_font_color = strip_comment(self.parent.get_config('COLORS', 'TAGLIST_FONT_COLOR')) or '#fff'
        self.taglist_bg_color = strip_comment(self.parent.get_config('COLORS', 'TAGLIST_BG_COLOR')) or '#000'
        font_metrics = QFontMetrics(QFont("Ubuntu", self.taglist_font_size))
        self.tag_height = font_metrics.height()
        self.active_taglist_path = None
        self.tag_label_refs = []
        self.setup_ui()
        self.load_taglist_and_conversions()
        self._startup_refill_done = False
        QTimer.singleShot(0, self._deferred_first_fill)

    def _deferred_first_fill(self):
        if not self._startup_refill_done:
            self._startup_refill_done = True
            self._refill_taglist()
            self._log_refill_diag()

    def _log_refill_diag(self):
        if not hasattr(self, 'grid_layout'):
            return
        n = self.grid_layout.count()
        vh = self.scroll_area.viewport().height()
        rows = getattr(self, '_last_rows_fit', 0)
        with open('Taggerist_v37.05-buglog.txt', 'a') as dbg:
            dbg.write(f"refill: {n} labels, rows_fit={rows}, viewport_h={vh}, font_color={self.taglist_font_color!r}, bg={self.taglist_bg_color!r}\n")

    def setup_ui(self):
        layout = QVBoxLayout(self)
        with open('Taggerist_v37.05-buglog.txt', 'a') as debug_file:
            debug_file.write(f"Main layout identified as: {type(layout).__name__}\n")
        top_grid = QGridLayout()
        top_grid.setSpacing(6)
        # Row 0: pathname only, flush-left (NEW.1 moves taglist buttons to a vertical column)
        self.pathname_edit = QLineEdit()
        self.pathname_edit.setReadOnly(True)
        top_grid.addWidget(self.pathname_edit, 0, 0, 1, 8)
        # Col 0, rows 1-3: CI buttons vertical (in-grid so they align exactly with the action buttons)
        self.x_btn = QPushButton()
        self.y_btn = QPushButton()
        self.z_btn = QPushButton()
        for btn in (self.x_btn, self.y_btn, self.z_btn):
            btn.setFont(QFont("Ubuntu", 11, QFont.Bold))
            btn.setMinimumHeight(30)
            btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        ci_w = max(b.sizeHint().width() for b in (self.x_btn, self.y_btn, self.z_btn)) + 16
        self.x_btn.setFixedWidth(ci_w)
        self.y_btn.setFixedWidth(ci_w)
        self.z_btn.setFixedWidth(ci_w)
        top_grid.addWidget(self.x_btn, 2, 0)
        top_grid.addWidget(self.y_btn, 3, 0)
        top_grid.addWidget(self.z_btn, 4, 0)
        # NEW (v36.01): Col 1, rows 1-3: font-size and column-count spin-controls (replace the taglist buttons)
        self.font_spin = QSpinBox()
        self.font_spin.setRange(6, 24)
        self.font_spin.setValue(self.taglist_font_size)
        self.font_spin.setFont(QFont("Ubuntu", 10, QFont.Bold))
        self.font_spin.setMinimumHeight(30)
        self.font_spin.setToolTip("Taglist font size")
        self.font_spin.valueChanged.connect(self.on_font_size_changed)
        self.columns_spin = QSpinBox()
        self.columns_spin.setRange(1, 40)
        self.columns_spin.setValue(self.taglist_columns)
        self.columns_spin.setFont(QFont("Ubuntu", 10, QFont.Bold))
        self.columns_spin.setMinimumHeight(30)
        self.columns_spin.setToolTip("Taglist columns")
        self.columns_spin.valueChanged.connect(self.on_columns_changed)
        spin_arrow_css = "QSpinBox::up-button { width: 22px; } QSpinBox::down-button { width: 22px; } QSpinBox::up-arrow { width: 12px; height: 12px; } QSpinBox::down-arrow { width: 12px; height: 12px; }"
        for spin in (self.font_spin, self.columns_spin):
            spin.setStyleSheet(spin_arrow_css)
        self.fix_date_btn = QPushButton("Fix Date")
        self.fix_date_btn.setFont(QFont("Ubuntu", 9, QFont.Bold))
        self.fix_date_btn.setMinimumHeight(30)
        self.fix_date_btn.setToolTip("Convert a camera-style date to the Taggerist datestamp (Alt+D)")
        self.fix_date_btn.clicked.connect(self.fix_camera_date)
        top_grid.addWidget(self.fix_date_btn, 4, 2)
        self.font_label = QLabel("  Font")
        self.font_label.setFont(QFont("Ubuntu", 9, QFont.Bold))
        self.columns_label = QLabel("  Cols")
        self.columns_label.setFont(QFont("Ubuntu", 9, QFont.Bold))
        top_grid.addWidget(self.font_label, 2, 1, Qt.AlignRight | Qt.AlignVCenter)
        top_grid.addWidget(self.font_spin, 2, 2)
        top_grid.addWidget(self.columns_label, 3, 1, Qt.AlignRight | Qt.AlignVCenter)
        top_grid.addWidget(self.columns_spin, 3, 2)
        # Col 2: Clear (row 1), Reduce (row 2), Sort Tagline + Skip (row 3)
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setStyleSheet("color: #fff; background-color: #000; border: 2px solid #fff; font-weight: bold; padding: 4px 10px;")
        self.reduce_btn = QPushButton("Reduce")
        self.reduce_btn.setStyleSheet("color: #fff; background-color: #000; border: 2px solid #fff; font-weight: bold; padding: 4px 10px;")
        self.sort_tags_btn = QPushButton("Sort Tagline")
        self.sort_tags_btn.setStyleSheet("color: #fff; background-color: #000; border: 2px solid #fff; font-weight: bold; padding: 4px 10px;")
        action_btn_width = self.sort_tags_btn.sizeHint().width()
        for btn in (self.clear_btn, self.reduce_btn, self.sort_tags_btn):
            btn.setFixedWidth(action_btn_width)
            btn.setMinimumHeight(30)
        top_grid.addWidget(self.clear_btn, 2, 4)
        top_grid.addWidget(self.reduce_btn, 3, 4)
        top_grid.addWidget(self.sort_tags_btn, 4, 4)
        # Col 2, rows 1-2: PROCESS (same height as the FilenameEditBox)
        self.process_btn = QPushButton("PROCESS")
        self.process_btn.setFont(QFont("Ubuntu", 18, QFont.Bold))
        self.process_btn.setStyleSheet("color: #fff; background-color: #2040c0; border: 1px solid #FFFFCC; padding: 6px 18px; font-weight: bold;")
        top_grid.addWidget(self.process_btn, 2, 6, 2, 1)
        # SKIP directly under PROCESS, same width
        self.skip_btn = QPushButton("SKIP")
        self.skip_btn.setStyleSheet("color: #fff; background-color: #e8752a; border: 1px solid #FFFFCC; font-weight: bold; padding: 4px 12px;")
        self.skip_btn.setFixedWidth(self.process_btn.sizeHint().width())
        self.skip_btn.setMinimumHeight(30)
        top_grid.addWidget(self.skip_btn, 4, 6)
        # Col 3, rows 1-2: FilenameEditBox (two rows tall, stretches right)
        self.filename_edit = FilenameEdit()
        self.filename_edit.setFont(QFont("Ubuntu", 18))
        self.filename_edit.setStyleSheet("background-color: #000; color: #fff; border: 1px solid #FFFFCC;")
        self.filename_edit.textChanged.connect(self.update_tag_highlights)
        self.filename_edit.selectionChanged.connect(self.on_filename_selection)
        self.filename_edit.textChanged.connect(self.update_length_monitor)
        self.filename_edit.process_requested.connect(self.save_and_next)
        top_grid.addWidget(self.filename_edit, 2, 7, 2, 1)
        # Row 3, col 3: thermometer under the edit box
        self.length_bar = QProgressBar()
        self.length_bar.setRange(0, 255)
        self.length_bar.setValue(0)
        self.length_bar.setTextVisible(True)
        self.length_bar.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.length_bar.setFormat("%v/255 chars.")
        self.length_bar.setFixedHeight(24)
        self.length_bar.setStyleSheet("QProgressBar { background-color: #000; border: 1px solid #FFFFCC; color: #000; font-weight: bold; font-size: 13px; } QProgressBar::chunk { background-color: #00cc00; }")
        self.length_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        top_grid.addWidget(self.length_bar, 4, 7)
        for c in range(7):
            top_grid.setColumnStretch(c, 0)
        top_grid.setColumnStretch(7, 1)
        top_grid.setRowStretch(0, 0)
        top_grid.setRowStretch(1, 0)
        top_grid.setRowStretch(2, 0)
        top_grid.setRowStretch(3, 0)
        top_grid.setRowStretch(4, 0)
        top_grid.setRowStretch(5, 0)
        layout.addLayout(top_grid, stretch=0)
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Search")
        self.search_edit.setStyleSheet("background-color: #000; color: #fff; border: 2px solid #e8752a; font-size: 14px; padding: 6px 4px;")
        self.search_edit.textChanged.connect(self.perform_search)
        self.search_edit.returnPressed.connect(self.accept_first_search_result)
        self.search_edit.keyPressEvent = self.search_keyPressEvent
        self._hot_chip = 0
        self.filename_edit.installEventFilter(self)
        self.filename_edit.setStyleSheet("background-color: #000; color: #fff; border: 2px solid #FFFFCC;")
        self.brackets_edit = QLineEdit()
        self.brackets_edit.setPlaceholderText("[Brackets]")
        bw = to_int(strip_comment(self.parent.get_config('DISPLAY', 'BRACKETS_BOX_WIDTH')), 24)
        fm40 = QFontMetrics(self.brackets_edit.font())
        self.brackets_edit.setFixedWidth(max(60, fm40.horizontalAdvance('M' * bw) + 24))
        self.brackets_edit.setStyleSheet("background-color: #000; color: #fff; border: 2px solid #2020c0; font-size: 14px; padding: 6px 4px;")
        self.brackets_edit.returnPressed.connect(self.commit_brackets_text)
        self.brackets_edit.keyPressEvent = self.brackets_keyPressEvent
        for wdg, normal in ((self.brackets_edit, '#2020c0'), (self.search_edit, '#e8752a')):
            wdg.installEventFilter(self)
        search_row = QHBoxLayout()
        search_row.addWidget(self.brackets_edit)
        search_row.addWidget(self.search_edit, stretch=1)
        # #w.59b rev: [Edit Tags]/[Refresh Tags] flush to the far right; Search fills the freed space
        self.edit_tags_btn = QPushButton("Edit Tags")
        self.edit_tags_btn.clicked.connect(self.open_current_taglist)
        self.refresh_btn = QPushButton("Refresh Tags")
        self.refresh_btn.clicked.connect(self.parent.refresh_taglist)
        for b in (self.edit_tags_btn, self.refresh_btn):
            b.setMinimumHeight(30)
            b.setStyleSheet("color: #fff; background-color: #000; border: 2px solid #fff; font-weight: bold; padding: 2px 8px;")
        search_row.addWidget(self.edit_tags_btn)
        search_row.addWidget(self.refresh_btn)
        layout.addLayout(search_row, stretch=0)
        # NEW.2: horizontal border line over the button/edit rows, flush with the TF/TV border
        hline = QFrame()
        hline.setFrameShape(QFrame.HLine)
        hline.setLineWidth(1)
        hline.setStyleSheet("color: #FFFFCC;")
        top_grid.addWidget(hline, 1, 0, 1, 8)
        # NEW.2: vertical border lines between the CI / Taglist / Tagline columns
        for col in (1, 3, 5):
            vline = QFrame()
            vline.setFrameShape(QFrame.VLine)
            vline.setLineWidth(1)
            vline.setStyleSheet("color: #FFFFCC;")
            top_grid.addWidget(vline, 2, col, 3, 1)
        self.search_results = QFrame(self)
        self.search_results.setStyleSheet("background-color: #000; border: 1px solid #FFFFCC;")
        self.search_results_layout = QHBoxLayout(self.search_results)
        self.search_results_layout.setContentsMargins(4, 4, 4, 4)
        self.search_results_layout.setSpacing(4)
        self.search_chips = []
        for _ in range(12):
            chip = ClickableTagLabel("", self.search_results)
            chip.setStyleSheet("color: #fff; background-color: #000; border: 1px solid #FFFFCC; padding: 1px 4px;")
            chip.clicked.connect(self.search_result_clicked)
            chip.hide()
            self.search_results_layout.addWidget(chip)
            self.search_chips.append(chip)
        self.search_results_layout.addStretch(1)
        self.search_results.hide()
        layout.addWidget(self.search_results, stretch=0)
        self.refresh_ci_buttons()
        # Connect buttons to their logic
        self.x_btn.clicked.connect(lambda: self.update_date_prefix(self.parent.get_taglist_id(1)))
        self.y_btn.clicked.connect(lambda: self.update_date_prefix(self.parent.get_taglist_id(2)))
        self.z_btn.clicked.connect(lambda: self.update_date_prefix(self.parent.get_taglist_id(3)))
        self.clear_btn.clicked.connect(self.clear_filename_edit)
        self.reduce_btn.clicked.connect(self.reduce_filename_edit)
        self.sort_tags_btn.clicked.connect(self.sort_filename_tags)
        self.skip_btn.clicked.connect(self.skip_file)
        self.process_btn.clicked.connect(self.save_and_next)
        QShortcut(QKeySequence('Alt+P'), self, activated=self.save_and_next)
        QShortcut(QKeySequence('Alt+S'), self, activated=self.skip_file)
        QShortcut(QKeySequence('Alt+R'), self, activated=self.reduce_filename_edit)
        QShortcut(QKeySequence('Alt+C'), self, activated=self.clear_filename_edit)
        QShortcut(QKeySequence('Alt+L'), self, activated=self.clear_filename_edit)
        QShortcut(QKeySequence('Alt+D'), self, activated=self.fix_camera_date)
        QShortcut(QKeySequence('Ctrl+Return'), self, activated=lambda: self.focus_filename_edit())
        QShortcut(QKeySequence('Escape'), self, activated=self.escape_key)
        QShortcut(QKeySequence('Alt+T'), self, activated=self.sort_filename_tags)
        QShortcut(QKeySequence('Alt+1'), self, activated=lambda: self.update_date_prefix(self.parent.get_taglist_id(1)))
        QShortcut(QKeySequence('Alt+2'), self, activated=lambda: self.update_date_prefix(self.parent.get_taglist_id(2)))
        QShortcut(QKeySequence('Alt+3'), self, activated=lambda: self.update_date_prefix(self.parent.get_taglist_id(3)))
        QShortcut(QKeySequence('Alt+Delete'), self, activated=self.clear_search_and_brackets)
        QShortcut(QKeySequence('Alt+Left'), self, activated=lambda: self._cycle_focus_box(-1))
        QShortcut(QKeySequence('Alt+Right'), self, activated=lambda: self._cycle_focus_box(1))
        QShortcut(QKeySequence('Alt+Down'), self, activated=lambda: self._cycle_focus_box(1))
        QShortcut(QKeySequence('Alt+Up'), self, activated=lambda: self._cycle_focus_box(-1))
        QShortcut(QKeySequence('Alt+K'), self, activated=self.toggle_keystroke_popup)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        self.original_filename_label = QLabel()
        self.original_filename_label.setStyleSheet("background-color: #FFFFCC; color: #000; border: 1px solid #FFFFCC;")
        self.original_filename_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.original_filename_label.setMinimumHeight(30)
        self.original_filename_label.setAlignment(Qt.AlignLeft)
        self.original_filename_label.setFont(QFont("Ubuntu", 12))
        self.original_filename_label.setWordWrap(True)
        self.original_filename_label.setTextFormat(Qt.PlainText)
        self.original_filename_label.hide()
        self.setup_taglist_window(layout)
        bottom_layout = QHBoxLayout()
        bottom_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.taglist_status_label = QLabel("0 tags")
        self.taglist_status_label.setMinimumHeight(36)
        self.taglist_status_label.setStyleSheet("color: #fff;")
        bottom_layout.addWidget(self.taglist_status_label)
        bottom_layout.addStretch()
        self.shortcut_legend_label = QLabel("Keystrokes = Alt+K or [?]")
        self.shortcut_legend_label.setAlignment(Qt.AlignCenter)
        self.shortcut_legend_label.setStyleSheet("color: #fff; font-size: 12px;")
        bottom_layout.addWidget(self.shortcut_legend_label, stretch=1)
        bottom_layout.addStretch()
        self.help_btn2 = QPushButton("?")
        self.help_btn2.clicked.connect(self.toggle_keystroke_popup)
        self.help_btn2.setStyleSheet("background-color: yellow; color: #000; font-weight: bold;")
        self.help_btn2.setFixedWidth(28)
        self.help_btn2.setMinimumHeight(36)
        bottom_layout.addWidget(self.help_btn2)
        self.help_window = None
        layout.addLayout(bottom_layout, stretch=0)

    def refresh_ci_buttons(self):
        for i, btn in enumerate([self.x_btn, self.y_btn, self.z_btn], start=1):
            cid = self.parent.get_taglist_id(i)
            label = (cid or '-').strip()
            btn.setText(label)
            fg, bg = self.parent.get_taglist_colors(i)
            btn.setStyleSheet(f"color: {fg}; background-color: {bg}; border: 2px solid #fff; font-weight: bold; padding: 2px 4px;")
            btn.setFont(QFont("Ubuntu", 11, QFont.Bold))
            fm = QFontMetrics(btn.font())
            three_chars = fm.horizontalAdvance('MMM')
            btn.setFixedWidth(max(three_chars + 12, fm.horizontalAdvance(label) + 12))
        self.filename_edit.ci_colors = {}
        self.filename_edit.convert_ci = True
        for i in (1, 2, 3):
            ident = self.parent.get_taglist_id(i)
            if ident:
                fg, bg = self.parent.get_taglist_colors(i)
                self.filename_edit.ci_colors[ident] = (fg, bg)

    def on_font_size_changed(self, value):
        self.taglist_font_size = max(6, min(24, int(value)))
        font_metrics = QFontMetrics(QFont("Ubuntu", self.taglist_font_size))
        self.tag_height = font_metrics.height()
        self._save_display_settings()
        self._refill_taglist()
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def on_columns_changed(self, value):
        self.taglist_columns = max(1, min(40, int(value)))
        self._save_display_settings()
        self._refill_taglist()
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def _save_display_settings(self):
        try:
            path = self.parent.config_path
            updated = {'taglist_font_size': str(self.taglist_font_size),
                       'taglist_columns': str(self.taglist_columns)}
            lines = []
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    lines = f.read().split('\n')
            except Exception:
                lines = []
            found = set()
            in_display = False
            for i, line in enumerate(lines):
                stripped = line.strip()
                if stripped.startswith('[') and stripped.endswith(']'):
                    in_display = stripped.lower() == '[display]'
                    continue
                if in_display and '=' in line:
                    head, tail = line.split('=', 1)
                    key = head.strip().lower()
                    if key in updated:
                        comment = ''
                        if ';' in tail:
                            comment = '   ' + tail[tail.index(';'):].rstrip()
                        lines[i] = f"{head}= {updated[key]}{comment}"
                        found.add(key)
            missing = [k for k in updated if k not in found]
            if missing:
                if not any(l.strip().lower() == '[display]' for l in lines):
                    lines.append('[DISPLAY]')
                idx = next((i for i, l in enumerate(lines) if l.strip().lower() == '[display]'), len(lines) - 1)
                for k in missing:
                    lines.insert(idx + 1, f"{k} = {updated[k]}")
            with open(path, 'w', encoding='utf-8') as f:
                f.write('\n'.join(lines))
            if self.parent.config is not None and self.parent.config.has_section('DISPLAY'):
                self.parent.config.set('DISPLAY', 'TAGLIST_FONT_SIZE', str(self.taglist_font_size))
                self.parent.config.set('DISPLAY', 'TAGLIST_COLUMNS', str(self.taglist_columns))
        except Exception as e:
            with open('Taggerist_v37.05-buglog.txt', 'a') as dbg:
                dbg.write(f"save_display_settings ERROR: {e}\n")

    def setup_taglist_window(self, layout):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setStyleSheet("background-color: #000; border: none;")
        self.scroll_area.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setViewportMargins(0, 0, 0, 0)
        layout.addWidget(self.scroll_area, stretch=1)
        self.grid_layout_widget = QWidget()
        self.grid_layout_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.grid_layout = QGridLayout(self.grid_layout_widget)
        self.grid_layout.setHorizontalSpacing(12)
        self.grid_layout.setVerticalSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.scroll_area.setWidget(self.grid_layout_widget)

    def populate_taglist(self):
        if hasattr(self, 'taglist_status_label'):
            n = len(self.all_tags)
            loaded = [n2 for n2 in (1, 2, 3) if getattr(self, 'list_tags', {}).get(n2)]
            if n:
                src = f"{len(loaded)} list{'s' if len(loaded) != 1 else ''}"
            else:
                src = "no taglists found"
            self.taglist_status_label.setText(f"{n} tags — {src}")
        self._teardown_tag_labels()
        sorted_tags = sorted(self.all_tags, key=str.casefold)
        self._pending_tags = sorted_tags
        self._refill_taglist()

    def _teardown_tag_labels(self):
        refs = getattr(self, 'tag_label_refs', [])
        self.tag_label_refs = []
        for label in refs:
            self.grid_layout.removeWidget(label)
            label.deleteLater()
        for i in reversed(range(self.grid_layout.count())):
            item = self.grid_layout.itemAt(i)
            if item and not item.widget():
                self.grid_layout.takeAt(i)

    def _refill_taglist(self):
        sorted_tags = getattr(self, '_pending_tags', [])
        self._teardown_tag_labels()
        num_tags = len(sorted_tags)
        columns = max(1, self.taglist_columns)
        spacing_px = max(0.0, self.taglist_vertical_spacing) * self.tag_height
        viewport_h = max(0, self.scroll_area.viewport().height())
        line_h = self.tag_height + spacing_px
        if self.taglist_rows > 0:
            rows_fit = int(self.taglist_rows)
        elif viewport_h > 0 and line_h > 0:
            rows_fit = max(1, int(viewport_h // line_h))
        else:
            rows_fit = max(1, -(-num_tags // columns))
        self.grid_layout_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        for r in range(getattr(self, '_last_rows_fit', 0)):
            self.grid_layout.setRowStretch(r, 0)
        self.grid_layout.setVerticalSpacing(spacing_px)
        if viewport_h > 0 and line_h > 0:
            max_rows = max(1, int(viewport_h // line_h))
            if rows_fit > max_rows:
                rows_fit = max_rows
        for i, tag in enumerate(sorted_tags):
            col = i // rows_fit
            row = i % rows_fit
            is_header = tag in self.header_tags
            shown = self.header_titles.get(tag, '') if is_header else self.display_names.get(tag, tag)
            label = ClickableTagLabel(tag)
            label.setText(shown)
            codes = self.tag_styles.get(tag, [])
            styled_font, italic = self._styled_font(self.taglist_font_size, codes) if codes else (None, False)
            if is_header:
                label.setFont(QFont("Ubuntu", self.taglist_font_size, QFont.Bold))
            elif styled_font is not None:
                label.setFont(styled_font)
                if italic:
                    f = label.font()
                    f.setItalic(True)
                    label.setFont(f)
            else:
                label.setFont(QFont("Ubuntu", self.taglist_font_size, QFont.Normal))
            if is_header:
                label.setStyleSheet(f"color: #FFFFCC; background-color: {self.taglist_bg_color}; font-weight: bold; border: none; padding: 0px; margin: 0px;")
                label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                label.setFixedHeight(self.tag_height)
                label.setFixedWidth(self.taglist_column_width)
                label.setWordWrap(False)
                label.setProperty("header_row", True)
                label.setProperty("full_tag", tag)
            else:
                label.setStyleSheet(f"color: {self.taglist_font_color}; background-color: {self.taglist_bg_color}; border: none; padding: 0px; margin: 0px;")
                label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
                label.setFixedWidth(self.taglist_column_width)
                label.setFixedHeight(self.tag_height)
                label.setWordWrap(False)
                label.setProperty("full_tag", tag)
                label.clicked.connect(self.toggle_tag)
                if tag.startswith(("PHTO_000", "PHTO_001", "PHTO_002")):
                    label.setStyleSheet(f"color: #FFFF00; background-color: {self.taglist_bg_color}; font-weight: bold; border: none; padding: 0px; margin: 0px;")
            self.tag_label_refs.append(label)
            self.grid_layout.addWidget(label, row, col)
        for r in range(rows_fit):
            self.grid_layout.setRowStretch(r, 0)
        self._last_rows_fit = rows_fit

    def toggle_tag(self, t):
        full = self._resolve_tag(t) or t
        shown = self.display_names.get(full, full)
        current_text = self.filename_edit.text()
        removed = False
        new_text = current_text
        for form in (shown, full):
            if form and f"|{form}|" in new_text:
                new_text = new_text.replace(f"|{form}|", '', 1)
                removed = True
                break
        if removed:
            self.selected_tags.discard(full)
        else:
            self.selected_tags.add(full)
            base, ext = os.path.splitext(current_text)
            new_text = f"|{shown}|{base}{ext}" if base or ext else f"|{shown}|"
        new_text = new_text.replace("||", "|")
        self.filename_edit.setText(new_text)
        self.update_tag_highlights()
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, '_pending_tags') and getattr(self, '_startup_refill_done', False):
            self._refill_taglist()

    def load_image(self, filepath):
        if not filepath:
            return
        self.original_filename = filepath
        self.original_filename_label.setText(filepath)
        self.original_filename_label.setToolTip(filepath)
        self.pathname_edit.setText(filepath)
        self.extract_tags_and_datestamp(filepath)
        converted_filename = self.convert_delimiters_to_pipes(os.path.basename(filepath))
        self.filename_edit.setText(converted_filename)
        self.selected_tags.clear()
        self.extract_tags_from_filename(converted_filename)
        self.update_tag_highlights()

    def get_ci_symbol(self):
        sym = strip_comment(self.parent.get_config('DISPLAY', 'CI_SYMBOL'))
        return '©'

    def convert_delimiters_to_pipes(self, filename):
        if not filename:
            return ""
        filename = filename.replace("(c)", "©")
        converted = filename.replace('`', '|')
        if self.conversion_table:
            parts = converted.split('|')
            for i, part in enumerate(parts):
                replacement = self.conversion_table.get(part.lower())
                if replacement:
                    parts[i] = replacement
            converted = '|'.join(parts)
        while '||' in converted:
            converted = converted.replace('||', '|')
        return converted

    def extract_tags_from_filename(self, filename):
        if not filename:
            return
        segs = [t for t in filename.split('|') if t]
        for seg in segs:
            full = self._resolve_tag(seg)
            if full:
                self.selected_tags.add(full)
        self.update_tag_highlights()

    def extract_tags_and_datestamp(self, filepath):
        if not filepath:
            return
        filename = os.path.basename(filepath)
        m = self._find_datestamp(filename)
        if m:
            self.current_mode = m.group('ci') or ''
        else:
            self.current_mode = None

    def update_filename_preview(self):
        if not hasattr(self.parent.tv, 'current_file') or not self.parent.tv.current_file:
            return
        base_filename = os.path.basename(self.parent.tv.current_file)
        self.original_filename_label.setText(self.parent.tv.current_file)
        m = self._find_datestamp(base_filename)
        if m:
            datestamp = m.group(0)
        else:
            if self.current_mode:
                base = datetime.now().strftime("%y.%m%d-%H%M.%S")
                unique_id = f"{random.randint(0, 99):02d}"
                datestamp = f"{self.current_mode}{base}{unique_id}"
            else:
                datestamp = ""
        all_tags = sorted(self.display_names.get(t, t) for t in self.selected_tags)
        tag_str = "".join([f"|{tag}|" for tag in all_tags]).replace("||", "|")
        wm_suffix = "_wm" if "_wm" in base_filename else ""
        if wm_suffix and not base_filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            wm_suffix += ".jpg"
        if wm_suffix:
            new_filename = f"{tag_str}{datestamp}{wm_suffix}.jpg" if wm_suffix == "_wm" else f"{tag_str}{datestamp}{wm_suffix}"
        else:
            new_filename = f"{tag_str}{datestamp}.jpg"
        new_filename = new_filename.replace("||", "|")
        self.filename_edit.setText(new_filename)
        self.update_tag_highlights()
        self.update_length_monitor()

    def update_pathname(self, filepath):
        if filepath:
            self.original_filename_label.setText(filepath)
            self.pathname_edit.setText(filepath)
            converted_filename = self.convert_delimiters_to_pipes(os.path.basename(filepath))
            self.filename_edit.setText(converted_filename)
            self.selected_tags.clear()
            self.extract_tags_from_filename(converted_filename)
            self.extract_tags_and_datestamp(filepath)
            self.update_tag_highlights()
        else:
            self.original_filename_label.setText("")
            self.pathname_edit.clear()
            self.filename_edit.setText("")
            self.selected_tags.clear()

    def update_tag_highlights(self):
        filename = self.filename_edit.text()
        length = len(filename)
        for i in range(self.grid_layout.count()):
            item = self.grid_layout.itemAt(i)
            if item:
                widget = item.widget()
                if widget:
                    tag = widget.property("full_tag")
                    if not tag or widget.property("header_row"):
                        continue
                    if tag in self.selected_tags:
                        widget.setStyleSheet(
                            f"color: #fff; background-color: #FFFFCC;" if length > 150 else
                            f"color: #000; background-color: #FFFFCC;" if length > 100 else
                            f"color: #000; background-color: #FFFFCC;"
                        )
                    else:
                        widget.setStyleSheet(
                            f"color: {self.taglist_font_color}; background-color: {self.taglist_bg_color};"
                            if not tag.startswith(("PHTO_000", "PHTO_001", "PHTO_002")) else
                            f"color: #FFFF00; background-color: {self.taglist_bg_color}; font-weight: bold;"
                        )

    def update_length_monitor(self):
        length = len(self.filename_edit.text())
        self.length_bar.setValue(min(length, 255))
        self.length_bar.setFormat(f"{min(length, 9999)}/255 chars.")
        if length >= 151:
            bar_color = '#ff3333'
        elif length >= 100:
            bar_color = '#ff9900'
        else:
            bar_color = '#00e600'
        self.length_bar.setStyleSheet(
            f"QProgressBar {{ background-color: #000; border: 1px solid #FFFFCC; color: #000; font-weight: bold; font-size: 13px; }}"
            f" QProgressBar::chunk {{ background-color: {bar_color}; }}")

    def perform_search(self, text):
        text = (text or '').strip()
        if not text:
            self.search_results.hide()
            return
        matches = []
        seen = set()
        disp = getattr(self, 'display_names', {})
        for tag in sorted(getattr(self, 'all_tags', []), key=str.casefold):
            if tag in getattr(self, 'header_tags', set()):
                continue
            shown = disp.get(tag, tag)
            if text.lower() in tag.lower() or text.lower() in shown.lower():
                seen.add(tag)
                matches.append(tag)
        for alias, new_tag in sorted(getattr(self, 'conversion_table', {}).items()):
            if text and text.lower() in alias.lower() and new_tag not in seen:
                seen.add(new_tag)
                matches.append(new_tag)
        self._last_match_count = len(matches)
        for idx, chip in enumerate(self.search_chips):
            if idx < len(matches):
                tag = matches[idx]
                owner = next((n for n in (1, 2, 3) if tag in getattr(self, 'list_tags', {}).get(n, ())), 1)
                fg, bg = self.parent.get_taglist_colors(owner)
                chip.setText(self.display_names.get(tag, tag))
                chip.tag = tag
                chip.setStyleSheet(f"color: {self._contrast_text(bg)}; background-color: {bg}; border: 1px solid #FFFFCC; padding: 1px 4px;")
                chip.setToolTip(f"List {owner}")
                chip.show()
            else:
                chip.setText("")
                chip.tag = None
                chip.hide()
        if not matches:
            self.search_results.hide()
            return
        self._hot_chip = 0
        self._paint_hot_chip()
        self.search_results.show()

    def accept_first_search_result(self):
        count = getattr(self, '_last_match_count', 0)
        hot = getattr(self, '_hot_chip', 0)
        chip = self.search_chips[hot] if 0 <= hot < len(self.search_chips) and self.search_chips[hot].tag else None
        if count > 0 and chip:
            self.search_result_clicked(chip.tag)
        else:
            self.search_results.hide()
            self.save_and_next()

    def search_result_clicked(self, tag):
        self.toggle_tag(tag)
        self.search_edit.clear()
        self._hot_chip = 0
        self.search_edit.setFocus()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.FocusIn:
            if obj is self.brackets_edit:
                self._set_focus_border(self.brackets_edit, '#2020c0', 'blue')
            elif obj is self.search_edit:
                self._set_focus_border(self.search_edit, '#e8752a', 'orange')
            elif obj is self.filename_edit:
                self._set_focus_border(self.filename_edit, '#FFFF00', 'yellow', thick=True)
        elif event.type() == QEvent.FocusOut:
            if obj is self.brackets_edit:
                self.brackets_edit.setStyleSheet("background-color: #000; color: #fff; border: 2px solid #2020c0; font-size: 14px; padding: 6px 4px;")
            elif obj is self.search_edit:
                self.search_edit.setStyleSheet("background-color: #000; color: #fff; border: 2px solid #e8752a; font-size: 14px; padding: 6px 4px;")
            elif obj is self.filename_edit:
                self.filename_edit.setStyleSheet("background-color: #000; color: #fff; border: 2px solid #FFFFCC;")
        return super().eventFilter(obj, event)

    def _set_focus_border(self, widget, color, name, thick=False):
        width = 4 if thick else 3
        base = "font-size: 14px; padding: 6px 4px;" if widget is not self.filename_edit else ""
        if widget is self.filename_edit:
            widget.setStyleSheet(f"background-color: #000; color: #fff; border: {width}px solid {color};")
        else:
            widget.setStyleSheet(f"background-color: #000; color: #fff; border: {width}px solid {color}; {base}")

    def commit_brackets_text(self):
        text = self.brackets_edit.text().strip()
        if text:
            current = self.filename_edit.text()
            base, ext = os.path.splitext(current)
            new_text = f"[{text}]{base}{ext}" if base or ext else f"[{text}]"
            self.filename_edit.setText(new_text)
            self._append_tag_candidates([text])
        self.brackets_edit.clear()
        self.search_edit.setFocus()

    def clear_search_and_brackets(self):
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.clear()
        if hasattr(self, 'brackets_edit') and self.brackets_edit:
            self.brackets_edit.clear()
        if hasattr(self, 'search_results') and self.search_results:
            self.search_results.hide()
        self._hot_chip = 0

    def _visible_chips(self):
        return [c for c in self.search_chips if c.tag]

    def _paint_hot_chip(self):
        hot = getattr(self, '_hot_chip', 0)
        for i, chip in enumerate(self.search_chips):
            if chip.tag is None:
                continue
            owner = next((n for n in (1, 2, 3) if chip.tag in getattr(self, 'list_tags', {}).get(n, ())), 1)
            fg, bg = self.parent.get_taglist_colors(owner)
            border = '3px solid #FFFFCC' if i == hot else '1px solid #FFFFCC'
            chip.setStyleSheet(f"color: {self._contrast_text(bg)}; background-color: {bg}; border: {border}; padding: 1px 4px;")

    def move_hot_chip(self, direction):
        chips = self._visible_chips()
        if not chips:
            return
        hot = getattr(self, '_hot_chip', 0)
        hot = max(0, min(hot + direction, len(chips) - 1))
        if direction < 0 and getattr(self, '_hot_chip', 0) == 0:
            self.brackets_edit.setFocus()
            return
        self._hot_chip = hot
        self._paint_hot_chip()

    def on_filename_selection(self):
        cursor = self.filename_edit.textCursor()
        if cursor.hasSelection():
            sel = cursor.selectedText().replace('\u2028', ' ').strip()
            if sel and hasattr(self, 'search_edit') and self.search_edit:
                self.search_edit.setText(sel)

    def escape_key(self):
        if hasattr(self, 'filename_edit') and self.filename_edit:
            cursor = self.filename_edit.textCursor()
            if cursor.hasSelection():
                cursor.clearSelection()
                self.filename_edit.setTextCursor(cursor)
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.clear()
            self.search_edit.setFocus()

    def _cycle_focus_box(self, step):
        boxes = [w for w in (self.filename_edit, self.brackets_edit, self.search_edit) if w]
        if not boxes:
            return
        focused = self.focusWidget()
        idx = -1
        for i, w in enumerate(boxes):
            if focused is w:
                idx = i
                break
        boxes[(idx + step) % len(boxes)].setFocus()

    def search_keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.move_hot_chip(1)
            return
        if event.key() == Qt.Key_Left:
            self.move_hot_chip(-1)
            return
        if event.key() == Qt.Key_Up and self.brackets_edit:
            self.brackets_edit.setFocus()
            return
        QLineEdit.keyPressEvent(self.search_edit, event)

    def brackets_keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.search_edit.setFocus()
            self._hot_chip = 0
            self._paint_hot_chip()
            return
        if event.key() == Qt.Key_Down and self.search_edit:
            self.search_edit.setFocus()
            self._hot_chip = 0
            self._paint_hot_chip()
            return
        if event.key() == Qt.Key_Up and self.filename_edit:
            self.filename_edit.setFocus()
            return
        QLineEdit.keyPressEvent(self.brackets_edit, event)

    def _normalize_tag_segments(self, filename):
        if '|' not in filename:
            return filename
        parts = filename.split('|')
        for i, part in enumerate(parts):
            full = self._resolve_tag(part)
            if full:
                parts[i] = self.display_names.get(full, full)
        return '|'.join(parts)

    def _strip_date_parts(self, text):
        text = re.sub(r'(?:' + self._ci_alt() + r')?\d{2,4}\.\d{4}-\d{4}(?:\.\d+)?', ' ', text)
        text = re.sub(r'(?:' + self._ci_alt() + r')?(?:19|20)\d{2}(?:[-._ ]+\d{1,4}){1,6}', ' ', text)
        text = text.replace('_wm', ' ')
        text = re.sub(r'(?:' + self._ci_alt() + r')+', ' ', text)
        return ' '.join(text.split())

    def _unknown_tags(self, filename):
        known = {t for n in (1, 2, 3) for t in self.list_tags.get(n, set())}
        known |= set(self.conversion_table.values())
        known |= set(self.all_tags)
        known |= set(self.display_names.values())
        known |= {t.lower() for t in known}
        unknown = []
        root, _ext = self._split_extension(filename)
        for seg in root.split('|'):
            seg = seg.strip()
            if not seg or seg.lower() in known:
                continue
            candidates = []
            for item in self._bracketed_items(seg):
                item = self._strip_date_parts(item).strip()
                if item and item.lower() not in known:
                    candidates.append(item)
            bare = self._strip_date_parts(re.sub(r'\[[^\[\]]*\]', ' ', seg)).strip()
            if bare and bare.lower() not in known:
                candidates.append(bare)
            for c in candidates:
                if c not in unknown:
                    unknown.append(c)
        return unknown

    def prompt_unknown_tags(self, filename):
        self._prompt_filename = filename
        unknown = self._unknown_tags(filename)
        if not unknown:
            return
        dlg = QDialog(self)
        dlg.setWindowTitle("Unknown tags in filename")
        dlg.setLayout(QVBoxLayout())
        dlg.layout().addWidget(QLabel("These words are not in the taglist.\nSelect the ones to ADD to the current taglist:"))
        boxes = []
        for word in unknown:
            cb = QCheckBox(word)
            cb.setChecked(True)
            dlg.layout().addWidget(cb)
            boxes.append((cb, word))
        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(dlg.accept)
        btns.rejected.connect(dlg.reject)
        dlg.layout().addWidget(btns)
        if dlg.exec() != QDialog.Accepted:
            return
        chosen = [w for cb, w in boxes if cb.isChecked()]
        if not chosen:
            return
        target = self.active_taglist_path
        if not target or not os.path.exists(target):
            QMessageBox.warning(self, "Taglist not found", "Active taglist file not found; cannot add tags.")
            return
        marked = []
        for w in chosen:
            fname = getattr(self, '_prompt_filename', filename)
            if w in self._bracketed_items(fname):
                marked.append(f"[{w}]")
            elif f"|{w}|" in fname:
                marked.append(f"|{w}|")
            else:
                marked.append(w)
        try:
            with open(target, 'a', newline='') as f:
                for w in marked:
                    f.write(f"{w},{w}\n")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not append to taglist: {e}")
            return
        self.parent.refresh_taglist()

    def save_and_next(self):
        # NEW.4: auto-sort the tagline before saving (config: PROCESS_AUTO_SORT)
        auto_sort = strip_comment(self.parent.get_config('DISPLAY', 'PROCESS_AUTO_SORT'))
        if auto_sort is not None and auto_sort.lower() == 'true':
            self.sort_filename_tags()
        new_filename = self.filename_edit.text()
        if not new_filename:
            QMessageBox.warning(self, "Error", "Filename cannot be empty")
            return
        new_filename = self._normalize_tag_segments(new_filename)
        self.prompt_unknown_tags(new_filename)
        for item in self._bracketed_items(new_filename):
            self._append_tag_candidates([item])
        if not new_filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            new_filename += ".jpg"

        old_path = self.parent.tv.current_file
        output_dir = self.parent.tf.proc_dir if self.parent.tf.proc_dir else self.parent.tv.current_dir
        new_path = os.path.join(output_dir, new_filename)

        save_error = None
        try:
            if os.path.abspath(old_path) != os.path.abspath(new_path):
                shutil.copy2(old_path, new_path)
                os.utime(new_path, (os.path.getatime(new_path), int(datetime.now().timestamp())))
                os.remove(old_path)
                self.parent.save_settings()
        except Exception as e:
            save_error = e
        self.parent.tf.refresh_lists()
        if save_error is not None:
            QMessageBox.critical(self, "Error", f"Error saving: {save_error}")
            return
        QTimer.singleShot(0, lambda fn=new_filename: self.parent.tf.scroll_to_file(fn, proc=True))
        if self.search_edit:
            self.search_edit.clear()
            self.search_edit.setFocus()

        # Clear FilenameEditBox, Pathname, and highlights
        self.filename_edit.clear()
        self.pathname_edit.clear()
        self.original_filename_label.clear()
        self.selected_tags.clear()
        self.parent.tf.highlight_current_file(None)

        # Highlight the oldest file in UNPROC
        if self.parent.tf.unproc_table.rowCount() > 0:
            oldest_row = 0
            oldest_file = self.parent.tf.unproc_table.item(oldest_row, 0).text()
            oldest_filepath = os.path.join(self.parent.tf.unproc_dir, oldest_file)
            self.parent.tv.load_file(oldest_filepath)
            self.parent.tf.highlight_current_file(oldest_filepath)

    def open_current_taglist(self):
        if (not self.active_taglist_path or not os.path.exists(self.active_taglist_path)):
            for n in (1, 2, 3):
                try:
                    path = self.parent.get_taglist_spec(n).split(',')[0].strip()
                except Exception:
                    continue
                if path and os.path.exists(path):
                    self.active_taglist_path = path
                    break
        if self.active_taglist_path and os.path.exists(self.active_taglist_path):
            subprocess.Popen(['xdg-open', self.active_taglist_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            QMessageBox.warning(self, "Taglist not found", f"Taglist file not found:\n{self.active_taglist_path}")
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def keystrokes_file_path(self):
        try:
            cfg_dir = strip_comment(self.parent.get_config('DIRECTORIES', 'CONFIGS_DIR'))
        except Exception:
            cfg_dir = ''
        if not cfg_dir or not os.path.isdir(os.path.expanduser(cfg_dir)):
            cfg_dir = os.path.dirname(self.parent.config_path) or '.'
        return os.path.join(os.path.expanduser(cfg_dir), 'Taggerist_Keystrokes.txt')

    def default_keystrokes_text(self):
        return (
            "PROCESS / SKIP\n"
            "Process = Alt+P (or Enter)\n"
            "Skip = Alt+S\n"
            "\n"
            "FILENAME\n"
            "Sort Filename = Alt+T\n"
            "Reduce = Alt+R\n"
            "Clear Filename = Alt+L or Alt+C\n"
            "Fix Date = Alt+D\n"
            "\n"
            "BOXES\n"
            "Focus Boxes = Alt+Arrow keys\n"
            "Brackets to Search = Arrow Down\n"
            "Search to Brackets = Arrow Up\n"
            "Filename to Brackets = Arrow Down\n"
            "Clear Search+Brackets = Alt+Delete\n"
            "Search Box = Esc (also clears selection + Search)\n"
            "Filename Box = Ctrl+Enter\n"
            "\n"
            "TAGS\n"
            "Hot tag = Arrow Left / Arrow Right (in Search)\n"
            "Accept hot tag = Enter\n"
            "CI buttons = Alt+1 / Alt+2 / Alt+3\n"
            "\n"
            "HELP\n"
            "This popup = Alt+K or [?]"
        )

    def _save_config_line(self, section, key, value):
        cfg_path = self.parent.config_path
        lines = []
        try:
            with open(cfg_path, 'r', encoding='utf-8') as f:
                lines = f.read().split('\n')
        except Exception:
            lines = []
        want = f"{key} = {value}"
        cur_section = None
        replaced = False
        for i, line in enumerate(lines):
            stripped = line.strip()
            if stripped.startswith('[') and stripped.endswith(']'):
                cur_section = stripped.strip('[]').lower()
                continue
            if cur_section == section.lower() and '=' in line:
                head = line.split('=', 1)[0].strip().lower()
                if head == key.lower():
                    lines[i] = want
                    replaced = True
                    break
        if not replaced:
            idx = next((i for i, l in enumerate(lines) if l.strip().lower() == '[' + section.lower() + ']'), None)
            if idx is None:
                lines.append('[' + section + ']')
                idx = len(lines) - 1
            lines.insert(idx + 1, want)
        with open(cfg_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))

    def toggle_keystroke_popup(self):
        if getattr(self, 'keystroke_window', None) is not None:
            self.keystroke_window.close()
            return
        path = self.keystrokes_file_path()
        text = None
        if os.path.exists(path):
            try:
                text = open(path, 'r', encoding='utf-8').read()
            except Exception:
                text = None
        if not text or not text.strip():
            text = self.default_keystrokes_text()
            try:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(text)
            except Exception:
                pass
        from PySide6.QtWidgets import QTextBrowser
        win = QWidget(self, Qt.Tool)
        win.setWindowTitle('Taggerist Keystrokes')
        lay = QVBoxLayout(win)
        lay.setContentsMargins(4, 4, 4, 4)
        browser = QTextBrowser()
        browser.setPlainText(text)
        browser.setStyleSheet('color: #fff; background-color: #000; font-size: 13px;')
        lay.addWidget(browser)
        btn = QPushButton('Close')
        btn.clicked.connect(win.close)
        btn.setStyleSheet('color: #000; background-color: yellow; font-weight: bold;')
        lay.addWidget(btn)
        win.resize(340, 520)
        try:
            geo = strip_comment(self.parent.get_config('DISPLAY', 'KEYSTROKE_POPUP_GEOMETRY'))
            if geo:
                win.restoreGeometry(bytes.fromhex(geo))
        except Exception:
            pass
        def _closing(event):
            try:
                self._save_config_line('DISPLAY', 'KEYSTROKE_POPUP_GEOMETRY',
                                       win.saveGeometry().toHex().data().decode())
            except Exception:
                pass
            event.accept()
        win.closeEvent = _closing
        win.show()
        self.keystroke_window = win
        self.keystroke_window.destroyed.connect(lambda: None if not hasattr(self, 'keystroke_window') else setattr(self, 'keystroke_window', None))

    def open_readme(self):
        help_path = os.path.expanduser(strip_comment(self.parent.get_config('DIRECTORIES', 'HELP_FILE_PATH')))
        if os.path.exists(help_path):
            subprocess.Popen(['xdg-open', help_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            QMessageBox.warning(self, "Help file not found", f"Help file not found:\n{help_path}")
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def _split_extension(self, filename):
        m = re.search(r'\.(jpe?g|png)$', filename, re.IGNORECASE)
        if m:
            return filename[:m.start()], m.group(0)
        return filename, ''

    def _find_datestamp(self, root):
        return re.search(r'(?P<ci>(?:' + self._ci_alt() + r'))?(?P<ds>\d{2,4}\.\d{4}-\d{4}\.\d+)', root)

    def focus_filename_edit(self):
        self.filename_edit.setFocus()
        cursor = self.filename_edit.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.filename_edit.setTextCursor(cursor)

    def fix_camera_date(self):
        filename = self.filename_edit.text()
        if not filename:
            return
        root, ext = self._split_extension(filename)
        if re.search(r'\d{2,4}\.\d{4}-\d{4}\.\d+', root):
            QMessageBox.information(self, "Already a Taggerist datestamp", "This filename already carries a Taggerist datestamp (yy.mmdd-hhmm.ssnn) — nothing to convert.\n\n[Fix Date] only converts camera-style dates like 2024-09-20 00-52-28.")
            return
        m = re.search(r'(?P<ci>(?:' + self._ci_alt() + r'))?(?P<ds>(?:19|20)\d{2}(?:[-._ ]+\d{1,4}){1,6})', root)
        if not m:
            m2 = re.search(r'(?P<ci>(?:' + self._ci_alt() + r'))?(?P<ds>(?:1[0-9]|2[0-9]|30)(?:[-._ ]+\d{1,4}){2,6})', root)
            if m2 and 10 <= int(re.split(r'[-._ ]+', m2.group('ds'))[0]) <= 30:
                ds = '20' + m2.group('ds')
                root = root[:m2.start('ds')] + ds + root[m2.end('ds'):]
                m = re.search(r'(?P<ci>(?:' + self._ci_alt() + r'))?(?P<ds>(?:19|20)\d{2}(?:[-._ ]+\d{1,4}){1,6})', root)
        if not m:
            QMessageBox.information(self, "No camera date found", "No camera-style date (like 2024-09-20 00-52-28) found in the filename.\n\nIf the file has no time part, the converted stamp uses zeros for time.")
            return
        parts = re.split(r'[-._ ]+', m.group('ds'))
        def p2(i):
            return parts[i].lstrip('0').zfill(2) if len(parts) > i and parts[i] else '00'
        yy = parts[0][2:]
        stamp = f"{yy}.{p2(1)}{p2(2)}-{p2(3)}{p2(4)}.{p2(5)}" + (parts[6] if len(parts) > 6 and parts[6] else '00')
        new_root = root[:m.start()] + (m.group('ci') or '') + stamp + root[m.end():]
        self.filename_edit.setText(new_root + ext)
        self.update_tag_highlights()
        self.update_length_monitor()
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def _is_date_like(self, seg):
        if not seg:
            return False
        if re.search(r'(?P<ci>(?:' + self._ci_alt() + r'))?(?P<ds>\d{2,4}\.\d{4}-\d{4}\.\d+)', seg):
            return True
        if re.search(r'(?:^|[^\d])(19|20)\d{2}[-._ ]?\d{1,2}[-._ ]?\d{1,2}', seg):
            return True
        if re.search(r'(?:^|[^\d])(1[0-9]|2[0-9]|30)[-._ ]+\d{1,2}[-._ ]+\d{1,2}([-._ ]+\d{1,2}){1,4}', seg):
            return True
        if re.fullmatch(r'(?:' + self._ci_alt() + r')?', seg):
            return True
        return False

    def _bracketed_items(self, text):
        return re.findall(r'\[([^\[\]]*)\]', text)

    def _append_tag_candidates(self, items):
        for item in items:
            item = item.strip()
            if not item:
                continue
            try:
                cfg_dir = strip_comment(self.parent.get_config('DIRECTORIES', 'CONFIGS_DIR'))
            except Exception:
                cfg_dir = ''
            if not cfg_dir or not os.path.isdir(os.path.expanduser(cfg_dir)):
                cfg_dir = os.path.dirname(self.parent.config_path) or '.'
            path = os.path.join(os.path.expanduser(cfg_dir), 'TagCandidates.txt')
            try:
                existing = ''
                if os.path.exists(path):
                    with open(path, 'r', encoding='utf-8') as f:
                        existing = f.read()
                if item not in existing.split('\n'):
                    with open(path, 'a', encoding='utf-8') as f:
                        f.write(item + '\n')
            except Exception as e:
                with open('Taggerist_v37.05-buglog.txt', 'a') as dbg:
                    dbg.write(f"tag_candidates ERROR: {e}\n")

    def sort_filename_tags(self):
        filename = self.filename_edit.text()
        if not filename:
            return
        root, ext = self._split_extension(filename)
        root = root.replace('`', '|')
        m = self._find_datestamp(root)
        ds = ''
        if m:
            ds = (m.group('ci') or '') + m.group('ds')
            root = root.replace(m.group(0), '', 1)
        wm = '_wm' if '_wm' in root else ''
        root = root.replace('_wm', '')
        parts = [p for p in root.split('|') if p]
        known = {t.lower() for t in self.all_tags}
        known.update(v.lower() for v in self.display_names.values())
        known.update(self.conversion_table)
        known.update(str(v).lower() for v in self.conversion_table.values())
        first_tag_idx = next((i for i, p in enumerate(parts) if p.lower() in known), None)
        if first_tag_idx is None:
            QMessageBox.information(self, "Sort Tagline", "No recognized tags in this filename to sort.\n\nWords not in any taglist are left in place; add them to a taglist first (the PROCESS prompt can do it).")
            if hasattr(self, 'search_edit') and self.search_edit:
                self.search_edit.setFocus()
            return
        leading = parts[:first_tag_idx]
        tags = [p for p in parts[first_tag_idx:] if p.lower() in known]
        trailing = [p for p in parts[first_tag_idx:] if p.lower() not in known]
        sorted_tags = sorted(tags, key=str.lower)
        new_name = '|'.join(leading + sorted_tags + trailing)
        if not leading:
            new_name = '|' + new_name
        if ds:
            new_name += '|' + ds
        elif not trailing:
            new_name += '|'
        while '||' in new_name:
            new_name = new_name.replace('||', '|')
        new_name += wm + ext
        self.filename_edit.setText(new_name)
        self.update_tag_highlights()
        self.update_length_monitor()
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def clear_filename_edit(self):
        filename = self.filename_edit.text()
        if not filename:
            return
        root, ext = self._split_extension(filename)
        m = self._find_datestamp(root)
        kept = ''
        if m:
            kept = (m.group('ci') or '') + m.group('ds')
        if '_wm' in root and '_wm' not in kept:
            kept += '_wm'
        self.selected_tags.clear()
        self.filename_edit.setText(kept + ext)
        self.extract_tags_from_filename(kept + ext)
        self.update_tag_highlights()
        self.update_length_monitor()
        self.clear_search_and_brackets()
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def reduce_filename_edit(self):
        filename = self.filename_edit.text()
        if not filename:
            return
        root, ext = self._split_extension(filename)
        m = self._find_datestamp(root)
        kept = ''
        if m:
            kept = (m.group('ci') or '') + m.group('ds')
            root = root.replace(m.group(0), '', 1)
        result = ''
        root = root.replace('`', '|')
        if '|' in root:
            segments = root.split('|')
            segments[-1] = segments[-1].replace('_wm', '')
            known = {t for n in (1, 2, 3) for t in self.list_tags.get(n, set())}
            known |= set(self.conversion_table.values())
            known |= set(self.all_tags)
            known |= set(self.display_names.values())
            known |= {t.lower() for t in known}
            words = [s.strip('`') for s in segments if s.strip('`')]
            tags = []
            dropped = []
            date_likes = []
            for t in words:
                if t.lower() in known:
                    tags.append(t)
                elif '[' in t and ']' in t:
                    for item in self._bracketed_items(t):
                        self._append_tag_candidates([item])
                    kept_parts = re.findall(r'\[[^\[\]]*\]', t)
                    remainder = re.sub(r'\[[^\[\]]*\]', '', t).strip()
                    if remainder and remainder.lower() in known:
                        tags.append(remainder)
                    elif remainder and self._is_date_like(remainder):
                        date_likes.append(remainder)
                    elif remainder:
                        dropped.append(remainder)
                    date_likes.extend(kept_parts)
                elif self._is_date_like(t):
                    date_likes.append(t)
                else:
                    dropped.append(t)
            with open('Taggerist_v37.05-buglog.txt', 'a') as dbg:
                dbg.write(f"reduce: known-tag pool = {len(known)} (list_tags: {sum(len(v) for v in self.list_tags.values())}, conversions: {len(self.conversion_table)}, all_tags: {len(self.all_tags)})\n")
                for t in tags:
                    dbg.write(f"reduce: kept '{t}'\n")
                for t in dropped:
                    dbg.write(f"reduce: dropped '{t}' (not found in any taglist)\n")
            if tags:
                result = '|' + '|'.join(tags) + '|'
            if date_likes:
                result += '|'.join(date_likes) + '|'
        result += kept
        if '_wm' in filename and '_wm' not in result:
            result += '_wm'
        self.selected_tags.clear()
        self.filename_edit.setText(result + ext)
        self.extract_tags_from_filename(result + ext)
        self.update_tag_highlights()
        self.update_length_monitor()
        self.clear_search_and_brackets()
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

    def skip_file(self):
        if not self.parent.tv.current_file:
            return

        # Update modification time to current system time
        try:
            current_time = int(datetime.now().timestamp())
            os.utime(self.parent.tv.current_file, (current_time, current_time))
            self.parent.tf.refresh_lists()
            self.parent.save_settings()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error updating modification time: {e}")
            return

        # Clear FilenameEditBox, Pathname, and highlights
        converted_filename = self.convert_delimiters_to_pipes(os.path.basename(self.parent.tv.current_file))
        self.filename_edit.setText(converted_filename)
        self.selected_tags.clear()
        self.extract_tags_from_filename(converted_filename)
        self.parent.tf.highlight_current_file(None)
        if hasattr(self, 'search_edit') and self.search_edit:
            self.search_edit.setFocus()

        # Highlight the oldest file in UNPROC
        if self.parent.tf.unproc_table.rowCount() > 0:
            oldest_row = 0
            oldest_file = self.parent.tf.unproc_table.item(oldest_row, 0).text()
            oldest_filepath = os.path.join(self.parent.tf.unproc_dir, oldest_file)
            self.parent.tv.load_file(oldest_filepath)
            self.parent.tf.highlight_current_file(oldest_filepath)

# ========== TF (Taggerist-Files) ==========
class TaggeristFiles(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.proc_dir = os.path.expanduser(self.parent.get_config('DIRECTORIES', 'PROC_DIR'))
        self.unproc_dir = os.path.expanduser(self.parent.get_config('DIRECTORIES', 'UNPROC_DIR'))
        self.current_file_in_proc = None
        self.current_file_in_unproc = None
        self.setup_ui()
        self.refresh_lists()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        # NEW.7: 'The TAGGERIST' title block at the top of TF
        title_label = QLabel("The TAGGERIST")
        title_label.setFont(QFont("Ubuntu", 14, QFont.Bold))
        title_label.setAlignment(Qt.AlignRight)
        title_label.setStyleSheet("color: #fff; background-color: #000; padding: 2px 0px;")
        layout.addWidget(title_label)
        byline_label = QLabel("by AtaraxiA and Vibe")
        byline_label.setFont(QFont("Ubuntu", 9, italic=True))
        byline_label.setAlignment(Qt.AlignRight)
        byline_label.setStyleSheet("color: #fff; background-color: #000; padding: 0px 0px 4px 0px;")
        layout.addWidget(byline_label)
        title_sep = QFrame()
        title_sep.setFrameShape(QFrame.HLine)
        title_sep.setLineWidth(1)
        title_sep.setStyleSheet("color: #FFFFCC;")
        layout.addWidget(title_sep)
        splitter = QSplitter(Qt.Vertical)
        splitter.setHandleWidth(0)
        layout.addWidget(splitter)

        # PROC Pane
        self.proc_frame = QFrame()
        self.proc_layout = QVBoxLayout(self.proc_frame)
        self.proc_label = QLabel("PROCESSED")
        self.proc_label.setStyleSheet("color: #fff; background-color: #cc0000; font-weight: bold; padding: 2px 6px;")
        self.proc_layout.addWidget(self.proc_label)
        proc_header_layout = QHBoxLayout()
        self.proc_open_btn = QPushButton("OPEN")
        self.proc_open_btn.setFixedWidth(80)
        self.proc_open_btn.clicked.connect(lambda: self.open_directory("proc"))
        proc_header_layout.addWidget(self.proc_open_btn)
        self.proc_path_label = QLabel(self.proc_dir)
        self.proc_path_label.setAlignment(Qt.AlignRight)
        self.proc_path_label.setStyleSheet("color: #fff; font-weight: bold;")
        proc_header_layout.addWidget(self.proc_path_label)
        self.proc_layout.addLayout(proc_header_layout)
        self.proc_table = QTableWidget()
        self.proc_table.setColumnCount(4)
        self.proc_table.setHorizontalHeaderLabels(["Filename", "Size", "Type", "Modified"])
        self.proc_table.setStyleSheet("background-color: #000; color: #fff;")
        self.proc_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.proc_table.setSelectionMode(QTableWidget.SingleSelection)
        self.proc_table.horizontalHeader().setStretchLastSection(False)
        self.proc_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.proc_table.setSortingEnabled(True)
        self.proc_table.horizontalHeader().sectionClicked.connect(lambda index: self.sort_table(self.proc_table, index))
        self.proc_table.itemDoubleClicked.connect(self.load_file_from_proc)
        self.proc_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.proc_layout.addWidget(self.proc_table)

        # Set column widths: 80%, 10%, 10%, 100px
        self.proc_table.setColumnWidth(0, int(self.proc_table.width() * 0.8))
        self.proc_table.setColumnWidth(1, int(self.proc_table.width() * 0.1))
        self.proc_table.setColumnWidth(2, int(self.proc_table.width() * 0.1))
        self.proc_table.setColumnWidth(3, 100)

        # UNPROC Pane
        self.unproc_frame = QFrame()
        self.unproc_layout = QVBoxLayout(self.unproc_frame)
        # [Default Sort All] row above UNPROCESSED, right-justified
        self.sort_all_btn = QPushButton("Default Sort All")
        self.sort_all_btn.setFont(QFont("Ubuntu", 9))
        self.sort_all_btn.setStyleSheet("border: 1px solid #FFFFCC;")
        self.sort_all_btn.clicked.connect(self.default_sort_all)
        sort_all_row = QHBoxLayout()
        sort_all_row.addStretch(1)
        sort_all_row.addWidget(self.sort_all_btn)
        self.unproc_layout.addLayout(sort_all_row)
        self.unproc_label = QLabel("UNPROCESSED")
        self.unproc_label.setStyleSheet("color: #fff; background-color: #008800; font-weight: bold; padding: 2px 6px;")
        self.unproc_layout.addWidget(self.unproc_label)
        unproc_header_layout = QHBoxLayout()
        self.unproc_open_btn = QPushButton("OPEN")
        self.unproc_open_btn.setFixedWidth(80)
        self.unproc_open_btn.clicked.connect(lambda: self.open_directory("unproc"))
        unproc_header_layout.addWidget(self.unproc_open_btn)
        self.unproc_path_label = QLabel(self.unproc_dir)
        self.unproc_path_label.setAlignment(Qt.AlignRight)
        self.unproc_path_label.setStyleSheet("color: #fff; font-weight: bold;")
        unproc_header_layout.addWidget(self.unproc_path_label)
        self.unproc_layout.addLayout(unproc_header_layout)
        
        self.unproc_table = QTableWidget()
        self.unproc_table.setColumnCount(4)
        self.unproc_table.setHorizontalHeaderLabels(["Filename", "Size", "Type", "Modified"])
        self.unproc_table.setStyleSheet("background-color: #000; color: #fff;")
        self.unproc_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.unproc_table.setSelectionMode(QTableWidget.SingleSelection)
        self.unproc_table.horizontalHeader().setStretchLastSection(False)
        self.unproc_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.unproc_table.setSortingEnabled(True)
        self.unproc_table.horizontalHeader().sectionClicked.connect(lambda index: self.sort_table(self.unproc_table, index))
        self.unproc_table.itemDoubleClicked.connect(self.load_file_from_unproc)
        self.unproc_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.unproc_layout.addWidget(self.unproc_table)

        # Set column widths: 80%, 10%, 10%, 100px
        self.unproc_table.setColumnWidth(0, int(self.unproc_table.width() * 0.8))
        self.unproc_table.setColumnWidth(1, int(self.unproc_table.width() * 0.1))
        self.unproc_table.setColumnWidth(2, int(self.unproc_table.width() * 0.1))
        self.unproc_table.setColumnWidth(3, 100)

        splitter.addWidget(self.proc_frame)
        splitter.addWidget(self.unproc_frame)
        splitter.setSizes([1, 1])

        self.proc_table.itemClicked.connect(self.handle_single_click)
        # Clear highlights in both tables at startup
        self.clear_highlights(self.proc_table)
        self.clear_highlights(self.unproc_table)

        # Disable alternating row colors for both tables
        self.proc_table.setAlternatingRowColors(False)
        self.unproc_table.setAlternatingRowColors(False)

        # Set default background color for all rows to black
        for row in range(self.proc_table.rowCount()):
            for col in range(self.proc_table.columnCount()):
                item = self.proc_table.item(row, col)
                if item:
                    item.setBackground(QColor("#000"))
        for row in range(self.unproc_table.rowCount()):
            for col in range(self.unproc_table.columnCount()):
                item = self.unproc_table.item(row, col)
                if item:
                    item.setBackground(QColor("#000"))

        self.unproc_table.itemClicked.connect(self.handle_single_click)
    def highlight_current_file(self, filepath):
        # Clear all highlights in both tables
        for row in range(self.proc_table.rowCount()):
            for col in range(self.proc_table.columnCount()):
                if self.proc_table.item(row, col):
                    self.proc_table.item(row, col).setBackground(QColor(53, 53, 53))
        for row in range(self.unproc_table.rowCount()):
            for col in range(self.unproc_table.columnCount()):
                if self.unproc_table.item(row, col):
                    self.unproc_table.item(row, col).setBackground(QColor(53, 53, 53))

        # Highlight the current file in the appropriate table
        if filepath:
            basename = os.path.basename(filepath)
            for row in range(self.proc_table.rowCount()):
                if self.proc_table.item(row, 0) and self.proc_table.item(row, 0).text() == basename:
                    for col in range(self.proc_table.columnCount()):
                        if self.proc_table.item(row, col):
                            self.proc_table.item(row, col).setBackground(QColor(100, 100, 200))
            for row in range(self.unproc_table.rowCount()):
                if self.unproc_table.item(row, 0) and self.unproc_table.item(row, 0).text() == basename:
                    for col in range(self.unproc_table.columnCount()):
                        if self.unproc_table.item(row, col):
                            self.unproc_table.item(row, col).setBackground(QColor(100, 100, 200))

    def sort_table(self, table, column):
        # Initialize sort order tracking dictionary if it doesn't exist
        if not hasattr(self, 'sort_orders'):
            self.sort_orders = {}
        
        # Get the current sort order for the column, default to AscendingOrder
        current_order = self.sort_orders.get(column, Qt.AscendingOrder)
        current_section = table.horizontalHeader().sortIndicatorSection()
        
        # Debugging: Log current state
        with open('Taggerist_v12k-14-Buglog.txt', 'a') as f:
            f.write("sort_table called: column=" + str(column) + ", current_order=" + str(current_order) + ", current_section=" + str(current_section) + "\n")
        
        # Toggle the sort order
        new_order = Qt.DescendingOrder if current_order == Qt.AscendingOrder else Qt.AscendingOrder
        
        # Debugging: Log new order
        with open('Taggerist_v12k-14-Buglog.txt', 'a') as f:
            f.write("  -> new_order=" + str(new_order) + "\n")
        
        # Update the sort order tracking
        self.sort_orders[column] = new_order
        
        table.sortItems(column, new_order)
        table.horizontalHeader().setSortIndicator(column, new_order)
        
        # Debugging: Log after sorting and setting the indicator
        with open('Taggerist_v12k-14-Buglog.txt', 'a') as f:
            f.write("  -> Applied sort: column=" + str(column) + ", order=" + str(new_order) + "\n")
            f.write("  -> Sort indicator set to column=" + str(column) + ", order=" + str(new_order) + "\n\n")

    def load_file_from_proc(self, item):
        row = item.row()
        filepath = os.path.join(self.proc_dir, self.proc_table.item(row, 0).text())
        self.parent.tv.load_file(filepath)

    def load_file_from_unproc(self, item):
        row = item.row()
        filepath = os.path.join(self.unproc_dir, self.unproc_table.item(row, 0).text())
        self.parent.tv.load_file(filepath)

    def open_directory(self, pane_type):
        dir_path = QFileDialog.getExistingDirectory(self, f"Select {pane_type.upper()} Directory")
        if dir_path:
            if pane_type == "proc":
                self.proc_dir = dir_path
                self.proc_path_label.setText(dir_path)
                self.refresh_proc_list()
            else:
                self.unproc_dir = dir_path
                self.unproc_path_label.setText(dir_path)
                self.refresh_unproc_list()
            self.parent.save_settings()

    def filename_tooltip(self, item):
        text = item.text()
        wrapped = ''
        line = ''
        for word in text.split(' '):
            if len(line) + len(word) + 1 > 60:
                wrapped += line.rstrip() + '\n'
                line = ''
            line += word + ' '
        wrapped += line.rstrip()
        item.setToolTip(wrapped.strip())

    def refresh_proc_list(self):
        self.proc_table.setSortingEnabled(False)
        self.proc_table.setRowCount(0)
        if os.path.exists(self.proc_dir):
            files = self.get_image_files_with_dates(self.proc_dir)
            for filename, size, filetype, mod_date in files:
                row = self.proc_table.rowCount()
                self.proc_table.insertRow(row)
                self.proc_table.setItem(row, 0, QTableWidgetItem(filename))
                self.filename_tooltip(self.proc_table.item(row, 0))
                self.proc_table.setItem(row, 1, QTableWidgetItem(size))
                self.proc_table.setItem(row, 2, QTableWidgetItem(filetype))
                self.proc_table.setItem(row, 3, QTableWidgetItem(mod_date))
                for col in range(self.proc_table.columnCount()):
                    if self.proc_table.item(row, col):
                        self.proc_table.item(row, col).setBackground(QColor(53, 53, 53))
        self.proc_table.setSortingEnabled(True)
        # Sort by modification date (oldest first)
        self.proc_table.sortItems(3, Qt.AscendingOrder)

    def refresh_unproc_list(self):
        self.unproc_table.setSortingEnabled(False)
        self.unproc_table.setRowCount(0)
        if os.path.exists(self.unproc_dir):
            files = self.get_image_files_with_dates(self.unproc_dir)
            for filename, size, filetype, mod_date in files:
                row = self.unproc_table.rowCount()
                self.unproc_table.insertRow(row)
                self.unproc_table.setItem(row, 0, QTableWidgetItem(filename))
                self.filename_tooltip(self.unproc_table.item(row, 0))
                self.unproc_table.setItem(row, 1, QTableWidgetItem(size))
                self.unproc_table.setItem(row, 2, QTableWidgetItem(filetype))
                self.unproc_table.setItem(row, 3, QTableWidgetItem(mod_date))
                for col in range(self.unproc_table.columnCount()):
                    if self.unproc_table.item(row, col):
                        self.unproc_table.item(row, col).setBackground(QColor(53, 53, 53))
        self.unproc_table.setSortingEnabled(True)
        # Sort by modification date (oldest first)
        self.unproc_table.sortItems(3, Qt.AscendingOrder)

    def default_sort_all(self):
        for table in (self.proc_table, self.unproc_table):
            table.setSortingEnabled(False)
        self.proc_table.sortItems(3, Qt.AscendingOrder)
        self.unproc_table.sortItems(3, Qt.AscendingOrder)
        self.proc_table.setSortingEnabled(True)
        self.unproc_table.setSortingEnabled(True)
        self.sort_orders = {3: Qt.AscendingOrder}
        if hasattr(self.parent, 'tl') and self.parent.tl.search_edit:
            self.parent.tl.search_edit.setFocus()

    def scroll_to_file(self, filename, proc=True):
        table = self.proc_table if proc else self.unproc_table
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item and item.text() == filename:
                table.scrollToItem(item, QTableWidget.PositionAtCenter)
                return

    def refresh_lists(self):
        self.refresh_proc_list()
        self.refresh_unproc_list()
            
    
    
    
    
    
    
    
    
    
    
    
    def handle_single_click(self, item):
        try:
            # Debugging: Log the start of the single-click handler
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("handle_single_click called at " + str(datetime.now()) + "\n")

            # Get the table and row that was clicked
            table = self.sender()
            row = item.row()

            # Debugging: Log the table object ID
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("  -> Clicked table ID: " + str(id(table)) + "\n")

            # Get the filename from the clicked row
            filename_item = table.item(row, 0)
            if not filename_item:
                with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                    f.write("  -> No filename_item at row " + str(row) + "\n")
                return
            filename = filename_item.text()

            # Debugging: Log the filename
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("  -> Filename: " + str(filename) + "\n")

            # Determine the directory (PROC or UNPROC)
            if table == self.proc_table:
                directory = self.proc_dir
            else:
                directory = self.unproc_dir

            filepath = os.path.join(directory, filename)

            # Debugging: Log the filepath
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("  -> Filepath: " + str(filepath) + "\n")

            # Clear highlights in BOTH tables (PROC and UNPROC) regardless of which was clicked
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("  -> Clearing highlights in proc_table (ID: " + str(id(self.proc_table)) + ") and unproc_table (ID: " + str(id(self.unproc_table)) + ")\n")
            self.clear_highlights(self.proc_table)
            self.clear_highlights(self.unproc_table)

            # Force background color to black for all rows in both tables
            for table_to_clear in [self.proc_table, self.unproc_table]:
                for row_to_clear in range(table_to_clear.rowCount()):
                    for col_to_clear in range(table_to_clear.columnCount()):
                        item_to_clear = table_to_clear.item(row_to_clear, col_to_clear)
                        if item_to_clear:
                            item_to_clear.setBackground(QColor("#000"))

            # Highlight the clicked row
            for col in range(table.columnCount()):
                table.item(row, col).setBackground(QColor("#FFFFCC"))

            # Load the full path into FullPathnameBox
            self.parent.tl.original_filename_label.setText(filepath)

            # Process the filename to retain tags, datestamps, _wm, and extension
            processed_filename = self.process_filename(filename)

            # Debugging: Log the processed filename
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("  -> Processed Filename: " + str(processed_filename) + "\n")

            # Load the processed filename into FilenameEditBox
            self.parent.tl.filename_edit.setText(processed_filename)

            # Extract and highlight tags in the Taglist
            self.parent.tl.selected_tags.clear()
            self.parent.tl.extract_tags_from_filename(processed_filename)
            self.parent.tl.update_tag_highlights()

            # Load the file into Taggerist Viewer (TV)
            self.parent.tv.load_file(filepath)

            # Debugging: Log successful completion
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("  -> Successfully loaded file into TV\n\n")
            if hasattr(self.parent.tl, 'search_edit') and self.parent.tl.search_edit:
                self.parent.tl.search_edit.setFocus()

        except Exception as e:
            # Debugging: Log any errors
            with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                f.write("  -> ERROR: " + str(e) + "\n\n")

    def clear_highlights(self, table):
        # Debugging: Log the table being cleared and its object ID
        with open('Taggerist_v37.05-buglog.txt', 'a') as f:
            f.write("  -> Clearing highlights in table: " + str(table) + " (ID: " + str(id(table)) + ")\n")
        
        # Clear current cell selection
        table.setCurrentCell(-1, -1)
        
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    item.setBackground(QColor("#000"))
                    # Debugging: Log the row and column being cleared
                    with open('Taggerist_v37.05-buglog.txt', 'a') as f:
                        f.write("    -> Cleared row " + str(row) + ", col " + str(col) + "\n")

    def process_filename(self, filename):
        # Normalize backtick-delimited tags to pipes; keep all other text intact
        return filename.replace('`', '|')
    def get_image_files_with_dates(self, directory):
        if not os.path.exists(directory):
            return []
        image_extensions = ('.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG')
        files = []
        for filename in os.listdir(directory):
            if filename.lower().endswith(image_extensions):
                filepath = os.path.join(directory, filename)
                timestamp = os.path.getmtime(filepath)
                dt = datetime.fromtimestamp(timestamp)
                mod_time = dt.strftime("%y.%m%d-%H%M.%S")
                nanoseconds = int((timestamp % 1) * 100)  # Two-digit nanoseconds
                mod_time_with_ns = f"{mod_time}{nanoseconds:02d}"
                size_kb = f"{os.path.getsize(filepath) / 1024:.1f} KB"
                filetype = "JPG" if filename.lower().endswith(('.jpg', '.jpeg')) else "PNG"
                files.append((filename, size_kb, filetype, mod_time_with_ns))
        return files

# ========== MAIN ==========
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaggeristMainWindow()
    window.show()
    sys.exit(app.exec())
