from ui.utils.helpers import *


def app_just_opened_and_entered_the_homepage(driver):
    wait_for_element(driver, AppiumBy.ACCESSIBILITY_ID, refresh_btn)


def expand_the_menu(driver):
    click_element(driver, AppiumBy.ACCESSIBILITY_ID, menu_btn)


def expand_the_forecast_warning_services_option(driver):
    click_element(driver, AppiumBy.XPATH, forecast_warning_services_option)


def go_to_the_9_day_forecast_page(driver):
    click_element(driver, AppiumBy.XPATH, the_9_day_forecast_option)


# ACCESSIBILITY ID
refresh_btn = 'Refresh'
menu_btn = 'Navigate up'

# XPATH
forecast_warning_services_option = '//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and ' \
                                   '@text="Forecast & Warning Services"] '

the_9_day_forecast_option = '//android.widget.TextView[@resource-id="hko.MyObservatory_v1_0:id/title" and ' \
                            '@text="9-Day Forecast"] '
