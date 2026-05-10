# tests/test_google.py
# ----------------------------------------------------------
# This is your ACTUAL test file.
# Rules pytest follows automatically:
#   → File must start with  "test_"
#   → Class must start with "Test"
#   → Function must start with "test_"
# ----------------------------------------------------------

# By → how we FIND elements on a webpage (by id, name, etc.)
from selenium.webdriver.common.by import By

# Keys → simulates keyboard keys like ENTER, TAB etc.
from selenium.webdriver.common.keys import Keys

# WebDriverWait → smarter way to wait for page to load
# Much better than time.sleep()!
from selenium.webdriver.support.ui import WebDriverWait

# expected_conditions → WHAT we are waiting for
from selenium.webdriver.support import expected_conditions as EC


# ----------------------------------------------------------
# We group related tests inside a Class
# Think of it like a FOLDER for tests about Google
# ----------------------------------------------------------
class TestGoogle:

    def test_page_title(self, driver):
        # --------------------------------------------------
        # TEST 1: Check if Google's title says "Google"
        #
        # 'driver' is the browser from conftest.py
        # pytest passes it in automatically!
        # --------------------------------------------------

        # Open Google in the browser
        driver.get("https://www.google.com")

        # driver.title → reads the text in the browser tab
        print(f"\n📋 Page title is: {driver.title}")

        # assert → if this is False, test FAILS with message
        assert "Google" in driver.title, \
            f"❌ Expected 'Google' in title but got: {driver.title}"

        print("✅ Test 1 Passed!")


    def test_search_box_visible(self, driver):
        # --------------------------------------------------
        # TEST 2: Is the search box visible on the page?
        #
        # We find the search box using By.NAME
        # Google's search box in HTML looks like:
        # <input name="q" ...>
        # --------------------------------------------------

        driver.get("https://www.google.com")

        # Find the element with name="q"
        search_box = driver.find_element(By.NAME, "q")

        # is_displayed() → True if element is visible
        assert search_box.is_displayed(), \
            "❌ Search box is not visible on page!"

        print("✅ Test 2 Passed — Search box is visible!")


    def test_search_returns_results(self, driver):
        # --------------------------------------------------
        # TEST 3: Type something and check results appear
        #
        # Steps:
        # 1. Open Google
        # 2. Find the search box
        # 3. Type "Selenium Python"
        # 4. Press ENTER
        # 5. Wait for results
        # 6. Check page title changed
        # --------------------------------------------------

        driver.get("https://www.google.com")

        # Find search box
        search_box = driver.find_element(By.NAME, "q")

        # Type into the search box
        search_box.send_keys("Selenium Python")

        # Press Enter key
        search_box.send_keys(Keys.RETURN)

        # Wait SMARTLY — up to 10 seconds
        # Only moves on when page title contains "Selenium Python"
        # Much better than time.sleep(5) which always waits 5 sec!
        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("Selenium Python"))

        print(f"\n📋 After search, title is: {driver.title}")

        assert "Selenium Python" in driver.title, \
            "❌ Search did not work, title did not update!"

        print("✅ Test 3 Passed — Search works!")