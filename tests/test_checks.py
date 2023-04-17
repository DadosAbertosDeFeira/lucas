from pathlib import Path

import pytest

from lucas.checks import has_robot_blocker, is_reachable


@pytest.mark.parametrize(
    "status_code,expected_result",
    [
        (200, True),
        (204, True),
        (500, False),
        (404, False),
    ],
)
def test_is_reachable(status_code, expected_result, requests_mock):
    fake_url = "https://www.fake.com.br"
    requests_mock.get(fake_url, status_code=status_code)

    assert is_reachable(fake_url)["reachable"] is expected_result


def test_has_robot_blocker():
    body = Path("tests/fixtures/contratos.html").read_text()
    assert has_robot_blocker(body) is True
