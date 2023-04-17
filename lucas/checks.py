import requests


def _has_recaptcha(html):  # TODO add typing
    """Check if recaptcha is on.

    Docs: https://developers.google.com/recaptcha/docs/v3
    """
    possibilities = [
        html.find("iframe[title^='reCAPTCHA']"),
        html.find("input#recaptcha-token"),
        html.find("div.g-recaptcha"),
        html.find("textarea#g-recaptcha-response"),
        html.find("textarea.g-recaptcha-response"),
        html.find("script[src*='www.google.com/recaptcha']"),
    ]
    return any(possibilities)


def has_robot_blocker(body):
    """Verify if robot blockers, like recaptcha, are configured."""
    return _has_recaptcha(body)


def is_reachable(url):
    result = {
        "reachable": True,
        "robot_friendly": True,
    }
    response = requests.get(url, timeout=(3.05, 27))
    try:
        response.raise_for_status()
    except requests.RequestException:
        result["reachable"] = False
    else:
        if has_robot_blocker(response.text):
            result["robot_friendly"] = False
    return result


url = "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=contratos"


def request_html_from(url):
    from requests_html import HTMLSession

    session = HTMLSession()
    response = session.get(url)
    # response.html.render() # TimeoutError: Navigation Timeout Exceeded: 8000 ms exceeded.
    # response.html.render(wait=10, sleep=15) # TimeoutError: Navigation Timeout Exceeded: 8000 ms exceeded.
    # response.html.render(30) # TimeoutError: Navigation Timeout Exceeded: 8000 ms exceeded.
    response.html.render(timeout=30)
