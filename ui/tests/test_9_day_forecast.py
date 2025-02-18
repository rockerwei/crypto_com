import pytest
from ui.page.homePage import *
from ui.page.forecast_warning_services.the_9_day_forecast import *


@pytest.mark.parametrize('expected_date, expected_day, expected_temp, expected_rh, expected_psr_text, expected_wind, expected_details',
                         [
                             ('23 Feb', '(Sun)', '15 - 18°C', '60 - 90%', 'Low',
                              'East force 4 to 5, becoming north to northeast force 4 to 5.',
                              'Mainly cloudy. One or two rain patches at first. Bright periods in the afternoon. Cool in the morning and at night.'
                              )
                        ])
def test_the_first_forecast_all_info(driver, expected_date, expected_day, expected_temp, expected_rh, expected_psr_text, expected_wind, expected_details):
    app_just_opened_and_entered_the_homepage(driver)
    expand_the_menu(driver)
    expand_the_forecast_warning_services_option(driver)
    go_to_the_9_day_forecast_page(driver)
    loading_to_the_9_day_forecast_page(driver)
    assert_first_day_all_info(driver, expected_date, expected_day, expected_temp, expected_rh, expected_psr_text, expected_wind, expected_details)

