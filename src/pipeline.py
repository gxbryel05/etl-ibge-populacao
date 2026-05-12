import sys
import os
sys.path.append(os.path.dirname(__file__))

from extract import extrair_municipios
from transform import transformar
from load import carregar

def executar():
    print("Iniciando pipeline ETL...")
    dados_brutos = extrair_municipios()
    df = transformar(dados_brutos)
    carregar(df)
    print("Pipeline concluído com sucesso!")

if __name__ == "__main__":
    executar()