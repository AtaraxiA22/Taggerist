# Taggerist v34.04

# Personal Configurations (fallback defaults; overridden by Taggerist.config.txt)
TAGLIST_1 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[Other].csv,white,red'
TAGLIST_2 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[NC].csv,white,yellow'
TAGLIST_3 = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/Taggerist.taglist.[Xpix].csv,white,green'

COLLECTION_ID_1 = '©'
COLLECTION_ID_2 = '@'
COLLECTION_ID_3 = '(all)'

DELIMITERS = ['|', '`']

HELP_FILE_PATH = '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs/README.md'
# P.D. Reviewed @26.0909-0700.00
# Taggerist v34.04: remove PyQt5/PySide6 double-binding (Process crash); [?] moved to row 3; duplicate pathname bar removed; config file no longer overwritten on exit
# (c) @26.0830-2150.00 by AtaraxiA under Creative Commons CC BY-SA license

import re
import re


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
                               QGridLayout, QRadioButton, QButtonGroup, QMessageBox, QListWidget,
                               QListWidgetItem, QSplitter, QSizePolicy, QTableWidget, QTableWidgetItem, QHeaderView, QDialog)
from PySide6.QtCore import Qt, QSize, QTimer, QPoint, QRect
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor, QShortcut, QKeySequence, QFontMetrics, QPainter, QGuiApplication, QScreen
from PIL import Image

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
    'TAGLIST_DIR': os.path.expanduser("~/Pictures/TAGLISTS/"),
    'PROC_DIR': '/home/jack/Pictures/TAGGERIST/test3',
    'UNPROC_DIR': '/home/jack/Pictures/TAGGERIST/Test2',
    'CONFIGS_DIR': '/home/jack/MEGA/TAGGERIST/TAGGERIST.configs',
    'TAGLIST_1': TAGLIST_1,
    'TAGLIST_2': TAGLIST_2,
    'TAGLIST_3': TAGLIST_3,
    'HELP_FILE_PATH': HELP_FILE_PATH,
    'COLLECTION_ID_1': COLLECTION_ID_1,
    'COLLECTION_ID_2': COLLECTION_ID_2,
    'COLLECTION_ID_3': COLLECTION_ID_3,
}

