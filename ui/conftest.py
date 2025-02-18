import pytest
from ui.drivers.appium_driver import get_driver


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

