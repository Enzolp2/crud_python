from view.interfaceLoja import Loja
from view.interfaceLogin import Login
from model.carro import Carro

class Controller:
    """ Controla os Models
        Controla as Interface
        Controla as interecoes entre models e interface
        Executa funcoes de CRUD e persistencia
    """
    def __init__(self, usuario=None) -> None:
        """ Inicializa o controlador com algumns parametros
            usuario        - Usuario logado para realizar as operacoes
            list_carros    - Lista de carros cadastrados no sistema
            loginWindow    - Interface principal de login 
                             usada para fazer logout
            lojaWindow     - Interface principal da Loja
            load_data()    - Funcao para carregar os dados salvos
        """

        self.usuario = usuario
        self.list_carros = []
        self.loginWindow = Login(controller=self)
        self.lojaWindow = None
        self.load_data()

    def run(self):
        """ Inicializa o loop principal com a tela de Login """
        self.loginWindow.mainloop()

    def load_data(self):
        """ Carrega os arquivos gravados em txt """
        with open('./model/db/carros.txt', 'r') as file:
            for i in file.read().split('\n'):
                if i != '':
                    values = i.split('/')
                    self.list_carros.append(Carro(values[0], values[1], int(values[2]), float(values[3]), values[4])) 
        for i in self.list_carros:
            print(i)

    def save_data(self):
        """ Implementa a persistencia em arquivos txt """
        with open('./model/db/carros.txt', 'w') as file:
            for i in self.list_carros:
                line = i.marca.upper() + '/' + i.modelo.upper() + '/' + str(i.ano).upper() + '/' + str(i.preco).upper() + '/' + i.estado.upper() + '\n'
                file.write(line)

    def add_carro(self, marca, modelo, ano, preco, estado):
        """ cadastra novo carro a lista de carros
            retorna True or False
        """
        try:
            self.list_carros.append(Carro(marca, modelo, ano, preco, estado))
            print('CRIADO', self.list_carros)
            return True
        except:
            return False

    def update_carro(self, carro, new_preco):
        """ atualiza somente preco de um carro existente
            retorna True or False
        """
        for i in self.list_carros:
            if i.marca == carro[0]:
                if i.modelo == carro[1]:
                    if str(i.ano) == str(carro[2]):
                        if 'R$ '+str(i.preco) == carro[3]:
                            if i.estado == carro[4]:
                                i.preco = new_preco
                                return True
        return False

    def delete_carro(self, carro):
        """ recebe uma lista com valores de um carro
            deleta a primeira ocorrencia
        """
        for i in self.list_carros:
            if i.marca == carro[0]:
                if i.modelo == carro[1]:
                    if str(i.ano) == str(carro[2]):
                        if 'R$ '+str(i.preco) == carro[3]:
                            if i.estado == carro[4]:
                                self.list_carros.remove(i)
                                print('DELETADO', i)
                                return True
        return False


    def average_carros(self):
        """ retorna a média dos preços dos carros cadastrados
        """
        sum, count = 0, len(self.list_carros)
        for i in self.list_carros:
            try:
                sum += float(i.preco)
            except:
                sum += i.preco
        return '{:.2f}'.format(sum/count)

