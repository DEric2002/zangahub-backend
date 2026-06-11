
import json
from get_pecas import coletar_peca

# CHAMANDO A FUNÇAO RESPONSÁVEL PELA COLETA DAS PEÇAS NO BRUTO DO ARQUIVO TXT
lista_pecas = coletar_peca()

# GRAVAR TUDO EM UM ARQUIVO JSON PARA FACIL MANIPULAÇÃO
with open("pecas.json", "w", encoding="UTF-8") as arquivo:
    json.dump(lista_pecas, arquivo, indent=4, ensure_ascii=False)
    print(f"O arquivo JSON está pronto para uso!")