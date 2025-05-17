import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    searchBox = page.locator("#input")
    searchBox.click()
    searchBox.type("weather")
    print(page.title())
    time.sleep(5)