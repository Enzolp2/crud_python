from marca import Marca


class Modelo:
    def __init__(self, nome_modelo, marca: Marca) -> None:
        self.__nome_modelo = nome_modelo
        if isinstance(marca, Marca):
            self.__marca = marca


    """ Getters e Setters """
    @property
    def nome_modelo(self):
        return self.__nome_modelo
    @nome_modelo.setter 
    def nome_modelo(self, nome_modelo):
        self.__nome_modelo = nome_modelo

    @property
    def marca(self):
        return self.__marca
    @marca.setter 
    def marca(self, marca: Marca):
        if isinstance(marca, Marca):
            self.__marca = marca
        