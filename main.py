import playwright
import playwright.sync_api
import time
import random
import logging


def rand_wait():
    rand_time = random.randrange(3, 12) / 10
    logging.debug(f"Waiting for {rand_time} seconds")
    time.sleep(rand_time)


def main():
    with playwright.sync_api.sync_playwright() as p:
        # Launch the browser (headless=False to see the browser window)
        browser = p.chromium.launch(headless=False).new_context()

        page = browser.new_page()

        # Navigate to a webpage
        page.goto("https://scrap.tf/login")
        logging.info("Navigated to login page")

        page.wait_for_url("https://scrap.tf", timeout=0)
        logging.info("User logged in")
        rand_wait()

        page.goto("https://scrap.tf/raffles")
        logging.info("Navigated to public raffles page")
        page.wait_for_selector("#raffles-list")
        logging.info("Raffles found")

        all_raffles = page.query_selector_all("#raffles-list .panel-raffle")
        unentered_raffle_links = []
        for raffle in all_raffles:
            if "raffle-entered" not in raffle.get_attribute("class"):
                href = raffle.query_selector(".raffle-name a").get_attribute("href")
                unentered_raffle_links.append(f"https://scrap.tf{href}")
                logging.info(f"Raffle https://scrap.tf{href} found")

        rand_wait()

        for link in unentered_raffle_links:
            raffle_page = browser.new_page()
            raffle_page.goto(link)
            logging.info(f"Navigated to raffle {link}")
            enter_button = raffle_page.wait_for_selector("button:has-text('Enter Raffle'):visible")
            if enter_button:
                logging.info("Raffle enter button found")
                rand_wait()
                logging.info("Attempting to enter raffle")
                enter_button.click()
                logging.info("Clicked button to enter raffle")
                try:
                    raffle_page.wait_for_selector("button:has-text('Leave Raffle')", timeout=18000)
                    logging.info("Raffle successfully entered")
                    rand_wait()
                except Exception:
                    logging.warning("Timed out waiting for raffle enter")
            else:
                logging.warning("Couldn't find enter raffle button")
            logging.info("Leaving raffle page")
            raffle_page.close()

        input("<Enter> to close")
        browser.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.StreamHandler()])
    main()
