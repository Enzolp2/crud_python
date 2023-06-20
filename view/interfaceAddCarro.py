from typing import Optional, Tuple, Union
import customtkinter
import tkinter as tk
from werkzeug.security import (generate_password_hash, check_password_hash)
from .messageBox import MessageBox

class AddCarro(customtkinter.CTkToplevel):
    def __init__(self, main, controller):
        super().__init__()
    
        self.main = main    # WINDOW PRINCIPAL
        self.controller = controller

        # CONFIGURATION
        self.geometry("600x400")
        self.maxsize(600, 400)
        self.minsize(600, 400)
        self.attributes('-alpha', 0.96)

        self.frame = customtkinter.CTkFrame(master=self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.create_label = customtkinter.CTkLabel(master=self.frame, text='Cadastrar Veículo', font=('Roboto', 24))
        self.create_label.pack(pady=25, padx=20)

        self.marca = customtkinter.CTkEntry(master=self.frame, placeholder_text='Marca', width=200)
        self.marca.pack(pady=6, padx=12)

        self.modelo = customtkinter.CTkEntry(master=self.frame, placeholder_text='Modelo', width=200)
        self.modelo.pack(pady=6, padx=12)

        self.ano = customtkinter.CTkEntry(master=self.frame, placeholder_text='Ano', width=200)
        self.ano.pack(pady=6, padx=12)

        self.preco = customtkinter.CTkEntry(master=self.frame, placeholder_text='Preco', width=200)
        self.preco.pack(pady=6, padx=12)

        self.estado = customtkinter.CTkEntry(master=self.frame, placeholder_text='Estado', width=200)
        self.estado.pack(pady=6, padx=12)

        # button frame
        self.button_frame = customtkinter.CTkFrame(master=self.frame, bg_color=self.frame['background'])
        self.button_frame.pack(pady=12)

        self.create_button = customtkinter.CTkButton(master=self.button_frame, text='Cadastrar', command=self.create_car)
        self.create_button.pack(side='left', pady=12, padx=10)

        self.back_button = customtkinter.CTkButton(master=self.button_frame, text='Voltar', fg_color='#891111', command=self.destroy_win)
        self.back_button.pack(side='right', pady=12, padx=10)

    def create_car(self):
        if self.verify_entry():
            self.controller.add_carro(self.marca.get(), self.modelo.get(), self.ano.get(), self.preco.get(), self.estado.get())
            self.destroy_win()
 

    def verify_entry(self):
        entry = [self.marca.get(), self.modelo.get(), self.ano.get(), self.preco.get(), self.estado.get()]
        if '' in entry:
            return MessageBox(self, 'Preencha os campos em branco!')
        else:
            try:
                int(self.ano.get())
            except:
                return MessageBox(self, 'Ano inválido!')

            try:
                float(self.preco.get())
            except:
                return MessageBox(self, 'Preco inválido!')
        return True

    def destroy_win(self):
        self.main.atualizar_view()
        self.main.deiconify()
        self.destroy()