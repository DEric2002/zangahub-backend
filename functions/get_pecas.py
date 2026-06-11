import re
import math

def coletar_peca():  
    pecas = { "pecas" : []}

    with open("KMB_PECAS.txt", "r", encoding="UTF-8") as arquivo:
        for linha in arquivo:
            #coletando o código da peça
            cod_peca = linha[:20] 
            cod_peca = cod_peca.replace(" ", "")
            
            #coletando o nome da peça
            nome_peca = linha[20:90]
            nome_peca = re.sub(" +"," ",nome_peca)

            #coletando o valor da peça
            cod_valor = linha[91:105]
            valor_peca = int(cod_valor) / 100

            #formatando o valor da peca
            valor_sek = f"R$ {valor_peca:,.2f}".replace(",","-").replace(".",",").replace("-",".")

            valor_venda = valor_peca * 1.15
            valor_venda_fmt = math.ceil(valor_venda)

            valor_final = f"R$ {float(valor_venda_fmt):,.2f}".replace(",","-").replace(".",",").replace("-",".")      

            pecas["pecas"].append(
                {
                    "codigo" : cod_peca,
                    "descricao" : nome_peca,
                    "valor_sek" : valor_sek,
                    "valor_venda" : valor_final
                }
            )

    return pecas


