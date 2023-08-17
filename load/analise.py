from transform.montando import renomeando_colunas, identificacao, tabela_coleta
from extract.coleta import arquivos_coletados
from tqdm import tqdm
import typing


def analise_dados() -> list:
    """
    Analise dos dados coletados.
    :param saida: retorna uma lista
    """
    guardar_analises = []
    var = [3, 4]
    coleta = tabela_coleta()
    iden = identificacao()
    cols = renomeando_colunas()
    columns_iden = identificacao().columns

    def pico(m, n) -> typing.List:
        """
        Obtem os picos de cada dado coletado e salva numa lista.

        :param entrada: Recebe o dataframe com todos dados e a coluna a ser analisado
        :param saida: Retorna uma lista
        """
        wavernumber = []
        for i in range(1, len(m) - 1):
            if (m[i - 1] < m[i]) and (m[i + 1] < m[i]) and m[i] > -10.0:
                wavernumber.append(n[i])
        return wavernumber

    def verifica(var, cols, iden, coleta, cols_0) -> None:
        """
        Faz a analise dos dados com objetivo de identificar a qual polimero a amostra
        pertence.

        :param var: Variacao do erro absoluto.
        :param cols: Nome de cada colunas exceto da primeira coluna do dataframe.
        :param iden: Tabela com os dados dos polmeros.
        :param coleta: Dataframe com as amostras.
        :param cols_0: Nome da primeira coluna do dataframe.
        """
        arquivo_nome = arquivos_coletados()
        for _, z in enumerate(cols):
            v = pico(coleta[z], coleta[cols_0])
            guardar_analises.append(93 * "-")
            guardar_analises.append(
                f"Analise dos dados contido no arquivo {arquivo_nome[_].stem}."
            )

            for k in columns_iden:
                comparando = []
                for i in range(iden[k].nunique()):
                    for j in range(len(v)):
                        com = abs(v[j] - iden[k][i])
                        if com <= var:
                            comparando.append(com)

                if len(comparando) == iden[k].nunique():
                    guardar_analises.append(f"É possível que o polimero seja: {k}")
        guardar_analises.append(93 * "-")
        return
 
    print("\n")
    print("########### Analisando amostras, aguarde! ###########")
    print("\n")
    guardar_analises.append("\n")
    guardar_analises.append("         🅂 🄲 🄸 🄴 🄽 🅃 🄸 🅂 🅃 ❜ 🅂  🄽 🄾 🅃 🄴 🅂 ")
    for var in tqdm(var):
        guardar_analises.append("\n")
        guardar_analises.append(
            f"########### Considerando o erro de {var}, temos que:##########"
        )
        guardar_analises.append("\n")
        verifica(var, cols[1:], iden, coleta, cols[0])
    return guardar_analises
