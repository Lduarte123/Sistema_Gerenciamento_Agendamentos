import customtkinter as ctk
from tkinter import messagebox

class CriarConta:
    def __init__(self, root):
        self.root = root
        self.criar_tela()

    def criar_tela(self):
        self.toplevel = ctk.CTkToplevel(self.root)
        self.toplevel.title("Criar Conta")
        self.toplevel.geometry("400x500")

        # Campos de entrada para o formulário de criação de conta
        self.label_nome = ctk.CTkLabel(self.toplevel, text="Nome:")
        self.label_nome.pack(pady=5)

        self.nome_entry = ctk.CTkEntry(self.toplevel, placeholder_text="Nome")
        self.nome_entry.pack(pady=5)

        self.label_data_nasc = ctk.CTkLabel(self.toplevel, text="Data de Nascimento:")
        self.label_data_nasc.pack(pady=5)

        self.data_nasc_entry = ctk.CTkEntry(self.toplevel, placeholder_text="DD/MM/AAAA")
        self.data_nasc_entry.pack(pady=5)

        self.label_cpf = ctk.CTkLabel(self.toplevel, text="CPF:")
        self.label_cpf.pack(pady=5)

        self.cpf_entry = ctk.CTkEntry(self.toplevel, placeholder_text="CPF")
        self.cpf_entry.pack(pady=5)

        self.label_usuario = ctk.CTkLabel(self.toplevel, text="Usuário:")
        self.label_usuario.pack(pady=5)

        self.usuario_entry = ctk.CTkEntry(self.toplevel, placeholder_text="Usuário")
        self.usuario_entry.pack(pady=5)

        self.label_senha = ctk.CTkLabel(self.toplevel, text="Senha:")
        self.label_senha.pack(pady=5)

        self.senha_entry = ctk.CTkEntry(self.toplevel, show="*", placeholder_text="Senha")
        self.senha_entry.pack(pady=5)

        self.criar_conta_button = ctk.CTkButton(self.toplevel, text="Criar Conta", command=self.criar_conta)
        self.criar_conta_button.pack(pady=20)

    def criar_conta(self):
        nome = self.nome_entry.get()
        data_nasc = self.data_nasc_entry.get()
        cpf = self.cpf_entry.get()
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if not all([nome, data_nasc, cpf, usuario, senha]):
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
        else:
            # Aqui você pode implementar a lógica de validação e salvamento de dados
            messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
            self.toplevel.destroy()
