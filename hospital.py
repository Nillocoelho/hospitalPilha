class FilaException(Exception):
    pass

class FilaVaziaException(FilaException):
    pass

class FilaCheiaException(FilaException):
    pass

class Paciente:
    def __init__(self, nome = None, cpf = None, plano = None):
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__plano: str = plano

    def __str__(self) -> str:
        informacoes = f'[{self.__nome},{self.__cpf},{self.__plano}]'
        return informacoes
    

class Node:
    
    def __init__(self, valor, proximo=None):
        self.valor = valor
        self.proximo: Node | None = proximo

    def __repr__(self):
        return f'Node(valor={self.valor})'

class FilaEncadeada:
    
    def __init__(self):
        self.__inicio: Node | None = None
        self.__fim: Node | None = None
        self.__tamanho: int = 0
        self.__contador: int = 0

    def tamanho(self) -> int:
        return self.__tamanho

    def estah_vazia(self) -> bool:
        return self.tamanho() == 0

    def enfileirar(self, valor) -> None:
        elemento = Node(valor)
        if self.estah_vazia():
            self.__inicio = elemento
        else:
            self.__fim.proximo = elemento

        self.__fim = elemento
        self.__tamanho += 1

    def desenfileirar(self):
        if self.estah_vazia():
            raise FilaVaziaException()

        valor = self.__inicio.valor
        self.__inicio = self.__inicio.proximo
        self.__tamanho -= 1
        self.__contador += 1
        return valor
    
    def busca(self, valor) -> bool:
        no = self.__inicio
        while no != None:
            if no.valor == valor:
                return True
            no = no.proximo
        return False
    
    def consulta(self):
        return f'[{self.__inicio}]'
    
    def contagem(self) -> int:
        return self.__contador
    
    def __contains__(self, valor):
        return self.busca(valor)

    def __str__(self):
        result = ["["]
    
        no = self.__inicio
        while no != None:
            result.append(str(no.valor))
            result.append(",")
            no = no.proximo

        if not self.estah_vazia():
            result.pop(-1)

        result.append("]")
        return "".join(result)
    