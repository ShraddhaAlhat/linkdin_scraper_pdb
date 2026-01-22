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

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ShraddhaAlhat/linkdin_scraper_pdb.git
cd linkdin_scraper_pdb
```

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

## 🔐 Step 1: Manual Login & Session Creation

```bash
python login_and_save_session.py
```

### What happens in this step:

* A browser window opens
* You log in **manually** to LinkedIn (email, password, OTP)
* After successful login, session cookies are saved in `cookies.json`

✅ No credentials are stored in code
✅ Safer and compliant with ethical scraping practices

---

## 📄 Step 2: Scrape Personal Profile Data

```bash
python scrape_profile.py
```

### This script extracts:

* Basic profile details (name, headline, location)
* Experience (from `/details/experience/` page)
* Education (from `/details/education/` page)
* Posts & reposts (from `/recent-activity/shares/` page)

All extracted data is saved in:

```
profile_data.json
```

---

## 🧠 Approach Explanation 

### 🔹 Why Manual Login?

Automating login using credentials can violate platform policies and risk account blocking. Therefore, this project uses **manual login once** and securely reuses the session cookies.

### 🔹 Handling Dynamic Content

LinkedIn is a JavaScript-heavy platform that loads data dynamically. Playwright was chosen because it:

* Automatically waits for elements to load
* Handles infinite scrolling gracefully

### 🔹 Clean Data Separation

Instead of scraping everything from the main profile page:

* **Experience** is scraped from a dedicated experience page
* **Education** is scraped from a dedicated education page
* **Posts/Reposts** are scraped separately from the activity feed

This avoids mixing feed content with profile sections.

### 🔹 Duplicate Post Handling

LinkedIn re-renders posts during scrolling. To avoid duplicates:

* Each post is identified using a unique `data-urn`
* Posts are deduplicated using ID-based logic

---

## ⚠️ Ethical Considerations & Limitations

* Scrapes **only my own LinkedIn profile**
* Does not accept external profile URLs
* Limited scroll depth to avoid excessive requests
* LinkedIn DOM structure may change over time
* Not intended for large-scale or commercial scraping

---

## ✅ Final Outcome

* Ethical and compliant scraping
* Structured, readable JSON output
* Robust handling of dynamic pages
* Interview- and assignment-ready implementation

---

## 📂 Output Example (Simplified)

```json
{
  "name": "Shraddha Alhat",
  "headline": "AI & Machine Learning Enthusiast | Python | GenAI",
  "location": "Pune, Maharashtra, India",
  "experience": [...],
  "education": [...],
  "posts": [...]
}
```

---

## 👩‍💻 Author

**Shraddha Alhat**

---

✨ This project focuses on learning browser automation, ethical scraping, and handling real-world dynamic web applications.
