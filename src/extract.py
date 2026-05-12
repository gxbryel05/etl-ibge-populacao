import requests

def extrair_municipios():
    print("Conectando à API do IBGE...")
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/municipios"
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    print(f"✅ {len(dados)} municípios extraídos com sucesso!")
    return dados