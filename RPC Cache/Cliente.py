from Rpc import Operacoes

HOST = '127.0.0.1'
PORT = 12349

while True:
    v = input("Fim para sair\n")


    
    operacoes = Operacoes(HOST, PORT)

    if v == "fim":  
        operacoes.finalizar(v)
        break

    #print(operacoes.soma(20, -40, 20))
    #print(operacoes.soma(6, 8, 5))
    #print(operacoes.multiplicacao(-1, -1))
    #print(operacoes.subtracao(-5, -5))
    print(operacoes.fatorial(0))

    

    