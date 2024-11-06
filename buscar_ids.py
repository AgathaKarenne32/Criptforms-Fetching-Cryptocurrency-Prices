import requests

def obter_todos_ids_cripto():
    # URL para obter a lista de todas as criptomoedas
    url = "https://api.coingecko.com/api/v3/coins/list"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        return [moeda['id'] for moeda in resposta.json()]
    else:
        print("Erro ao obter a lista de criptomoedas:", resposta.status_code)
        return []
