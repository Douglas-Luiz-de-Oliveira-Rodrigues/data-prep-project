import pandas as pd

def analyze_data(df: pd.DataFrame):
    print("Resumo estatístico:")
    print(df.describe())
    print("\nColunas e tipos:")
    print(df.dtypes)
