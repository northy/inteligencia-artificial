if __name__=="__main__" :
    arquivo = open("base.dot", "w+", encoding="UTF-8")
    arquivo.write("strict digraph {\n")

    arquivo.writelines(map(lambda rel : '"'+rel[0]+'"->"'+rel[1]+'"\n', (linha.strip().split('-') for linha in open('db/db.txt', 'r', encoding='UTF-8'))))
    arquivo.writelines(map(lambda pergunta : '"'+pergunta[0]+'"->"'+pergunta[1]+'"\n', (linha.strip().split(':') for linha in open('db/db_perguntas.txt', 'r', encoding='UTF-8'))))

    arquivo.write("}\n")
