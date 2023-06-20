from typing import Optional, Tuple, Union
import customtkinter
import tkinter as tk
from werkzeug.security import (generate_password_hash, check_password_hash)

class MessageBox(customtkinter.CTkToplevel):
    def __init__(self, main, message):
        super().__init__()

        self.main = main

        # CONFIGURATION
        self.title('MessageBox')
        self.geometry(f"200x100+200+200")
        self.maxsize(200, 100)
        self.minsize(200, 100)

        

        self.attributes('-alpha', 0.96)


        # WIDGETS
        self.frame = customtkinter.CTkFrame(master=self)
        self.message = customtkinter.CTkLabel(master=self.frame, text=message, font=('Roboto', 12))
        self.confirm = customtkinter.CTkButton(master=self.frame, text='Ok', command=self.destroy_win)

        # PACKING WIDGETS
        self.frame.pack()
        self.message.pack(pady=12, padx=12)
        self.confirm.pack(pady=9, padx=12)
    
    def destroy_win(self):
        try:
            self.main.deiconify()
            self.destroy()
        except:
            self.destroy()
