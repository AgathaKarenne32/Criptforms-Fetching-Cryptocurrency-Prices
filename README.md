# Criptforms: Fetching Cryptocurrency Prices

## Descrição do Projeto

Este projeto tem como objetivo buscar e exibir os preços das criptomoedas a partir de uma API pública. Através de um script Python, é possível recuperar os dados em tempo real e processá-los para exibir o preço das criptomoedas em dólares (USD).

A execução do script busca os preços de diversas criptomoedas e exibe as informações no formato JSON.

## Funcionalidades

- **Busca de preços em tempo real:** O script consulta a API e retorna os preços das criptomoedas.
- **Exibição de dados:** Os preços das criptomoedas são exibidos no formato JSON, facilitando a análise e o processamento dos dados.
- **Suporte para múltiplas criptomoedas:** A API retorna dados para uma lista extensa de criptomoedas, incluindo nomes e preços em USD.

## Estrutura do Projeto

A estrutura de arquivos do projeto é a seguinte:

```
/Criptforms
    ├── fetch_ids.py         # Script responsável por buscar os identificadores das criptomoedas
    ├── fetch_data.py        # Script responsável por buscar os preços das criptomoedas
    ├── main.py              # Arquivo principal que executa o fluxo de busca e exibição de dados
    └── requirements.txt     # Arquivo de dependências do projeto
```

### Arquivos principais

- **`fetch_ids.py`**: Este script é responsável por buscar os identificadores das criptomoedas através de uma consulta à API. Os dados de identificadores são usados como base para buscar os preços.
  
- **`fetch_data.py`**: Este script faz a consulta para obter os preços das criptomoedas em USD. Ele recebe os identificadores das criptomoedas e retorna os preços.

- **`main.py`**: Arquivo principal que executa o fluxo completo. Ele importa funções dos scripts `fetch_ids.py` e `fetch_data.py`, e exibe os dados de preços das criptomoedas no formato desejado.

- **`requirements.txt`**: Contém as dependências necessárias para rodar o projeto, como bibliotecas para realizar requisições HTTP (ex: `requests`).

## Requisitos

- **Python 3.x**: O projeto foi desenvolvido utilizando Python 3.7 ou superior.
- **Bibliotecas**: O projeto utiliza a biblioteca `requests` para realizar requisições HTTP à API. Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

## Como Executar

1. **Instalar dependências**

   Se ainda não tiver as dependências instaladas, execute o seguinte comando:

   ```bash
   pip install -r requirements.txt
   ```

2. **Executar o script principal**

   Para buscar e exibir os preços das criptomoedas, execute o seguinte comando no terminal:

   ```bash
   python main.py
   ```

   O script irá buscar os preços das criptomoedas em USD e exibi-los no terminal.

3. **Verificar resultados**

   Os dados serão exibidos no formato JSON, contendo o nome da criptomoeda e seu respectivo preço em USD, se disponível. Caso não haja preço para uma criptomoeda, o campo estará vazio.

## Exemplo de Saída

Aqui está um exemplo da saída que será exibida após a execução do script:

```json
{
  "01coin": {"usd": 0.00019859},
  "0chain": {"usd": 0.03107839},
  "0dog": {"usd": 0.0070529},
  "0-knowledge-network": {"usd": 0.00029556},
  "0-mee": {"usd": 4.96e-05},
  "0vix-protocol": {},
  "0x": {"usd": 0.294415},
  "0x0-ai-ai-smart-contract": {"usd": 0.098794},
  "0x678-landwolf-1933": {"usd": 2.1481e-07},
  ...
}
```

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
