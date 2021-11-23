# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

import pandas as pd


def proporcao_cidade(cidade, partido, turno):
    
    """ 
    Calcula a porcentagem de votos do cadidato passado como argumento em determinada cidade do país.
    
    Parametros
    ----------
    cidade: str
        Nome da cidade para calculo da proporção
    partido: str
        Sigla do partido do candidato
    turno: int
        turno da votação
        
    Retorna
    -------
    Porcentagem de votos que o candidato no turno informado.
        
    """
    
    # Definindo filtros
    
    local = df['nome'] == cidade 
    sigla = df['sigla_partido'] == partido
    etapa = df['turno'] == turno
    
    # Calculando a proporção de votos do candidato
    
    total = df.loc[local & etapa, 'votos'].sum()
    partido = df.loc[local & etapa & sigla, 'votos'].sum()
    round((int(partido)/total)*100, 2)
    
    return round((int(partido)/total)*100, 2)
    
    
    
def proporcao_estado(estado, partido, turno):
    
    """ 
    Calcula a porcentagem de votos do partido passado como argumento em um estado do país.

    Parametros
    ----------
    cidade: str
        Sigla do estado para calculo da proporção
    partido: str
        Sigla do partido
    turno: int
        turno da votação
        
    Retorna
    -------
    Porcentagem de votos que o candidato no turno informado.
    
"""
    
    # Criando filtros
    
    e = df['sigla_uf'] == estado
    p = df['sigla_partido'] == partido 
    t = df['turno'] == turno
    
    # Calculando proporção
    
    total = df.loc[e & t, 'votos'].sum()
    partido = int(df.loc[e & p & t, 'votos'].sum())
    
    return round((partido / total) * 100, 2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    