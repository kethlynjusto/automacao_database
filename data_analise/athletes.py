# athletes.py
import pandas as pd
from pathlib import Path
from ..import_excel import athletes_csv

def athletes(athletes_csv: Path = athletes_csv) -> pd.DataFrame:
    df = pd.read_csv(athletes_csv)

    # --- aqui vão seus tratamentos e colunas adicionais ---
    df.head()
    print(df.head())
    #df.columns = df.columns.str.strip().str.lower()
    #df['imc'] = df['peso_kg'] / ( (df['altura_cm']/100) ** 2 )
    # -------------------------------------------------------

    return df
