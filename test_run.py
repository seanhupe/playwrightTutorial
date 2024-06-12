import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Assess
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    # Open a new page
    page = context.new_page()
    # Page to go to
    page.goto("https://playwright.dev/")
    page.set_default_timeout(2000)

    # Act
    # Page Actions
    page.get_by_role("link", name="Get started").click()
    page.get_by_role("link", name="Playwright logo Playwright").click()
    page.get_by_role("link", name="Trace Viewer.").click()

    # Assert
    assert page.is_visible("text=Trace Viewer")
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
