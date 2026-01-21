venv\Scripts\activate
pip install -r requirements.txt
playwright install
python login_and_save_session.py
python scrape_profile.

# LinkedIn Personal Profile Scraper

## 📌 Project Overview

This project demonstrates an **ethical and controlled approach** to extracting data **only from my own LinkedIn profile** using browser automation.

The scraper logs into LinkedIn via **manual authentication**, reuses the authenticated session securely, and extracts structured profile information such as:

* Name
* Headline
* Location
* Work Experience
* Education
* Posts / Reposts

⚠️ **Important:** This project is strictly limited to my **personal LinkedIn profile** and does **not** scrape data from other users.

---

## 🛠 Tools & Technologies Used

* **Python 3.9+**
* **Playwright (Python)** – for browser automation and handling dynamic content
* **Chromium Browser** – controlled via Playwright
* **JSON** – for structured data storage

---

## ⚙️ Setup Instructions

### 1️⃣ Activate Virtual Environment

```bash
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

> Note: Playwright requires browser binaries. If not installed, run:

```bash
playwright install
```

---



