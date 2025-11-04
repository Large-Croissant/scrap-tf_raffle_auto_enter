import playwright
import playwright.sync_api


def main():
    with playwright.sync_api.sync_playwright() as p:
        # Launch the browser (headless=False to see the browser window)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to a webpage
        page.goto("https://scrap.tf/login")

        input("Press <Enter> when logged in...")

        page.goto("https://scrap.tf/raffles")

        page.wait_for_selector("#raffles-list")

        all_raffles = page.query_selector_all("#raffles-list .panel-raffle")
        unentered_raffles = []
        for raffle in all_raffles:
            print(raffle)

        # for raffle in unentered_raffles:
        #     raffle_page = browser.new_page()
        #     raffle_page.goto("")

        input("<Enter> to close")
        browser.close()


if __name__ == "__main__":
    main()
