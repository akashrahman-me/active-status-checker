import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import os
from datetime import datetime as dt
from utils.notify import notify


class OnlineStatusChecker:
    def __init__(self, account_path, nickname):
        self.account_path = account_path
        self.nickname = nickname
        self.driver = self._initialize_driver()


    def _initialize_driver(self):
        # Initialize Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1366,768")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # To avoid blink detection
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--remote-debugging-port=9222")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

        # Launch browser with undetected-chromedriver
        return uc.Chrome(options=chrome_options)

    def check_online_status(self):
        start = time.perf_counter()

        # Open the URL
        self.driver.get(self.account_path)

        # Execute the script to check if the user is online
        is_online = self.driver.execute_script(f"""
            return Array.from(document.getElementsByTagName("div"))
                        .filter((div) => div.textContent === "{self.nickname}")
                        .filter((div) => {{
                           return div.nextElementSibling?.textContent?.includes("Online");
                        }})?.length > 0
            """)

        if not is_online:
            dirname = os.path.abspath(__file__)
            dirname = os.path.dirname(dirname)
            notify( icon=f"{dirname}\\..\\images\\fiverr.png",
                    title="Not Online!",
                    message="Fiverr account isn't online, take action!")

        # Take a screenshot
        self.take_screenshot()

        print(f"Time to take online status: {round(time.perf_counter() - start)} seconds")

        self.driver.close()
        self.driver.quit()

        return is_online

    def take_screenshot(self):
        dirname = os.path.abspath(__file__)
        dirname = os.path.dirname(dirname)
        suffix = dt.now().strftime("%Y.%m.%d__%I.%M__%p")
        self.driver.save_screenshot(f"{dirname}\\..\\history\\screenshot__{suffix}.png")


# Usage
if __name__ == "__main__":
    ACCOUNT_PATH = "https://www.fiverr.com/username"  # Replace with actual URL
    NICKNAME = "your_nickname"  # Replace with actual nickname

    checker = OnlineStatusChecker(account_path=ACCOUNT_PATH, nickname=NICKNAME)
    is_online = checker.check_online_status()

    print(f"{NICKNAME} is online {'Yes' if is_online else 'No'}")
