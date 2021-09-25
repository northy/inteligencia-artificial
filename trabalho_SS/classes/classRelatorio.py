from datetime import datetime
from pathlib import Path

class Relatorio:
    def __init__(self):
        self.estado = []

    def adicionar(self,linha):
        self.estado.append(linha+'\n')
        print(linha)
    
    def salvar(self) :
        self.estado[0] = self.estado[0].lstrip()
        Path("relatorios").mkdir(exist_ok=True)
        now = datetime.now()
        arquivo = open(now.strftime("relatorios/Relatorio %d_%m_%Y %H_%M_%S.txt"), "w+", encoding="UTF-8")
        arquivo.writelines(self.estado)
