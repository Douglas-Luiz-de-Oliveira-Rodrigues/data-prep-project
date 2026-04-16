import pandas as pd
import os

def load_csv(filepath: str) -> pd.DataFrame:
    if not os.path.exists(filepath):
        print(f"Erro: O arquivo {filepath} não foi encontrado.")
        return None
    
    try:
        df = pd.read_csv(filepath)
        print(f"Arquivo {filepath} carregado com sucesso!")
        return df
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None
