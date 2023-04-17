import requests


def is_reachable(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except:
        return False
    return True


if __name__ == "__main__":
    url = "http://www.transparencia.feiradesantana.ba.gov.br/"
    print(f"Acessível? {'✅' if is_reachable(url) else '❌'}")
