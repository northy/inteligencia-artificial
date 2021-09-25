from classes.classDiagnostico import *
from classes.classPerguntas import *
from classes.classRelatorio import *
import pyautogui as pag

if __name__=="__main__" :
    se = Diagnostico()
    base_perguntas = Pergunta().proxima()
    relatorio = Relatorio()

    print("Relatório:")

    while se.probabilidade() != 100 :
        try:
            pergunta = next(base_perguntas)
        except StopIteration :
            break
        se.pergunta(pergunta[0],pergunta[1],relatorio)
        relatorio.adicionar(se.status())

    salvar = pag.confirm(title="Sistema Especialista", text=se.status()+"\n\n"+"Deseja salvar o relatório?", buttons=["Sim","Não"])
    if salvar=="Sim" : print("\nSalvando relatório..."); relatorio.salvar()
