from pathlib import Path

if __name__=="__main__" :
    Path("dot").mkdir(exist_ok=True)
    with open("dot/base.dot", "w+", encoding="UTF-8") as arquivo :
        arquivo.write("strict digraph {\n")

        arquivo.writelines(map(lambda rel : '"'+rel[0]+'"->"'+rel[1]+'"\n', (linha.strip().split('-') for linha in open('db/db.txt', 'r', encoding='UTF-8'))))
        arquivo.writelines(map(lambda pergunta : '"'+pergunta[0]+'"->"'+pergunta[1]+'"\n'+'"'+pergunta[0]+'"->"n_'+pergunta[1]+'"\n', (linha.strip().split(':') for linha in open('db/db_perguntas.txt', 'r', encoding='UTF-8'))))

        arquivo.write("}\n")
        arquivo.close()

    for pergunta in open("db/db_perguntas.txt", "r", encoding="UTF-8") :
        pergunta = pergunta.strip().split(':')
        with open("dot/"+pergunta[1]+".dot", "w+", encoding="UTF-8") as arquivo :
            arquivo.write("strict digraph {\n")
            arquivo.writelines(['"'+pergunta[0]+'"->"'+pergunta[1]+'"\n','"'+pergunta[0]+'"->"n_'+pergunta[1]+'"\n'])
            arquivo.writelines(map(lambda rel : '"'+rel[0]+'"->"'+rel[1]+'"\n', filter(lambda x : x[0]==pergunta[1] or x[0]=='n_'+pergunta[1], (linha.strip().split('-') for linha in open('db/db.txt', 'r', encoding='UTF-8')))))
            arquivo.write("}\n")
        