# ========== CONFIG LOADER ==========
CONFIG_SECTIONS = {
    'DIRECTORIES': [
        ('TAGLIST_1', 'Taglist button 1: path,font-color,background-color'),
        ('TAGLIST_2', 'Taglist button 2: path,font-color,background-color'),
        ('TAGLIST_3', 'Taglist button 3: path,font-color,background-color'),
        ('PROC_DIR', 'Directory where PROCESS copies files'),
        ('UNPROC_DIR', 'Directory of files waiting to be processed'),
        ('CONFIGS_DIR', 'Directory holding this config and the .csv taglists'),
        ('HELP_FILE_PATH', 'Path of the help file shown by [?]'),
        ('COLLECTION_ID_1', 'Date identifier for the [x] button (empty = no CI)'),
        ('COLLECTION_ID_2', 'Date identifier for the [y] button (empty = no CI)'),
        ('COLLECTION_ID_3', 'Date identifier for the [z] button (empty = no CI)'),
    ],
    'DISPLAY': [
        ('TAGLIST_COLUMNS', 'Max columns of tagnames (list wraps to a new column at screen bottom)'),
        ('TAGLIST_ROWS', 'Max rows per column; 0 = fit to screen height'),
        ('TAGLIST_COLUMN_WIDTH', 'Pixel width of each tagname column'),
        ('TAGLIST_FONT_SIZE', 'Font size of tagnames in TL'),
        ('TAGLIST_VERTICAL_SPACING', 'Blank lines between tagnames (1 = one full line)'),
        ('START_DISPLAY', 'Display number to open on'),
        ('START_MAXIMIZED', 'True or False'),
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
        for marker in [';', '#']:
            if marker in value:
                value = value.split(marker)[0].strip()
        return value
    return value

# ========== MAIN WINDOW ==========
class TaggeristMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
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
        self.setStyleSheet("""
            background-color: #000;
            color: #fff;
            QFrame { background-color: #000; border: 1px solid #FFFFCC; }
            QLabel { color: #fff; background-color: #000; }
            QLineEdit { background-color: #000; color: #fff; border: 1px solid #FFFFCC; }
            QPushButton { background-color: #000; color: #fff; border: 1px solid #FFFFCC; }
            QTableWidget { background-color: #000; color: #fff; gridline-color: #000; }
            QScrollArea { background-color: #000; border: 1px solid #FFFFCC; }
            QRadioButton { color: #fff; background-color: #000; }
            QHeaderView::section { background-color: #000; color: #fff; border: 1px solid #FFFFCC; }
            QSplitter::handle { background-color: #000; }
        """)
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

    def closeEvent(self, event):
        self.save_settings()
        super().closeEvent(event)

    def update_window_title(self):
        if self.current_file:
            self.setWindowTitle(f"Taggerist v34.04 - {os.path.basename(self.current_file)}")
        else:
            self.setWindowTitle("Taggerist v34.04")

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
        button_layout = QHBoxLayout()
        self.prev_btn = QPushButton("←")
        self.prev_btn.clicked.connect(self.prev_file)
        self.next_btn = QPushButton("→")
        self.next_btn.clicked.connect(self.next_file)
        self.external_btn = QPushButton("External Viewer")
        self.external_btn.clicked.connect(self.open_external_viewer)
        button_layout.addWidget(self.prev_btn)
        button_layout.addWidget(self.next_btn)
        button_layout.addWidget(self.external_btn)
        layout.addLayout(button_layout)
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
            if img.mode == "P":
                img = img.convert("RGB")
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

# ========== TL (Taggerist-List) ==========
class TaggeristList(QFrame):
    def update_date_prefix(self, symbol):
        current_filename = self.filename_edit.text()
        if not current_filename:
            return
        # Replace any existing CI(s) before the datestamp with the selected symbol
        new_filename, n_sub = re.subn(r'[@©\(c\)\(all\)]+(?=\d{2,4}\.\d{4}-\d{4}\.)', symbol, current_filename)
        # If a datestamp exists but has no CI in front of it, insert the CI before the datestamp
        if n_sub == 0:
            m = re.search(r'\d{2,4}\.\d{4}-\d{4}\.', new_filename)
            if m:
                new_filename = new_filename[:m.start()] + symbol + new_filename[m.start():]
        # If no datestamp present, append current system date/timestamp with the CI
        if not re.search(r'\d{2,4}\.\d{4}-\d{4}\.\d+', new_filename):
            now = datetime.now()
            stamp = now.strftime("%y.%m%d-%H%M.%S") + f"{now.microsecond // 10000:02d}"
            base, ext = self._split_extension(new_filename)
            new_filename = f"{base}{symbol}{stamp}{ext}"
        # Ensure _wm is at the end (before the extension)
        if '_wm' in new_filename:
            root, ext = self._split_extension(new_filename)
            root = root.replace('_wm', '')
            new_filename = f"{root}_wm{ext}"
        self.filename_edit.setText(new_filename)
        self.update_tag_highlights()
        self.update_length_monitor()

    def select_taglist(self, number):
        spec = strip_comment(self.parent.get_config('DIRECTORIES', f'TAGLIST_{number}'))
        parts = [p.strip() for p in spec.split(',')]
        path = parts[0]
        if not os.path.exists(path):
            QMessageBox.warning(self, "Taglist not found", f"Taglist file not found:\n{path}")
            return
        self.active_taglist_number = number
        self.active_taglist_path = path
        self.load_taglist_and_conversions()
        self.refresh_taglist_buttons()

    def load_taglist_and_conversions(self):
        self.all_tags = []
        self.conversion_table = {}
        taglist_file = self.active_taglist_path
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
                            if len(row) > 1:
                                for old_tag in row[1:]:
                                    old_tag = old_tag.strip()
                                    if old_tag:
                                        self.conversion_table[old_tag.lower()] = new_tag
            except Exception as e:
                print(f"Error loading taglist: {e}")
        self.all_tags = sorted(set(self.all_tags))
        self.populate_taglist()

    def refresh_taglist_buttons(self):
        buttons = [self.abcd_btn, self.mnlo_btn, self.wxyz_btn]
        for i, btn in enumerate(buttons, start=1):
            spec = strip_comment(self.parent.get_config('DIRECTORIES', f'TAGLIST_{i}'))
            parts = [p.strip() for p in spec.split(',')]
            f, b = parts[1] if len(parts) > 1 else 'white', parts[2] if len(parts) > 2 else 'black'
            if i == self.active_taglist_number:
                btn.setStyleSheet(f"color: {f}; background-color: {b}; border: 1px solid #FFFFCC; padding: 2px;")
            else:
                btn.setStyleSheet(f"color: {f}; background-color: #000; border: 1px solid #FFFFCC; padding: 2px;")


    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.selected_tags = set()
        self.all_tags = []
        self.current_mode = None
        self.conversion_table = {}
        self.taglist_columns = int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_COLUMNS')))
        self.taglist_rows = int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_ROWS')))
        self.taglist_column_width = int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_COLUMN_WIDTH')))
        self.taglist_font_size = int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_FONT_SIZE')))
        self.taglist_vertical_spacing = int(strip_comment(self.parent.get_config('DISPLAY', 'TAGLIST_VERTICAL_SPACING')))
        self.taglist_font_color = strip_comment(self.parent.get_config('COLORS', 'TAGLIST_FONT_COLOR'))
        self.taglist_bg_color = strip_comment(self.parent.get_config('COLORS', 'TAGLIST_BG_COLOR'))
        font_metrics = QFontMetrics(QFont("Ubuntu", self.taglist_font_size))
        self.tag_height = font_metrics.height()
        self.active_taglist_path = None
        self.active_taglist_number = 1
        self.setup_ui()
        self.select_taglist(self.active_taglist_number)

    def setup_ui(self):
        layout = QVBoxLayout(self)
        with open('Taggerist_v34.04-buglog.txt', 'a') as debug_file:
            debug_file.write(f"Main layout identified as: {type(layout).__name__}\n")
        top_grid = QGridLayout()
        top_grid.setSpacing(6)
        # Row 1: taglist-choice buttons | Pathname | [SKIP] [?]
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
        top_grid.addWidget(self.pathname_edit, 0, 1)
        self.skip_btn = QPushButton("[SKIP]")
        top_grid.addWidget(self.skip_btn, 0, 2)
        # Row 2: date-identifier (CI) buttons | FilenameEditBox | [PROCESS]
        ci_buttons_widget = QWidget()
        ci_buttons_layout = QHBoxLayout(ci_buttons_widget)
        ci_buttons_layout.setContentsMargins(0, 0, 0, 0)
        ci_buttons_layout.setSpacing(4)
        self.x_btn = QPushButton()
        self.y_btn = QPushButton()
        self.z_btn = QPushButton()
        ci_buttons_layout.addWidget(self.x_btn)
        ci_buttons_layout.addWidget(self.y_btn)
        ci_buttons_layout.addWidget(self.z_btn)
        top_grid.addWidget(ci_buttons_widget, 1, 0)
        self.filename_edit = QLineEdit()
        self.filename_edit.setFont(QFont("Ubuntu", 12))
        self.filename_edit.setStyleSheet("background-color: #000; color: #fff; border: 1px solid #FFFFCC;")
        self.filename_edit.textChanged.connect(self.update_tag_highlights)
        self.filename_edit.textChanged.connect(self.update_length_monitor)
        top_grid.addWidget(self.filename_edit, 1, 1)
        self.process_btn = QPushButton("[PROCESS]")
        top_grid.addWidget(self.process_btn, 1, 2)
        # Row 3: [Clear]/[Reduce]/[?] | empty | empty
        clear_reduce_widget = QWidget()
        clear_reduce_layout = QHBoxLayout(clear_reduce_widget)
        clear_reduce_layout.setContentsMargins(0, 0, 0, 0)
        clear_reduce_layout.setSpacing(4)
        self.clear_btn = QPushButton("[Clear]")
        self.reduce_btn = QPushButton("[Reduce]")
        self.help_btn = QPushButton("[?]")
        self.help_btn.clicked.connect(self.open_readme)
        clear_reduce_layout.addWidget(self.clear_btn)
        clear_reduce_layout.addWidget(self.reduce_btn)
        clear_reduce_layout.addWidget(self.help_btn)
        top_grid.addWidget(clear_reduce_widget, 2, 0)
        top_grid.setColumnStretch(0, 0)
        top_grid.setColumnStretch(1, 1)
        top_grid.setColumnStretch(2, 0)
        top_grid.setRowStretch(0, 0)
        top_grid.setRowStretch(1, 0)
        top_grid.setRowStretch(2, 0)
        layout.addLayout(top_grid, stretch=0)
        self.refresh_taglist_button_labels()
        # Connect buttons to their logic
        self.x_btn.clicked.connect(lambda: self.update_date_prefix(strip_comment(self.parent.get_config('DIRECTORIES', 'COLLECTION_ID_1'))))
        self.y_btn.clicked.connect(lambda: self.update_date_prefix(strip_comment(self.parent.get_config('DIRECTORIES', 'COLLECTION_ID_2'))))
        self.z_btn.clicked.connect(lambda: self.update_date_prefix(strip_comment(self.parent.get_config('DIRECTORIES', 'COLLECTION_ID_3'))))
        self.clear_btn.clicked.connect(self.clear_filename_edit)
        self.reduce_btn.clicked.connect(self.reduce_filename_edit)
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
        self.length_label = QLabel("0/255")
        self.length_label.setStyleSheet("color: #fff;")
        bottom_layout.addWidget(self.length_label)
        bottom_layout.addStretch()
        self.refresh_btn = QPushButton("Refresh Tags")
        self.refresh_btn.clicked.connect(self.parent.refresh_taglist)
        bottom_layout.addWidget(self.refresh_btn)
        self.help_btn2 = QPushButton("[?]")
        self.help_btn2.clicked.connect(self.open_help_window)
        bottom_layout.addWidget(self.help_btn2)
        self.help_window = None
        bottom_layout.addStretch()
        layout.addLayout(bottom_layout, stretch=0)

    def refresh_taglist_button_labels(self):
        for i, btn in enumerate([self.abcd_btn, self.mnlo_btn, self.wxyz_btn], start=1):
            spec = strip_comment(self.parent.get_config('DIRECTORIES', f'TAGLIST_{i}'))
            path = spec.split(',')[0].strip()
            base = os.path.splitext(os.path.basename(path))[0]
            idx = base.rfind('[')
            btn.setText(base[idx:] if idx >= 0 else f"[{base}]")
        for i, btn in enumerate([self.x_btn, self.y_btn, self.z_btn], start=1):
            cid = strip_comment(self.parent.get_config('DIRECTORIES', f'COLLECTION_ID_{i}'))
            btn.setText(f"[{cid}]")

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
        for i in reversed(range(self.grid_layout.count())):
            item = self.grid_layout.itemAt(i)
            if item and item.widget():
                item.widget().setParent(None)
        sorted_tags = sorted(self.all_tags)
        self._pending_tags = sorted_tags
        self._refill_taglist()

    def _refill_taglist(self):
        sorted_tags = getattr(self, '_pending_tags', [])
        for i in reversed(range(self.grid_layout.count())):
            item = self.grid_layout.itemAt(i)
            if item and item.widget():
                item.widget().setParent(None)
        num_tags = len(sorted_tags)
        columns = max(1, self.taglist_columns)
        viewport_h = max(0, self.scroll_area.viewport().height())
        spacing_px = max(0, self.taglist_vertical_spacing) * self.tag_height
        line_h = self.tag_height + spacing_px
        if self.taglist_rows > 0:
            rows_fit = self.taglist_rows
        elif viewport_h > 0 and line_h > 0:
            rows_fit = max(1, viewport_h // line_h)
        else:
            rows_fit = num_tags
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
            label = QLabel(tag)
            label.setFont(QFont("Ubuntu", self.taglist_font_size))
            label.setStyleSheet(f"color: {self.taglist_font_color}; background-color: {self.taglist_bg_color}; border: none; padding: 0px; margin: 0px;")
            label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            label.setFixedWidth(self.taglist_column_width)
            label.setFixedHeight(self.tag_height)
            label.setWordWrap(False)
            label.setProperty("full_tag", tag)
            def make_click_handler(t):
                def handler(event):
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
                return handler
            label.mousePressEvent = make_click_handler(tag)
            if tag.startswith(("PHTO_000", "PHTO_001", "PHTO_002")):
                label.setStyleSheet(f"color: #FFFF00; background-color: {self.taglist_bg_color}; font-weight: bold; border: none; padding: 0px; margin: 0px;")
            self.grid_layout.addWidget(label, row, col)
        for r in range(rows_fit):
            self.grid_layout.setRowStretch(r, 0)
        self._last_rows_fit = rows_fit
        self.grid_layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.grid_layout_widget.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, '_pending_tags'):
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

    def convert_delimiters_to_pipes(self, filename):
        if not filename:
            return ""
        filename = filename.replace("(c)", "©")
        converted = filename.replace('`', '|')
        for old_tag_lower, new_tag in self.conversion_table.items():
            old_tag_pattern = re.compile(re.escape(old_tag_lower), re.IGNORECASE)
            converted = old_tag_pattern.sub(new_tag, converted)
        while '||' in converted:
            converted = converted.replace('||', '|')
        converted = converted.replace("©", "(c)")
        return converted

    def extract_tags_from_filename(self, filename):
        if not filename:
            return
        tags_in_filename = re.findall(r'\|([^|]+)\|', filename)
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
        self.length_label.setText(f"{length}/255")

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

        try:
            shutil.copy2(old_path, new_path)
            os.utime(new_path, (os.path.getatime(new_path), int(datetime.now().timestamp())))
            if old_path != new_path:
                os.remove(old_path)
            self.parent.tf.refresh_lists()
            self.parent.save_settings()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saving: {e}")
            return

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

    def open_help_window(self):
        if self.help_window is None:
            # Create a floating window
            self.help_window = QDialog(self, Qt.WindowStaysOnTopHint)
            self.help_window.setWindowTitle("Taggerist Help")
            self.help_window.setGeometry(100, 100, 600, 400)

            # Add a QTextEdit to display the help file
            self.help_text = QTextEdit(self.help_window)
            self.help_text.setReadOnly(True)
            layout = QVBoxLayout(self.help_window)
            layout.addWidget(self.help_text)

            # Load the help file
            help_path = os.path.expanduser(strip_comment(self.parent.get_config('DIRECTORIES', 'HELP_FILE_PATH')))
            try:
                with open(help_path, "r", encoding="utf-8") as file:
                    self.help_text.setPlainText(file.read())
            except Exception:
                self.help_text.setPlainText(f"Help file not found:\n{help_path}")

        # Show the window and bring it to the front
        self.help_window.show()
        self.help_window.raise_()
        self.help_window.activateWindow()

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
        return re.search(r'(?P<ci>\(c\)|\(all\)|[@\u00a9])?(?P<ds>\d{2,4}\.\d{4}-\d{4}\.\d+)', root)

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
        self.filename_edit.setText(kept + ext)
        self.update_tag_highlights()
        self.update_length_monitor()

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
            tags = [s.strip('`') for s in segments[1:-1] if s.strip('`')]
            if tags:
                result = '|' + '|'.join(tags) + '|'
        result += kept
        if '_wm' in filename and '_wm' not in result:
            result += '_wm'
        self.filename_edit.setText(result + ext)
        self.update_tag_highlights()
        self.update_length_monitor()

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
        self.proc_label.setStyleSheet("color: #fff; font-weight: bold;")
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
        self.unproc_label = QLabel("UNPROCESSED")
        self.unproc_label.setStyleSheet("color: #fff; font-weight: bold;")
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

    def refresh_proc_list(self):
        self.proc_table.setRowCount(0)
        if os.path.exists(self.proc_dir):
            files = self.get_image_files_with_dates(self.proc_dir)
            for filename, size, filetype, mod_date in files:
                row = self.proc_table.rowCount()
                self.proc_table.insertRow(row)
                self.proc_table.setItem(row, 0, QTableWidgetItem(filename))
                self.proc_table.setItem(row, 1, QTableWidgetItem(size))
                self.proc_table.setItem(row, 2, QTableWidgetItem(filetype))
                self.proc_table.setItem(row, 3, QTableWidgetItem(mod_date))
                for col in range(self.proc_table.columnCount()):
                    if self.proc_table.item(row, col):
                        self.proc_table.item(row, col).setBackground(QColor(53, 53, 53))
            # Sort by modification date (oldest first)
            self.proc_table.sortItems(3, Qt.AscendingOrder)

    def refresh_unproc_list(self):
        self.unproc_table.setRowCount(0)
        if os.path.exists(self.unproc_dir):
            files = self.get_image_files_with_dates(self.unproc_dir)
            for filename, size, filetype, mod_date in files:
                row = self.unproc_table.rowCount()
                self.unproc_table.insertRow(row)
                self.unproc_table.setItem(row, 0, QTableWidgetItem(filename))
                self.unproc_table.setItem(row, 1, QTableWidgetItem(size))
                self.unproc_table.setItem(row, 2, QTableWidgetItem(filetype))
                self.unproc_table.setItem(row, 3, QTableWidgetItem(mod_date))
                for col in range(self.unproc_table.columnCount()):
                    if self.unproc_table.item(row, col):
                        self.unproc_table.item(row, col).setBackground(QColor(53, 53, 53))
            # Sort by modification date (oldest first)
            self.unproc_table.sortItems(3, Qt.AscendingOrder)

    def refresh_lists(self):
        self.refresh_proc_list()
        self.refresh_unproc_list()
            
    
    
    
    
    
    
    
    
    
    
    
    def handle_single_click(self, item):
        try:
            # Debugging: Log the start of the single-click handler
            with open('Taggerist_v34.04-buglog.txt', 'a') as f:
                f.write("handle_single_click called at " + str(datetime.now()) + "\n")

            # Get the table and row that was clicked
            table = self.sender()
            row = item.row()

            # Debugging: Log the table object ID
            with open('Taggerist_v34.04-buglog.txt', 'a') as f:
                f.write("  -> Clicked table ID: " + str(id(table)) + "\n")

            # Get the filename from the clicked row
            filename_item = table.item(row, 0)
            if not filename_item:
                with open('Taggerist_v34.04-buglog.txt', 'a') as f:
                    f.write("  -> No filename_item at row " + str(row) + "\n")
                return
            filename = filename_item.text()

            # Debugging: Log the filename
            with open('Taggerist_v34.04-buglog.txt', 'a') as f:
                f.write("  -> Filename: " + str(filename) + "\n")

            # Determine the directory (PROC or UNPROC)
            if table == self.proc_table:
                directory = self.proc_dir
            else:
                directory = self.unproc_dir

            filepath = os.path.join(directory, filename)

            # Debugging: Log the filepath
            with open('Taggerist_v34.04-buglog.txt', 'a') as f:
                f.write("  -> Filepath: " + str(filepath) + "\n")

            # Clear highlights in BOTH tables (PROC and UNPROC) regardless of which was clicked
            with open('Taggerist_v34.04-buglog.txt', 'a') as f:
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

            # Add a small delay to ensure the table is fully updated
            from PySide6.QtCore import QCoreApplication
            QCoreApplication.processEvents()

            # Highlight the clicked row
            for col in range(table.columnCount()):
                table.item(row, col).setBackground(QColor("#FFFFCC"))

            # Load the full path into FullPathnameBox
            self.parent.tl.original_filename_label.setText(filepath)

            # Process the filename to retain tags, datestamps, _wm, and extension
            processed_filename = self.process_filename(filename)

            # Debugging: Log the processed filename
            with open('Taggerist_v34.04-buglog.txt', 'a') as f:
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
            with open('Taggerist_v34.04-buglog.txt', 'a') as f:
                f.write("  -> Successfully loaded file into TV\n\n")

        except Exception as e:
            # Debugging: Log any errors
            with open('Taggerist_v34.04-buglog.txt', 'a') as f:
                f.write("  -> ERROR: " + str(e) + "\n\n")

    def clear_highlights(self, table):
        # Debugging: Log the table being cleared and its object ID
        with open('Taggerist_v34.04-buglog.txt', 'a') as f:
            f.write("  -> Clearing highlights in table: " + str(table) + " (ID: " + str(id(table)) + ")\n")
        
        # Clear current cell selection
        table.setCurrentCell(-1, -1)
        
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    item.setBackground(QColor("#000"))
                    # Debugging: Log the row and column being cleared
                    with open('Taggerist_v34.04-buglog.txt', 'a') as f:
                        f.write("    -> Cleared row " + str(row) + ", col " + str(col) + "\n")

    def process_filename(self, filename):
        # Retain pipe-delimited tags, datestamps, _wm, and file extension
        tag_pattern = r'\|[^|]+\|'
        datestamp_patterns = [
            r'@\d{2}\.\d{4}-\d{4}\.\d{6}',
            r'@\d{4}\.\d{4}-\d{4}\.\d{6}',
            r'\(c\)\d{2}\.\d{4}-\d{4}\.\d{6}',
            r'\(c\)\d{4}\.\d{4}-\d{4}\.\d{6}',
            r'©\d{2}\.\d{4}-\d{4}\.\d{6}',
        ]
        wm_pattern = r'_wm'
        extension_pattern = r'\.[^.]+$'

        combined_pattern = f"({tag_pattern}|{'|'.join(datestamp_patterns)}|{wm_pattern}|{extension_pattern})"
        matches = re.findall(combined_pattern, filename)
        processed_filename = ''.join(matches)

        while '||' in processed_filename:
            processed_filename = processed_filename.replace('||', '|')

        return processed_filename

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
