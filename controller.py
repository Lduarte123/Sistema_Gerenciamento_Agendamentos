import customtkinter as ctk
from button import ButtonFrame
from criarAgendamento import CriarAgendamento 
from visualizar import Visualizar
from tkinter import messagebox
from criarConta import CriarConta
class AppController:
    def __init__(self, root):
        self.root = root
        self.agendamentos = []  # Lista de agendamentos
        self.setup_login_ui()  # Configura a interface de login

    def setup_login_ui(self):
        self.root.title("Login")
        self.root.geometry("400x300")

        # Campos de login
        self.label_usuario = ctk.CTkLabel(self.root, text="Usuário:")
        self.label_usuario.pack(pady=5)

        self.username_entry = ctk.CTkEntry(self.root, placeholder_text="Usuário")
        self.username_entry.pack(pady=5)

        self.label_senha = ctk.CTkLabel(self.root, text="Senha:")
        self.label_senha.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self.root, show="*", placeholder_text="Senha")
        self.password_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(self.root, text="Login", command=self.login)
        self.login_button.pack(pady=20)

      # Botão para criar conta
        self.criar_conta_button = ctk.CTkButton(self.root, text="Criar conta", command=self.abrir_tela_criar_conta)
        self.criar_conta_button.pack(pady=10)

    def abrir_tela_criar_conta(self):
        CriarConta(self.root)  # Abre a janela para criar conta

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "senha":  # Exemplo simples
            self.setup_agendamento_ui()  # Se o login for bem-sucedido
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def setup_agendamento_ui(self):
        # Esconde os campos de login
        self.label_usuario.pack_forget()
        self.username_entry.pack_forget()
        self.label_senha.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()

        # Configura a janela principal para agendamentos
        self.root.title("Sistema de Agendamento")
        self.root.geometry("700x500")

        self.button_frame = ButtonFrame(self.root)
        self.button_frame.button_a.configure(command=self.criar_agendamento)
        self.button_frame.button_b.configure(command=self.visualizar_agendamento)

    def criar_agendamento(self):
        CriarAgendamento(self.root, self.agendamentos)

    def visualizar_agendamento(self):
        Visualizar(self.root, self.agendamentos)
