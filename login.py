import customtkinter as ctk
from tkinter import messagebox

class Login:
    def __init__(self, controller, on_success):
        self.controller = controller
        self.on_success = on_success  # Função a ser chamada em caso de sucesso
        self.janela_login = ctk.CTkToplevel(self.controller.root)  # Cria uma nova janela
        self.janela_login.title("Login")
        self.janela_login.geometry("400x300")

        self.label = ctk.CTkLabel(self.janela_login, text="Login")
        self.label.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self.janela_login, placeholder_text="Usuário")
        self.username_entry.pack(pady=5)

        self.password_entry = ctk.CTkEntry(self.janela_login, show="*", placeholder_text="Senha")
        self.password_entry.pack(pady=5)

        self.login_button = ctk.CTkButton(self.janela_login, text="Login", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "senha":  # Exemplo simples
            self.on_success()  # Chama a função de sucesso
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
