from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from enum import Enum


def click_element(driver, element_type, locator, timeout=30):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((element_type, locator))
        )
        element.click()
    except TimeoutException:
        print(f"Error: element: {locator}, unclickable for {timeout} seconds")
    except NoSuchElementException:
        print(f"Error: Unable to find element: {locator}")


def input_text(driver, element_type, locator, text, timeout=30):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((element_type, locator))
        )
        element.clear()
        element.send_keys(text)
    except TimeoutException:
        print(f"Error: Unable to find the input element: {locator}")


def wait_for_element(driver, element_type, locator, timeout=30):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((element_type, locator))
        )
    except TimeoutException:
        print(f"Error: Unable to find element: {locator}, timeout: {timeout} sec")
        return None


def is_element_present(driver, element_type, locator):
    return len(driver.find_elements(element_type, locator)) > 0


def determine_element_exists(driver, element_type, locator):
    obj = is_element_present(driver, element_type, locator)
    if obj is True:
        return True
    else:
        print(f"Error: Unable to find element: {locator}")
        raise NoSuchElementException(f"Element not found: {locator}")


def kill_app(driver):
    driver.quit()

