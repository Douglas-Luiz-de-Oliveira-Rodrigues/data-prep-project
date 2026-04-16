import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicados
    df = df.drop_duplicates()
    # Preenche valores nulos
    df = df.fillna(0)
    print("Dados limpos com sucesso!")
    return df
