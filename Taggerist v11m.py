#!/usr/bin/env python3
# P.D. Reviewed @26.0908-2100.00
# Taggerist v11m: QGridLayout vertical sort (column-first)
# (c) @26.0830-2150.00 by AtaraxiA under Creative Commons CC BY-SA license

import sys
import os
import re
import csv
import shutil
import random
import subprocess
import configparser
from datetime import datetime
from PySide6.QtWidgets import (QApplication, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QWidget,
                               QLabel, QLineEdit, QTextEdit, QPushButton, QFileDialog, QScrollArea,
                               QGridLayout, QRadioButton, QButtonGroup, QMessageBox, QListWidget,
                               QListWidgetItem, QSplitter, QSizePolicy, QTableWidget, QTableWidgetItem)
from PySide6.QtCore import Qt, QSize, QTimer, QPoint, QRect
from PySide6.QtGui import QPixmap, QFont, QPalette, QColor, QShortcut, QKeySequence, QFontMetrics, QPainter, QGuiApplication, QScreen
from PIL import Image

# ========== DEFAULT CONFIG ==========
DEFAULTS = {
    'TAGLIST_COLUMNS': '10',
    'TAGLIST_ROWS': '0',
    'TAGLIST_COLUMN_WIDTH': '160',
    'TAGLIST_FONT_SIZE': '14',
    'TAGLIST_SPACING': '0',
    'TAGLIST_FONT_COLOR': '#fff',
    'TAGLIST_BG_COLOR': '#000',
    'FULLWINDOW_FONT_COLOR': '#fff',
    'FULLWINDOW_BG_COLOR': '#000',
    'START_DISPLAY': '2',
    'START_MAXIMIZED': 'True',
    'TAGLIST_DIR': os.path.expanduser("~/Pictures/TAGLISTS/"),
    'PROC_DIR': os.path.expanduser("~/Pictures/TAGGERIST/PROC/"),
    'UNPROC_DIR': os.path.expanduser("~/Pictures/TAGGERIST/UNPROC/")
}

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
        self.config = configparser.ConfigParser()
        self.config.read_dict({'DEFAULT': DEFAULTS, 'DIRECTORIES': {}})
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
        fullwindow_bg = self.get_config('COLORS', 'FULLWINDOW_BG_COLOR')
        fullwindow_font = self.get_config('COLORS', 'FULLWINDOW_FONT_COLOR')
        self.setStyleSheet(f"background-color: {fullwindow_bg}; color: {fullwindow_font};")
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
        self.tl.all_tags = []
        self.tl.conversion_table = {}
        taglist_dir = os.path.expanduser(self.get_config('DIRECTORIES', 'TAGLIST_DIR'))
        taglist_file = os.path.join(taglist_dir, "Taggerist_taglist.csv")
        if not os.path.exists(taglist_dir):
            os.makedirs(taglist_dir, exist_ok=True)
        if os.path.exists(taglist_file):
            try:
                with open(taglist_file, mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        if not row:
                            continue
                        new_tag = row[0].strip()
                        if new_tag:
                            self.tl.all_tags.append(new_tag)
                            if len(row) > 1:
                                for old_tag in row[1:]:
                                    old_tag = old_tag.strip()
                                    if old_tag:
                                        self.tl.conversion_table[old_tag.lower()] = new_tag
            except Exception as e:
                print(f"Error loading taglist: {e}")
        self.tl.all_tags = sorted(set(self.tl.all_tags))
        self.tl.populate_taglist()

    def refresh_taglist(self):
        self.tl.filename_edit.textChanged.disconnect()
        self.tl.at_radio.clicked.disconnect()
        self.tl.copyright_radio.clicked.disconnect()
        try:
            self.load_taglist_and_conversions()
            self.tl.populate_taglist()
            if hasattr(self.tv, 'current_file') and self.tv.current_file:
                self.tl.load_image(self.tv.current_file)
                self.tl.update_pathname(self.tv.current_file)
        finally:
            self.tl.filename_edit.textChanged.connect(self.tl.update_tag_highlights)
            self.tl.at_radio.clicked.connect(self.tl.handle_radio_click)
            self.tl.copyright_radio.clicked.connect(self.tl.handle_radio_click)

    def load_settings(self):
        proc_dir = os.path.expanduser(self.get_config('DIRECTORIES', 'PROC_DIR'))
        unproc_dir = os.path.expanduser(self.get_config('DIRECTORIES', 'UNPROC_DIR'))
        self.tf.proc_dir = proc_dir
        self.tf.unproc_dir = unproc_dir
        self.tf.proc_path_label.setText(proc_dir)
        self.tf.unproc_path_label.setText(unproc_dir)
        self.tf.refresh_lists()

    def save_settings(self):
        pass

    def closeEvent(self, event):
        super().closeEvent(event)

    def update_window_title(self):
        if self.current_file:
            self.setWindowTitle(f"Taggerist v11m - {os.path.basename(self.current_file)}")
        else:
            self.setWindowTitle("Taggerist v11m")

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
        self.image_label.setStyleSheet("background-color: #000; border: 1px solid #444;")
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
        self.taglist_font_color = strip_comment(self.parent.get_config('COLORS', 'TAGLIST_FONT_COLOR'))
        self.taglist_bg_color = strip_comment(self.parent.get_config('COLORS', 'TAGLIST_BG_COLOR'))
        font_metrics = QFontMetrics(QFont("Ubuntu", self.taglist_font_size))
        self.tag_height = font_metrics.height()
        self.setup_ui()
        self.setup_radio_buttons()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        filename_header_layout = QHBoxLayout()
        self.original_filename_label = QLabel()
        self.original_filename_label.setStyleSheet("background-color: #ADD8E6; color: #000; border: 1px solid #444;")
        self.original_filename_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.original_filename_label.setMinimumHeight(30)
        self.original_filename_label.setAlignment(Qt.AlignLeft)
        self.original_filename_label.setFont(QFont("Ubuntu", 12))
        self.original_filename_label.setWordWrap(True)
        self.original_filename_label.setTextFormat(Qt.PlainText)
        filename_header_layout.addWidget(self.original_filename_label)
        self.skip_btn = QPushButton("SKIP")
        self.skip_btn.clicked.connect(self.skip_file)
        filename_header_layout.addWidget(self.skip_btn)
        layout.addLayout(filename_header_layout, stretch=0)
        filename_layout = QHBoxLayout()
        self.at_radio = QRadioButton("@")
        self.at_radio.setStyleSheet("color: #fff; font-size: 16px;")
        self.at_radio.setFixedWidth(40)
        self.copyright_radio = QRadioButton("©")
        self.copyright_radio.setStyleSheet("color: #fff; font-size: 16px;")
        self.copyright_radio.setFixedWidth(40)
        self.mode_group = QButtonGroup()
        self.mode_group.addButton(self.at_radio)
        self.mode_group.addButton(self.copyright_radio)
        filename_layout.addWidget(self.at_radio)
        filename_layout.addWidget(self.copyright_radio)
        self.filename_edit = QLineEdit()
        self.filename_edit.setFont(QFont("Ubuntu", 14))
        self.filename_edit.setStyleSheet("background-color: #000; color: #fff;")
        filename_layout.addWidget(self.filename_edit, stretch=1)
        self.process_btn = QPushButton("Process")
        self.process_btn.clicked.connect(self.save_and_next)
        filename_layout.addWidget(self.process_btn)
        layout.addLayout(filename_layout, stretch=0)
        self.setup_taglist_window(layout)
        bottom_layout = QHBoxLayout()
        self.length_label = QLabel("0/255")
        self.length_label.setStyleSheet("color: #fff;")
        bottom_layout.addWidget(self.length_label)
        bottom_layout.addStretch()
        self.refresh_btn = QPushButton("Refresh Tags")
        self.refresh_btn.clicked.connect(self.parent.refresh_taglist)
        bottom_layout.addWidget(self.refresh_btn)
        bottom_layout.addStretch()
        layout.addLayout(bottom_layout, stretch=0)

    def setup_radio_buttons(self):
        pass

    def setup_taglist_window(self, layout):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet(f"background-color: {self.taglist_bg_color}; border: none;")
        self.scroll_area.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setViewportMargins(0, 0, 0, 0)
        layout.addWidget(self.scroll_area, stretch=1)
        self.grid_layout_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_layout_widget)
        self.grid_layout.setSpacing(0)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area.setWidget(self.grid_layout_widget)

    def populate_taglist(self):
        for i in reversed(range(self.grid_layout.count())):
            item = self.grid_layout.itemAt(i)
            if item:
                item.widget().setParent(None)
        sorted_tags = sorted(self.all_tags)
        num_tags = len(sorted_tags)
        columns = self.taglist_columns
        rows_needed = (num_tags + columns - 1) // columns
        for i, tag in enumerate(sorted_tags):
            col = i // rows_needed
            row = i % rows_needed
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
                    tag_pattern = f'|{t}|'
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

    def load_image(self, filepath):
        if not filepath:
            return
        self.original_filename = filepath
        self.original_filename_label.setText(filepath)
        self.original_filename_label.setToolTip(filepath)
        self.extract_tags_and_datestamp(filepath)
        converted_filename = self.convert_delimiters_to_pipes(os.path.basename(filepath))
        self.filename_edit.setText(converted_filename)
        self.selected_tags.clear()
        self.extract_tags_from_filename(converted_filename)

    def convert_delimiters_to_pipes(self, filename):
        if not filename:
            return ""
        filename = filename.replace("(c)", "©")
        converted = filename.replace('`', '|').replace('[', '|').replace(']', '|')
        for old_tag_lower, new_tag in self.conversion_table.items():
            old_tag_pattern = re.compile(re.escape(old_tag_lower), re.IGNORECASE)
            converted = old_tag_pattern.sub(new_tag, converted)
        while '||' in converted:
            converted = converted.replace('||', '|')
        return converted

    def extract_tags_from_filename(self, filename):
        if not filename:
            return
        tags_in_filename = re.findall(r'\|([^\|]+)\|', filename)
        for tag in tags_in_filename:
            self.selected_tags.add(tag)
        self.update_tag_highlights()

    def extract_tags_and_datestamp(self, filepath):
        if not filepath:
            return
        filename = os.path.basename(filepath)
        at_match = re.search(r'(@\d{2}\.\d{4}-\d{4}\.\d{6})', filename)
        copyright_match = re.search(r'(©\d{2}\.\d{4}-\d{4}\.\d{6})', filename)
        if at_match:
            self.current_mode = "@"
            self.at_radio.setChecked(True)
            self.copyright_radio.setChecked(False)
        elif copyright_match:
            self.current_mode = "©"
            self.at_radio.setChecked(False)
            self.copyright_radio.setChecked(True)
        else:
            self.current_mode = None
            self.flash_radio_buttons()
        self.reset_radio_styles()

    def flash_radio_buttons(self):
        self.at_radio.setStyleSheet("color: #fff; background-color: #f00; font-size: 16px;")
        self.copyright_radio.setStyleSheet("color: #fff; background-color: #f00; font-size: 16px;")
        QTimer.singleShot(1000, self.reset_radio_styles)

    def reset_radio_styles(self):
        if self.current_mode is None:
            self.flash_radio_buttons()
        else:
            self.at_radio.setStyleSheet("color: #fff; font-size: 16px;")
            self.copyright_radio.setStyleSheet("color: #fff; font-size: 16px;")

    def handle_radio_click(self):
        sender = self.sender()
        new_mode = sender.text()
        if self.current_mode == new_mode:
            return
        current_tags = self.selected_tags.copy()
        self.current_mode = new_mode
        self.update_filename_preview()
        self.selected_tags = current_tags
        self.update_tag_highlights()
        self.reset_radio_styles()

    def update_filename_preview(self):
        if not hasattr(self.parent.tv, 'current_file') or not self.parent.tv.current_file:
            return
        base_filename = os.path.basename(self.parent.tv.current_file)
        self.original_filename_label.setText(self.parent.tv.current_file)
        at_match = re.search(r'(@\d{2}\.\d{4}-\d{4}\.\d{6})', base_filename)
        copyright_match = re.search(r'(©\d{2}\.\d{4}-\d{4}\.\d{6})', base_filename)
        if at_match:
            datestamp = at_match.group(1)
        elif copyright_match:
            datestamp = copyright_match.group(1)
        else:
            if self.current_mode:
                base = datetime.now().strftime("%y.%m%d-%H%M.%S")
                unique_id = f"{random.randint(0, 9999):04d}"
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
            converted_filename = self.convert_delimiters_to_pipes(os.path.basename(filepath))
            self.filename_edit.setText(converted_filename)
            self.selected_tags.clear()
            self.extract_tags_from_filename(converted_filename)
            self.extract_tags_and_datestamp(filepath)
        else:
            self.original_filename_label.setText("")
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
                            f"color: #fff; background-color: #f00;" if length > 150 else
                            f"color: #000; background-color: #f90;" if length > 100 else
                            f"color: #000; background-color: #ff0;"
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
            self.parent.tf.refresh_lists()
            self.parent.save_settings()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error saving: {e}")
            return
        if hasattr(self.parent.tv, 'current_index') and self.parent.tv.current_index < len(self.parent.tv.file_list) - 1:
            next_file = os.path.join(self.parent.tv.current_dir, self.parent.tv.file_list[self.parent.tv.current_index + 1])
            self.parent.tv.load_file(next_file)

    def skip_file(self):
        if not self.parent.tv.current_file:
            return
        try:
            current_time = int(datetime.now().timestamp())
            os.utime(self.parent.tv.current_file, (current_time, current_time))
            self.parent.tf.refresh_lists()
            self.parent.save_settings()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error updating modification time: {e}")
            return
        converted_filename = self.convert_delimiters_to_pipes(os.path.basename(self.parent.tv.current_file))
        self.filename_edit.setText(converted_filename)
        self.selected_tags.clear()
        self.extract_tags_from_filename(converted_filename)
        self.update_filename_preview()
        self.parent.tf.refresh_lists()
        if hasattr(self.parent.tv, 'current_index') and self.parent.tv.current_index < len(self.parent.tv.file_list) - 1:
            next_file = os.path.join(self.parent.tv.current_dir, self.parent.tv.file_list[self.parent.tv.current_index + 1])
            self.parent.tv.load_file(next_file)

