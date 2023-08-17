from pathlib import Path
from itertools import chain
import typing
from extract.diretorio import caminho_global


def arquivos_coletados() -> typing.List[Path]:
    """
     Guarda os diretorios dos arquivos.
    :param saida: lista de diretorios.
    """

    def find_excel_files_in(directory: Path) -> list[Path]:
        """
        Lê todos os arquivos dentro da página
        :param entrada: Entra o diretorio o qual está contido todos os arquivos.
        :param saida: Retorna diretorio de todos os arquivos.
        """
        files: list[Path] = [
            file for file in directory.rglob("*.xlsx") if file.is_file()
        ]
        return files

    caminho = caminho_global()
    directories: list[Path] = [
        caminho / "analise_de_microplasticos/arquivos",
        caminho / "analise_de_microplasticos/arquivo_identificacao",
    ]

    found_files: list[Path] = list(
        chain(*[find_excel_files_in(directory) for directory in directories])
    )
    return found_files
