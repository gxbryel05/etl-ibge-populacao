import pandas as pd

def transformar(dados_brutos):
    print("Transformando dados...")
    df = pd.json_normalize(dados_brutos)

    df = df[[
        'id',
        'nome',
        'microrregiao.mesorregiao.UF.sigla',
        'microrregiao.mesorregiao.UF.regiao.nome'
    ]].copy()

    df.columns = ['codigo_ibge', 'nome', 'uf', 'regiao']

    df['codigo_ibge'] = df['codigo_ibge'].astype(str)
    df['nome']        = df['nome'].str.strip().str.title()
    df['uf']          = df['uf'].str.upper()
    df['regiao']      = df['regiao'].str.strip()

    df = df.drop_duplicates(subset='codigo_ibge')
    df = df.dropna(subset=['nome', 'uf'])

    print(f"✅ {len(df)} municípios transformados!")
    return df