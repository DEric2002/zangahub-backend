
from pathlib import Path
import json

def ler_pecas():
    # LER AS PECAS DO ARQUIVO JSON, PARA DEPOIS INSERIR NO BANCO
    caminho_json = Path(__file__).parent.parent / "pecas.json"
    
    with open(caminho_json, "r", encoding="UTF-8") as arquivo:
        pecas_json = json.load(arquivo)

    return pecas_json
