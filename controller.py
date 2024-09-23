import customtkinter as ctk
from button import ButtonFrame

class AppController:
    def __init__(self, root):
        self.root = root
        self.janelaPrincipal()

    def janelaPrincipal(self):
        # Define as propriedades da janela principal
        self.root.title("Sistema de Agendamento")
        self.root.geometry("800x600")

        # Cria os botões
        self.button_frame = ButtonFrame(self.root)
