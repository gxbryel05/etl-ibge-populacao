CREATE TABLE IF NOT EXISTS municipios (
    id          SERIAL PRIMARY KEY,
    codigo_ibge VARCHAR(10) UNIQUE NOT NULL,
    nome        VARCHAR(100) NOT NULL,
    uf          VARCHAR(2) NOT NULL,
    regiao      VARCHAR(20),
    extraido_em TIMESTAMP DEFAULT NOW()
);