import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / "mais-um-novo-diretorio")

# arquivo = open(ROOT_PATH / "outro-novo.txt", "w")
# arquivo.close()

# os.rename(ROOT_PATH / "outro-novo.txt", ROOT_PATH / "novo-denovo.txt")

os.remove(ROOT_PATH / "novo-denovo.txt")

# shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-diretorio" / "novo.txt")
