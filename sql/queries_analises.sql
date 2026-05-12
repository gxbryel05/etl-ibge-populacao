-- Total de municípios
SELECT COUNT(*) FROM municipios;

-- Municípios por estado
SELECT uf, COUNT(*) as total
FROM municipios
GROUP BY uf
ORDER BY total DESC;

-- Municípios por região
SELECT regiao, COUNT(*) as total
FROM municipios
GROUP BY regiao
ORDER BY total DESC;

-- Busca Salvador
SELECT * FROM municipios
WHERE nome ILIKE '%salvador%';