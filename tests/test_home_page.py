from playwright.sync_api import Page, expect


BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"


def test_parabank_homepage(page: Page):

    page.goto(BASE_URL)

    expect(page).to_have_title("ParaBank | Welcome | Online Banking")

    expect(page.get_by_text("Customer Login")).to_be_visible()

    expect(page.locator('input[name="username"]')).to_be_visible()

    expect(page.locator('input[name="password"]')).to_be_visible()
    