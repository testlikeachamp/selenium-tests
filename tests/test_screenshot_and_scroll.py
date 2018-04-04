import time

from selenium.webdriver.common.by import By

from utils.screenshot import take_screenshot


def test_screenshot(driver):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        lognLink = driver.find_element(By.LINK_TEXT, "Login")
        lognLink.click()
        emialField = driver.find_element(By.ID, "user_email")
        emialField.send_keys("999999999@test.com")
        passwordField = driver.find_element_by_xpath("//input[@id='user_password']")
        passwordField.send_keys("123456")
        btnLogin = driver.find_element_by_xpath("//input[@name='commit']")
        btnLogin.click()
        # time.sleep(2)
        take_screenshot(driver)


def test_scroll_elements(driver):
    baseUrl = "https://letskodeit.teachable.com/p/practice"
    driver.maximize_window()
    driver.get(baseUrl)
    driver.implicitly_wait(5)

    driver.execute_script("window.scrollBy(0, 1000)")
    # time.sleep(3)

    element = driver.find_element(By.ID, "mousehover")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
