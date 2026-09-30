# Taggerist

**A portable, database-free image tagging system for managing large collections.**

---

DEVELOPMENT STAGE: **Pre-Alpha**: Early development, unstable, unpolished, limited testing, and tailored for specific use cases.

---

## 📌 About

Taggerist allows you to **individually tag image files** by embedding metadata *directly into filenames*. No database required—just your files and a simple, portable script.

**Key Features**:

- Rapidly add/edit human-readable/meaningful tagnames in image filenames. Oriented to production.
- **Use your system search tools** to search and filter images using (no database overhead).
- Fully **portable** (NO database!):
- GUI Script works on any system with Python.
- Use system tools to manually edit individual tagnames in files, if needed. Edit/Add/remove tags via a **GUI or CLI**.
- Accommodates hundreds of tagnames in simple .CSV file.
- Ideal for **photographers, archivists, or fetish artists** managing large, complex image collections.
- GUI includes 3 windows: (1) Files (select file to process), (2) View (visually preview the image) (3) Taglist (select tags to add)
- Automatically converts obsolete tagnames to new ones. (e.g. Canine,Rover,mutt ---> Dog)

---

## 🛠 Setup

### Prerequisites

- Python 3.8+
- PySide6 (for GUI)
- Pillow (for image handling)

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/AtaraxiA22/Taggerist.git
   cd Taggerist
   ```

---

## ⌨️ Keyboard Shortcuts

- **Alt+P** — PROCESS the current file and move to the next
- **Alt+S** — SKIP the current file
- **Alt+R** — REDUCE the filename (strip redundant segments, keep tags/brackets/dates)
- **Alt+L** or **Alt+C** — CLEAR the filename edit box (two keys, since some Linux desktops reserve Alt+C)
- **Alt+Delete** — clear the Search and Brackets boxes
- **Alt+T** — SORT the tags in the filename alphabetically
- **Alt+D** — FIX DATE: convert a camera-style date (e.g. `2024-08-20 01-25-25-024`) into a Taggerist datestamp
- **Alt+Delete** — clear the Search and Brackets boxes
- **Alt+1 / Alt+2 / Alt+3** — press the 1st / 2nd / 3rd CI button (adds CI symbol + date prefix)
- **Alt+← / Alt+→ / Alt+↑ / Alt+↓** — move focus between the Filename edit box, Brackets box and Search box
- **← / →** (in the Search box) — move the highlight (hot tag) through the search-result chips
- **↑ / ↓** (in the Search or Brackets box) — jump focus up/down between the Filename edit box, Brackets box and Search box
- **Enter** (in Search or Brackets box) — accept the first search result / commit the bracket text
- **Esc** — jump focus to the Search box
- **Ctrl+Enter** — jump focus to the Filename edit box
