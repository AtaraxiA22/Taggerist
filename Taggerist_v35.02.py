# Taggerist v35.02

# Personal Configurations (fallback defaults; overridden by Taggerist.config.txt)
TAGLIST_1 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[Other].csv,©,white,red'
TAGLIST_2 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[NC].csv,@,white,yellow'
TAGLIST_3 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[Xpix].csv,(all),white,green'

TAGLIST_ID_1 = '©'
TAGLIST_ID_2 = '@'
TAGLIST_ID_3 = '(all)'

DELIMITERS = ['|', '`']

HELP_FILE_PATH = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/README.md'
# P.D. Reviewed @26.0909-0700.00
# Taggerist v35.02: #w.17 rev2 — all primary buttons clustered left of the edit box per user map: taglist/CI rows + CLEAR→PROCESS column, PROCESS button 3 rows tall, edit box and pathname stretch to right margin, thermometer right-aligned above search; #w.12 rev — bar numerals left-justified (centered text sat on the unfilled black part when the count is low), colors now green→yellow→red traffic-light order; #w.26 — [Reduce] now validates every pipe-delimited segment against all taglists and drops unknown words (keeps CI/datestamp/_wm/extension); [Sort Tags] stays in the left cluster on row 4 beside SKIP
# Taggerist v35.01: #w.25 — mouseover on a PROC/UNPROC filename shows a small wrapping popup with the full filename+ext. #w.12 — thermometer numerals are now larger bold black (taller bar) for visibility. #w.17 — cosmetic batch: TV nav buttons moved top-right; CI buttons vertical stack; Clear/Reduce/Sort Tags row under the thermometer with bold distinct colors; Search box beside the edit-box column; brackets stripped from all button labels; PROC header red / UNPROC header green. #w.15 — bottom row 50% taller. #w.14 — full taglist path shown in the status line. NOTE: #4.24 cancelled by user — he will batch-rename existing files instead; CI symbol handling stays generic
# Taggerist v34.22: #5.22 fix — the window title and the debug-log file name were hard-coded to v34.19; both now use the true version number. #3.23 fix — the PROC/UNPROC directory choices are now actually written to the config file on disk (previously kept only in memory), so the app remembers them between sessions. #4.24 — when the config copyright symbol is ©, clicking a date-prefix button now converts an existing (c) prefix to © in the filename
# Taggerist v34.21: #4.12 fix — the char count inside the thermometer bar is now always bold black text in all four places that style the bar; previously the text color was only set on one of them, so after switching taglists the count fell back to white and vanished on the yellow (100+ chars) warning bar
# Taggerist v34.20: #w.19 fix — [Clear] and [Reduce] now reset selected_tags and re-extract them from the kept text (datestamp, _wm, extension) before repainting the taglist; previously tag names stayed highlighted after the FilenameEditBox was emptied
# Taggerist v34.19: #4.18 fix — unselected taglist buttons now use FULLWINDOW_FONT_COLOR on FULLWINDOW_BG_COLOR (was hard-coded #000); unquoted hex colors in Taggerist.config.txt were being swallowed as comments — bare #RGB/#RRGGBB values now pass through unchanged; #3.12 — char count '22/255' now shown centered inside the thermometer bar (side label removed); #3.11 — search now matches aliases from every taglist CSV line (typing 'grn' finds CLR_grn); #2.13 — NEW [Sort Tags] button (third row, beside [Clear]/[Reduce]) sorts the |tags| in FilenameEditBox alphabetically, preserving leading text, datestamp, _wm, and extension
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
                               QSplitter, QSizePolicy, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QProgressBar, QLayout)
