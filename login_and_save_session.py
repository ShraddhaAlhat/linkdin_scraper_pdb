from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.linkedin.com/login")

    print("🔐 Please login manually in the opened browser.")
    print("👉 After successful login, press ENTER here.")
    input()

    cookies = context.cookies()
    with open("cookies.json", "w") as f:
        json.dump(cookies, f, indent=2)

    print("✅ Login session saved successfully.")
    browser.close()
