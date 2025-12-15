
from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Since this is a static HTML file, we can load it directly via file protocol
        # We need the absolute path
        cwd = os.getcwd()
        file_path = f"file://{cwd}/YearEnd_2025.html"
        print(f"Loading {file_path}")
        page.goto(file_path)

        # Wait for content to load (images might take a sec)
        page.wait_for_timeout(2000)

        # Take a screenshot
        page.screenshot(path="verification/yearend_2025.png", full_page=True)
        print("Screenshot saved to verification/yearend_2025.png")
        browser.close()

if __name__ == "__main__":
    run()
