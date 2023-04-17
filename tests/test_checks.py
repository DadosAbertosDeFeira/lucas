from unittest.mock import Mock
from lucas.checks import is_reachable
import pytest


@pytest.mark.parametrize("status_code,expected_result", [
    (200, True),
    (204 , True),
    (500, False),
    (404, False),
])
def test_is_reachable(status_code, expected_result, requests_mock):
    fake_url = "https://www.fake.com.br"
    requests_mock.get(fake_url, status_code=status_code)
    
    assert is_reachable(fake_url) is expected_result
