import customtkinter
import tkinter as tk
from werkzeug.security import (generate_password_hash, check_password_hash)
from .interfaceCreateUser import CreateUser
from .interfaceLoja import Loja
from model.usuario import Usuario
from .messageBox import MessageBox

class Login(customtkinter.CTk):
    """ Interface principal de login
        Realiza verificao de usuario
        Controla criacao de usuario
        Retorna login ao Controlador
    """
    def __init__(self, controller):
        super().__init__()

        # INIT VARIABLES
        user_remember = self.getUserRemember()
        self.controller = controller

        # CONFIGURATION
        self.title('Revenda de Carros')
        self.geometry("600x400")
        self.maxsize(600, 400)
        self.minsize(600, 400)
        self.attributes('-alpha', 0.96)

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.login_label = customtkinter.CTkLabel(master=self.frame, text='Login', font=('Roboto', 24))
        self.login_label.pack(pady=50, padx=20)

        if user_remember == None:
            self.username = customtkinter.CTkEntry(master=self.frame, placeholder_text='Usuário')
            self.username.pack(pady=12, padx=10)
        else:
            self.username = customtkinter.CTkEntry(master=self.frame, placeholder_text='Usuário')
            self.username.insert(0, user_remember)
            self.username.pack(pady=12, padx=10)

        self.password = customtkinter.CTkEntry(master=self.frame, placeholder_text="Senha", show='*')
        self.password.pack(pady=12, padx=10)

        # button frame
        self.button_frame = customtkinter.CTkFrame(master=self.frame, bg_color=self.frame['background'])
        self.button_frame.pack()

        self.login_button = customtkinter.CTkButton(master=self.button_frame, text='Login', command=self.login)
        self.login_button.pack(side='left', pady=12, padx=10)

        self.create_button = customtkinter.CTkButton(master=self.button_frame, text='Criar Conta', command=self.create_account)
        self.create_button.pack(side='right', pady=12, padx=10)

        # bottom frame
        self.b_frame = customtkinter.CTkFrame(master=self.frame, bg_color=self.frame['background'])
        self.b_frame.pack()

        self.login_checkbox = customtkinter.CTkCheckBox(master=self.b_frame, text="Lembrar-me")
        self.login_checkbox.pack(side='left', pady=12, padx=10)

        self.forgot_label = customtkinter.CTkLabel(master=self.b_frame, text='Esqueceu a senha?', font=('Helvetica', 12, 'bold'))
        self.forgot_label.pack(side='right', pady=12, padx=10)
    

    def getUserRemember(self):
        """ verifica se houve último usuário
            retorna o usuario
        """
        with open('./model/db/remember.txt', 'r') as file:
            user = file.readline()
            if user == '':
                return None
            else:
                return user

    def login(self):
        """ verifica usuario e senha no banco de dados
            usuario verificado: inicializa a interfaceLoja
            usuario nao verificado: retorna messagebox com erro
        """
        username, password = self.username.get(), self.password.get()
        with open('./model/db/users.txt', 'r') as file:
            for line in file.readlines():
                user = line[0:-1].split('/')   # LISTA COM USUARIO E SENHA
                if username == user[0]:
                    if check_password_hash(user[1], password):
                        if self.login_checkbox.get():
                            with open('./model/db/remember.txt', 'w') as remember:
                                remember.write(username)
                        else:
                            with open('./model/db/remember.txt', 'w') as remember:
                                pass
                        self.withdraw()
                        self.controller.usuario = Usuario(username, password)
                        self.controller.lojaWindow = Loja(self, self.controller)
                        return
                    else:
                        return MessageBox(self, f'Senha Incorreta').grab_set()
            return MessageBox(self, f'Usuário Incorreto').grab_set()

    def create_account(self):
        self.withdraw()
        createUser = CreateUser(self)
