from playwright.sync_api import sync_playwright
import json
import time

PROFILE_URL = "https://www.linkedin.com/in/shraddhaalhat/"

def load_cookies(context):
    with open("cookies.json", "r") as f:
        cookies = json.load(f)
    context.add_cookies(cookies)

profile_data = {}

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    load_cookies(context)

    page = context.new_page()
    page.goto(PROFILE_URL, timeout=60000)
    page.wait_for_selector("h1")

    # Scroll to load sections
    for _ in range(4):
        page.mouse.wheel(0, 1500)
        time.sleep(1)

    # Basic info
    profile_data["name"] = page.locator("h1").inner_text()
    profile_data["headline"] = page.locator("div.text-body-medium").first.inner_text()
    profile_data["location"] = page.locator("span.text-body-small.inline").inner_text()

    # EXPERIENCE
    # ---------- EXPERIENCE ----------
    page.goto("https://www.linkedin.com/in/shraddhaalhat/details/experience/")
    page.wait_for_timeout(3000)

    profile_data["experience"] = []

    for role in page.locator("li.pvs-list__paged-list-item").all():
        text = role.inner_text().strip()
        if text:
            profile_data["experience"].append(text)


    # EDUCATION
    # ---------- EDUCATION ----------
    page.goto("https://www.linkedin.com/in/shraddhaalhat/details/education/")
    page.wait_for_timeout(3000)

    profile_data["education"] = []

    for edu in page.locator("li.pvs-list__paged-list-item").all():
        text = edu.inner_text().strip()
        if text:
            profile_data["education"].append(text)

    # ---------- POSTS / REPOSTS ----------
    # ---------- POSTS / REPOSTS ----------
    # ---------- POSTS / REPOSTS ----------
    page.goto("https://www.linkedin.com/in/shraddhaalhat/recent-activity/shares/")
    page.wait_for_timeout(4000)

    profile_data["posts"] = {}
    SCROLL_COUNT = 6

    for _ in range(SCROLL_COUNT):
        post_cards = page.locator("div.feed-shared-update-v2").all()

        for card in post_cards:
            try:
                post_id = card.get_attribute("data-urn")
                text = card.inner_text().strip()

                if post_id and post_id not in profile_data["posts"]:
                    profile_data["posts"][post_id] = text

            except:
                continue

        page.mouse.wheel(0, 3000)
        page.wait_for_timeout(3000)

    # convert dict to list
    profile_data["posts"] = list(profile_data["posts"].values())




    browser.close()

with open("profile_data.json", "w", encoding="utf-8") as f:
    json.dump(profile_data, f, indent=2, ensure_ascii=False)

print("✅ Profile data extracted successfully")
