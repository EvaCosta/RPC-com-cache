import socket

class Operacoes:
    def __init__(self, ip, porta):
        self.conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        destino = (ip, porta)
        self.conexao.connect(destino)

    def finalizar(self, msg):
        self.conexao.send(msg.encode('utf-8'))
        self.conexao.close()

    def enviar_msg(self, msg, numeros):
        for numero in numeros:
            msg += str(numero) + " "

        self.conexao.send(msg.strip().encode('utf-8'))
        return self.conexao.recv(2048).decode('utf-8')

    def soma(self, *numeros):
        msg = "soma "
        return self.enviar_msg(msg, numeros)

    def subtracao(self, *numeros):
        msg = "subtração "
        return self.enviar_msg(msg, numeros)

    def multiplicacao(self, *numeros):
        msg = "multiplicação "
        return self.enviar_msg(msg, numeros)

    def fatorial(self, *numeros):
        msg = "fatorial "
        return self.enviar_msg(msg, numeros)