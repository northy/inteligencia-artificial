import pyautogui as pag

class Diagnostico():
    def __init__(self):
        self.resultado, self.db = set(), {}
        
        arquivo = open('db/db.txt','r')
        for linha in arquivo :
            pergunta, resposta = linha.strip().split('-', 1)
            if pergunta not in self.db : self.db[pergunta] = set()
            self.db[pergunta].add(resposta)
            self.resultado.add(resposta)

    def probabilidade(self):
        if len(self.resultado)==0 : print("O sistema está 0% decidido, possibilidade não cadastrada"); exit(1)
        return 100//len(self.resultado)
    
    def status(self)->str :
        return "O sistema está {}% decidido, seu pet {}:\n• {}".format(self.probabilidade(),'está' if self.probabilidade()==100 else 'pode estar','\n• '.join(self.resultado))

    def exclui_quem_nao_bate(self, estadoPergunta): self.resultado = set(filter(lambda x : x in self.db[estadoPergunta], self.resultado))

    def exclui_quem_bate(self, estadoPergunta): self.resultado = set(filter(lambda x : x not in self.db[estadoPergunta], self.resultado))

    def pergunta(self,pergunta,estado,relatorio):
        resp = pag.confirm(title="Sistema Especialista", text=self.status()+"\n\n"+pergunta, buttons=["Sim","Não"])
        if resp : relatorio.adicionar('\n'+pergunta+' '+resp)
        if resp == "Sim" : self.exclui_quem_nao_bate(estado)
        elif resp == "Não" : self.exclui_quem_bate(estado)
        else : exit(1)
