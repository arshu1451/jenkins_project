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


