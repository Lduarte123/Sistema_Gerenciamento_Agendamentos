# controller.py
import customtkinter as ctk
from button import ButtonFrame
from criarAgendamento import CriarAgendamento  # Importa a classe de agendamentos
from visualizar import Visualizar
import random

class AppController:
    def __init__(self, root):
        self.root = root
        self.agendamentos = []  # Lista de agendamentos
        self.janelaPrincipal()

    def janelaPrincipal(self):
        # Define as propriedades da janela principal
        self.root.title("Sistema de Agendamento")
        self.root.geometry("700x500")

        # Cria os botões
        self.button_frame = ButtonFrame(self.root)
        self.button_frame.button_a.configure(command=self.criar_agendamento)
        self.button_frame.button_b.configure(command=self.visualizar_agendamento)

    def criar_agendamento(self):
        CriarAgendamento(self.root, self.agendamentos)  # Chama a classe para criar agendamentos
    def visualizar_agendamento(self):
        Visualizar(self.root, self.agendamentos)  # Passa a lista de agendamentos