# ========== TF (Taggerist-Files) ==========
class TaggeristFiles(QFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.proc_dir = os.path.expanduser(self.parent.get_config('DIRECTORIES', 'PROC_DIR'))
        self.unproc_dir = os.path.expanduser(self.parent.get_config('DIRECTORIES', 'UNPROC_DIR'))
        self.setup_ui()
        self.refresh_lists()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(10, 10, 10, 10)
        splitter = QSplitter(Qt.Vertical)
        layout.addWidget(splitter)
        self.proc_frame = QFrame()
        self.proc_layout = QVBoxLayout(self.proc_frame)
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
        self.proc_label = QLabel("PROCESSED")
        self.proc_label.setStyleSheet("color: #fff; font-weight: bold;")
        self.proc_layout.addWidget(self.proc_label)
        self.proc_table = QTableWidget()
        self.proc_table.setColumnCount(2)
        self.proc_table.setHorizontalHeaderLabels(["Filename", "Modified"])
        self.proc_table.setStyleSheet("background-color: #000; color: #fff;")
        self.proc_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.proc_table.setSelectionMode(QTableWidget.SingleSelection)
        self.proc_table.horizontalHeader().setStretchLastSection(True)
        self.proc_table.setColumnWidth(0, int(self.width() * 0.9))
        self.proc_table.itemDoubleClicked.connect(self.load_file_from_proc)
        self.unproc_frame = QFrame()
        self.unproc_layout = QVBoxLayout(self.unproc_frame)
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
        self.unproc_label = QLabel("UNPROCESSED")
        self.unproc_label.setStyleSheet("color: #fff; font-weight: bold;")
        self.unproc_layout.addWidget(self.unproc_label)
        self.unproc_table = QTableWidget()
        self.unproc_table.setColumnCount(2)
        self.unproc_table.setHorizontalHeaderLabels(["Filename", "Modified"])
        self.unproc_table.setStyleSheet("background-color: #000; color: #fff;")
        self.unproc_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.unproc_table.setSelectionMode(QTableWidget.SingleSelection)
        self.unproc_table.horizontalHeader().setStretchLastSection(True)
        self.unproc_table.setColumnWidth(0, int(self.width() * 0.9))
        self.unproc_table.itemDoubleClicked.connect(self.load_file_from_unproc)
        splitter.addWidget(self.proc_frame)
        splitter.addWidget(self.unproc_frame)

    def open_directory(self, dir_type):
        if dir_type == "proc":
            path = self.proc_dir
        elif dir_type == "unproc":
            path = self.unproc_dir
        else:
            return
        try:
            subprocess.Popen(["xdg-open", path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            QMessageBox.warning(self, "Error", f"Could not open directory: {path}")

    def load_file_from_proc(self, item):
        filename = item.text()
        filepath = os.path.join(self.proc_dir, filename)
        if os.path.exists(filepath):
            self.parent.tv.load_file(filepath)

    def load_file_from_unproc(self, item):
        filename = item.text()
        filepath = os.path.join(self.unproc_dir, filename)
        if os.path.exists(filepath):
            self.parent.tv.load_file(filepath)

    def refresh_lists(self):
        self.refresh_proc_list()
        self.refresh_unproc_list()

    def refresh_proc_list(self):
        self.proc_table.setRowCount(0)
        if os.path.exists(self.proc_dir):
            files = [f for f in os.listdir(self.proc_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            files.sort()
            for i, filename in enumerate(files):
                filepath = os.path.join(self.proc_dir, filename)
                mod_time = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%Y-%m-%d %H:%M:%S")
                self.proc_table.insertRow(i)
                self.proc_table.setItem(i, 0, QTableWidgetItem(filename))
                self.proc_table.setItem(i, 1, QTableWidgetItem(mod_time))

    def refresh_unproc_list(self):
        self.unproc_table.setRowCount(0)
        if os.path.exists(self.unproc_dir):
            files = [f for f in os.listdir(self.unproc_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            files.sort()
            for i, filename in enumerate(files):
                filepath = os.path.join(self.unproc_dir, filename)
                mod_time = datetime.fromtimestamp(os.path.getmtime(filepath)).strftime("%Y-%m-%d %H:%M:%S")
                self.unproc_table.insertRow(i)
                self.unproc_table.setItem(i, 0, QTableWidgetItem(filename))
                self.unproc_table.setItem(i, 1, QTableWidgetItem(mod_time))

    def highlight_current_file(self, filepath):
        if not filepath:
            return
        filename = os.path.basename(filepath)
        for i in range(self.proc_table.rowCount()):
            if self.proc_table.item(i, 0).text() == filename:
                self.proc_table.selectRow(i)
                self.proc_table.scrollToItem(self.proc_table.item(i, 0))
                break
        for i in range(self.unproc_table.rowCount()):
            if self.unproc_table.item(i, 0).text() == filename:
                self.unproc_table.selectRow(i)
                self.unproc_table.scrollToItem(self.unproc_table.item(i, 0))
                break

# ========== MAIN ==========
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaggeristMainWindow()
    window.show()
    sys.exit(app.exec())
