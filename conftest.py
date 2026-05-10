# conftest.py
# ----------------------------------------------------------
# Selenium 4.6+ built-in driver management
# No ChromeDriverManager needed!
# ----------------------------------------------------------

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def driver():

    print("\n🚀 Opening Chrome browser...")

    # Chrome settings
    chrome_options = Options()

    # Comment this line to SEE the browser while testing locally
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # ✨ No Service, No ChromeDriverManager needed!
    # Selenium 4.6+ handles driver download automatically!
    browser = webdriver.Chrome(options=chrome_options)

    yield browser

    print("\n✅ Closing Chrome browser...")
    browser.quit()