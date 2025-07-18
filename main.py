# main.py
import pandas as pd
from pathlib import Path

from data_analise.athletes import athletes
from data_analise.teams import teams
# from data_analise.outra_função import ...

def main():
    output_path = Path("C:/Users/kethl/Documents/Programacao/Excel/novo.xlsx")
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        # 1ª aba: atletas
        df_athletes = athletes()
        df_athletes.to_excel(writer, sheet_name="Atletas", index=False)

        # 2ª aba: treinadores
        df_teams = teams()
        df_teams.to_excel(writer, sheet_name="Teams", index=False)
        

        # … repita para cada função que retornar um df …

    print("Planilha final salva em:", output_path)

if __name__ == "__main__":
    main()