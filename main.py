from buscar_ids import obter_todos_ids_cripto
from buscar_precos import obter_precos_cripto

if __name__ == "__main__":
    # Passo 1: Obter IDs de todas as criptomoedas
    ids_cripto = obter_todos_ids_cripto()
    
    # Passo 2: Obter preços para as criptomoedas obtidas
    if ids_cripto:
        # Limitar a quantidade de IDs para evitar erros de limite na API
        ids_cripto_limitados = ids_cripto[:100]  # Pega os primeiros 100 como exemplo
        precos_cripto = obter_precos_cripto(ids_cripto_limitados)
        
        if precos_cripto:
            print("Dados de preços de criptomoedas:", precos_cripto)

