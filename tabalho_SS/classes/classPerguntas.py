class Pergunta:
    def __init__(self):
        self.perguntas = [linha.strip().split(':', 1) for linha in open('db/db_perguntas.txt', 'r', encoding='UTF-8')]

    def proxima(self):
        for p in self.perguntas :
            yield p
