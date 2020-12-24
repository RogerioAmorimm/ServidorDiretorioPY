from const import *
import rpyc
from rpyc.utils.server import ForkingServer


class ServerDir(rpyc.Service):
    
    serverNEncontrado = f"Server não encontrado ou não existente"
    
    ListaDir = {}
    
    def __init__(self, Dicionario):
        self.ListaDir = Dicionario

    def exposed_registraServer(self, serverName, ipAdress, portNum):
        self.ListaDir.update({serverName : (ipAdress, portNum)})
        print(f"Registrando Server")
        print(self.ListaDir)

    def exposed_buscaServer(self, serverName):
        print(f"Buscando Server")
        print({serverName})
        print(f"tem no dic: {serverName in self.ListaDir}")

        if  serverName in self.ListaDir:
            print(f"Server encontrado")
            print(self.ListaDir)
            return self.ListaDir[serverName]
        else:
            print(f"Server não encontrado")
            print(self.ListaDir)
            return self.serverNEncontrado


if __name__ == "__main__":
    ListaDir = {}
    print(f"Iniciando servidor de diretórios na porta: {PORTDIR}")
    serverDir = ForkingServer(ServerDir(ListaDir), port=12307)
    serverDir.start()
