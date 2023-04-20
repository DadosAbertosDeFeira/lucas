import pytest
from playwright.sync_api import expect


@pytest.mark.rules
def test_page_show_contracts(page):
    page.goto(
        "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=contratos"
    )
    page.wait_for_load_state()

    expect(page.get_by_text("Nº CONTRATO")).to_be_visible()
    expect(page.get_by_text("SECRETARIA")).to_be_visible()
    expect(page.get_by_text("FORNECEDOR")).to_be_visible()
    expect(page.get_by_text("DATA ASSINATURA")).to_be_visible()
    expect(page.get_by_text("INÍCIO EXECUÇÃO")).to_be_visible()
    expect(page.get_by_text("FIM EXECUÇÃO")).to_be_visible()
    expect(page.get_by_text("VALOR")).to_be_visible()


@pytest.mark.rules
def test_page_show_revenue(page):
    page.goto(
        "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=receita"
    )
    page.wait_for_load_state()
    page.get_by_role("button", name="Pesquisar").click()

    published_date_text = page.locator(
        '//*[@id="editable-sample"]/tbody/tr[1]/td[1]'
    ).text_content()
    # TODO check if it is a valid date

    expect(page.get_by_text("Data de Publicação")).to_be_visible()
    expect(page.get_by_text("Valor")).to_be_visible()


@pytest.mark.rules
@pytest.mark.parametrize(
    "url",
    ["http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=contratos"],
)
def test_page_is_accessible_by_robots(page, url):
    page.goto(url)
    page.wait_for_load_state()

    outter_iframe = page.frame_locator("iframe")
    recaptcha_iframe = outter_iframe.locator('iframe[title^="reCAPTCHA"]')
    textarea = outter_iframe.locator("textarea")

    expect(recaptcha_iframe, "should not have recaptcha").not_to_be_visible()
    expect(textarea, "should not have g-recaptcha-response").not_to_have_id(
        "g-recaptcha-response"
    )
