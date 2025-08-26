import os
import pandas as pd
from pathlib import Path

from data_analise.athletes import athletes
from data_analise.teams    import teams
from data_analise.medals_total import medals_total

# def main():
#     output_path = Path("C:/Users/kethl/Documents/Programacao/Excel/novo_teste.xlsx")
    
#     # Garante que o diretório existe
#     os.makedirs(os.path.dirname(output_path), exist_ok=True)

#     # Lista de (nome da aba, função que retorna df)
#     ALL_SHEETS = [
#         ("Atletas", athletes),
#         ("Teams",   teams),
#         ("Medals_total", medals_total),
#         # … outras funções …
#     ]

#     for idx, (name, _) in enumerate(ALL_SHEETS, start=1):
#         print(f"{idx}. {name}")

#     choices = input("Digite os números das abas separados por vírgula (ou ENTER para todas): ")
#     if choices.strip():
#         indices = [int(i)-1 for i in choices.split(",")]
#         selected = {ALL_SHEETS[i][0] for i in indices}
#     else:
#         selected = {name for name, _ in ALL_SHEETS}

#     # Usa o contexto 'with' para garantir salvamento correto
#     with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
#         for name, func in ALL_SHEETS:
#             if name not in selected:
#                 continue
#             try:
#                 df = func()
#             except Exception as e:
#                 df = pd.DataFrame({"Erro": [str(e)]})
#             df.to_excel(writer, sheet_name=name, index=False)

#     print("Planilha final salva em:", output_path)

# if __name__ == "__main__":
#     main()


######################################################################################################################

def main():
    output_path = Path("C:/Users/kethl/Documents/Programacao/Excel/novo_teste.xlsx")
    
    # Garante que o diretório existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Lista de (nome da aba, função que retorna df)
    ALL_SHEETS = [
        ("Atletas", athletes),
        ("Teams",   teams),
        ("Medals_total", medals_total),
        # … outras funções …
    ]

    # mapeamento de grupos → listas de nomes de abas
    SHEET_GROUPS = {
        "grupo_principal": ["Atletas", "Teams"],
        "estatisticas":    ["Medals_total"],
        "tudo":            [name for name, _ in ALL_SHEETS],
    }

    group_names = list(SHEET_GROUPS.keys())
    for idx, group in enumerate(group_names, start=1):
        print(f"{idx}. {group}")

    choices = input("Digite os números dos grupos separados por vírgula (ou ENTER para todos): ")
    if choices.strip():
        indices = [int(i)-1 for i in choices.split(",")]
        selected = set()
        for i in indices:
            selected.update(SHEET_GROUPS[group_names[i]])
    else:
        selected = set(name for name, _ in ALL_SHEETS)

    # Usa o contexto 'with' para garantir salvamento correto
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        for name, func in ALL_SHEETS:
            if name not in selected:
                continue
            try:
                df = func()
            except Exception as e:
                df = pd.DataFrame({"Erro": [str(e)]})
            df.to_excel(writer, sheet_name=name, index=False)

    print("Planilha final salva em:", output_path)

if __name__ == "__main__":
    main()