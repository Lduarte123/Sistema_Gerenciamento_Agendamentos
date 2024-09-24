# controller.py
import customtkinter as ctk
from button import ButtonFrame
from criarAgendamento import CriarAgendamento  # Importa a classe de agendamentos
import random

class AppController:
    def __init__(self, root):
        self.root = root
        self.agendamentos = []  # Lista de agendamentos
        self.janelaPrincipal()

    def janelaPrincipal(self):
        # Define as propriedades da janela principal
        self.root.title("Sistema de Agendamento")
        self.root.geometry("800x600")

        # Cria os botões
        self.button_frame = ButtonFrame(self.root)
        self.button_frame.button_a.configure(command=self.criar_agendamento)

    def criar_agendamento(self):
        CriarAgendamento(self.root, self.agendamentos)  # Chama a classe para criar agendamentos
