# medals_total.py
import pandas as pd
from pathlib import Path
from importExcel.path_excel import medals_total_csv

def medals_total(medals_total_csv: Path = medals_total_csv) -> pd.DataFrame:
    df = pd.read_csv( medals_total_csv )

    # --- aqui vão seus tratamentos e colunas adicionais ---
    df.head()
    print(df.head())
    #df.columns = df.columns.str.strip().str.lower()
    #df['imc'] = df['peso_kg'] / ( (df['altura_cm']/100) ** 2 )
    # -------------------------------------------------------

    return df