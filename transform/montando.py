from extract.coleta import arquivos_coletados

import pandas as pd
import os
import typing


def agrupando() -> pd.DataFrame:
    """
    Agruapa os dados em um dataframe.

    :param saida: dataframe
    """
    arquivos_origem = arquivos_coletados()[:-1]
    df_armazenados = []
    for i, arquivo in enumerate(arquivos_origem):
        if i == 0:
            df_read = pd.read_excel(arquivo)
            df_armazenados.append(df_read)
        else:
            if os.path.exists(arquivo):
                df_origem = (pd.read_excel(arquivo)).drop(df_read.columns[0], axis=1)
                df_armazenados.append(df_origem)
    df_agrupado = pd.concat(df_armazenados, axis=1)
    return df_agrupado


def renomeando_colunas() -> typing.List[str]:
    """
    Renomea nomes de coluna.

    :param saida: Lista
    """
    renomear = agrupando().columns
    cont_restante = renomear[1:]
    cont_primeiro = [renomear[0]]
    renomear = [col + str(i + 1) for i, col in enumerate(cont_restante)]
    colunas_renomeadas = cont_primeiro + renomear
    return colunas_renomeadas


def tabela_coleta() -> pd.DataFrame:
    """
    Renomeia todas as colunas do dataframe.

    :param saida: retorna dataframe
    """
    df = agrupando()
    df.columns = renomeando_colunas()
    return df


def identificacao() -> pd.DataFrame:
    """
    Cria uma tabela dos polimeros.

    :param saida: retorna dataframe
    """
    ident = arquivos_coletados()[-1]
    df_read = pd.read_excel(ident)
    return df_read
