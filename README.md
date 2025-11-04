# Scrap.tf Automatic Raffle Entering

A Python script using **Playwright** to automate entering public raffles on [Scrap.tf](https://scrap.tf).  

> **Disclaimer:** This script is intended for personal use. Automating entries may violate Scrap.tf’s Terms of Service. Use responsibly.

---

## Features

- Detects unentered raffles on the public raffles page.
- Opens each raffle in a new tab.
- Clicks the visible **Enter Raffle** button.
- Confirms entry by detecting the **Leave Raffle** button.
- Logs activity with timestamps to console.
- Random short delays between actions to mimic human behavior.

---

## Requirements

- Python
- uv
- Playwright
- Playwright chromium driver

## Installation

1. Clone the repo

    `git clone https://github.com/Large-Croissant/scrap-tf_raffle_auto_enter.git`

2. Install playwright drivers

    `uv playwright install`

## Usage

1. Run the script

    `uv run ./main.py`

2. Log into Steam in the window that pops up

3. Let the script run

4. Press `Enter` in the terminal to exit the script after it finishes when prompted