from PySide6.QtCore import Qt, QSize, QTimer, QPoint, QRect, Signal
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor, QShortcut, QKeySequence, QFontMetrics, QPainter, QGuiApplication, QScreen
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
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
                f.write("--- Taggerist v35.02 startup ---\n")
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
            if hasattr(self.tv, 'current_file') and self.tv.current_file:
                self.tl.load_image(self.tv.current_file)
                self.tl.update_pathname(self.tv.current_file)
        finally:
            self.tl.filename_edit.textChanged.connect(self.tl.update_tag_highlights)
            self.tl.filename_edit.textChanged.connect(self.tl.update_length_monitor)

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
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                self.config.write(f)
        except Exception as e:
            print(f"Error saving config: {e}")

    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)

    def update_window_title(self):
        if self.current_file:
            self.setWindowTitle(f"Taggerist v35.02 - {os.path.basename(self.current_file)}")
        else:
            self.setWindowTitle("Taggerist v35.02")

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
        nav_layout = QHBoxLayout()
        nav_layout.addStretch(1)
        self.prev_btn = QPushButton("←")
        self.prev_btn.clicked.connect(self.prev_file)
        self.next_btn = QPushButton("→")
        self.next_btn.clicked.connect(self.next_file)
        self.external_btn = QPushButton("External Viewer")
        self.external_btn.clicked.connect(self.open_external_viewer)
        nav_layout.addWidget(self.prev_btn)
        nav_layout.addWidget(self.next_btn)
        nav_layout.addWidget(self.external_btn)
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

    def prev_file(self):
        if self.current_index > 0:
            prev_file = os.path.join(self.current_dir, self.file_list[self.current_index - 1])
            self.load_file(prev_file)

    def next_file(self):
        if self.current_index < len(self.file_list) - 1:
            next_file = os.path.join(self.current_dir, self.file_list[self.current_index + 1])
            self.load_file(next_file)

    def open_external_viewer(self):
        if self.current_file:
            command = ["xdg-open", self.current_file]
            try:
                subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                QMessageBox.warning(self, "Error", "Could not open external viewer.")

