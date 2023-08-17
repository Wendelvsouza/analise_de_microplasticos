from extract.diretorio import caminho_global
from load.analise import analise_dados
from load.graficos import plotando_graficos


def start(path) -> None:
    """
    Inicializa a analise
    :param entrada: caminho da pasta Postagem_0002
    """

    with open(path / "analise_dados.txt", "w") as file:
        for row in analise_dados():
            s = "".join(map(str, row))
            file.write(s + "\n")

    with open(str(path / "analise_dados.txt")) as file:
        print(file.read())
        print(24 * "#", "Deseja plotar o gráfico?", 25 * "#")
        print(
            "# Para plotar e salvar em PDF, digite 'Sim', caso contrario, digite 'Nao' #"
        )
        print("")
        decisao = input("Digite aqui: ")

        if decisao == "sim" or decisao == "Sim" or decisao == "SIM":
            print("")
            print("Gerando o grafico, aguarde!")
            print("")
            plotando_graficos(path)
            print("")
            print("Grafico salvo em PDF.")
            print("")
            print("Gerado um arquivo txt com os dados analisados.")
        else:
            print("")
            print("Gerado um arquivo txt com os dados analisados.")
            exit
    return


path = caminho_global()
start(path)
