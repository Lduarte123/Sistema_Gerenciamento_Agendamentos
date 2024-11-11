import customtkinter as ctk
from services.emails import VerificacaoEmail
from tkinter import messagebox
from repository.usuario_repository import UsuarioRepository

class RedefinirSenhaWindow(ctk.CTkToplevel):
    def __init__(self, master, title):
        super().__init__(master)
        self.title(title)
        self.geometry("300x150")
        self.resizable(False, False)

        # Centralizar a janela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (300 // 2)
        y = (screen_height // 2) - (150 // 2)
        self.geometry(f"350x200+{x}+{y}")  # Centraliza a nova janela

        # Inicializar variáveis
        self.email_usuario = None
        self.verificacao_email = None

        # Primeira tela: Solicitar E-mail
        self.label = ctk.CTkLabel(self, text="Digite seu e-mail:")
        self.label.pack(pady=(20, 5))

        self.email_entry = ctk.CTkEntry(self, placeholder_text="Digite seu e-mail", width=200)
        self.email_entry.pack(pady=(5, 10))

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=(5, 10))

        self.ok_button = ctk.CTkButton(self.button_frame, text="OK", command=self.enviar_codigo, width=95)
        self.ok_button.pack(side="left", padx=5)

        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancelar", command=self.on_cancel, width=95)
        self.cancel_button.pack(side="right", padx=5)

    def enviar_codigo(self):
        email = self.email_entry.get()
        if email:
            # Armazenando o e-mail fornecido
            self.email_usuario = email

            # Cria o objeto de Verificação e envia o código
            self.verificacao_email = VerificacaoEmail(self.email_usuario)
            codigo = self.verificacao_email.gerar_codigo()
            self.verificacao_email.enviar_email()

            # Fecha a tela atual e abre a tela de validação do código
            self.label.configure(text="Digite o código enviado para o e-mail:")
            self.email_entry.destroy()  # Remove o campo de e-mail
            self.ok_button.configure(text="Validar Código", command=self.validar_codigo)

            # Cria o campo para inserir o código
            self.codigo_entry = ctk.CTkEntry(self, placeholder_text="Digite o código", width=200)
            self.codigo_entry.pack(pady=(5, 10))

        else:
            messagebox.showerror("Erro", "Por favor, insira um e-mail válido.")

    def validar_codigo(self):
        codigo_inserido = self.codigo_entry.get()
        if codigo_inserido:
            # Verifica se o código inserido é válido
            if self.verificacao_email.validar_codigo(codigo_inserido):
                self.redefinir_senha()  # Código válido, permite redefinir a senha
            else:
                messagebox.showerror("Erro", "Código inválido. Tente novamente.")
        else:
            messagebox.showwarning("Atenção", "Por favor, insira o código de verificação.")

    def redefinir_senha(self):
        # Atualiza a interface para permitir a redefinição da senha
        self.label.configure(text="Digite a nova senha:")
        self.codigo_entry.destroy()  # Remove o campo de código
        self.ok_button.configure(text="Redefinir Senha", command=self.salvar_nova_senha)

        # Cria os campos para inserir nova senha
        self.senha_entry = ctk.CTkEntry(self, placeholder_text="Nova senha", show="*", width=200)
        self.senha_entry.pack(pady=(5, 10))

        self.confirm_senha_entry = ctk.CTkEntry(self, placeholder_text="Confirmar senha", show="*", width=200)
        self.confirm_senha_entry.pack(pady=(5, 10))

    def salvar_nova_senha(self):
        senha = self.senha_entry.get()
        confirm_senha = self.confirm_senha_entry.get()
        if senha and senha == confirm_senha:
            # Aqui você deve colocar a lógica para salvar a nova senha no banco de dados
            # Supondo que você tenha um repositório de usuários
            if self.atualizar_senha(self.email_usuario, senha):
                messagebox.showinfo("Sucesso", "Senha redefinida com sucesso!")
                self.destroy()  # Fecha a janela de redefinição de senha
            else:
                messagebox.showerror("Erro", "Erro ao redefinir a senha. Tente novamente.")
        else:
            messagebox.showerror("Erro", "As senhas não coincidem ou estão vazias.")

    def atualizar_senha(self, email, nova_senha):
        """
        Atualiza a senha no banco de dados. Aqui você deve implementar a lógica para alterar a senha.
        """
        try:
            # Exemplo de como você pode chamar o método do repositório de usuários para atualizar a senha
            usuario_repo = UsuarioRepository()  # Seu repositório de usuários
            return usuario_repo.atualizar_senha(email, nova_senha)
        except Exception as e:
            print(f"Erro ao atualizar a senha: {e}")
            return False

    def on_cancel(self):
        self.destroy()
