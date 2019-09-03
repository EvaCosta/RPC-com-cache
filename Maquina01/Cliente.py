from Rpc import Operacoes
from random import choice
from servidor_de_nomes import NOMES

#HOST = '127.0.0.1'
PORT = 12349

while True:
    v = input("Fim para sair\n")

    if v == "fim":
        operacoes.finalizar(v)
        break

    tokens = NOMES["soma"].copy()
    if len(tokens) > 0:
        while True:
            try:
                ip = choice(tokens)
                print(ip)
                operacoes = Operacoes(ip, PORT)
                print(operacoes.soma(15, 2))
                break
            except:
                tokens.remove(ip)
                print("nao encontrado")
                continue





    #print(operacoes.soma(20, 5, 5))
    #print(operacoes.soma(6, 8, 5))
    #print(operacoes.multiplicacao(10, 5, 6))

    #print(operacoes.fatorial(8))
