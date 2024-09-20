import customtkinter as ctk

class AppController:
    def __init__(self, root):
        self.root = root
        self.janelaPrincipal()

    def janelaPrincipal(self):
        # Define as propriedades da janela principal
        self.root.title("Sistema de Agendamento")
        self.root.geometry("800x600")

    # Inserir aqui  as demais funções para criar as janelas e componentes da aplicação
