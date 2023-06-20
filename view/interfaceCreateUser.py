from typing import Optional, Tuple, Union
import customtkinter
import tkinter as tk
from werkzeug.security import (generate_password_hash, check_password_hash)
from .messageBox import MessageBox

class CreateUser(customtkinter.CTkToplevel):
    def __init__(self, main):
        super().__init__()
    
        # TOPLEVEL WINDOW
        self.main = main

        # CONFIGURATION
        self.title('Criar Usuário')
        self.geometry("500x400")
        self.maxsize(600, 400)
        self.minsize(500, 400)
        self.attributes('-alpha', 0.96)

        # WIDGETS
        self.frame = customtkinter.CTkFrame(master=self)
        self.create_label = customtkinter.CTkLabel(master=self.frame, text='Criar Conta', font=('Roboto', 24))
        self.username = customtkinter.CTkEntry(master=self.frame, placeholder_text='Usuário')
        self.password = customtkinter.CTkEntry(master=self.frame, placeholder_text="Senha", show='*')
        self.confirm_pass = customtkinter.CTkEntry(master=self.frame, placeholder_text="Confirmar Senha", show='*')
        self.button_frame = customtkinter.CTkFrame(master=self.frame, bg_color=self.frame['background'])
        self.create_button = customtkinter.CTkButton(master=self.button_frame, text='Criar Conta', command=self.create_account)
        self.back_button = customtkinter.CTkButton(master=self.button_frame, text='Voltar', command=self.destroy_win)

        # PACKING WIDGETS
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.create_label.pack(pady=50, padx=20)
        self.username.pack(pady=12, padx=10)
        self.password.pack(pady=12, padx=10)
        self.confirm_pass.pack(pady=12, padx=10)
        self.button_frame.pack()
        self.create_button.pack(side='left', pady=12, padx=10)
        self.back_button.pack(side='right', pady=12, padx=10)
        
        # PROTOCOLS
        self.protocol("WM_DELETE_WINDOW", self.destroy_win)

    def create_account(self):
        username, pass1, pass2 = self.username.get(), self.password.get(), self.confirm_pass.get()
        if username == '':
            MessageBox(self, 'Preencha o Usuário').grab_set()
        elif pass1 == '':
            MessageBox(self, 'Preencha a Senha').grab_set()
        elif pass1 != pass2:
            MessageBox(self, 'Senhas não coicidem').grab_set()
        else:
            self.verify_user(username, pass1)


    def verify_user(self, username, password):
        with open('./model/db/users.txt', 'r') as file:

            for i in file.read().split('\n'):
                user = i.split('/')
                if user[0] == username:
                    return MessageBox(self, f'Usuário {username} já cadastrado!').grab_set()
            self.create_user(username, password)
                    
    def create_user(self, username, password):
        with open('./model/db/users.txt', 'a') as file:
            try:
                file.write(username + '/' + generate_password_hash(password) + '\n')
                MessageBox(self, f'Usuário {username} cadastrado!').grab_set()
            except Exception:
                MessageBox(self, f'{Exception}').grab_set()
        self.destroy_win()

    def destroy_win(self):
        self.main.deiconify()
        self.destroy()





        