from lucas.checks import is_reachable

config = {
    "portal": "http://www.transparencia.feiradesantana.ba.gov.br/",
    "despesas": "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=despesa",
    "receitas": "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=receita",
    "licitacoes": "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=licitacoes",
    "contratos": "http://www.transparencia.feiradesantana.ba.gov.br/index.php?view=contratos",
}


def main():
    print("Acessível?")
    for key, url in config.items():
        print(f"{key} - {url}")
        result = is_reachable(url)
        for criteria, criteria_result in result.items():
            print(f"- {criteria} {'✅' if criteria_result else '❌'}")


if __name__ == "__main__":
    main()
