import playwright
import playwright.sync_api
import time
import random
import sys
import logging

def rand_wait():
    time.sleep(random.randrange(3, 12)/10)


def main():
    with playwright.sync_api.sync_playwright() as p:
        # Launch the browser (headless=False to see the browser window)
        browser = p.chromium.launch(headless=False).new_context()
        
        page = browser.new_page()

        # Navigate to a webpage
        page.goto("https://scrap.tf/login")
        print("Navigated to login page", file=sys.stderr, flush=True)

        input("Press <Enter> when logged in...")
        print("User logged in", file=sys.stderr, flush=True)

        page.goto("https://scrap.tf/raffles")
        print("Navigated to raffles page", file=sys.stderr, flush=True)
        page.wait_for_selector("#raffles-list")
        print("Raffles found", file=sys.stderr, flush=True)

        all_raffles = page.query_selector_all("#raffles-list .panel-raffle")
        unentered_raffle_links = []
        for raffle in all_raffles:
            if "raffle-entered" not in raffle.get_attribute("class"):
                href = raffle.query_selector(".raffle-name a").get_attribute("href")
                unentered_raffle_links.append(f"https://scrap.tf{href}")
                print(f"Raffle https://scrap.tf{href} found", file=sys.stderr, flush=True)
        
        rand_wait()

        for link in unentered_raffle_links:
            raffle_page = browser.new_page()
            raffle_page.goto(link)
            print(f"Navigated to raffle {link}", file=sys.stderr, flush=True)
            raffle_page.wait_for_selector("#raffle-enter", state="visible")
            print("Enter raffle button found", file=sys.stderr, flush=True)
            rand_wait()
            raffle_page.click("#raffle-enter")
            print("Clicked enter raffle button", file=sys.stderr, flush=True)
            raffle_page.wait_for_selector("#raffle-leave")
            print("Raffle enter successful", file=sys.stderr, flush=True)
            rand_wait()
            print("Leaving page", file=sys.stderr, flush=True)
            raffle_page.close()

        input("<Enter> to close")
        browser.close()


if __name__ == "__main__":
    main()
