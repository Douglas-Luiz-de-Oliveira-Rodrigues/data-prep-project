# Data Prep Project 📊🐍

Este projeto é uma ferramenta modular em Python desenvolvida para automatizar as etapas iniciais de preparação de dados (Data Preparation). Ele permite carregar arquivos CSV, realizar limpezas automáticas e gerar análises estatísticas rápidas.

## 🚀 Funcionalidades

- **Carga de Dados**: Leitura eficiente de arquivos CSV utilizando a biblioteca Pandas.
- **Limpeza Automatizada**: 
  - Remoção automática de registros duplicados.
  - Tratamento de valores nulos (preenchimento com 0).
- **Análise Estatística**: 
  - Resumo descritivo (média, desvio padrão, min/max, etc.).
  - Verificação de tipos de dados das colunas.

## 📁 Estrutura do Projeto

```text
data-prep-project/
├── data/                   # Pasta contendo os arquivos de dados (CSV)
├── src/                    # Códigos fonte do projeto
│   ├── main.py             # Ponto de entrada da aplicação
│   ├── data_loader.py      # Módulo de carregamento
│   ├── data_cleaner.py     # Módulo de limpeza
│   └── data_analysis.py    # Módulo de análise
├── requirements.txt        # Lista de dependências do Python
└── README.md               # Documentação do projeto
```

## 🛠️ Pré-requisitos

- Python 3.x
- Pandas

## 🔧 Instalação

1. Clone o repositório ou baixe os arquivos.
2. No diretório raiz do projeto, instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Como Usar

Para executar o pipeline completo de processamento:

```bash
python src/main.py
```

O script irá carregar o arquivo localizado em `data/sample.csv`, aplicar as regras de limpeza e exibir o resultado diretamente no terminal.

## 📝 Licença

Este projeto é para fins de estudo e prática de engenharia de dados. Sinta-se à vontade para expandir e modificar!