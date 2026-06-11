
import json
import sqlite3
from functions.write_pecas import ler_pecas

pecas_json = ler_pecas()

# CONECTANDO AO SQLITE
conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tb_pecas (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               codigo_peca TEXT NOT NULL UNIQUE,
               descricao TEXT NOT NULL,
               valor_sek FLOAT NOT NULL,
               valor_venda FLOAT NOT NULL
               )""")

# PREPARANDO O JSON PARA UM FORMATO QUE O SQLITE ACEITE.
# EXTRAI APENAS O VALOR DE CADA DICIONARIO DA LISTA, EX: LISTA "PECAS" TEM VARIOS DICIONÁRIOS DE CADA PEÇA
# OU SEJA, PRECISAMOS SOMENTE DO VALOR DE CADA CHAVE, SEM COLETAR A CHAVE PROPRIAMENTE 
dados_para_inserir = [
    (p["codigo"], p["descricao"], p["valor_sek"], p["valor_venda"])
    for p in pecas_json["pecas"]
]

# INSERIR OS DADOS TODOS DE UM VEZ
comando_sql = ("""INSERT OR REPLACE INTO tb_pecas (codigo_peca, descricao, valor_sek, valor_venda)
                VALUES (?, ?, ?, ?)
                """)

try:
    conexao.execute("BEGIN")

    cursor.execute("DELETE FROM tb_pecas")
    cursor.executemany(comando_sql, dados_para_inserir)

    conexao.commit()
except:
    conexao.rollback()
    raise

print(f"Sucesso! {len(dados_para_inserir)} peças do arquivo 'pecas.json', foram salvas no banco!")

