

class Usuario:
    def __init__(self, username, password) -> None:
        self.__username = username
        self.__password = password
    
    """ Getters e Setters """
    @property
    def username(self):
        return self.__username
    @username.setter 
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter 
    def password(self, password):
        self.__password = password

    
    def __str__(self):
        return f'Usuário: {self.username}'