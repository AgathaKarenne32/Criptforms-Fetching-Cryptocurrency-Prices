import requests

def obter_precos_cripto(ids_cripto):
    # Obtendo preços para todas as criptomoedas especificadas
    url = "https://api.coingecko.com/api/v3/simple/price"
    parametros = {
        "vs_currencies": "usd",
        "ids": ",".join(ids_cripto)  # Unindo os IDs em uma string separada por vírgulas
    }
    
    resposta = requests.get(url, params=parametros)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        print("Erro ao obter preços de criptomoedas:", resposta.status_code)
        return None

