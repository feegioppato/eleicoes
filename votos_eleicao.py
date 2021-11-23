# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 13:12:23 2021

@author: ferna
"""

# Carregando bibliotecas

import pandas as pd
import numpy as np
import basedosdados as bd

# Definindo a query

query = """

WITH resultados as (
SELECT 
    turno,
    id_municipio,
    sigla_partido,
    numero_candidato,
    votos
FROM 
    `basedosdados.br_tse_eleicoes.resultados_candidato_municipio`
WHERE ano = 2018
    AND cargo = 'presidente'
)
SELECT 
    t2.sigla_uf,
    t2.id_municipio,
    t2.nome,
    t1.numero_candidato,
    t1.sigla_partido,
    t1.votos,
    t1.turno
FROM
    resultados t1
JOIN 
    `basedosdados.br_bd_diretorios_brasil.municipio` t2
ON 
    t1.id_municipio = t2.id_municipio     
ORDER BY 
    t2.id_municipio
    
"""

# Baixando conjunto de dados

df = bd.read_sql(query, billing_project_id = 'projeto1-311803')

# Salvando dados em formato .csv

df.to_csv('eleicoes_br.csv', index = False)










