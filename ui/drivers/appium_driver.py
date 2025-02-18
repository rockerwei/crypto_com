from appium import webdriver
from ui.config.capabilities import desired_caps


def get_driver():
    capabilities = desired_caps
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
    return driver

