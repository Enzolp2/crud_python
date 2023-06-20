

class Marca:
    def __init__(self, nome_marca) -> None:
        self.__nome_marca = nome_marca
        self.__list_modelos = []
        
    """ Getters e Setters """
    @property
    def nome_marca(self):
        return self.__nome_marca
    @nome_marca.setter 
    def nome_marca(self, nome_marca):
        self.__nome_marca = nome_marca
    
    @property
    def list_modelos(self):
        return self.__list_modelos
