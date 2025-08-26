import pandas as pd
from pathlib import Path

from data_analise.athletes import athletes
from data_analise.teams    import teams

def main():
    output_path = Path("C:/…/novo.xlsx")
    writer = pd.ExcelWriter(output_path, engine="openpyxl")

    # Lista de (nome da aba, função que retorna df)
    sheets = [
        ("Atletas", athletes),
        ("Teams",   teams),
        # … outras funções …
    ]

    for sheet_name, func in sheets:
        try:
            df = func()
        except Exception as e:
            # Se falhar, cria um DataFrame com a mensagem de erro
            df = pd.DataFrame({ "Erro": [ str(e) ] })
        finally:
            # Mesmo que dê erro, executa to_excel e segue
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Salva sempre, sem aguardar o with (para não descartar em caso de erro)
    writer.save()
    print("Planilha final salva em:", output_path)

if __name__ == "__main__":
    main()
