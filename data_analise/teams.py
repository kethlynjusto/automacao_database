# teams.py
import pandas as pd
from pathlib import Path
from importExcel.path_excel import teams_csv

def teams(teams_csv: Path = teams_csv) -> pd.DataFrame:
    df = pd.read_csv( teams_csv )

    # --- aqui vão seus tratamentos e colunas adicionais ---
    df.head()
    print(df.head())
    #df.columns = df.columns.str.strip().str.lower()
    #df['imc'] = df['peso_kg'] / ( (df['altura_cm']/100) ** 2 )
    # -------------------------------------------------------

    return df