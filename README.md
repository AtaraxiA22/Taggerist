# Taggerist
# Taggerist

**A portable, database-free image tagging system for managing large collections.**

---
DEVELOPMENT STAGE: **Pre-Alpha**: Early development, unstable, unpolished, limited testing, and tailored for specific use cases.
---

## 📌 About
Taggerist allows you to **individually tag image files** by embedding metadata *directly into filenames*. No database required—just your files and a simple, portable script.

**Key Features**:
- Rapidly add/edit human-readable/meaningful tagnames in image filenames. Oriented to production.
- Search and filter images using **your system search tools** (no database overhead).
- Fully **portable** (NO database!):
- GUI Script works on any system with Python.
- Use system tools to manually edit individual tagnames in files, if needed. Edit/Add/remove tags via a **GUI or CLI**.
- Accommodates hundreds of tagnames in simple .CSV file.
- Ideal for **photographers, archivists, or fetish artists** managing large image collections.
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
