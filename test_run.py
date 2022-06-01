import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Assess  - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    time.sleep(2)

    # Act - When/And
    # page.click('button:visible')
    # page.click("'Log In'", timeout=5000) //IT DID NOT WORK
    page.locator('text="Log In"').click()
    page.click("[data-testid=\"signUp\\.switchToSignUp\"]")
    page.click("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]")
    page.click("[data-testid=\"emailAuth\"] input[type=\"email\"]")
    page.fill("[data-testid=\"emailAuth\"] input[type=\"email\"]", "symon.storozhenko@gmail.com")
    page.press("[data-testid=\"emailAuth\"] input[type=\"email\"]", "Tab")
    page.fill("input[type=\"password\"]", "test123")
    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")
    page.click("[aria-label=\"symon\\.storozhenko account menu\"]")

    # Assert - Then
    assert page.is_visible('text=My Orders')

    # Click text=My Orders
    # with page.expect_navigation(url="https://symonstorozhenko.wixsite.com/website-1/account/my-orders"):
    # with page.expect_navigation():
    #     page.locator("text=My Orders").click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

# I had to change the selector for the log in button
# I use playwright codegen 'website' to generate code
# use playwright.$("") to search for elements like , text, button, button:visible, etc...
# continue watching new section 56.NEW!
