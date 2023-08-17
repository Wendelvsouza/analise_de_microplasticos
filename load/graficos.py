from transform.montando import tabela_coleta, renomeando_colunas
from extract.coleta import arquivos_coletados
import matplotlib.pyplot as plt
import re
from tqdm import tqdm
from matplotlib.backends.backend_pdf import PdfPages


def plotando_graficos(path) -> None:
    """
    Gera o grafico dos dados e salva na pasta mãe
    :param entrada: diretorio
    """
    coleta = tabela_coleta()
    cols = renomeando_colunas()
    with PdfPages(path / "grafico.pdf") as pdf:

        def split(arr):
            """
            Dividi uma lista em sublista, sendo o limite de 5 elementos em cada lista.

            :param entrada: Entra uma lista
            :param saida: Retorna uma lista subdividida,
            """
            arrs = []
            while len(arr) > 5:
                pice = arr[:5]
                arrs.append(pice)
                arr = arr[5:]
            arrs.append(arr)
            return arrs

        arquivo_nome = arquivos_coletados()
        dividindo_listas = split(cols[1:])
        for j, _ in enumerate(tqdm(dividindo_listas)):
            f, axes = plt.subplots(
                nrows=len(_), ncols=1, figsize=(8.27, 11.69), tight_layout=True
            )
            for i, col in enumerate(_):
                ax = axes.flat[i]
                ax.plot(coleta[cols[0]], coleta[col], color="blue", linewidth="1")
                ax.set_title(f"{arquivo_nome[i].stem}")
                ax.set_xlabel(xlabel=f"{cols[0]}")
                ax.set_ylabel(ylabel=f"{re.sub('[0-9]', '', col)}")
            pdf.savefig()
        plt.show()
    return
