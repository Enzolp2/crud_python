import customtkinter
from controller.controller import Controller

""" GLOBAL CONFIGURATION """
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

if __name__ == "__main__":
    """ Inicializa o controlador
        Inicializa o loop principal
    """
    app = Controller()
    app.run()