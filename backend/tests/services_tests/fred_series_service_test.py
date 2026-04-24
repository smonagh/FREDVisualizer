import pytest
import datetime
import math

from app.services.fred_series_service import (
    get_numeric_value, 
    get_date_value,
    process_observations
)

def test_get_numeric_value_float():
    
    input_float = "3.14"
    expected_value = 3.14
    generated_value = get_numeric_value(input_float)

    assert math.isclose(generated_value, expected_value)

def test_get_numeric_value_int():

    input_float = "4"
    expected_value = 4
    generated_value = get_numeric_value(input_float)

    assert math.isclose(generated_value, expected_value)

def test_get_numeric_value_alpha():

    input_float = "Not a float"
    generated_value = get_numeric_value(input_float)
    
    assert generated_value is None

def test_get_date_value_correct():

    input_date = "2024-10-12"
    expected_value = datetime.datetime.strptime(input_date, "%Y-%m-%d").date()
    generated_value = get_date_value(input_date)

    assert generated_value == expected_value

def test_get_date_value_incorrect():

    input_date = "12/12/2023"
    generated_value = get_date_value(input_date)

    assert generated_value is None

@pytest.fixture
def mock_helpers(monkeypatch):
    def fake_get_date_value(date):
        return date  # simple passthrough for testing

    def fake_get_numeric_value(value):
        return float(value)

    monkeypatch.setattr("tests.services_tests.fred_series_service_test.get_date_value", fake_get_date_value)
    monkeypatch.setattr("tests.services_tests.fred_series_service_test.get_numeric_value", fake_get_numeric_value)


def test_process_observations_filters_invalid(mock_helpers):
    observations = [
        {"date": "2020-01-01", "value": "10"},
        {"date": None, "value": "20"},          # invalid
        {"date": "2020-01-02", "value": None},  # invalid
    ]

    result = process_observations(observations)

    assert result == [
        {"date": datetime.date(2020, 1, 1), "value": 10.0},
    ]


def test_process_observations_sorts_by_date(mock_helpers):
    observations = [
        {"date": "2020-01-03", "value": "30"},
        {"date": "2020-01-01", "value": "10"},
        {"date": "2020-01-02", "value": "20"},
    ]

    result = process_observations(observations)

    assert result == [
        {"date": datetime.date(2020, 1, 1), "value": 10.0},
        {"date": datetime.date(2020, 1, 2), "value": 20.0},
        {"date": datetime.date(2020, 1, 3), "value": 30.0},
    ]


def test_process_observations_skips_unparsable():

    observations = [
        {"date": "bad", "value": "bad"},
    ]

    result = process_observations(observations)

    assert result == []


def test_process_observations_mixed_cases(mock_helpers):
    observations = [
        {"date": "2020-01-02", "value": "20"},
        {"date": "", "value": "10"},            # missing date
        {"date": "2020-01-01", "value": ""},    # missing value
    ]

    result = process_observations(observations)

    assert result == [
        {"date": datetime.date(2020, 1, 2), "value": 20.0},
    ]