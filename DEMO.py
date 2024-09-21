from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

try:
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Enable headless mode
    firefox_options.add_argument("--window-size=1366,768")
    firefox_options.add_argument("--no-sandbox")  # No sandbox mode
    firefox_options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Set custom user agent

    # Automation-controlled workaround
    firefox_options.set_preference("dom.webdriver.enabled", False)
    firefox_options.set_preference('useAutomationExtension', False)

    # Use the Service object for the GeckoDriver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    driver.get("https://www.google.com")
    driver.save_screenshot('akashrahman_me.png')

except Exception as e:
    print(e)
    pass
