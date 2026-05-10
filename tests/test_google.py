# tests/test_google.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestGoogle:

    def test_page_title(self, driver):
        driver.get("https://www.google.com")
        print(f"\nPage title is: {driver.title}")
        assert "Google" in driver.title, \
            f"Expected 'Google' in title but got: {driver.title}"
        print("Test 1 Passed!")


    def test_search_box_visible(self, driver):
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        assert search_box.is_displayed(), \
            "Search box is not visible on page!"
        print("Test 2 Passed - Search box is visible!")

    def test_search_returns_results(self, driver):
        driver.get("https://www.google.com")

        # Wait for search box to be ready first
        wait = WebDriverWait(driver, 10)
        search_box = wait.until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # Type search term
        search_box.send_keys("Selenium Python")
        search_box.send_keys(Keys.RETURN)

        # Wait for URL to change instead of title
        # URL is more reliable than title in headless mode!
        wait.until(EC.url_contains("search"))

        # Check current URL contains search query
        current_url = driver.current_url
        print(f"\nCurrent URL after search: {current_url}")

        assert "search" in current_url, \
            f"Search did not work! URL: {current_url}"
        print("Test 3 Passed - Search works!")