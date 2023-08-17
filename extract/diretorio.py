from pathlib import Path


def caminho_global() -> Path:
    """
    Obtem o caminho da pasta mãe.
    :param saida: retorna um diretorio
    """
    path = Path(__file__).parent.parent.absolute()
    return path
