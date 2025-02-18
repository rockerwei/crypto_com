from ui.utils.helpers import *


def loading_to_the_9_day_forecast_page(driver):
    wait_for_element(driver, AppiumBy.XPATH, tab_local_forecast)


def assert_first_day_all_info(driver, expected_date, expected_day, expected_temp, expected_rh, expected_psr_text, expected_wind,
                              expected_details):
    first_date = driver.find_element(AppiumBy.XPATH, first_day_date)
    first_week = driver.find_element(AppiumBy.XPATH, first_day_week)
    first_temp = driver.find_element(AppiumBy.XPATH, first_day_temp)
    first_rh = driver.find_element(AppiumBy.XPATH, first_day_rh)
    first_psr_text = driver.find_element(AppiumBy.XPATH, first_day_psr_text)
    first_wind = driver.find_element(AppiumBy.XPATH, first_day_wind)
    first_details = driver.find_element(AppiumBy.XPATH, first_day_details)

    # get content
    actual_date = first_date.text
    actual_day = first_week.text
    actual_temp = first_temp.text
    actual_rh = first_rh.text
    actual_psr_text = first_psr_text.text
    actual_wind = first_wind.text
    actual_details = first_details.text

    # assert text
    assert actual_date == expected_date, f"Date does not match, expected result: {expected_date},  actual outcome {actual_date}"
    assert actual_day == expected_day, f"Day does not match, expected result: {expected_day},  actual outcome {actual_day}"
    assert actual_temp == expected_temp, f"Day does not match, expected result: {expected_temp},  actual outcome {actual_temp}"
    assert actual_rh == expected_rh, f"Day does not match, expected result: {expected_rh},  actual outcome {actual_rh}"
    assert actual_psr_text == expected_psr_text, f"Day does not match, expected result: {expected_psr_text},  actual outcome {actual_psr_text}"
    assert actual_wind == expected_wind, f"Day does not match, expected result: {expected_wind},  actual outcome {actual_wind}"
    assert actual_details == expected_details, f"Day does not match, expected result: {expected_details},  actual outcome {actual_details}"

    # assert element exist
    assert bool(determine_element_exists(driver, AppiumBy.XPATH, first_day_icon)), f"Element {first_day_icon} not found!"
    assert bool(determine_element_exists(driver, AppiumBy.XPATH, first_day_psr_icon)), f"Element {first_day_psr_icon} not found!"


# XPATH
tab_local_forecast = '//android.widget.TextView[@text="Local Forecast"]'
first_day_date = "//*[@resource-id='hko.MyObservatory_v1_0:id/sevenday_forecast_date' and @bounds='[22,892][323,942]']"
first_day_week = "//*[@resource-id='hko.MyObservatory_v1_0:id/sevenday_forecast_day_of_week' and @bounds='[22,960][323," \
                 "1010]'] "
first_day_icon = "//*[@resource-id='hko.MyObservatory_v1_0:id/sevenday_forecast_Icon' and @bounds='[114,1028][231," \
                 "1145]'] "
first_day_temp = "//*[@resource-id='hko.MyObservatory_v1_0:id/sevenday_forecast_temp' and @bounds='[354,892][706,942]']"
first_day_rh = "//*[@resource-id='hko.MyObservatory_v1_0:id/sevenday_forecast_rh' and @bounds='[706,892][1058,942]']"
first_day_psr_icon = "//*[@resource-id='hko.MyObservatory_v1_0:id/psrIcon' and @bounds='[354,964][423,1033]']"
first_day_psr_text = "//*[@resource-id='hko.MyObservatory_v1_0:id/psrText' and @bounds='[440,973][1058,1023]']"
first_day_wind = "//*[@resource-id='hko.MyObservatory_v1_0:id/sevenday_forecast_wind' and @bounds='[354,1055][1058," \
                 "1155]'] "
first_day_details = "//*[@resource-id='hko.MyObservatory_v1_0:id/sevenday_forecast_details' and @bounds='[354,1177][1058,1377]']"