# ========== FilenameEditBox (rich text: color-coded date prefixes) ==========
class FilenameEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ci_colors = {}
        self.convert_ci = False
        self.setFixedHeight(84)
        self.setLineWrapMode(QTextEdit.NoWrap)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTabChangesFocus(True)
        self.setAlignment(Qt.AlignRight)

    def text(self):
        return self.toPlainText()

    def setText(self, plain):
        plain = plain or ''
        if getattr(self, 'convert_ci', False) and '(c)' in plain:
            plain = plain.replace('(c)', '©')
        rendered = html.escape(plain)
        for sym in sorted(self.ci_colors, key=len, reverse=True):
            fg, bg = self.ci_colors[sym]
            esc_sym = html.escape(sym)
            rendered = rendered.replace(esc_sym, f'<span style="color:{fg}; background-color:{bg};">{esc_sym}</span>')
        self.blockSignals(True)
        self.setHtml(rendered)
        self.blockSignals(False)
        self.textChanged.emit()

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
        # If no datestamp present, strip any stray CI symbol, then append current system date/timestamp with the new CI
        if not re.search(r'\d{2,4}\.\d{4}-\d{4}\.\d+', new_filename):
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

    def select_taglist(self, number):
        spec = self.parent.get_taglist_spec(number)
        path = spec.split(',')[0].strip()
        with open('Taggerist_v35.02-buglog.txt', 'a') as dbg:
            dbg.write(f"select_taglist: number={number} path={path} exists={os.path.exists(path)}\n")
        if not os.path.exists(path):
            QMessageBox.warning(self, "Taglist not found", f"Taglist file not found:\n{path}")
            return
        self.active_taglist_number = number
        self.active_taglist_path = path
        self.load_taglist_and_conversions()
        fg, bg = self.parent.get_taglist_colors(number)
        self.apply_border_colors(bg)
        self.refresh_taglist_buttons()

    def load_taglist_and_conversions(self):
        self.all_tags = []
        self.conversion_table = {}
        self.list_tags = {n: set() for n in (1, 2, 3)}
        taglist_file = self.active_taglist_path
        for n in (1, 2, 3):
            try:
                spec = self.parent.get_taglist_spec(n)
                conv_path = spec.split(',')[0].strip()
            except Exception:
                continue
            if conv_path and os.path.exists(conv_path) and conv_path != taglist_file:
                try:
                    with open(conv_path, mode='r') as conv_csv:
                        for row in csv.reader(conv_csv):
                            if not row:
                                continue
                            new_tag = row[0].strip()
                            if new_tag:
                                self.list_tags[n].add(new_tag)
                                if len(row) > 1:
                                    for old_tag in row[1:]:
                                        old_tag = old_tag.strip()
                                        if old_tag:
                                            self.conversion_table[old_tag.lower()] = new_tag
                except Exception as e:
                    with open('Taggerist_v35.02-buglog.txt', 'a') as dbg:
                        dbg.write(f"load_conversions (list {n}) ERROR: {e}\n")
        if taglist_file and os.path.exists(taglist_file):
            try:
                with open(taglist_file, mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        if not row:
                            continue
                        new_tag = row[0].strip()
                        if new_tag:
                            self.all_tags.append(new_tag)
                            self.list_tags[self.active_taglist_number].add(new_tag)
                            if len(row) > 1:
                                for old_tag in row[1:]:
                                    old_tag = old_tag.strip()
                                    if old_tag:
                                        self.conversion_table[old_tag.lower()] = new_tag
            except Exception as e:
                print(f"Error loading taglist: {e}")
                with open('Taggerist_v35.02-buglog.txt', 'a') as dbg:
                    dbg.write(f"load_taglist ERROR: {e}\n")
        else:
            with open('Taggerist_v35.02-buglog.txt', 'a') as dbg:
                dbg.write(f"load_taglist: file missing or no path set: {taglist_file}\n")
        self.all_tags = sorted(set(self.all_tags))
        with open('Taggerist_v35.02-buglog.txt', 'a') as dbg:
            dbg.write(f"load_taglist: {len(self.all_tags)} tags, {len(self.conversion_table)} conversions from {taglist_file}\n")
        self.populate_taglist()

    @staticmethod
    def _contrast_text(bg):
        try:
            c = QColor(bg)
            lum = 0.299 * c.red() + 0.587 * c.green() + 0.114 * c.blue()
            return '#000' if lum > 127 else '#fff'
        except Exception:
            return '#fff'

    def refresh_taglist_buttons(self):
        border = self.active_border_color
        win_fg = strip_comment(self.parent.get_config('COLORS', 'FULLWINDOW_FONT_COLOR')) or '#fff'
        win_bg = strip_comment(self.parent.get_config('COLORS', 'FULLWINDOW_BG_COLOR')) or '#000'
        buttons = [self.abcd_btn, self.mnlo_btn, self.wxyz_btn]
        for i, btn in enumerate(buttons, start=1):
            f, b = self.parent.get_taglist_colors(i)
            if i == self.active_taglist_number:
                btn.setStyleSheet(f"color: {self._contrast_text(b)}; background-color: {b}; border: 1px solid {border}; padding: 2px;")
            else:
                btn.setStyleSheet(f"color: {win_fg}; background-color: {win_bg}; border: 1px solid {border}; padding: 2px;")

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
        self.active_border_color = '#FFFFCC'
        self.taglist_columns = to_int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_COLUMNS')), 8)
        self.taglist_rows = to_int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_ROWS')), 0)
        self.taglist_column_width = to_int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_COLUMN_WIDTH')), 160)
        self.taglist_font_size = to_int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_FONT_SIZE')), 12)
        self.taglist_vertical_spacing = to_float(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_VERTICAL_SPACING')), 1.0)
        self.taglist_font_color = strip_comment(self.parent.get_config('COLORS', 'TAGLIST_FONT_COLOR')) or '#fff'
        self.taglist_bg_color = strip_comment(self.parent.get_config('COLORS', 'TAGLIST_BG_COLOR')) or '#000'
        font_metrics = QFontMetrics(QFont("Ubuntu", self.taglist_font_size))
        self.tag_height = font_metrics.height()
        self.active_taglist_path = None
        self.active_taglist_number = 1
        self.tag_label_refs = []
        self.setup_ui()
        self.select_taglist(self.active_taglist_number)
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
        with open('Taggerist_v35.02-buglog.txt', 'a') as dbg:
            dbg.write(f"refill: {n} labels, rows_fit={rows}, viewport_h={vh}, font_color={self.taglist_font_color!r}, bg={self.taglist_bg_color!r}\n")

    def setup_ui(self):
        layout = QVBoxLayout(self)
        with open('Taggerist_v35.02-buglog.txt', 'a') as debug_file:
            debug_file.write(f"Main layout identified as: {type(layout).__name__}\n")
        top_grid = QGridLayout()
        top_grid.setSpacing(6)
        # Row 0: taglist buttons | pathname (stretches to right margin)
        taglist_buttons_widget = QWidget()
        taglist_buttons_layout = QHBoxLayout(taglist_buttons_widget)
        taglist_buttons_layout.setContentsMargins(0, 0, 0, 0)
        taglist_buttons_layout.setSpacing(4)
        self.abcd_btn = QPushButton()
        self.mnlo_btn = QPushButton()
        self.wxyz_btn = QPushButton()
        taglist_buttons_layout.addWidget(self.abcd_btn)
        taglist_buttons_layout.addWidget(self.mnlo_btn)
        taglist_buttons_layout.addWidget(self.wxyz_btn)
        top_grid.addWidget(taglist_buttons_widget, 0, 0)
        self.pathname_edit = QLineEdit()
        self.pathname_edit.setReadOnly(True)
        top_grid.addWidget(self.pathname_edit, 0, 1, 1, 4)
        # Col 0, rows 1-3: CI buttons vertical
        ci_buttons_widget = QWidget()
        ci_buttons_layout = QVBoxLayout(ci_buttons_widget)
        ci_buttons_layout.setContentsMargins(0, 0, 0, 0)
        ci_buttons_layout.setSpacing(4)
        self.x_btn = QPushButton()
        self.y_btn = QPushButton()
        self.z_btn = QPushButton()
        ci_buttons_layout.addWidget(self.x_btn)
        ci_buttons_layout.addWidget(self.y_btn)
        ci_buttons_layout.addWidget(self.z_btn)
        top_grid.addWidget(ci_buttons_widget, 1, 0, 3, 1)
        # Col 1: Clear (row 1), Reduce (row 2), Sort Tags + Skip (row 3)
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setStyleSheet("color: #000; background-color: #ffee00; border: 1px solid #FFFFCC; font-weight: bold; padding: 4px 10px;")
        top_grid.addWidget(self.clear_btn, 1, 1)
        self.reduce_btn = QPushButton("Reduce")
        self.reduce_btn.setStyleSheet("color: #000; background-color: #ff9900; border: 1px solid #FFFFCC; font-weight: bold; padding: 4px 10px;")
        top_grid.addWidget(self.reduce_btn, 2, 1)
        sort_skip_widget = QWidget()
        sort_skip_layout = QHBoxLayout(sort_skip_widget)
        sort_skip_layout.setContentsMargins(0, 0, 0, 0)
        sort_skip_layout.setSpacing(4)
        self.sort_tags_btn = QPushButton("Sort Tags")
        self.sort_tags_btn.setStyleSheet("color: #fff; background-color: #7a0099; border: 1px solid #FFFFCC; font-weight: bold; padding: 4px 10px;")
        self.skip_btn = QPushButton("SKIP")
        self.skip_btn.setStyleSheet("color: #fff; background-color: #e8752a; border: 1px solid #FFFFCC; padding: 6px 12px; font-weight: bold;")
        sort_skip_layout.addWidget(self.sort_tags_btn)
        sort_skip_layout.addWidget(self.skip_btn)
        top_grid.addWidget(sort_skip_widget, 3, 1)
        # Col 2, rows 1-3: PROCESS (three rows tall)
        self.process_btn = QPushButton("PROCESS")
        self.process_btn.setFont(QFont("Ubuntu", 18, QFont.Bold))
        self.process_btn.setStyleSheet("color: #fff; background-color: #2040c0; border: 1px solid #FFFFCC; padding: 6px 18px; font-weight: bold;")
        top_grid.addWidget(self.process_btn, 1, 2, 3, 1)
        # Col 3, rows 1-2: FilenameEditBox (two rows tall, stretches right)
        self.filename_edit = FilenameEdit()
        self.filename_edit.setFont(QFont("Ubuntu", 18))
        self.filename_edit.setStyleSheet("background-color: #000; color: #fff; border: 1px solid #FFFFCC;")
        self.filename_edit.textChanged.connect(self.update_tag_highlights)
        self.filename_edit.textChanged.connect(self.update_length_monitor)
        top_grid.addWidget(self.filename_edit, 1, 3, 2, 1)
        # Row 3, col 3: thermometer under the edit box
        self.length_bar = QProgressBar()
        self.length_bar.setRange(0, 255)
        self.length_bar.setValue(0)
        self.length_bar.setTextVisible(True)
        self.length_bar.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.length_bar.setFormat("%v/255")
        self.length_bar.setFixedHeight(24)
        self.length_bar.setStyleSheet("QProgressBar { background-color: #000; border: 1px solid #FFFFCC; color: #000; font-weight: bold; font-size: 13px; } QProgressBar::chunk { background-color: #00cc00; }")
        self.length_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        top_grid.addWidget(self.length_bar, 3, 3)
        top_grid.setColumnStretch(0, 0)
        top_grid.setColumnStretch(1, 0)
        top_grid.setColumnStretch(2, 0)
        top_grid.setColumnStretch(3, 1)
        top_grid.setRowStretch(0, 0)
        top_grid.setRowStretch(1, 0)
        top_grid.setRowStretch(2, 0)
        top_grid.setRowStretch(3, 0)
        layout.addLayout(top_grid, stretch=0)
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Search")
        self.search_edit.setStyleSheet("background-color: #000; color: #fff; border: 1px solid #FFFFCC;")
        self.search_edit.textChanged.connect(self.perform_search)
        self.search_edit.returnPressed.connect(self.accept_first_search_result)
        top_grid.addWidget(self.search_edit, 4, 0, 1, 4)
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
        self.refresh_taglist_button_labels()
        # Connect buttons to their logic
        self.x_btn.clicked.connect(lambda: self.update_date_prefix(self.parent.get_taglist_id(1)))
        self.y_btn.clicked.connect(lambda: self.update_date_prefix(self.parent.get_taglist_id(2)))
        self.z_btn.clicked.connect(lambda: self.update_date_prefix(self.parent.get_taglist_id(3)))
        self.clear_btn.clicked.connect(self.clear_filename_edit)
        self.reduce_btn.clicked.connect(self.reduce_filename_edit)
        self.sort_tags_btn.clicked.connect(self.sort_filename_tags)
        self.skip_btn.clicked.connect(self.skip_file)
        self.process_btn.clicked.connect(self.save_and_next)
        self.abcd_btn.clicked.connect(lambda: self.select_taglist(1))
        self.mnlo_btn.clicked.connect(lambda: self.select_taglist(2))
        self.wxyz_btn.clicked.connect(lambda: self.select_taglist(3))
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
        self.edit_tags_btn = QPushButton("Edit tags")
        self.edit_tags_btn.clicked.connect(self.open_current_taglist)
        bottom_layout.addWidget(self.edit_tags_btn)
        self.refresh_btn = QPushButton("Refresh Tags")
        self.refresh_btn.clicked.connect(self.parent.refresh_taglist)
        bottom_layout.addWidget(self.refresh_btn)
        self.help_btn2 = QPushButton("?")
        self.help_btn2.clicked.connect(self.open_readme)
        bottom_layout.addWidget(self.help_btn2)
        for wdg in (self.edit_tags_btn, self.refresh_btn, self.help_btn2):
            wdg.setMinimumHeight(36)
        self.help_window = None
        bottom_layout.addStretch()
        layout.addLayout(bottom_layout, stretch=0)

    def refresh_taglist_button_labels(self):
        for i, btn in enumerate([self.abcd_btn, self.mnlo_btn, self.wxyz_btn], start=1):
            spec = self.parent.get_taglist_spec(i)
            path = spec.split(',')[0].strip()
            base = os.path.splitext(os.path.basename(path))[0]
            idx = base.rfind('[')
            btn.setText(base[idx:] if idx >= 0 else f"[{base}]")
        for i, btn in enumerate([self.x_btn, self.y_btn, self.z_btn], start=1):
            cid = self.parent.get_taglist_id(i)
            btn.setText(f"[{cid}]" if cid else "[-]")
            fg, bg = self.parent.get_taglist_colors(i)
            btn.setStyleSheet(f"color: {fg}; background-color: {bg}; border: 1px solid {getattr(self, 'active_border_color', '#FFFFCC')}; padding: 2px;")
        self.filename_edit.ci_colors = {}
        self.filename_edit.convert_ci = (self.get_ci_symbol() == '©')
        for i in (1, 2, 3):
            ident = self.parent.get_taglist_id(i)
            if ident:
                fg, bg = self.parent.get_taglist_colors(i)
                self.filename_edit.ci_colors[ident] = (fg, bg)

    def setup_taglist_window(self, layout):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background-color: #000; border: none;")
        self.scroll_area.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setViewportMargins(0, 0, 0, 0)
        layout.addWidget(self.scroll_area, stretch=1)
        self.grid_layout_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_layout_widget)
        self.grid_layout.setHorizontalSpacing(0)
        self.grid_layout.setVerticalSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(0)
        self.scroll_area.setWidget(self.grid_layout_widget)

    def populate_taglist(self):
        if hasattr(self, 'taglist_status_label'):
            n = len(self.all_tags)
            base = os.path.basename(self.active_taglist_path) if self.active_taglist_path else 'no taglist selected'
            self.taglist_status_label.setText(f"{n} tags — {self.active_taglist_path}" if n else f"0 tags — {self.active_taglist_path} (empty or unreadable)")
        self._teardown_tag_labels()
        sorted_tags = sorted(self.all_tags)
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
        viewport_h = max(0, self.scroll_area.viewport().height())
        spacing_px = max(0.0, self.taglist_vertical_spacing) * self.tag_height
        line_h = self.tag_height + spacing_px
        if self.taglist_rows > 0:
            rows_fit = int(self.taglist_rows)
        elif viewport_h > 0 and line_h > 0:
            rows_fit = max(1, int(viewport_h // line_h))
        else:
            rows_fit = int(num_tags)
        if num_tags <= rows_fit:
            rows_fit = max(1, num_tags)
        else:
            rows_fit = min(rows_fit, columns * max(1, (num_tags + columns - 1) // columns))
        for r in range(getattr(self, '_last_rows_fit', 0)):
            self.grid_layout.setRowStretch(r, 0)
        self.grid_layout.setVerticalSpacing(spacing_px)
        for i, tag in enumerate(sorted_tags):
            col = i // rows_fit
            row = i % rows_fit
            label = ClickableTagLabel(tag)
            label.setFont(QFont("Ubuntu", self.taglist_font_size))
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
        self.grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.grid_layout_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

    def toggle_tag(self, t):
        current_text = self.filename_edit.text()
        tag_pattern = f"|{t}|"
        if tag_pattern in current_text:
            new_text = current_text.replace(tag_pattern, '')
            self.selected_tags.discard(t)
        else:
            base, ext = os.path.splitext(current_text)
            new_text = f"|{t}|{base}{ext}"
            self.selected_tags.add(t)
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
        return sym if sym == '©' else '(c)'

    def convert_delimiters_to_pipes(self, filename):
        if not filename:
            return ""
        filename = filename.replace("(c)", "©")
        converted = filename.replace('`', '|')
        if self.conversion_table:
            old_tags = sorted(self.conversion_table, key=len, reverse=True)
            pattern = re.compile('|'.join(re.escape(t) for t in old_tags), re.IGNORECASE)
            converted = pattern.sub(lambda m: self.conversion_table[m.group(0).lower()], converted)
        while '||' in converted:
            converted = converted.replace('||', '|')
        if self.get_ci_symbol() != '©':
            converted = converted.replace('©', "(c)")
        return converted

    def extract_tags_from_filename(self, filename):
        if not filename:
            return
        segs = [t for t in filename.split('|') if t]
        all_names = set(self.all_tags) | {t.lower() for t in self.all_tags}
        for old_tag_lower, new_tag in self.conversion_table.items():
            all_names.add(old_tag_lower)
            all_names.add(new_tag.lower())
        tags_in_filename = [s for s in segs if s.lower() in all_names]
        for tag in tags_in_filename:
            self.selected_tags.add(tag)
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
        all_tags = sorted(self.selected_tags)
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
        self.length_bar.setFormat(f"{min(length, 9999)}/255")
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
        for n in (1, 2, 3):
            for tag in sorted(getattr(self, 'list_tags', {}).get(n, ())):
                if tag not in seen and text.lower() in tag.lower():
                    seen.add(tag)
                    matches.append((tag, n))
        for alias, new_tag in sorted(getattr(self, 'conversion_table', {}).items()):
            if text and text.lower() in alias.lower() and new_tag not in seen:
                seen.add(new_tag)
                owner = next((n for n in (1, 2, 3) if new_tag in getattr(self, 'list_tags', {}).get(n, ())), 1)
                matches.append((new_tag, owner))
        self._last_match_count = len(matches)
        for idx, chip in enumerate(self.search_chips):
            if idx < len(matches):
                tag, n = matches[idx]
                fg, bg = self.parent.get_taglist_colors(n)
                chip.setText(tag)
                chip.tag = tag
                chip.setStyleSheet(f"color: {self._contrast_text(bg)}; background-color: {bg}; border: 1px solid #FFFFCC; padding: 1px 4px;")
                chip.setToolTip(f"List {n}")
                chip.show()
            else:
                chip.setText("")
                chip.tag = None
                chip.hide()
        if not matches:
            self.search_results.hide()
            return
        self.search_results.show()

    def accept_first_search_result(self):
        count = getattr(self, '_last_match_count', 0)
        if count > 0 and self.search_chips and self.search_chips[0].tag:
            self.search_result_clicked(self.search_chips[0].tag)

    def search_result_clicked(self, tag):
        self.toggle_tag(tag)
        self.search_edit.clear()
        self.search_edit.setFocus()

    def save_and_next(self):
        new_filename = self.filename_edit.text()
        if not new_filename:
            QMessageBox.warning(self, "Error", "Filename cannot be empty")
            return
        if not new_filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            new_filename += ".jpg"

        old_path = self.parent.tv.current_file
        output_dir = self.parent.tf.proc_dir if self.parent.tf.proc_dir else self.parent.tv.current_dir
        new_path = os.path.join(output_dir, new_filename)

        save_error = None
        try:
            shutil.copy2(old_path, new_path)
            os.utime(new_path, (os.path.getatime(new_path), int(datetime.now().timestamp())))
            if old_path != new_path:
                os.remove(old_path)
            self.parent.save_settings()
        except Exception as e:
            save_error = e
        self.parent.tf.refresh_lists()
        if save_error is not None:
            QMessageBox.critical(self, "Error", f"Error saving: {save_error}")
            return
        self.parent.tf.scroll_to_file(new_filename, proc=True)
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
        if self.active_taglist_path and os.path.exists(self.active_taglist_path):
            subprocess.Popen(['xdg-open', self.active_taglist_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            QMessageBox.warning(self, "Taglist not found", f"Taglist file not found:\n{self.active_taglist_path}")

    def open_readme(self):
        help_path = os.path.expanduser(strip_comment(self.parent.get_config('DIRECTORIES', 'HELP_FILE_PATH')))
        if os.path.exists(help_path):
            subprocess.Popen(['xdg-open', help_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            QMessageBox.warning(self, "Help file not found", f"Help file not found:\n{help_path}")

    def _split_extension(self, filename):
        m = re.search(r'\.(jpe?g|png)$', filename, re.IGNORECASE)
        if m:
            return filename[:m.start()], m.group(0)
        return filename, ''

    def _find_datestamp(self, root):
        return re.search(r'(?P<ci>(?:' + self._ci_alt() + r'))?(?P<ds>\d{2,4}\.\d{4}-\d{4}\.\d+)', root)

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
        known.update(self.conversion_table)
        known.update(str(v).lower() for v in self.conversion_table.values())
        first_tag_idx = next((i for i, p in enumerate(parts) if p.lower() in known), None)
        if first_tag_idx is None:
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
            known |= {t.lower() for t in known}
            tags = [s.strip('`') for s in segments[1:-1] if s.strip('`')]
            tags = [t for t in tags if t.lower() in known]
            if tags:
                result = '|' + '|'.join(tags) + '|'
        result += kept
        if '_wm' in filename and '_wm' not in result:
            result += '_wm'
        self.selected_tags.clear()
        self.filename_edit.setText(result + ext)
        self.extract_tags_from_filename(result + ext)
        self.update_tag_highlights()
        self.update_length_monitor()
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
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
                f.write("handle_single_click called at " + str(datetime.now()) + "\n")

            # Get the table and row that was clicked
            table = self.sender()
            row = item.row()

            # Debugging: Log the table object ID
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
                f.write("  -> Clicked table ID: " + str(id(table)) + "\n")

            # Get the filename from the clicked row
            filename_item = table.item(row, 0)
            if not filename_item:
                with open('Taggerist_v35.02-buglog.txt', 'a') as f:
                    f.write("  -> No filename_item at row " + str(row) + "\n")
                return
            filename = filename_item.text()

            # Debugging: Log the filename
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
                f.write("  -> Filename: " + str(filename) + "\n")

            # Determine the directory (PROC or UNPROC)
            if table == self.proc_table:
                directory = self.proc_dir
            else:
                directory = self.unproc_dir

            filepath = os.path.join(directory, filename)

            # Debugging: Log the filepath
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
                f.write("  -> Filepath: " + str(filepath) + "\n")

            # Clear highlights in BOTH tables (PROC and UNPROC) regardless of which was clicked
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
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
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
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
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
                f.write("  -> Successfully loaded file into TV\n\n")

        except Exception as e:
            # Debugging: Log any errors
            with open('Taggerist_v35.02-buglog.txt', 'a') as f:
                f.write("  -> ERROR: " + str(e) + "\n\n")

    def clear_highlights(self, table):
        # Debugging: Log the table being cleared and its object ID
        with open('Taggerist_v35.02-buglog.txt', 'a') as f:
            f.write("  -> Clearing highlights in table: " + str(table) + " (ID: " + str(id(table)) + ")\n")
        
        # Clear current cell selection
        table.setCurrentCell(-1, -1)
        
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    item.setBackground(QColor("#000"))
                    # Debugging: Log the row and column being cleared
                    with open('Taggerist_v35.02-buglog.txt', 'a') as f:
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
