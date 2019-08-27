"""
Module docstring
test google.com
"""

from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.mark.google
def test_google_com(driver):
    """
    Test login page: with valid username and invalid password.
    Verify that proper error message is given to user.
    """
    # go to the google home page
    driver.get("http://www.google.com")

    # the page is ajaxy so the title is originally this:
    print(driver.title)

    # find the element that's name attribute is q (the google search box)
    search_box = driver.find_element_by_name("q")

    # type in the search
    search_box.send_keys("cheese!")
    # import time
    # time.sleep(3)
    # submit the form (although google automatically searches now without submitting)
    search_box.send_keys(Keys.RETURN)

    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))

    # You should see "cheese! - Google Search"
    assert "cheese!" in driver.title
