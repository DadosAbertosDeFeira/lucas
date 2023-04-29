import re

import pytest
from playwright.sync_api import expect

pages = {
    "portal": "http://www.transparencia.feiradesantana.ba.gov.br/",
    "despesas": "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=despesa",
    "receitas": "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=receita",
    "licitacoes": "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=licitacoes",
    "contratos": "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=contratos",
}


@pytest.mark.rules
@pytest.mark.parametrize("url", pages.values(), ids=pages.keys())
def test_page_is_accessible_by_humans(page, url):
    response = page.request.get(url)
    expect(response).to_be_ok()

    page.goto(url)
    page.wait_for_load_state()

    expect(page).to_have_title(re.compile("Portal da Transparência"))


@pytest.mark.rules
@pytest.mark.parametrize("url", pages.values(), ids=pages.keys())
def test_page_is_accessible_by_robots(page, url):
    page.goto(url)
    page.wait_for_load_state()

    outer_iframe = page.frame_locator("iframe")
    recaptcha_iframe = outer_iframe.locator('iframe[title^="reCAPTCHA"]')
    textarea = outer_iframe.locator("textarea=g-recaptcha-response")

    expect(recaptcha_iframe, "should not have recaptcha").not_to_be_visible()
    expect(textarea, "should not have g-recaptcha-response").to_have_count(0)
