#socketTPC.py
#coding:utf-8

import socket
import threading
import os

serverPort = 12349
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(0)

print("OK")

def realiza_operacao(res):
    resposta = 0
    if res[0] == "soma":
        for digito in res[1:]:
            resposta += int(digito)
    elif res[0] == "multiplicação":
        resposta = 1
        for digito in res[1:]:
            resposta *= int(digito)

    return resposta

def connection(connectionSocket, addr):
    while True:
        message = connectionSocket.recv(2048).decode('utf-8')

        if not message: break

        res = message.split(" ")

        if(res[0] == "soma"):
            cache("soma.txt",message, res, connectionSocket)
        if(res[0] == "multiplicação"):
            cache("mul.txt",message, res, connectionSocket)

    connectionSocket.close()

def cache(nome_arquivo, message, res, connectionSocket):
    arquivo = le_arquivo(nome_arquivo, "r+")
    retorno = 0
    conteudo = arquivo.readlines()

    #print(message)
    #print(conteudo)

    if not conteudo:
        resultado = str(realiza_operacao(res))
        arquivo.writelines(message + ";" + resultado + "\n")
        arquivo.close()
        connectionSocket.send(str(resultado).encode('utf-8'))

    else:
        for linha in conteudo:
            linha = linha.replace("\n", "")

            aux = linha.split(";")
            #print(aux)
            #print(len(aux))
            operacao = aux[0]
            resultado = aux[1]

            #print(operacao)
            #print(resultado)
            #print("===========================")
            #print(linha)
            #print(message)
            #print("##########################")

            if operacao == message:
                connectionSocket.send(str(resultado).encode('utf-8'))
                retorno = 1

                #break

        if(retorno == 0):
            resultado = str(realiza_operacao(res))
            arquivo.writelines(message + ";" + resultado + "\n")
            arquivo.close()
            connectionSocket.send(str(resultado).encode('utf-8'))

def le_arquivo(mensagem, tipo_abertura):
    arquivo = open(mensagem, tipo_abertura)

    return arquivo


def main():
    resultado = []
    threads = []
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão vinda de {}".format(addr))
        th = threading.Thread(target=connection, args=(connectionSocket, addr))

        th.start()
        threads.append(th)


if __name__ == "__main__":
    main()
