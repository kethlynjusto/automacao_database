import os
import pandas as pd
from pathlib import Path

from data_analise.athletes import athletes
from data_analise.teams    import teams
from data_analise.medals_total import medals_total

def main():
    output_path = Path("C:/Users/kethl/Documents/Programacao/Excel/novo_teste.xlsx")
    
    # Garante que o diretório existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Lista de (nome da aba, função que retorna df)
    sheets = [
        ("Atletas", athletes),
        ("Teams",   teams),
        ("Medals_total", medals_total),
        # … outras funções …
    ]

    # Usa o contexto 'with' para garantir salvamento correto
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for sheet_name, func in sheets:
            try:
                df = func()
            except Exception as e:
                df = pd.DataFrame({ "Erro": [ str(e) ] })
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print("Planilha final salva em:", output_path)

if __name__ == "__main__":
    main()
