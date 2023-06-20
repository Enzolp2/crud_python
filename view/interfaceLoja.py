from typing import Optional, Tuple, Union
import customtkinter
import tkinter as tk
from tkinter import ttk
from werkzeug.security import (generate_password_hash, check_password_hash)
from .interfaceAddCarro import AddCarro
from .messageBox import MessageBox


class Loja(customtkinter.CTkToplevel):
    """ Interface principal da loja
        Controla a interface de criacao de carro
        Controla os metodos de CRUD
        Tem acesso a messageBox
    """
    def __init__(self, main, controller):
        super().__init__()

        # TOPLEVEL WINDOW
        self.main = main
        self.controller = controller

        # CONFIGURATION
        self.title('Criar Usuário')
        self.geometry("1300x500")
        self.maxsize(1800, 800)
        self.minsize(700, 500)
        self.attributes('-alpha', 0.96)

        # WIDGETS
        self.search_label = customtkinter.CTkLabel(master=self, text='Marca', font=('Helvetica', 12, 'bold'))
        self.search_entry = customtkinter.CTkEntry(master=self, placeholder_text='Digite a marca do carro', font=('Helvetica', 12, 'bold'), width=200)
        self.search = customtkinter.CTkButton(master=self, text='Filtrar', width=200, command=self.filterMarca)
        self.add_car = customtkinter.CTkButton(master=self, text='Adicionar Carro', width=200, command=self.add_carro)
        self.update_car = customtkinter.CTkButton(master=self, text='Atualizar Carro', width=200, command=self.atualizar_carro)
        self.delete_car = customtkinter.CTkButton(master=self, text='Deletar Carro', width=200, command=self.delete_value)
        self.x_car = customtkinter.CTkButton(master=self, text='Calcular Média', width=200, command=self.calcular_media)
        self.close = customtkinter.CTkButton(master=self, text='Sair', width=200, fg_color='#891111', command=self.destroy_win)

        self.list_carros = ttk.Treeview(self, columns=['marca', 'modelo', 'ano', 'preco', 'estado'], show='headings')
        #self.list_carros.heading('id', text='ID')
        self.list_carros.heading('marca', text='Marca')
        self.list_carros.heading('modelo', text='Modelo')
        self.list_carros.heading('ano', text='Ano')
        self.list_carros.heading('preco', text='Preco')
        self.list_carros.heading('estado', text='Status')


        # GRID WIDGETS
        self.search_label.grid(row=0, column=0, padx=12, pady=8)
        self.search_entry.grid(row=0, column=1, padx=12, pady=8)
        self.search.grid(row=2, column=0, columnspan=2, padx=3, pady=24, sticky='N')    
        self.add_car.grid(row=3, column=0, columnspan=2, padx=3, pady=4)
        self.update_car.grid(row=4, column=0, columnspan=2, padx=3, pady=4)
        self.delete_car.grid(row=5, column=0, columnspan=2, padx=3, pady=4)
        self.x_car.grid(row=6, column=0, columnspan=2, padx=3, pady=4)
        self.close.grid(row=7, column=0, columnspan=2, padx=3, pady=4)

        self.list_carros.grid(row=0, column=3, rowspan=5, pady=12, sticky='nsew')

        # PROTOCOLS
        self.protocol("WM_DELETE_WINDOW", self.destroy_win)
        self.list_carros.bind('<<TreeviewSelect>>', self.item_select)
        self.list_carros.bind('<Delete>', self.delete_values)

        # ATUALIZAÇÃO DA VIEW
        self.atualizar_view()
    
    def add_carro(self):
        """ Oculta a tela de loja principal
            Inicializa a tela para cadastrar novo carro 
        """
        self.withdraw()
        create_car = AddCarro(self, self.controller)

    def item_select(self, _):
        """ Resgatar eventos de seleção na treeView """
        print(self.list_carros.selection())
        for i in self.list_carros.selection():
            print(self.list_carros.item(i)['values'])

    def delete_values(self, _):
        """ Deletar valores de seleção na treeView """
        print('delete')
        for i in self.list_carros.selection():
            print(self.list_carros.item(i)['values'])
            self.controller.delete_carro(self.list_carros.item(i)['values'])
            self.list_carros.delete(i)

    def delete_value(self):
        """ Deletar valor único de seleção na treeView """
        for i in self.list_carros.selection():
            self.controller.delete_carro(self.list_carros.item(i)['values'])
            self.list_carros.delete(i)    

    def clear_all(self):
        """ Limpa todos os valores da treeView para atualizar a view """
        for item in self.list_carros.get_children():
            self.list_carros.delete(item)
    
    def atualizar_view(self):
        """ Atualiza a view """
        index=0
        self.clear_all()
        for i in self.controller.list_carros:
            self.list_carros.insert(parent='', index=index, values=(i.marca.upper(), i.modelo.upper(), str(i.ano),'R$ '+str(i.preco), i.estado.upper()))
            index+=1

    def filterMarca(self):
        """ filtra a TreeView com base na marca da entry SearchEntry
        """
        search = self.search_entry.get()
        filter_items = []
        if search == '':
            self.atualizar_view()
        else:
            for item in self.list_carros.get_children():
                if search in self.list_carros.item(item)['values'][0]:
                    filter_items.append(self.list_carros.item(item)['values'])
            self.filter(filter_items)
        
    def filter(self, items):
        self.clear_all()
        index=0
        for i in items:
            self.list_carros.insert(parent='', index=index, values=(i[0], i[1], str(i[2]), str(i[3]), i[4]))
            index+=1

    def calcular_media(self):
        avg = self.controller.average_carros()
        return MessageBox(self, f'Média dos {len(self.controller.list_carros)} carros: R$ {avg}').grab_set()
    
    def atualizar_carro(self):
        selected_car = self.list_carros.selection()
        dialog = customtkinter.CTkInputDialog(text="Digite o novo preço:", title="Atualizar Preço")
        try:
            self.controller.update_carro(self.list_carros.item(selected_car)['values'], float(dialog.get_input()))
        except:
            MessageBox(self, 'Valor inválido!')


    def destroy_win(self):
        self.controller.usuario = None
        self.controller.save_data()
        self.main.deiconify()
        self.destroy()
    

    
