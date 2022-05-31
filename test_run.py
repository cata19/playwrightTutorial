import time

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # Assess  - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    page.set_default_timeout(3000)

    # Act - When/And
    # Click button:has-text("Log In")
    page.click('//html/body/div[1]/div/div[4]/div/header/div/div[2]/div[2]/div/div/section[3]/div[2]/div[2]/div['
               '2]/div/div[1]/button/span')
    # page.click("button:has-text(\"Log In\")", timeout=7000)
    # Click [data-testid="signUp\.switchToSignUp"]
    page.click("[data-testid=\"signUp\\.switchToSignUp\"]")
    # Click [data-testid="switchToEmailLink"] [data-testid="buttonElement"]
    page.click("[data-testid=\"switchToEmailLink\"] [data-testid=\"buttonElement\"]")
    # Click [data-testid="emailAuth"] input[type="email"]
    page.click("[data-testid=\"emailAuth\"] input[type=\"email\"]")
    # Fill [data-testid="emailAuth"] input[type="email"]
    page.fill("[data-testid=\"emailAuth\"] input[type=\"email\"]", "symon.storozhenko@gmail.com")
    # Press Tab
    page.press("[data-testid=\"emailAuth\"] input[type=\"email\"]", "Tab")
    # Fill input[type="password"]
    page.fill("input[type=\"password\"]", "test123")
    # Click [data-testid="submit"] [data-testid="buttonElement"]
    page.click("[data-testid=\"submit\"] [data-testid=\"buttonElement\"]")
    # Click [aria-label="symon\.storozhenko account menu"]
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
