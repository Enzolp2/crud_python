

class Carro:
    def __init__(self, marca, modelo, ano, preco, estado) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__preco = preco
        self.__estado = estado
    
    """ Getters e Setters """
    @property
    def marca(self):
        return self.__marca
    @marca.setter 
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter 
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano
    @ano.setter 
    def ano(self, ano):
        self.__ano = ano

    @property
    def preco(self):
        return self.__preco
    @preco.setter 
    def preco(self, preco):
        self.__preco = preco

    @property
    def estado(self):
        return self.__estado
    @estado.setter 
    def estado(self, estado):
        self.__estado = estado

    def __str__(self):
        return f'{self.marca}, {self.modelo}, {self.ano}, {self.preco}, {self.estado}'
