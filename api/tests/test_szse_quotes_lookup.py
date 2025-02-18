import requests
import pytest

# API endpoint
API_URL = "https://www.szse.cn/api/market/ssjjhq/getTimeData?marketId=1&code=000001"


@pytest.fixture
def fetch_market_data():
    response = requests.get(API_URL)
    assert response.status_code == 200, f"API request failed with status {response.status_code}"
    return response.json()['data']


# Verify API status code
def test_api_response_status():
    response = requests.get(API_URL)
    assert response.status_code == 200, "API request failed"


# Verify response include high and low data
def test_market_data_include_high_and_low_data(fetch_market_data):
    data = fetch_market_data
    assert 'high' in data, "Missing 'high' in API response"
    assert 'low' in data, "Missing 'low' in API response"


# Verify data high greater than data low
def test_high_greater_than_low(fetch_market_data):
    data = fetch_market_data
    high = float(data["high"])
    low = float(data["low"])
    assert high > low, f"High ({high}) is not greater than Low ({low})"

